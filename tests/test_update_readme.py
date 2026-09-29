from contextlib import contextmanager
import shutil
import unittest
import uuid
from pathlib import Path
from scripts.update_readme import (START, END, BOT_COMMIT, collect, excluded,
                                   generate, render, replace_section, validate)


@contextmanager
def test_folder():
    # Use inherited directory permissions, including in restricted Windows runners.
    root = (Path.cwd() / '.test-work').resolve()
    root.mkdir(exist_ok=True)
    folder = root / uuid.uuid4().hex
    folder.mkdir()
    try:
        yield folder
    finally:
        resolved = folder.resolve()
        if resolved.parent != root:
            raise RuntimeError('Unexpected test cleanup path.')
        shutil.rmtree(resolved)


def commit(n=1, message='Add documentation', bot=False):
    return {'sha': f'{n:040x}', 'author': {'type': 'Bot' if bot else 'User', 'login': 'demo'},
            'commit': {'message': message, 'committer': {'date': '2026-09-29T01:00:00Z'}}}


class ReadmeTests(unittest.TestCase):
    def setUp(self):
        self.text = f'# Handwritten introduction\n\n{START}\nold\n{END}\n\nKeep this footer.\n'

    def test_valid_markers(self):
        validate(self.text)

    def test_missing_marker(self):
        with self.assertRaises(ValueError): validate(self.text.replace(END, ''))

    def test_duplicate_marker(self):
        with self.assertRaises(ValueError): validate(self.text + START)

    def test_reversed_markers(self):
        with self.assertRaises(ValueError): validate(END + '\n' + START)

    def test_inline_marker(self):
        with self.assertRaises(ValueError): validate(self.text.replace(START, 'prefix ' + START))

    def test_preserves_outside_content(self):
        result = replace_section(self.text, 'new activity')
        self.assertEqual(result.split(START)[0], self.text.split(START)[0])
        self.assertEqual(result.split(END)[1], self.text.split(END)[1])

    def test_crlf_preservation(self):
        source = self.text.replace('\n', '\r\n')
        result = replace_section(source, 'one\ntwo')
        self.assertNotIn('\n', result.replace('\r\n', ''))

    def test_idempotent_render(self):
        body = render([commit()], 'demo/repo')
        once = replace_section(self.text, body)
        self.assertEqual(once, replace_section(once, body))

    def test_excludes_own_update_and_bots(self):
        self.assertTrue(excluded(commit(message=BOT_COMMIT)))
        self.assertTrue(excluded(commit(bot=True)))
        self.assertFalse(excluded(commit()))

    def test_title_escaping(self):
        result = render([commit(message='<script>[bad](url) | *x*\nprivate body')], 'demo/repo')
        self.assertNotIn('<script>', result)
        self.assertNotIn('[bad]', result)
        self.assertNotIn('private body', result)

    def test_pagination_after_100_bot_commits(self):
        def fetch(repo, ref, page, token):
            return [commit(bot=True) for _ in range(100)] if page == 1 else [commit(i) for i in range(1, 7)]
        items, scanned, skipped = collect('demo/repo', 'main', '', fetch)
        self.assertEqual((len(items), scanned, skipped), (5, 105, 100))

    def test_api_failure_does_not_write(self):
        def fail(*args): raise ValueError('Simulated API failure')
        with test_folder() as folder:
            path = Path(folder) / 'README.md'; path.write_text(self.text, encoding='utf-8')
            with self.assertRaises(ValueError):
                generate(path, 'demo/repo', 'main', '', outdir=Path(folder)/'out', fetch=fail)
            self.assertEqual(path.read_text(encoding='utf-8'), self.text)

    def test_preview_does_not_write(self):
        with test_folder() as folder:
            path = Path(folder) / 'README.md'; path.write_text(self.text, encoding='utf-8')
            metrics = generate(path, 'demo/repo', 'main', '', preview=True,
                               outdir=Path(folder)/'out', fetch=lambda *a: [commit()])
            self.assertTrue(metrics['changed'])
            self.assertEqual(path.read_text(encoding='utf-8'), self.text)
            self.assertTrue((Path(folder)/'out'/'README.preview.md').exists())

    def test_unchanged_rerun_even_with_new_bot_commit(self):
        with test_folder() as folder:
            path = Path(folder) / 'README.md'; path.write_text(self.text, encoding='utf-8')
            kwargs = {'outdir': Path(folder)/'out'}
            first = generate(path, 'demo/repo', 'main', '', fetch=lambda *a: [commit()], **kwargs)
            second = generate(path, 'demo/repo', 'main', '',
                              fetch=lambda *a: [commit(2, BOT_COMMIT), commit()], **kwargs)
            self.assertTrue(first['changed']); self.assertFalse(second['changed'])


if __name__ == '__main__': unittest.main()
