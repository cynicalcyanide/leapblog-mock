# The Leap Journal — mock rehearsal site

A full-featured mock of the planned Leap Journal migration to Quarto (Middle-earth edition).
Live at: https://cynicalcyanide.github.io/leapblog-mock/

Exercises: listings, announcements, author tile pages, Giscus comments, copyable
citation/BibTeX blocks, Typst PDF downloads, search, topic/author filtering, and an
executable Plotly chart (cached via `freeze`).

## Local development

```sh
python3.13 -m venv .venv && ./.venv/bin/pip install jupyter plotly pandas
# (note: the Homebrew python@3.14 on this machine has a broken pyexpat — use 3.13)
QUARTO_PYTHON=.venv/bin/python quarto preview
```

Publishing: push to `main` — GitHub Actions renders and deploys to `gh-pages`.
If you edit the Python chart, re-render locally first so `_freeze/` is updated and committed
(CI has no Python on purpose).
