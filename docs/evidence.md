# Assignment 3 Evidence

## Project and delivery links

- Repository: [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard)
- Project board: [https://github.com/users/wagyboy/projects/3](https://github.com/users/wagyboy/projects/3)
- Implementation issue: [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/issues/1](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/issues/1)
- Merged feature PR: [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/pull/2](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/pull/2)

## Workflow evidence

| Experiment              | Observed result                                                                                                      | Evidence                                                                                                                                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First README update     | Five activity entries were displayed; README changed and an update commit was created.                               | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/4ab6da40638d546dd7502ca1f3f4a236c68ab173](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/4ab6da40638d546dd7502ca1f3f4a236c68ab173) |
| Unchanged rerun         | Six commits were scanned, one was excluded, and five were displayed. No README change or update commit was produced. | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36549535573](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36549535573)                                               |
| New activity update     | The documentation commit `ffc0f28` appeared in the README activity list.                                             | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36549750457](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36549750457)                                               |
| Missing END marker      | PR validation failed at the actual README marker check.                                                              | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36634031355](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36634031355)                                               |
| Marker restored         | PR validation succeeded and generated a preview artifact.                                                            | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36634632928](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36634632928)                                               |
| Automatic issue closure | Merging PR #2 closed issue #1 automatically.                                                                         | [https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/issues/1](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/issues/1)                                                                               |

## First automated README commit

[https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/4ab6da40638d546dd7502ca1f3f4a236c68ab173](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/commit/4ab6da40638d546dd7502ca1f3f4a236c68ab173)

The diff replaced the placeholder with five activity entries while retaining the activity markers.

## Preview artifact inspection

The corrected PR run produced `readme-preview`, containing:

- `README.preview.md`
- `README.diff`
- `metrics.json`

Observed metrics:

- scanned: 7
- excluded: 2
- displayed: 5
- changed: false
- preview_only: true

The preview contained both activity markers and five entries. The diff was empty, consistent with `changed: false`.

## Review and limitations

Implementation and evidence review used AI assistance; no independent approval is claimed.

The missing-marker failure was deliberately introduced on the feature branch and corrected before merge. API-failure behavior is covered by a simulated unit test, not a real GitHub outage experiment.

Scheduled execution has now been verified independently of the original manual demonstrations. See the scheduled-run evidence below. Scheduling is not a timing guarantee.

These results demonstrate content updates, an unchanged rerun, validation failure and recovery, and issue closure. They do not establish general productivity or delivery-speed improvements.

## Scheduled execution verified on 2 October 2026

| Run | Trigger | Result | Recorded start (Asia/Taipei) |
| --- | --- | --- | --- |
| [Run #5](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36680133494) | schedule | success | 30 September 2026, 14:47:59 |
| [Run #6](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/actions/runs/36829054309) | schedule | success | 1 October 2026, 15:13:00 |

Run #6 logs show 14 passing unit tests and metrics of scanned=6, excluded=1, displayed=5, changed=false, preview_only=false. The push step printed "No content change; no commit created." This verifies a successful scheduled no-op, not a scheduled write of new content.

The configured cron is 01:17 UTC (09:17 Taipei). Actual starts above occurred later. These observations establish eventual scheduled execution, not punctual daily delivery.

## Measured behavior and interpretation

| Measurement | Observation | Practical meaning |
| --- | --- | --- |
| First update | 5 entries, 1 new update commit | A real README update occurred. |
| Immediate unchanged rerun | 0 additional update commits | The tested rerun avoided redundant commit history. |
| Scheduled run #6 | 5 displayed entries, no content change or commit | A scheduler-triggered execution preserved unchanged content. |
| Negative marker experiment | Failure followed by success after correction | Validation detected the missing marker before merge. |
| Unit tests | 14 passed | This is a test count, not a coverage percentage. |

No baseline for manual effort was collected, so no time-saving or productivity percentage is claimed.

## Follow-up maintenance

The proposed maintenance updates pin Actions to full SHAs, use upload-artifact v7.0.1 (Node 24), select ubuntu-24.04, request 90-day retention for new artifacts, and add workflow status badges. New runs must verify these changes after implementation; older screenshots accurately retain their original warnings.

The repository intentionally retains direct pushes and does not enforce required checks. The private project board remains documented by screenshots.

For the exact push-step code and token boundary, see [security evidence](security-evidence.md).
