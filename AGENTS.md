# Project Guidelines

This repository is a FastAPI boilerplate with an optional Vue 3 frontend. It
is intended to be copied and extended for small API projects, not shipped as a
finished product. Keep changes focused on making the template easier to reuse.

## Repository Layout

- `backend/main.py` is the FastAPI application entry point.
- `backend/src/` contains application code: models, routers, dependencies,
  settings, logging, and exceptions.
- `backend/tests/` contains pytest tests organized to mirror the backend
  modules, with shared fixtures in `backend/tests/conftest.py`.
- `frontend/` contains the Vue 3 and Vite application.
- `docker/` contains the backend and frontend Dockerfiles and Compose files.
- `docs/adr/` records architectural decisions. Update or add an ADR when a
  structural decision changes. Also, review the relevant ADRs to understand the rationale behind existing decisions.
- `taskfile.yaml` is the preferred command entry point for backend workflows.

## Working Rules

- Preserve the existing backend structure and public behavior unless the task
  explicitly requires a change.
- Use type hints in new Python code, including tests. Pyrefly is the project's
  type checker; do not silently replace it with mypy or another checker.
- Use Pydantic models for validated API data and settings, FastAPI routers for
  HTTP endpoints, and the existing exception and logging abstractions.
- Keep tests in `backend/tests/unit/` alongside the corresponding source area.
  Add tests for new branches and behavior rather than relying only on happy
  path coverage.
- Use Ruff for Python linting and formatting. The configured target is Python
  3.14 with an 80-character line length and double-quoted strings.
- Use the existing Vue/Vite conventions in `frontend/src/`; do not introduce a
  second frontend framework or package manager.
- Follow the repository's Conventional Commits convention when creating
  commits. Do not create branches or commits as part of an implementation task
  unless explicitly requested.

## Commands

The commands below assume the required tools are installed.

### Backend via Taskfile

Run these from the repository root:

```text
task init              # install Poetry dependencies and install pre-commit hooks
task lint              # Ruff lint check and formatting check
task hint              # Pyrefly type check
task test              # pytest with the configured coverage settings
task coverage          # pytest plus an HTML coverage report
task ci                # run the same restrictive checks as GitHub Actions
task frontend:init     # install frontend dependencies
task frontend:dev      # start the Vite development server
task frontend:build    # build the frontend
task frontend:preview  # preview the frontend production build
task docker:build      # build the Compose services
task docker:up         # start the Compose services
task docker:down       # stop and remove the Compose services
task docker:ps         # list the Compose services
```

The frontend and Docker tasks use the existing `frontend/` directory and
`docker/compose.yaml` file.
The developer tasks run in their service directories; `task ci` intentionally
runs from the repository root to match GitHub Actions. A command that passes in
one context may not pass in the other.

### Frontend

Run from `frontend/`:

```text
npm install
npm run dev
npm run build
npm run preview
```

The Vite development server is configured for port `8999`.

### Docker Compose

The Compose file is not at the repository root, so include its path when
running commands from the root:

```text
docker compose -f docker/compose.yaml build
docker compose -f docker/compose.yaml up -d
docker compose -f docker/compose.yaml down
docker compose -f docker/compose.yaml ps
```

The backend serves on port `8000` and the frontend on port `8999`. The Compose
services bind-mount source directories and are intended for development.
`docker/compose-prod.yaml` is currently a comment-only placeholder; no
production Compose deployment is documented yet.

## Validation Expectations

- Backend pytest configuration enables coverage and currently fails below
  100% coverage. Treat that as a required gate for backend changes.
- Before considering a Python change complete, run the narrowest relevant test,
  then `task ci` when the environment permits. `task ci` mirrors the GitHub
  Actions checks and installs dependencies from
  `backend/requirements-dev.txt`.
- Frontend currently exposes build and preview commands but no frontend test
  command. Do not claim frontend behavior is tested unless a test tool is
  added and used.
- End-to-end testing is not currently available; backend unit/functional tests
  do not replace browser or cross-service verification.

## Dependency Changes

There are two dependency paths that must remain consistent:

- Local Poetry configuration: `backend/pyproject.toml`.
- Docker and CI requirements: `backend/requirements.txt` and
  `backend/requirements-dev.txt`.

When changing a backend dependency, update the applicable files together and
check the Dockerfile, Taskfile, CI workflow, and pre-commit configuration.
Pyrefly's pre-commit hook has its own `additional_dependencies` list; missing
runtime dependencies there can cause type-checking failures even when Poetry
works locally.

## Files Requiring Care

- Treat `backend/pyproject.toml`, `.pre-commit-config.yaml`,
  `.github/workflows/python-app.yaml`, `taskfile.yaml`, and `docker/*` as
  workflow configuration. Change them deliberately and validate the affected
  command afterward.
- Do not edit generated or cached output such as `backend/htmlcov/`, coverage
  XML/data files, `.mypy_cache/`, `.ruff_cache/`, `__pycache__/`, or
  `frontend/node_modules/`. These paths are explicitly ignored by
  `.gitignore` and should be regenerated.
- Keep secrets out of source and local `.env` files out of version control.
