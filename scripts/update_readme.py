"""Generate a deterministic activity section using only Python's standard library."""
import argparse
import difflib
import html
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

START = '<!-- ACTIVITY:START -->'
END = '<!-- ACTIVITY:END -->'
BOT_COMMIT = 'chore(readme): refresh repository activity [skip ci]'


class SafeError(ValueError):
    """A diagnostic written by this application, safe to show in CI."""


def validate(text):
    if text.count(START) != 1 or text.count(END) != 1:
        raise SafeError('README must contain exactly one START marker and one END marker.')
    if text.index(START) > text.index(END):
        raise SafeError('README activity markers are in the wrong order.')
    for marker in (START, END):
        if marker not in text.splitlines():
            raise SafeError('Each activity marker must occupy its own line.')


def replace_section(text, section):
    validate(text)
    a = text.index(START) + len(START)
    b = text.index(END)
    newline = '\r\n' if '\r\n' in text else '\n'
    return text[:a] + newline + section.replace('\n', newline) + newline + text[b:]


def excluded(item):
    message = item['commit']['message'].splitlines()[0]
    author = item.get('author') or {}
    return (message == BOT_COMMIT or author.get('type') == 'Bot'
            or author.get('login', '').endswith('[bot]'))


def safe_title(message):
    title = (message.splitlines() or ['(no subject)'])[0][:160]
    title = ''.join(c for c in title if c.isprintable())
    title = html.escape(title, quote=True)
    for char in ('\\', '`', '*', '_', '[', ']', '|', '~'):
        title = title.replace(char, '&#%d;' % ord(char))
    return title


def render(items, repo):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise SafeError('Invalid repository name.')
    rows = []
    for item in items:
        sha = item['sha']
        date = item['commit']['committer']['date'][:10]
        if not re.fullmatch(r'[0-9a-f]{40}', sha) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
            raise SafeError('Invalid commit data.')
        title = safe_title(item['commit']['message'])
        rows.append(f'- {date} — {title} ([{sha[:7]}](https://github.com/{repo}/commit/{sha}))')
    return '\n'.join(rows) if rows else 'No eligible commits found.'


def api_commits(repo, ref, page, token):
    query = urllib.parse.urlencode({'sha': ref, 'per_page': 100, 'page': page})
    url = f'https://api.github.com/repos/{repo}/commits?{query}'
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'a3-readme-updater'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        raise SafeError(f'GitHub API returned HTTP {exc.code}; README was not changed.') from None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        raise SafeError('Could not retrieve valid GitHub data; README was not changed.') from None
    if not isinstance(data, list):
        raise SafeError('Unexpected GitHub API response; README was not changed.')
    return data


def collect(repo, ref, token, fetch=api_commits):
    selected, scanned, skipped = [], 0, 0
    for page in range(1, 11):
        batch = fetch(repo, ref, page, token)
        for item in batch:
            scanned += 1
            if excluded(item):
                skipped += 1
            else:
                selected.append(item)
                if len(selected) == 5:
                    return selected, scanned, skipped
        if len(batch) < 100:
            return selected, scanned, skipped
    raise SafeError('Scan limit exceeded; README was not changed.')


def generate(path, repo, ref, token, preview=False, outdir=Path('artifacts'), fetch=api_commits):
    original = path.read_bytes().decode('utf-8')
    validate(original)  # Validate before any network access.
    items, scanned, skipped = collect(repo, ref, token, fetch)
    updated = replace_section(original, render(items, repo))
    changed = updated != original
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / 'README.preview.md').write_bytes(updated.encode('utf-8'))
    diff = ''.join(difflib.unified_diff(original.splitlines(True), updated.splitlines(True),
                                       fromfile='README.md', tofile='README.preview.md'))
    (outdir / 'README.diff').write_text(diff, encoding='utf-8')
    metrics = {'scanned': scanned, 'excluded': skipped, 'displayed': len(items),
               'changed': changed, 'preview_only': preview}
    (outdir / 'metrics.json').write_text(json.dumps(metrics, indent=2), encoding='utf-8')
    if not preview and changed:
        path.write_bytes(updated.encode('utf-8'))
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--validate-only', action='store_true')
    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--repo', default=os.environ.get('GITHUB_REPOSITORY', ''))
    parser.add_argument('--ref', default='main')
    args = parser.parse_args()
    try:
        if args.validate_only:
            validate(Path('README.md').read_bytes().decode('utf-8'))
            print('README markers: valid')
            return
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
            raise SafeError('Set --repo to OWNER/REPOSITORY.')
        metrics = generate(Path('README.md'), args.repo, args.ref, os.environ.get('GH_TOKEN', ''), args.preview)
        print(json.dumps(metrics))  # Counts only; never tokens or raw API responses.
        if os.environ.get('GITHUB_STEP_SUMMARY'):
            with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
                summary.write('## README activity result\n\n')
                for key, value in metrics.items():
                    summary.write(f'- {key}: {value}\n')
    except SafeError as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    except (ValueError, KeyError, TypeError, IndexError, UnicodeError, OSError):
        # Exceptions can contain response text or local information; use a safe generic error.
        print('ERROR: README update failed. Check markers, token access, API availability, and data format. No API response or token is logged.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main() or 0)
