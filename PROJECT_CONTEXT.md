# APP FACTORY VIDEO IA - Project Context

## Vision

APP FACTORY VIDEO IA is a global SaaS platform by AppFactoryChile for intelligent content creation. The platform is designed to analyze opportunities, plan editorial strategy, compose animated scenes, prepare narration, render vertical videos, and learn from results over time.

The current strategic direction prioritizes a proprietary animated video engine. Hyperrealistic video remains a future expansion path, but the core product now focuses on professional animated videos generated locally through modular engines.

## Company

- Parent company: AppFactoryChile
- Main contact: appfactorychile@gmail.com
- Official repository: https://github.com/appfactorychile-cell/appfactory-video-ia
- Local path: C:\src\appfactory-video-ia

## Architecture

The project follows a modular SaaS architecture prepared for FastAPI, React, PostgreSQL, Redis, Celery, FFmpeg, cloud storage, AI providers, and official social media APIs.

Current backend architecture is FastAPI-based and organized by domain modules:

- `agents`: AI agent coordination mock platform.
- `ai`: AI Provider Platform abstraction.
- `animation`: animated video planning, scene composition, and timeline.
- `characters`: reusable character library, poses, expressions, gestures, and lip-sync planning.
- `image_video`: image-to-video local MP4 generation.
- `intelligence`: global opportunity and executive decision mock engine.
- `motion`: motion graphics, camera, layouts, animation and transition catalog.
- `narration`: local mock narration, script segmentation, voice planning, timing and subtitles.
- `production`: AI production pipeline mock.
- `projects`: optional Project Source Library.
- `render`: FFmpeg detection and MP4 render pipeline.

The frontend prototype is currently a static, navigable SaaS dashboard in `frontend/prototype/`, using mock and backend data through `fetch()`.

## Completed Phases

- Phase 1: Professional planning and repository structure.
- Phase 2: Premium visual SaaS prototype.
- Phase 3: FastAPI mock backend and MVP workflow.
- Phase 4: AI Agents Platform mock.
- Phase 5: Optional Project Source Library.
- Phase 6: PostgreSQL persistence layer.
- Phase 6.2: Global Opportunity Intelligence.
- Phase 7: AI Production Engine.
- Phase 7.1: AI Provider Platform for OpenAI architecture.
- Phase 8: Animated Video Engine foundation.
- Phase 8.1: Animated Scene Composer.
- Phase 8.2: Animation Timeline.
- Phase 8.3: FFmpeg integration and first real MP4 render.
- Phase 9: Motion Graphics Engine.
- Phase 9.1: Image to Animated Video Engine.
- Phase 9.2: Character Animation Engine.
- Phase 9.3: Narration Engine with local mock audio planning.

## Current Generation Flow

1. User creates or selects a content idea.
2. Global Opportunity Intelligence audits if it is worth producing.
3. Content Brain plans ideas, hooks, story and production strategy.
4. Scene Composer turns the storyboard into 9:16 visual scenes.
5. Character Engine assigns reusable characters, gestures, poses and lip-sync plans.
6. Narration Engine segments the script, plans voice, timing and subtitles.
7. Animation Timeline aligns scenes, character tracks, voice tracks and subtitles.
8. Motion Graphics Engine applies layouts, camera movements, particles and transitions.
9. Render Engine uses FFmpeg to generate a local MP4.
10. Learning systems will later evaluate performance and improve future decisions.

## Current Render Capabilities

- Local FFmpeg detection.
- Real MP4 output at `output/video_0001.mp4`.
- Vertical 9:16 format.
- 720x1280 resolution.
- Four animated scenes.
- Motion graphics.
- Reusable vector-style characters.
- Mock narration timeline.
- Synchronized subtitle planning.
- No real TTS provider yet.
- No external video or audio APIs yet.

## Data and Persistence

PostgreSQL persistence was introduced for core entities. Some newer engines still use in-memory mock stores while their architecture matures. Generated files are kept out of Git through ignored folders such as `generated/`, `uploads/`, and media extensions.

## Conventions

- Work only inside `C:\src\appfactory-video-ia`.
- Do not use files from unrelated projects.
- Verify `git remote -v`, current branch and `git status` before changes.
- Do not commit or push without explicit approval.
- Do not store real credentials in code.
- Use official APIs only when real integrations are introduced.
- No fake views, fake engagement, algorithm manipulation or copyrighted copying.
- Keep modules clean, modular and prepared for future providers.

## Current Status

The platform has a professional prototype, a modular FastAPI backend, PostgreSQL persistence groundwork, AI provider abstraction, animated scene composition, timeline, motion graphics, image-to-video generation, character animation and local mock narration planning.

The product is not yet a complete SaaS. It is an advanced MVP foundation with real local render capability and mock AI workflows.

## Next Objectives

- Add real voice provider integration through the Narration Engine interface.
- Add audio track muxing into FFmpeg output.
- Improve subtitle timing at word or phrase level.
- Add reusable animated character variants and richer expressions.
- Add editable scene/timeline controls in the frontend.
- Connect production jobs to persistent database tables.
- Add authentication and company/team roles.
- Add real publication integrations only through official APIs.
