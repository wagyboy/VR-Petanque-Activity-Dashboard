# VR Petanque Activity Dashboard

Assignment 3 demonstrates automated README updates, GitHub Actions checks, and issue-linked delivery. This repository contains automation and documentation; it does not implement a playable game.

## How it works

- A manual or daily workflow lists up to five recent eligible commits on `main`.
- The updater skips its own commits and commits attributed to GitHub bot accounts. This is a filtering rule, not proof of human authorship.
- Only the marked section below may change. Identical source data produces no new update commit.
- Pull requests validate the markers, run automated tests, and upload a preview and diff without using the write token.

## Recent repository activity

<!-- ACTIVITY:START -->
Activity has not been generated yet.
<!-- ACTIVITY:END -->

## Verification

Run `python -m unittest discover -s tests -v` and `python scripts/update_readme.py --validate-only`.

See [design and security notes](docs/design.md), [delivery evidence](docs/evidence.md), and [demo notes](docs/demo-notes.md).

## Scope and limitations

Activity means eligible commits reachable from the selected default-branch snapshot, in GitHub API order. It does not measure productivity, issue progress, or contributor effort. At most 1,000 commits are scanned; an excessive backlog causes a safe failure rather than a silently incomplete result.
