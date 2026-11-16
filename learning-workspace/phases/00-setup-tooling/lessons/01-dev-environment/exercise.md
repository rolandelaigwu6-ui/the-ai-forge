# Lesson Exercise: Dev Environment

## Task

Complete the environment setup exercise from the Phase 0, Lesson 1 curriculum material.

## Steps taken

- Checked the available tools: Python 3.13.12, Node.js 24.22.2, `uv` 0.13.1, and Git 2.53.0 are available. Rust, Julia, and `nvidia-smi` are not available in this environment.
- Confirmed `.venv/bin/python` points to the project virtual environment (Python 3.14.8).
- Installed NumPy into `.venv` and ran a dot-product example successfully.
- Installed CPU-only PyTorch 2.9.1, Matplotlib 3.11.2, and Jupyter 1.1.1 into `.venv`; confirmed PyTorch imports and reports CUDA unavailable, as expected on this CPU-only environment.
- The first `uv` operation hit a read-only cache path. An approved retry found that `.venv` already existed; the existing environment was then used.
- Wrote and ran `exercises/hello.py` with Python 3.13.12.
- Wrote and ran `exercises/hello.ts` with Node.js 24.22.2, then type-checked it with `tsc --noEmit`.
- At the time of the original session, Rust and Julia were not installed (`rustc`, `cargo`, and `julia` were unavailable), so their examples were deferred. Julia remains optional; Rust is used in later systems lessons.
- Follow-up (2026-11-16): installed the minimal Rust toolchain (rustc/cargo 1.100.0), added `exercises/hello.rs`, compiled it, and ran it; output was `Hello, world!`.

## Evidence

Command: `.venv/bin/python -c 'import sys; print("Python", sys.version.split()[0]); import numpy as np; print("NumPy", np.__version__); a = np.array([1, 2, 3]); print("Vector:", a, "dot:", np.dot(a, a))'`

Output: Python 3.14.8; NumPy 2.5.4; vector `[1 2 3]`; dot product `14`.

Hello-world evidence: `python3 exercises/hello.py`, `node exercises/hello.ts`, and the compiled Rust program printed `Hello, world!`; `tsc --noEmit exercises/hello.ts` completed without errors. The Rust binary was written under `/tmp` and is not part of the repository.

Additional package evidence: `.venv/bin/python` imported PyTorch, Matplotlib, and NumPy; PyTorch reported `2.9.1+cpu`, CUDA availability was `False`, and the NumPy dot product returned `14`. `.venv/bin/jupyter --version` listed JupyterLab 4.1.6 and Notebook 7.1.3.

Route verification: ran the official `verify.py --route beginner --show-later` from a shallow course checkout, using this workspace's `.venv` and Rust toolchain. Both required beginner checks passed (Python 3.14.8 and Git 2.53.0); optional Node.js, npx, NumPy, Matplotlib, Jupyter, PyTorch, CPU backend, and Cargo checks passed. Julia was the only optional check not installed.

## Result

Python, Node.js, TypeScript, Rust, Git, `uv`, the existing virtual environment, NumPy, CPU-only PyTorch, Matplotlib, Jupyter, and their hello-world/setup checks work. No NVIDIA GPU was detected. The quiz score is 2/3. Julia is optional and not installed, and the route verification script is absent from this learning workspace; see `verification/questions.md`.

