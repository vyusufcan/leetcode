# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Solutions

Each problem lives in its own directory with a `main.py`. Run any solution directly:

```powershell
python two_sums/main.py
python palindrome/main.py
```

No build step, no test framework, no dependencies — pure Python.

## Structure

One directory per LeetCode problem, each containing a single `main.py`:

```
<problem-slug>/
    main.py    # Solution class + inline example assertions at the bottom
```

## Conventions

- Solutions use the LeetCode `class Solution` pattern with method signatures matching the problem.
- Example test cases are included inline at the bottom of each file (not in a separate test file), using `print()` calls with expected output in comments.
- Problem constraints and examples are copied as comments at the top of the file.

## Notes Vault

`solutions/` is an Obsidian vault (practice questions, notes). `.obsidian/workspace.json` is gitignored — it's local UI state, not vault content.

## GitHub

- Remote: `git@github-personal:vyusufcan/leetcode.git`
- SSH Host: `github-personal` (defined in `~/.ssh/config`, uses `~/.ssh/id_ed25519_github`)
- Push: `git push origin main`

## Practice Sessions

When asking the user coding questions:

- Each question gets its own folder under `practice/q<n>_<slug>/`
- Only Python solutions (`main.py`) — no Go
- Check `solutions/Practice Questions.md` before asking a new question — never repeat a question already listed there
- After asking a new question, add it to that file immediately
- Expected output from functions is always `return`, not `print`
