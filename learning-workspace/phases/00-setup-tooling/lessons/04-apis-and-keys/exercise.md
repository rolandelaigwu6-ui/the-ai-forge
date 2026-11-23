# APIs & Keys — Exercise Record

**Date:** 2026-11-23
**Status:** Local preparation complete; live API exercises await a learner key.

## Work recorded

- Checked the existing repository before creating files. No `.env` file, API
  lesson code, or Anthropic SDK was present; `ANTHROPIC_API_KEY` was not
  configured in the shell or project virtual environment.
- Reused the existing `my-progress` branch and checkpoint ignore rules from
  Lesson 02.
- Added `.env` and `.env.*` ignores while allowing the empty `.env.example`
  template.
- Prepared one Python program with separate SDK and raw HTTP modes. Both use
  the same endpoint, model setting, short prompt, and token limit.
- Installed Anthropic SDK 2.13.0 into the existing project `.venv`; no new
  environment or branch was created.
- Confirmed the Python script compiles and its `--help` runs. Invoking SDK mode
  without a key stops locally before sending a request.
- Added a TypeScript example with a local mock mode, so its request/response
  shape can be explored without a key or network call.
- Ran the TypeScript mock with Node.js 24.22.2. It printed the fixture response
  and token counts without making a network request.
- Confirmed `.env` and `.env.local` are ignored while `.env.example` remains
  trackable.
- Added an API error troubleshooting artifact.

## Not run

No key was available, so I did not send a request to Anthropic, trigger a
billable call, or send a deliberately invalid key. The SDK and raw HTTP
response comparison, 401 exercise, and quiz are still pending. No credential
was created or recorded here.

## How to resume

From the lesson directory:

1. Copy `.env.example` to `.env` and enter the key locally; do not paste it into
   chat or commit `.env`.
2. Load the file in a shell with `set -a; . ./.env; set +a`.
3. Run `python code/first_api_call.py sdk`, then
   `python code/first_api_call.py http` and compare text and token usage.
4. For the invalid-key exercise, use a fake value only in a one-command shell
   environment, never overwrite the real key.
