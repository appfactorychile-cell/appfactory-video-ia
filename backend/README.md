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
- `GET /api/pipeline` - list simulated pipeline runs.`r`n- `POST /api/pipeline/start` - simulate the production pipeline.`r`n- `POST /api/content-brain/analyze` - transform an opportunity into a complete mock editorial strategy.`r`n- `POST /api/content-brain/recommend` - explain why the selected idea is best and how it should be produced.`r`n- `POST /api/content-brain/storyboard` - generate a mock storyboard, narration, subtitles and CTA.`r`n- `POST /api/content-brain/production-plan` - return the mock narrator, visual style, camera, music, platforms and duration.

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

## AI Agents Platform Routes

The mock AI company is exposed under the `AI Agents Platform` Swagger tag:

- `GET /api/agents` - list the Director General IA and all specialized agents.
- `GET /api/agents/status` - show availability, average time and simulated load.
- `POST /api/agents/simulate` - simulate a coordinated mission from Director IA to final result.
- `GET /api/agents/{agent_name}` - inspect one agent by slug or name.

The module is mock-only. It does not call OpenAI, Gemini, external APIs, video generators, audio providers or publishing services.

## Project Source Library Routes

Projects are optional. APP FACTORY VIDEO IA can work in `Contenido global` mode without any linked project, or in `Proyecto vinculado` mode using only authorized project sources.

- `GET /api/projects` - list mock projects.
- `POST /api/projects` - create a mock project.
- `GET /api/projects/active` - show current source mode and active project.
- `POST /api/projects/deactivate` - return to global content mode.
- `GET /api/projects/supported-sources` - list document types prepared for future parsing.
- `GET /api/projects/{project_id}` - inspect a project, documents, sources and mock memory.
- `DELETE /api/projects/{project_id}` - delete a mock project.
- `POST /api/projects/{project_id}/documents` - register a document without processing it.
- `GET /api/projects/{project_id}/documents` - list registered documents.
- `POST /api/projects/{project_id}/activate` - activate project-linked mode.
