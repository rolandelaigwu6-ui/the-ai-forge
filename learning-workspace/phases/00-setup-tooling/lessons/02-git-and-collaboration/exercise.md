# Lesson Exercise: Git & Collaboration

## Task

Practice a branch-based workflow in this personal learning repository.

## Steps taken

- Confirmed `origin` points to the personal GitHub repository and the working tree was clean on `main`.
- Created and switched to branch `my-progress`.
- Prepared this evidence file and a root `.gitignore` for model checkpoint files; verified all three patterns with `git check-ignore`.
- Committed and pushed the exercise as `fa81b8c` (`Prepare Git collaboration lesson exercise`) and updated the evidence as `710a114` (`Record Git lesson push evidence`).
- Added the question log in `c1fe5e2` (`Add Git lesson question log`) and pushed it to `origin/my-progress`.
- Inspected recent history with `git log --oneline`, filtered lesson history with `git log --oneline -- learning-workspace/phases/00-setup-tooling`, and viewed `fa81b8c` with `git show --stat`.
- The full curriculum source is not cloned here, so its lesson-author history and a separate fork/clone exercise were not completed.

## Evidence

- Branch: `my-progress`
- Ignore patterns: `*.pt`, `*.pth`, and `*.safetensors`
- Remote branch: `origin/my-progress`
- `git status --short --branch` showed the branch in sync after pushing.

## Result

The branch and ignore patterns are pushed to the personal repository. The post-lesson quiz was deferred; the lesson remains in progress. See `verification/questions.md` for unanswered checks and deferred work.
