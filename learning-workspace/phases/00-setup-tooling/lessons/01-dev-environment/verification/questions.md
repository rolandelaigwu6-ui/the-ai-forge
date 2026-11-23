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

## Optional follow-ups

- Revisit the three concept questions above and explain the answers in your own words.
- Julia remains optional and deferred; its toolchain is not installed.

## Completed on 2026-11-16

- Installed PyTorch CPU 2.9.1, Matplotlib 3.11.2, and Jupyter 1.1.1 in `.venv` and confirmed imports and the CPU-only backend.
- Installed Rust 1.100.0, compiled `../exercises/hello.rs`, and ran it successfully.
- Ran the official route verification script from a shallow curriculum checkout with `--route beginner --show-later`; both required checks passed. All optional checks passed except optional Julia, which remains deferred.
- Post-lesson quiz score is 2/3. Review the layer order: system foundation, package managers, language runtimes, then AI/ML libraries. The missed question remains in the Review queue until the learner confirms recall.
