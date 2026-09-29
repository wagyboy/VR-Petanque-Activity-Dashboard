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

The workflow includes a daily schedule. Scheduled execution is not claimed as verified by the manual-run evidence above.

These results demonstrate content updates, an unchanged rerun, validation failure and recovery, and issue closure. They do not establish general productivity or delivery-speed improvements.
