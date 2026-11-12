# Questions to Revisit: Git & Collaboration

Record lesson questions that are currently unanswered, then add the explanation
and a later check when they become clear.

| Date | Question | Your response | Answer / follow-up |
|------|----------|---------------|--------------------|
| 2026-11-12 | If you switch to `main` before merging, will `main` include a commit made only on `my-progress`? | “Don't know.” | A branch keeps its commits separate. `main` gets those changes only after a merge. Pushing publishes the branch to the remote; it does not merge it into `main`. |
| 2026-11-12 | Does pushing `my-progress` by itself update `main`? | “Yes.” | Correction: no. `git push origin my-progress` updates the remote `my-progress` branch. To update `main`, merge the changes into local `main`, then push `main`. Revisit this distinction. |
| 2026-11-12 | Which remote branch was updated by `git push -u origin my-progress`? | “git merge my-progress” | You named the merge command that brings branch changes into `main`. The push updated remote branch `origin/my-progress`; review the difference between merge and push. |
