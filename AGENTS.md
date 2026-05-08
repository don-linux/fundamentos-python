# AGENTS.md

## Repo Shape
- This repo is course material: root-level `*.ipynb` notebooks are the main source of truth, plus one standalone script, `26 Funciones.py`.
- Keep the existing Spanish filenames and lesson numbering intact unless the user explicitly asks for a reorganization.

## Editing Rules
- Edit notebooks carefully as JSON; prefer notebook-aware edits and avoid touching unrelated cells or metadata.
- Keep changes localized to the lesson being worked on. Do not split this repo into packages or add new tooling unless requested.

## Commands
- There is no repo-defined `pyproject.toml`, requirements file, test suite, CI workflow, or `opencode.json` here.
- Do not guess build/test/lint commands; verify changes directly against the file you edited.

## Small Gotchas
- `README.md` is only a title, so the notebooks themselves are the documentation.
- `.gitignore` already excludes `.env`, `.venv/`, `node_modules/`, logs/tmp files, and `test.py`/`test.ipynb`; avoid using those names for real work.
