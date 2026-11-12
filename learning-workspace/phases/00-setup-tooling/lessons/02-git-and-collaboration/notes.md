# Lesson Notes: Git & Collaboration

## Core workflow

`git status` shows the current branch and working-tree changes. `git add` stages
selected changes; `git commit` saves a local snapshot; `git push` publishes
commits to a remote branch.

```text
working directory -> staging area -> local repository -> remote repository
      git add             git commit          git push
```

## Branches and remotes

A branch is a name pointing to a line of commits. Switching branches changes
which line is checked out. To merge `my-progress` into `main`, switch to `main`,
run `git merge my-progress`, then push `main`. Pushing `my-progress` updates
`origin/my-progress`; it does not update `origin/main`.

## Ignore files and history

The root `.gitignore` contains `*.pt`, `*.pth`, and `*.safetensors` to keep
model checkpoint binaries out of ordinary Git history. `git log --oneline`
shows one commit per line, newest first. `git show --stat <hash>` summarizes
which files a commit changed.

## Session evidence

- Created and pushed branch `my-progress` to `origin/my-progress`.
- Verified the checkpoint patterns with `git check-ignore`.
- Used `git status`, `git log`, and `git show --stat` to inspect status and
  history.
- The question log records concepts to revisit. The quiz was deferred, so this
  lesson has no quiz score yet.
