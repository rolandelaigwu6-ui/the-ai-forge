# APIs & Keys — Lesson Notes

## Request and response

An API call sends a request to an endpoint and receives a response. For a
Messages API request, the request includes the model, a token limit, and the
messages. Authentication is separate from the request content: the SDK reads
`ANTHROPIC_API_KEY` from the environment, while raw HTTP sends the key in the
`x-api-key` header.

## Keep credentials out of Git

- Read the key from an environment variable; never hardcode it in source.
- A local `.env` file can hold the variable, but it must be ignored by Git.
- `.env.example` is a safe, empty template and is explicitly allowed by the
  root `.gitignore`.
- Never print a key, place it in a command committed to shell history, or add it
  to lesson notes.

## SDK versus raw HTTP

The SDK builds the HTTP request and parses the JSON response into Python
objects. Raw HTTP makes the endpoint, headers, JSON body, and parsing explicit.
Both approaches use the same Messages endpoint and response fields; raw HTTP is
useful when debugging a request.

## Errors

- `401`: authentication problem; check that the key is present, valid, and
  permitted. Do not print it while debugging.
- `403`: the key or account lacks access to the requested resource.
- `429`: rate limit; wait before retrying and use backoff for repeated calls.
- `400`: inspect request parameters and the response's error type.
- Connection failures: check endpoint and network connectivity; do not retry
  blindly if a request may already have reached the service.

## What was not repeated

Lesson 02 already created and pushed `my-progress`, inspected Git history, and
added checkpoint patterns to `.gitignore`. Lesson 04 reuses those records and
only adds secret-file patterns.
