# Roadmap - APP FACTORY VIDEO IA

## Phase 0 - Repository Foundation

- Create official repository structure.
- Define documentation standards.
- Establish architecture boundaries.
- Prepare project for FastAPI, React, PostgreSQL, Redis, and Celery.
- Keep the repository free of product logic until the architecture is approved.

Status: in progress.

## Phase 1 - Architecture Documentation

- Define enterprise architecture in `docs/`.
- Define API design principles.
- Define database model and migration strategy.
- Define AI workflow and provider abstraction.
- Define compliance and official API rules.
- Define deployment and infrastructure direction.

## Phase 2 - Backend Foundation

- Create FastAPI project skeleton.
- Add configuration management.
- Add health check only after approval.
- Add PostgreSQL connection layer.
- Add migration tooling.
- Add service/module boundaries.

No business endpoints should be created until the core contracts are approved.

## Phase 3 - Frontend Foundation

- Create React project skeleton.
- Establish design system direction.
- Add routing structure.
- Add API client boundary.
- Add authentication-ready shell.

No product screens should be implemented until UX scope is approved.

## Phase 4 - Async Processing Foundation

- Create Celery worker skeleton.
- Define queues by responsibility.
- Add Redis broker configuration.
- Add scheduler design for channel timezones.
- Add task observability patterns.

## Phase 5 - MVP Workflow

- Channel configuration.
- Simulated trend analysis.
- Simulated script generation.
- Simulated voice, subtitles, and video states.
- Manual review workflow.
- Audit log for each automation run.

## Phase 6 - AI and Media Pipeline

- Add real AI provider adapters.
- Add prompt/version management.
- Add cultural localization workflow.
- Add voice generation workflow.
- Add subtitle generation workflow.
- Add FFmpeg media composition.

## Phase 7 - Official Integrations

- Add OAuth flows.
- Add official YouTube integration.
- Add official Meta integrations for Instagram and Facebook.
- Add official TikTok integration when access is approved.
- Add platform quota and retry handling.

## Phase 8 - SaaS Scale

- Multi-organization support.
- Plans and usage limits.
- Billing readiness.
- Horizontal workers.
- Advanced observability.
- Backups and recovery.
- More languages, countries, niches, and channels.
