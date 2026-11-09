# Lesson Exercise: Dev Environment

## Task

Complete the environment setup exercise from the Phase 0, Lesson 1 curriculum material.

## Steps taken

- Checked the available tools: Python 3.13.12, Node.js 24.22.2, `uv` 0.13.1, and Git 2.53.0 are available. Rust, Julia, and `nvidia-smi` are not available in this environment.
- Confirmed `.venv/bin/python` points to the project virtual environment (Python 3.14.8).
- Installed NumPy into `.venv` and ran a dot-product example successfully.
- The first `uv` operation hit a read-only cache path. An approved retry found that `.venv` already existed; the existing environment was then used.

## Evidence

Command: `.venv/bin/python -c 'import sys; print("Python", sys.version.split()[0]); import numpy as np; print("NumPy", np.__version__); a = np.array([1, 2, 3]); print("Vector:", a, "dot:", np.dot(a, a))'`

Output: Python 3.14.8; NumPy 2.5.4; vector `[1 2 3]`; dot product `14`.

## Result

Python, Node.js, Git, `uv`, the existing virtual environment, and the NumPy vector example work. CPU use is available; no NVIDIA GPU was detected. Remaining exercise steps are listed in `verification/questions.md`.

