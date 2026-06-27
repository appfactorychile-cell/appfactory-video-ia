# Contributing - APP FACTORY VIDEO IA

## Purpose

This repository is the official development home for APP FACTORY VIDEO IA. Contributions must preserve a clean, modular, scalable architecture prepared for long-term SaaS growth.

## Required Checks Before Changes

Before making any change, verify:

```bash
git remote -v
git branch --show-current
git status --short --branch
```

The remote must point to:

```text
https://github.com/appfactorychile-cell/appfactory-video-ia.git
```

If the repository is not `appfactory-video-ia`, stop immediately.

## Development Rules

- Work only in this repository for this project.
- Do not use files from VENTAPRO, SKANO, or unrelated projects.
- Read existing documentation before creating code.
- Keep modules separated by responsibility.
- Do not create product logic before the architecture and scope are approved.
- Do not create endpoints, screens, workers, or integrations during documentation-only phases.
- Keep secrets out of Git.
- Keep each important change documented and explain why it exists.

## Architecture Principles

- Backend logic belongs in `backend/`.
- Frontend logic belongs in `frontend/`.
- Worker logic belongs in `workers/`.
- AI provider abstractions belong in `ai/`.
- Schedulers belong in `scheduler/`.
- External APIs belong in `integrations/`.
- Storage adapters belong in `storage/`.
- Database models and migrations belong in `database/`.
- Shared contracts belong in `shared/`.
- Tests belong in `tests/`.
- Infrastructure belongs in `infra/`.
- Documentation belongs in `docs/`.

## Compliance Rules

Contributions must not add functionality for:

- Unauthorized bots.
- Fake views or fake engagement.
- Algorithm manipulation.
- Copyright copying.
- Impersonation.
- Unauthorized voice cloning.
- Publishing through unofficial or prohibited methods.

Official APIs and clear audit trails are mandatory for future publishing functionality.
