# Questions to Revisit: Dev Environment

Record lesson questions that are currently unanswered. Add the answer and the
date when each question is resolved; keep the original response as evidence of
what needs another explanation.

| Date | Question | Your response | Answer / follow-up |
|------|----------|---------------|--------------------|
| 2026-11-09 | Why should AI/ML libraries be installed after the system foundation, package managers, and language runtimes? | “I don't know.” | Explained: libraries depend on the lower layers; for example, PyTorch needs a Python runtime and package manager, and GPU access may need system drivers. Follow-up check answered: Python. |
| 2026-11-09 | Which layer comes directly before AI/ML libraries? | “I don't know.” | Explained: the layer immediately before AI/ML libraries is language runtimes. Follow-up check confirmed Python is the runtime PyTorch needs. |
| 2026-11-09 | What work did NumPy handle in the vector example that you would otherwise write yourself? | “Don't know.” | Explained: NumPy stores the numbers in an array and computes the dot product; plain Python would add the products `1×1`, `2×2`, and `3×3` in a loop. |
| 2026-11-13 | In the four-layer environment stack, which layer must be installed first? | “A” (Language runtimes) | Incorrect; score review: start with the system foundation, then package managers, language runtimes, and AI/ML libraries. Added to the Review queue in `LEARNING.md`. |

## Finish later

- Revisit the three concept questions above and explain the answers in your own words.
- Run the lesson's route verification script from a full curriculum checkout; that script is not present in this learning workspace.
- Finish the Python setup: install PyTorch in `.venv` (CPU is fine here), then verify its version and GPU availability.
- Install the remaining Python lesson packages (`matplotlib` and `jupyter`) if needed for later examples.
- Write and run a Rust and Julia hello-world when those toolchains are installed. They are not available in this environment (`rustc`, `cargo`, and `julia` are missing); Python and TypeScript hello-worlds are complete in `../exercises/`.
- The post-lesson quiz is complete: 2/3. The missed layer-order question is in the Review queue. Other environment setup tasks remain pending.
