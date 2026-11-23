# APIs & Keys

**Curriculum:** Phase 0, Lesson 04
**Status:** In progress; local examples prepared and mock checked, live request and quiz pending

This is the next lesson in the official Phase 0 sequence. Read the source
[APIs & Keys lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/04-apis-and-keys).

The lesson covers safe API-key storage, a first API request using an SDK and
raw HTTP, and common authentication and rate-limit errors. Never put real API
keys in this repository or in lesson notes.

## Avoid repeating earlier work

- Continue on the existing `my-progress` branch; Lesson 02 already created and
  pushed it.
- Keep the checkpoint ignore patterns already in the root `.gitignore`.
- This lesson adds `.env` protection to that existing file instead of creating
  another ignore file.

## Lesson files

- [Notes](notes.md)
- [Exercise record](exercise.md)
- [API error troubleshooting artifact](outputs/prompt-api-troubleshooter.md)
- [Python SDK and raw HTTP example](code/first_api_call.py)
- [TypeScript local mock / explicit live request](code/first_api_call.ts)
- [Safe environment template](.env.example)

The TypeScript mock was run locally with Node.js 24.22.2. The Python program
compiled and its missing-key guard stopped before any request. No live API
request has been sent.
