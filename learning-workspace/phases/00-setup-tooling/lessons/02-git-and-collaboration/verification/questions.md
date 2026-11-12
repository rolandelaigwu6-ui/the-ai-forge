# Questions to Revisit: Git & Collaboration

Record lesson questions that are currently unanswered, then add the explanation
and a later check when they become clear.

| Date | Question | Your response | Answer / follow-up |
|------|----------|---------------|--------------------|
| 2026-11-12 | If you switch to `main` before merging, will `main` include a commit made only on `my-progress`? | “Don't know.” | A branch keeps its commits separate. `main` gets those changes only after a merge. Follow-up answered: switch to `main` before running `git merge my-progress`. |
| 2026-11-12 | Does pushing `my-progress` by itself update `main`? | “Yes.” | Correction: no. `git push origin my-progress` updates the remote `my-progress` branch. To update `main`, merge the changes into local `main`, then push `main`. Revisit this distinction. |
| 2026-11-12 | Which remote branch was updated by `git push -u origin my-progress`? | “git merge my-progress” | You named the merge command that brings branch changes into `main`. The push updated remote branch `origin/my-progress`; review the difference between merge and push. |
| 2026-11-12 | Which remote branch label is beside commit `c1fe5e2`? | “Don't have an idea.” | Output shows `origin/my-progress` beside `c1fe5e2`. `origin/main` still points to `c719bc7`, so pushing `my-progress` did not update `main`. |
| 2026-11-12 | What problem could a very large model checkpoint cause if committed to the repository? | “Don't have an idea.” | A large binary can make the repository history grow, so clones and fetches take longer. Checkpoints are usually regenerated or stored separately. |
| 2026-11-12 | In `git log --oneline`, is the newest commit at the top or bottom? | “At the bottom.” | Correction: the newest commit is listed first, at the top. After reading the output, you correctly answered that the newest commit appears first. |

## Revisit later

- Review the difference between pushing `my-progress` and merging it into `main`; the history output showed that `origin/main` stayed on an earlier commit.
- Revisit why large model checkpoint files should be excluded from ordinary Git history.
- If desired, clone the original curriculum repository separately to inspect its lesson-author commit history; this workspace is your personal repository.
- Take the three post-lesson quiz questions. They were not asked in this session; no score is recorded and Lesson 02 remains in progress.
