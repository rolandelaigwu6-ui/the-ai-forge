# Questions to Revisit: Dev Environment

Record lesson questions that are currently unanswered. Add the answer and the
date when each question is resolved; keep the original response as evidence of
what needs another explanation.

| Date | Question | Your response | Answer / follow-up |
|------|----------|---------------|--------------------|
| 2026-11-09 | Why should AI/ML libraries be installed after the system foundation, package managers, and language runtimes? | “I don't know.” | Explained: libraries depend on the lower layers; for example, PyTorch needs a Python runtime and package manager, and GPU access may need system drivers. Follow-up check answered: Python. |
| 2026-11-09 | Which layer comes directly before AI/ML libraries? | “I don't know.” | Explained: the layer immediately before AI/ML libraries is language runtimes. Follow-up check confirmed Python is the runtime PyTorch needs. |
| 2026-11-09 | What work did NumPy handle in the vector example that you would otherwise write yourself? | “Don't know.” | Explained: NumPy stores the numbers in an array and computes the dot product; plain Python would add the products `1×1`, `2×2`, and `3×3` in a loop. |

## Finish later

- Revisit the three concept questions above and explain the answers in your own words.
- Run the lesson's route verification script from a full curriculum checkout; that script is not present in this learning workspace.
- Finish the Python setup: install PyTorch in `.venv` (CPU is fine here), then verify its version and GPU availability.
- Install the remaining Python lesson packages (`matplotlib` and `jupyter`) if needed for later examples.
- Write and run a hello-world program in Python, TypeScript, Rust, and Julia. Rust and Julia are not currently installed.
- Take the three post-lesson quiz questions. The quiz has not been taken, so no score is recorded and the lesson remains in progress.
