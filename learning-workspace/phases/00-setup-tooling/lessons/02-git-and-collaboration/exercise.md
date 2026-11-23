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
- This exercise used the existing personal learning repository and its
  `my-progress` branch, rather than making a duplicate clone or fork.
- Reviewing maintainers' lesson-author history is optional for this personal
  repository workflow and does not block progression.

## Evidence

- Branch: `my-progress`
- Ignore patterns: `*.pt`, `*.pth`, and `*.safetensors`
- Remote branch: `origin/my-progress`
- `git status --short --branch` showed the branch in sync after pushing.

## Result

The practical exercise is complete with agent assistance. The post-lesson
quiz score is 2/3; the missed Git workflow distinction remains in the Review
queue. The learner chose to advance to Phase 0, Lesson 04.
