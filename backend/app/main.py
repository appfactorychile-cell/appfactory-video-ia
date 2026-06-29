from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    agents,
    channels,
    content,
    content_brain,
    editorial,
    global_intelligence,
    health,
    opportunities,
    pipeline,
    projects,
    workflow,
)
from app.core.config import get_settings
from app.database.init_db import init_database

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Backend MVP base for APP FACTORY VIDEO IA using mock data only.",
)

@app.on_event("startup")
def startup() -> None:
    init_database()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(channels.router, prefix=settings.api_prefix)
app.include_router(opportunities.router, prefix=settings.api_prefix)
app.include_router(editorial.router, prefix=settings.api_prefix)
app.include_router(content.router, prefix=settings.api_prefix)
app.include_router(content_brain.router, prefix=settings.api_prefix)
app.include_router(global_intelligence.router, prefix=settings.api_prefix)
app.include_router(workflow.router, prefix=settings.api_prefix)
app.include_router(pipeline.router, prefix=settings.api_prefix)
app.include_router(agents.router, prefix=settings.api_prefix)
app.include_router(projects.router, prefix=settings.api_prefix)



