# GPU and Cloud Setup — Learning Log

**Started:** 2026-11-18
**Status:** Closed by learner decision on 2026-11-23

## What I learned

- A GPU (Graphics Processing Unit) is a specialized processor that can run
  many simple math operations at the same time.
- A cloud setup can rent access to GPU hardware over the internet, so the
  compute can be used without owning that hardware locally.
- A GPU can accelerate AI workloads by processing many numerical operations in
  parallel. Having a GPU available is only one part of a working setup: the
  operating system, drivers, runtime, and AI library also need to work
  together.
- Cloud platforms can provide access to GPU machines without requiring the
  same hardware locally. The machine's GPU, installed software, storage, and
  access settings all affect whether a workload can run successfully.
- I need to check which device my code can actually see, rather than assuming
  that selecting a GPU machine means my Python environment is using it.
- A machine-specific end-to-end GPU workload was not recorded in this
  workspace.

## Optional follow-up

If I revisit this setup, record the machine and GPU model, framework detection,
a small workload result, and cloud cleanup evidence.

## Reflection

The main idea I am taking away is that GPU setup is a chain of dependencies:
hardware access, drivers, runtime, framework, and code all have to line up. I
want to verify each layer instead of treating “GPU enabled” as a single switch.

## Session note — 2026-11-23

I captured my understanding in [note.md](note.md): a GPU handles many math
operations in parallel, and cloud computing lets me rent access to that
hardware online. I chose to close the lesson and move on; machine-specific
checks and a verified workload were not recorded here.
