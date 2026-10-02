# Writer token boundary

The following is the complete push-step excerpt from `.github/workflows/update-readme.yml`. The secret reference is a variable name, not a token value.

```yaml
      - name: Commit README only when changed
        env:
          REPO_TOKEN: ${{ secrets.REPO_TOKEN }}
        shell: bash
        run: |
          set -euo pipefail
          if git diff --quiet -- README.md; then
            echo 'No content change; no commit created.'
            echo '- update_commit_created: false' >> "$GITHUB_STEP_SUMMARY"
            exit 0
          fi
          if [ -z "$REPO_TOKEN" ]; then
            echo 'REPO_TOKEN is missing. Add the repository secret.'
            exit 1
          fi
          git config user.name 'github-actions[bot]'
          git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
          git add -- README.md
          git commit -m 'chore(readme): refresh repository activity [skip ci]'
          askpass="$RUNNER_TEMP/a3-askpass.sh"
          trap 'rm -f "$askpass"' EXIT
          cat > "$askpass" <<'ASKPASS'
          #!/bin/sh
          case "$1" in
            *Username*) printf '%s\n' 'x-access-token' ;;
            *Password*) printf '%s\n' "$REPO_TOKEN" ;;
          esac
          ASKPASS
          chmod 700 "$askpass"
          GIT_ASKPASS="$askpass" GIT_TERMINAL_PROMPT=0 git push origin HEAD:main
          echo '- update_commit_created: true' >> "$GITHUB_STEP_SUMMARY"
          echo "- update_commit_sha: $(git rev-parse HEAD)" >> "$GITHUB_STEP_SUMMARY"
```

## What the evidence establishes

- The `env` block belongs to this step. The YAML does not inject REPO_TOKEN at workflow or job scope.
- The preceding API step uses `GH_TOKEN: ${{ github.token }}`.
- Checkout uses `persist-credentials: false`.
- Only README.md is staged. A no-change run exits before committing or pushing.
- The askpass helper returns credentials to Git via its authentication channel. Shell tracing is off, the token is absent from the remote URL, and the helper file contains only the environment-variable reference.
- The workflow's `contents: read` applies to GITHUB_TOKEN. The PAT separately has Contents read/write for this one repository.
- The PR workflow has no REPO_TOKEN reference and no push step.

Step-scoped injection reduces unnecessary exposure but is not a security boundary against malicious code already running on a compromised runner. Review workflow and script changes before merging them. This repository currently does not enforce that review through required checks.

[Writer workflow](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/blob/main/.github/workflows/update-readme.yml)  
[PR workflow](https://github.com/wagyboy/VR-Petanque-Activity-Dashboard/blob/main/.github/workflows/validate-readme.yml)
