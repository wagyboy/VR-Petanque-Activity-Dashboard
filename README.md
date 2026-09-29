# VR Petanque Activity Dashboard

Assignment 3 demonstrates automated README updates, GitHub Actions checks, and issue-linked delivery. This repository contains automation and documentation; it does not implement a playable game.

## How it works

- A manual or daily workflow lists up to five recent eligible commits on `main`.
- The updater skips its own commits and commits attributed to GitHub bot accounts. This is a filtering rule, not proof of human authorship.
- Only the marked section below may change. Identical source data produces no new update commit.
- Pull requests validate the markers, run automated tests, and upload a preview and diff without using the write token.

## Recent repository activity

<!-- ACTIVITY:START -->
- 2026-09-29 — docs: record A3 workflow and delivery evidence ([5f174ca](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/5f174ca1493b1c25c580a6f4589fa1b5e6ffa1e0))
- 2026-09-29 — Merge pull request #2 from wagyboy/a3-01-readme-validation ([589a2fc](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/589a2fcac2e7c0a0dbc3580915b50260503520c5))
- 2026-09-29 — fix: restore README end marker ([58c931c](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/58c931cc0e78a19c5abdeb6177c1a140ca306113))
- 2026-09-29 — test: demonstrate missing README end marker ([c5a18fb](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/c5a18fb40587dc8f914a218fd5ed52d22093ba0e))
- 2026-09-29 — ci: add README validation and preview ([c28b188](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/c28b188de22c31889749cec0a0a863c23f077f8c))
<!-- ACTIVITY:END -->
## Verification

Run `python -m unittest discover -s tests -v` and `python scripts/update_readme.py --validate-only`.

See [design and security notes](docs/design.md), [delivery evidence](docs/evidence.md), and [demo notes](docs/demo-notes.md).

## Scope and limitations

Activity means eligible commits reachable from the selected default-branch snapshot, in GitHub API order. It does not measure productivity, issue progress, or contributor effort. At most 1,000 commits are scanned; an excessive backlog causes a safe failure rather than a silently incomplete result.
