# Lesson Exercise: Dev Environment

## Task

Complete the environment setup exercise from the Phase 0, Lesson 1 curriculum material.

## Steps taken

- Checked the available tools: Python 3.13.12, Node.js 24.22.2, `uv` 0.13.1, and Git 2.53.0 are available. Rust, Julia, and `nvidia-smi` are not available in this environment.
- Confirmed `.venv/bin/python` points to the project virtual environment (Python 3.14.8).
- Installed NumPy into `.venv` and ran a dot-product example successfully.
- The first `uv` operation hit a read-only cache path. An approved retry found that `.venv` already existed; the existing environment was then used.
- Wrote and ran `exercises/hello.py` with Python 3.13.12.
- Wrote and ran `exercises/hello.ts` with Node.js 24.22.2, then type-checked it with `tsc --noEmit`.
- Rust and Julia are not installed in this environment (`rustc`, `cargo`, and `julia` are unavailable). Their hello-world programs are deferred rather than installing new toolchains for this session. Julia is optional in this lesson; Rust is used in later systems lessons.

## Evidence

Command: `.venv/bin/python -c 'import sys; print("Python", sys.version.split()[0]); import numpy as np; print("NumPy", np.__version__); a = np.array([1, 2, 3]); print("Vector:", a, "dot:", np.dot(a, a))'`

Output: Python 3.14.8; NumPy 2.5.4; vector `[1 2 3]`; dot product `14`.

Hello-world evidence: both `python3 exercises/hello.py` and `node exercises/hello.ts` printed `Hello, world!`; `tsc --noEmit exercises/hello.ts` completed without errors.

## Result

Python, Node.js, TypeScript, Git, `uv`, the existing virtual environment, the NumPy vector example, and the available-language hello-world programs work. CPU use is available; no NVIDIA GPU was detected. The quiz score is 2/3. Rust and Julia examples and remaining setup are listed in `verification/questions.md`.

