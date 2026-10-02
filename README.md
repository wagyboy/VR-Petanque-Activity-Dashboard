# VR Petanque Activity Dashboard

[![README update](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/workflows/update-readme.yml/badge.svg?branch=main)](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/workflows/update-readme.yml)
[![README validation](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/workflows/validate-readme.yml/badge.svg?branch=main)](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/workflows/validate-readme.yml)

Assignment 3 demonstrates automated README updates, GitHub Actions checks, and issue-linked delivery. This repository contains automation and documentation; it does not implement a playable game.

## How it works

- A manual or daily workflow lists up to five recent eligible commits on `main`.
- The updater skips its own commits and commits attributed to GitHub bot accounts. This is a filtering rule, not proof of human authorship.
- Only the marked section below may change. Identical source data produces no new update commit.
- Pull requests validate the markers, run automated tests, and upload a preview and diff without using the write token.

## Recent repository activity

<!-- ACTIVITY:START -->
- 2026-10-02 — docs: finalize A3 maintenance evidence ([4dfa177](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/4dfa1774244446edef69eb35120c69853e50616a))
- 2026-10-02 — Merge pull request #3 from wagyboy/a3-evidence-runtime-polish ([ffa5869](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/ffa58697b5a5fdd9a55fdc46f8ca7639e76a6413))
- 2026-10-02 — docs: verify scheduled runs and token boundary ([bfcddae](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/bfcddaefa6b2802c1db7d815c10e487328095910))
- 2026-10-02 — ci: pin Node 24 actions and runner ([ca7c27d](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/ca7c27d6f76b30b19bacc3b466b94050646d306d))
- 2026-10-02 — docs: add workflow status badges ([3947a9d](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/3947a9d9d93a22c4acf134bad26166d5d5a178dc))
<!-- ACTIVITY:END -->
## Verification

Run `python -m unittest discover -s tests -v` and `python scripts/update_readme.py --validate-only`.

See [design and security notes](docs/design.md), [delivery evidence](docs/evidence.md), and [demo notes](docs/demo-notes.md).

## Scope and limitations

Activity means eligible commits reachable from the selected default-branch snapshot, in GitHub API order. It does not measure productivity, issue progress, or contributor effort. At most 1,000 commits are scanned; an excessive backlog causes a safe failure rather than a silently incomplete result.
