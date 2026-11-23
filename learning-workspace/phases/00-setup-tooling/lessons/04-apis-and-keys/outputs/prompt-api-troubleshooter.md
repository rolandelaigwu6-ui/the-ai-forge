# API Error Troubleshooter

Use the status code and error type to diagnose the request. Never paste an API
key into a report or log.

| Result | Likely cause | Next check |
|---|---|---|
| HTTP 400 | Invalid request body, model name, or parameter | Check endpoint and JSON fields; compare with the Messages API schema. |
| HTTP 401 | Missing, malformed, expired, or revoked API key | Check `ANTHROPIC_API_KEY` locally; do not print the value. |
| HTTP 403 | Key or account lacks permission | Check organization, workspace, and model access. |
| HTTP 429 | Rate limit reached | Wait and retry later; use bounded exponential backoff in applications. |
| HTTP 5xx | Provider-side service error | Check status page and request ID; retry cautiously with a limit. |
| Connection error | Network, DNS, TLS, or endpoint issue | Confirm the API base URL and network; avoid tight retry loops. |

The SDK raises typed exceptions for API status and connection failures. The
raw HTTP implementation exposes the status code and JSON error type directly.
Both should produce the same diagnosis without printing the API key.

References: [Phase 0 Lesson 04](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/04-apis-and-keys) and [Anthropic API errors](https://docs.anthropic.com/en/api/errors).
