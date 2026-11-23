import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import process from "node:process";

type MessageRequest = {
  model: string;
  max_tokens: number;
  messages: { role: "user"; content: string }[];
};

type MessageResponse = {
  content: { type: string; text?: string }[];
  usage: { input_tokens: number; output_tokens: number };
};

function readDotenv(path: string): Record<string, string> {
  let source: string;
  try {
    source = readFileSync(path, "utf8");
  } catch {
    return {};
  }

  const values: Record<string, string> = {};
  for (const line of source.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const separator = trimmed.indexOf("=");
    if (separator < 1) continue;

    const name = trimmed.slice(0, separator).trim();
    let value = trimmed.slice(separator + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    values[name] = value;
  }
  return values;
}

const MOCK_RESPONSE: MessageResponse = {
  content: [
    {
      type: "text",
      text: "A neural network learns patterns by adjusting connected numerical weights.",
    },
  ],
  usage: { input_tokens: 12, output_tokens: 13 },
};

async function main(): Promise<number> {
  const mode = process.argv[2] ?? "mock";
  if (mode !== "mock" && mode !== "live") {
    console.error("Usage: node code/first_api_call.ts [mock|live]");
    return 2;
  }

  const fileEnv = readDotenv(resolve(process.cwd(), ".env"));
  const env = { ...fileEnv, ...process.env };
  const model = env.LLM_MODEL || "claude-sonnet-5";
  const request: MessageRequest = {
    model,
    max_tokens: 64,
    messages: [
      { role: "user", content: "What is a neural network? Answer in one short sentence." },
    ],
  };

  let response: MessageResponse;
  if (mode === "mock") {
    response = MOCK_RESPONSE;
    console.log("Mode: MOCK (no network request)");
  } else {
    const apiKey = env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      console.error("ANTHROPIC_API_KEY is not set. Configure it locally; never commit it.");
      return 1;
    }

    const httpResponse = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": apiKey,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify(request),
    });
    if (!httpResponse.ok) {
      let errorType = "unknown_error";
      try {
        const payload = (await httpResponse.json()) as { error?: { type?: string } };
        errorType = payload.error?.type ?? errorType;
      } catch {
        // A status code is still useful if the response body is not JSON.
      }
      console.error(`API error: HTTP ${httpResponse.status} (${errorType}).`);
      return 1;
    }
    response = (await httpResponse.json()) as MessageResponse;
    console.log("Mode: LIVE");
  }

  const text = response.content
    .filter((block) => block.type === "text")
    .map((block) => block.text ?? "")
    .join("\n");
  console.log(text);
  console.log(
    `Tokens: input=${response.usage.input_tokens}, output=${response.usage.output_tokens}`,
  );
  return 0;
}

main().then((code) => process.exit(code));
