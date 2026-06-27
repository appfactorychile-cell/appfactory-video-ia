# Backend - APP FACTORY VIDEO IA

FastAPI backend foundation for APP FACTORY VIDEO IA.

This module is an MVP base with mock data only. It does not connect to a real database, external APIs, AI providers, workers, publishing platforms or authentication providers yet.

## Run Locally

From this directory:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Default local URL:

```text
http://127.0.0.1:8000
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## Available Routes

- `GET /health` - service health check.
- `GET /api/channels` - list mock channels.
- `POST /api/channels` - create an in-memory mock channel.
- `GET /api/opportunities` - list analyzed mock opportunities.
- `POST /api/opportunities/analyze` - return a simulated opportunity score.
- `POST /api/editorial/recommend` - return a mock editorial recommendation.
- `POST /api/content/idea` - generate a mock content idea.
- `POST /api/content/script` - generate a mock 20 to 45 second script.
- `GET /api/pipeline` - list simulated pipeline runs.
- `POST /api/pipeline/start` - simulate the production pipeline.`r`n- `POST /api/content-brain/analyze` - transform an opportunity into a complete mock editorial strategy.`r`n- `POST /api/content-brain/recommend` - explain why the selected idea is best and how it should be produced.`r`n- `POST /api/content-brain/storyboard` - generate a mock storyboard, narration, subtitles and CTA.`r`n- `POST /api/content-brain/production-plan` - return the mock narrator, visual style, camera, music, platforms and duration.

## Simulated Pipeline

The current mocked production flow is:

```text
Opportunity -> Editorial -> Story -> Script -> Voice -> Video -> Subtitles -> Quality -> Schedule
```

Each step includes a status, estimated processing time and responsible AI role.

## Architecture Direction

The backend is organized to grow toward:

- PostgreSQL persistence.
- Redis cache and queues.
- Celery workers.
- Official social platform APIs.
- Real AI provider adapters.
- Auditable content and publishing workflows.

## Compliance Boundaries

This MVP base must remain responsible and mock-only:

- No fake engagement.
- No unauthorized bots.
- No real publishing.
- No copyrighted content copying.
- No real credentials in the repository.
- No external API calls.


## MVP Workflow Routes

The first complete user flow is exposed under the `Workflow` Swagger tag:

- `POST /api/workflow/create-channel` - create a temporary channel workflow.
- `POST /api/workflow/analyze-opportunity` - analyze the saved channel opportunity.
- `POST /api/workflow/generate-ideas` - generate 10 mock editorial ideas.
- `POST /api/workflow/choose-idea` - save the selected idea in workflow state.
- `POST /api/workflow/generate-hooks` - generate 5 hook options.
- `POST /api/workflow/choose-hook` - save the selected hook in workflow state.
- `POST /api/workflow/generate-story` - generate story strategy and a 4-scene storyboard.
- `POST /api/workflow/generate-production-plan` - generate the mock production plan.
- `POST /api/workflow/ready-to-generate` - mark the workflow ready without generating video.
- `GET /api/workflow/{workflow_id}` - inspect temporary workflow state.
