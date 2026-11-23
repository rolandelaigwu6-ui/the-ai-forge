"""Compare an Anthropic SDK call with the equivalent raw HTTP request."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


API_BASE = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
API_URL = f"{API_BASE}/v1/messages"
API_VERSION = "2023-06-01"
MODEL = os.environ.get("LLM_MODEL", "claude-sonnet-5")
PROMPT = "What is a neural network? Answer in one short sentence."
MAX_TOKENS = 64


def require_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise SystemExit(
            "ANTHROPIC_API_KEY is not set. Configure it locally; never put it in source code."
        )
    return key


def print_text_and_usage(text: str, usage: dict[str, int] | None = None) -> None:
    print(text)
    if usage:
        print(
            "Tokens: "
            f"input={usage.get('input_tokens', 0)}, "
            f"output={usage.get('output_tokens', 0)}"
        )


def call_with_sdk(api_key: str) -> None:
    try:
        import anthropic
    except ImportError as exc:
        raise SystemExit(
            "The Anthropic SDK is missing. Install it in the project environment with: "
            "uv pip install --python .venv/bin/python anthropic"
        ) from exc

    client = anthropic.Anthropic(api_key=api_key)
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": PROMPT}],
        )
    except anthropic.APIStatusError as exc:
        report_api_error(exc.status_code)
        return
    except anthropic.APIConnectionError:
        print("Connection failed. Check the endpoint and network before retrying.", file=sys.stderr)
        raise SystemExit(1)

    text = "\n".join(block.text for block in response.content if block.type == "text")
    print_text_and_usage(
        text,
        {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    )


def call_with_raw_http(api_key: str) -> None:
    body = json.dumps(
        {
            "model": MODEL,
            "max_tokens": MAX_TOKENS,
            "messages": [{"role": "user", "content": PROMPT}],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": API_VERSION,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        report_api_error(exc.code, exc.read())
        return
    except urllib.error.URLError:
        print("Connection failed. Check the endpoint and network before retrying.", file=sys.stderr)
        raise SystemExit(1)

    text = "\n".join(
        block["text"] for block in result.get("content", []) if block.get("type") == "text"
    )
    print_text_and_usage(text, result.get("usage"))


def report_api_error(status: int, body: bytes = b"") -> None:
    error_type = "unknown_error"
    try:
        payload = json.loads(body)
        error_type = payload.get("error", {}).get("type", error_type)
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass

    guidance = {
        400: "Check the endpoint and request fields.",
        401: "Authentication failed. Check the key locally without printing it.",
        403: "The account or key may not have permission for this resource.",
        429: "Rate limited. Wait before retrying; do not retry in a tight loop.",
    }.get(status, "Inspect the status and error type; avoid logging credentials.")
    print(f"API error: HTTP {status} ({error_type}). {guidance}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("sdk", "http"), help="request through the SDK or raw HTTP")
    args = parser.parse_args()
    api_key = require_api_key()
    if args.mode == "sdk":
        call_with_sdk(api_key)
    else:
        call_with_raw_http(api_key)


if __name__ == "__main__":
    main()
