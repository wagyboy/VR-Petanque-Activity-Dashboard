# Design and security

## Workflow separation

`validate-readme.yml` runs on PRs and relevant main-branch pushes, with a read-only GITHUB_TOKEN. It validates the proposed README and previews main-branch activity using proposed code. The preview does not claim to include the future merge commit. It receives no PAT and never pushes.

`update-readme.yml` runs manually or daily at 01:17 UTC (09:17 Taipei), on main only. Schedules may be delayed; manual execution is the reproducible demonstration path. It checks out main, tests and validates, reads commits at that exact snapshot, and pushes only README.md if changed.

## Least privilege

REPO_TOKEN must be a fine-grained PAT for this repository only, with Contents read/write and an expiry covering grading. Metadata read access is automatic. It is exposed only to the push step, not the PR preview or API reader. The PAT has independent permissions: workflow `permissions: contents: read` does not restrict the PAT.

The Git askpass helper references an environment variable; it contains no token literal. Tokens are not included in URLs, files, screenshots, or debug output. Checkout does not retain credentials. Do not enable shell tracing or print environment variables. Rotate/revoke the PAT on expiry, after grading, or immediately after exposure.

## Determinism and preservation

No current-run timestamp is inserted into README. The updater excludes its exact commit subject and linked Bot accounts. Filtering does not prove that every remaining commit was written by a human. Markers must be unique, ordered, and on separate lines. Text outside markers and existing CRLF line endings are preserved. Titles are escaped before rendering.

## Failure and concurrency

API timeout, errors, invalid data, or scan-limit exhaustion fail the run rather than erasing existing activity. Pagination can scan up to 1,000 commits. Writes use one concurrency group, but GitHub can replace pending runs; it is not a durable queue. A concurrent human push can still cause a non-fast-forward rejection. The workflow never force-pushes: rerun on current main after checking the failure.

The writer has no push trigger. Its commit includes [skip ci], preventing redundant push validation; PR checks still run for normal feature commits. A branch rule requiring every change through a PR will block this direct-push design. A production alternative is a bot-created update PR; this exercise uses an isolated assignment repository permitting the explicitly authorized writer.

## Limitations and improvements

The workflows pin checkout, setup-python, and upload-artifact to reviewed full commit SHAs. upload-artifact uses v7.0.1 on Node 24. The runner is ubuntu-24.04, avoiding implicit migration of ubuntu-latest. Review dependency updates regularly rather than treating pins as permanent. API retry/backoff is not implemented: failures are bounded and visible. Scheduled operation is not a timing SLA. New artifacts request retention for 90 days (subject to repository policy); this does not extend older artifacts that requested 14 days. Artifacts still expire; preserve report evidence separately. No performance improvement is claimed without measurements.

## Merge controls and grading access

This assignment retains its direct README push architecture. The main branch has no required status checks or mandatory PR rule. A failed PR check provides feedback but does not enforce a merge block. Do not describe this repository as having enforced branch protection. Enabling mandatory PRs later requires migrating the writer to an update-PR model and reviewing permissions first.

The project board was private when the evidence screenshots were captured. Repository, issue, PR and run links provide public evidence; board screenshots remain in the report. No project visibility change is part of this maintenance update.

Status badges report workflow outcomes on main. They do not measure test coverage, code quality, or correctness of requirements.
