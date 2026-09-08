# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## State of the repository

This is a freshly scaffolded Django 4.2.7 project with essentially no application code yet. Every module in the `transit` app is still the `startapp` boilerplate: `models.py`, `views.py`, `admin.py`, and `tests.py` contain only imports and "Create your ... here" comments, `transit/urls.py` is empty, `transit/migrations/` has no migrations, and `transit/templates/transit/transit.html` is a zero-byte file. `db.sqlite3` exists but is empty (0 bytes) — migrations have never been run.

Treat almost any request here as greenfield work rather than a change to existing behavior.

## Commands

Django is installed against the system `python3` (no virtualenv is checked in or present in the working tree).

```bash
python3 manage.py runserver          # dev server on http://127.0.0.1:8000/
python3 manage.py makemigrations transit
python3 manage.py migrate            # required before first run — db.sqlite3 is empty
python3 manage.py createsuperuser    # needed to reach /admin/
python3 manage.py shell
python3 manage.py check
```

Tests use Django's built-in runner (no pytest configured):

```bash
python3 manage.py test                                   # all tests
python3 manage.py test transit                           # one app
python3 manage.py test transit.tests.SomeTestCase.test_x  # single test
```

There is no linter, formatter, or CI configuration in the repo.

## Structure

- `LagosTransit/` — project package: `settings.py`, root `urls.py`, `wsgi.py`/`asgi.py`.
- `transit/` — the single application, already listed first in `INSTALLED_APPS`.

Wiring that still needs to be done when adding the first view: `LagosTransit/urls.py` currently routes only `admin/` and does **not** yet `include('transit.urls')`, even though `include` is already imported. Templates resolve via `APP_DIRS` (`TEMPLATES['DIRS']` is empty), so app-level `transit/templates/transit/` is the right place for them.

## Settings caveats

`settings.py` is unmodified `startproject` output: `DEBUG = True`, a hardcoded `django-insecure-` `SECRET_KEY`, empty `ALLOWED_HOSTS`, SQLite, and `TIME_ZONE = 'UTC'` (not `Africa/Lagos`, despite the project name). Flag these rather than silently relying on them if work moves toward deployment.
