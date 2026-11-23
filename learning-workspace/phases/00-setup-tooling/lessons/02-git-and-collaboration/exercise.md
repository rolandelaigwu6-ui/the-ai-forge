# Git & Collaboration — Exercise Record

**Date:** 2026-11-23
**Completion:** Practical exercises completed with agent assistance at the
learner's request. The quiz was skipped to advance; no quiz score is claimed.

## Exercise evidence

- Used the existing clone of the learner's GitHub repository (`origin` points
  to the learner's repository).
- Created the `my-progress` branch for this lesson work.
- Added this record as the lesson artifact, then committed and pushed it on
  `my-progress`.
- Added `.pt`, `.pth`, and `.safetensors` patterns to the repository-root
  `.gitignore` and checked that Git ignores matching checkpoint paths.
- Inspected repository history with `git log --oneline` and reviewed the
  Phase 0 lesson history.

## Reflection

The normal save-and-back-up sequence is stage changes, commit a local snapshot,
then push the commit to the remote. A branch lets a change be pushed for review
without putting it directly on `main`. The ignore rules prevent generated model
checkpoint files from being added accidentally.
