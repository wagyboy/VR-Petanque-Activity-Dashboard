# VR Petanque Activity Dashboard

Assignment 3 demonstrates automated README updates, GitHub Actions checks, and issue-linked delivery. This repository contains automation and documentation; it does not implement a playable game.

## How it works

- A manual or daily workflow lists up to five recent eligible commits on `main`.
- The updater skips its own commits and commits attributed to GitHub bot accounts. This is a filtering rule, not proof of human authorship.
- Only the marked section below may change. Identical source data produces no new update commit.
- Pull requests validate the markers, run automated tests, and upload a preview and diff without using the write token.

## Recent repository activity

<!-- ACTIVITY:START -->
- 2026-09-29 — Add GitHub Actions workflow to update README ([e63a848](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/e63a848af0cfe0e55c8309a986f23bd2aa8b824e))
- 2026-09-29 — Create .gitignore ([eebcdc7](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/eebcdc7a33ec3d814d2e8871d75b812aabb55864))
- 2026-09-29 — Add files via upload ([0290bdb](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/0290bdbdd75a1b5dea1e76b9a6ac71d3ae94f4f7))
- 2026-09-29 — Update README.md ([e86442e](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/e86442e37f84a404489db9157dab534c463e5668))
- 2026-09-29 — Initial commit ([2811589](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/2811589d1b0c3f7b86784a06f984788df47920de))
<!-- ACTIVITY:END -->

## Verification

Run `python -m unittest discover -s tests -v` and `python scripts/update_readme.py --validate-only`.

See [design and security notes](docs/design.md), [delivery evidence](docs/evidence.md), and [demo notes](docs/demo-notes.md).

## Scope and limitations

Activity means eligible commits reachable from the selected default-branch snapshot, in GitHub API order. It does not measure productivity, issue progress, or contributor effort. At most 1,000 commits are scanned; an excessive backlog causes a safe failure rather than a silently incomplete result.
