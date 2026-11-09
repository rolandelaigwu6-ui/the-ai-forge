# Lesson Notes: Dev Environment

## Key ideas

The environment has four layers, installed from the bottom up:

1. System foundation: operating system, shell, Git, editor, and GPU drivers.
2. Package managers: tools such as `uv`, `pnpm`, and `cargo`.
3. Language runtimes: Python, Node.js, Rust, and Julia.
4. AI/ML libraries: tools such as PyTorch and JAX.

Each upper layer depends on lower layers. For example, PyTorch needs a Python
runtime, a package manager to install it, and suitable system drivers to use a
GPU. See `questions.md` for the concept check that is still unclear.

## Commands and tools

Record commands you used and what each one does. Do not include secrets.

## Questions

- See [questions.md](questions.md) for questions asked during this lesson and
  answers that are not known yet.

