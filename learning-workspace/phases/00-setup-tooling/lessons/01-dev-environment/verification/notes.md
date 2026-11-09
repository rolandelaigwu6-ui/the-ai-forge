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

- `uv --version`, `git --version`, `python3 --version`, and `node --version` check tool versions.
- `uv venv` creates a project virtual environment. The existing `.venv` was used.
- `.venv/bin/python -c 'import sys; print(sys.executable)'` confirmed the interpreter path is inside `.venv`.
- `uv pip install --python .venv/bin/python numpy` installs NumPy into that environment.
- NumPy's `np.dot([1, 2, 3], [1, 2, 3])` computes `1×1 + 2×2 + 3×3 = 14`; a plain Python loop can compute the same result one pair at a time.

Scratch version of the dot product:

```python
values = [1, 2, 3]
total = 0
for x in values:
    total += x * x
print(total)  # 14
```

## Questions

- See [questions.md](questions.md) for questions asked during this lesson and
  answers to revisit and lesson work deferred for later.

