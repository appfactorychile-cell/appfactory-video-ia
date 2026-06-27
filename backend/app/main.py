from fastapi import FastAPI

from app.api.routes import channels, content, editorial, health, opportunities, pipeline
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Backend MVP base for APP FACTORY VIDEO IA using mock data only.",
)

app.include_router(health.router)
app.include_router(channels.router, prefix=settings.api_prefix)
app.include_router(opportunities.router, prefix=settings.api_prefix)
app.include_router(editorial.router, prefix=settings.api_prefix)
app.include_router(content.router, prefix=settings.api_prefix)
app.include_router(pipeline.router, prefix=settings.api_prefix)
