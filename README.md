# APP FACTORY VIDEO IA

APP FACTORY VIDEO IA is the official repository for a global, multilingual, scalable SaaS platform by AppFactoryChile.

The platform is planned to analyze global and local trends, generate original AI-assisted video content in multiple languages, prepare natural voiceovers, subtitles, automated editing workflows, scheduled publishing, and future social distribution through official APIs.

This repository is intentionally in an architecture-first stage. It contains the base project organization and documentation needed to begin development cleanly. It does not yet implement backend services, frontend screens, workers, endpoints, schedulers, or platform integrations.

## Company

AppFactoryChile

Primary contact:

```text
appfactorychile@gmail.com
```

## Product Vision

APP FACTORY VIDEO IA is designed to operate by country, language, niche, channel, timezone, platform, and editorial rules.

Initial languages planned:

- Spanish.
- English.
- Portuguese.
- French.
- Italian.
- German.

The architecture must support adding more languages and regions over time without redesigning the platform.

## Planned Daily Automation

Each channel will eventually run according to its own timezone:

- 08:00: analyze global/local trends, generate 2 videos, and publish.
- 13:00: analyze global/local trends, generate 2 videos, and publish.
- 17:00: analyze global/local trends, generate 2 videos, and publish.
- 21:00: analyze global/local trends, generate 2 videos, and publish.

Expected result:

```text
4 daily blocks x 2 videos per block = 8 videos per day per channel
```

## Suggested Stack

- Backend: FastAPI.
- Frontend: React.
- Database: PostgreSQL.
- Cache and queues: Redis.
- Workers: Celery.
- Media processing: FFmpeg.
- Storage: cloud object storage.
- Infrastructure: Docker and cloud-ready deployment.

## Repository Structure

```text
app/           Global application composition and future orchestration layer.
backend/       FastAPI backend service.
frontend/      React dashboard.
workers/       Celery workers and async processing units.
ai/            AI provider adapters, prompts, localization, voice, and video logic.
scheduler/     Timezone-aware automation scheduling.
integrations/  Official API integrations for social platforms and external services.
storage/       Storage adapters and media asset organization.
database/      Database models, migrations, seeds, and schema documentation.
shared/        Shared contracts, constants, schemas, and utilities.
tests/         Automated tests.
scripts/       Developer and operational scripts.
infra/         Infrastructure, Docker, deployment, and environment resources.
docs/          Project documentation and architecture notes.
```

## Ethical and Compliance Rules

The platform must be designed around responsible automation:

- Use official APIs for publishing and metrics.
- Do not use unauthorized bots.
- Do not generate fake views, likes, comments, followers, or engagement.
- Do not manipulate algorithms.
- Do not copy copyrighted content.
- Do not impersonate people, brands, or institutions.
- Do not clone or imitate real voices without authorization.
- Keep traceability for trends, scripts, videos, publications, and metrics.

## Current Stage

Status: repository architecture base.

No application logic exists yet. The next step is to complete architectural documentation before implementing the first MVP components.
