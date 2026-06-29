from dataclasses import asdict

from fastapi import APIRouter

from app.animation.animation_manager import animation_manager
from app.schemas.animation_schema import (
    AnimationCreateRequest,
    AnimationLibraryResponse,
    AnimationProjectResponse,
    AnimationRenderPlanResponse,
    AnimationTemplateSchema,
    AnimationTimelineSchema,
)

router = APIRouter(prefix="/animation", tags=["Animated Video Engine"])


@router.get("/types", response_model=list[str], summary="Animated Video Types")
def animation_types() -> list[str]:
    return animation_manager.list_video_types()


@router.get("/templates", response_model=list[AnimationTemplateSchema], summary="Animation Templates")
def animation_templates() -> list[dict[str, object]]:
    return [asdict(template) for template in animation_manager.list_templates()]


@router.get("/assets", response_model=AnimationLibraryResponse, summary="Animation Asset Library")
def animation_assets() -> dict[str, object]:
    return {
        "categories": {
            category: [asdict(asset) for asset in assets]
            for category, assets in animation_manager.list_assets().items()
        }
    }


@router.get("/projects", response_model=list[AnimationProjectResponse], summary="Animation Projects")
def animation_projects() -> list[dict[str, object]]:
    return [asdict(project) for project in animation_manager.list_projects()]


@router.post("/create", response_model=AnimationProjectResponse, summary="Create Animated Video Plan")
def create_animation(payload: AnimationCreateRequest) -> dict[str, object]:
    return asdict(animation_manager.create_project(payload.model_dump()))


@router.get("/{project_id}", response_model=AnimationProjectResponse, summary="Animated Video Detail")
def animation_detail(project_id: str) -> dict[str, object]:
    return asdict(animation_manager.get_project(project_id))


@router.get("/{project_id}/timeline", response_model=AnimationTimelineSchema, summary="Animation Timeline")
def animation_timeline(project_id: str) -> dict[str, object]:
    return asdict(animation_manager.timeline(project_id))


@router.get("/{project_id}/preview", summary="Animation Preview")
def animation_preview(project_id: str) -> dict[str, object]:
    return animation_manager.preview(project_id)


@router.get("/{project_id}/render-plan", response_model=AnimationRenderPlanResponse, summary="Animation Render Plan")
def animation_render_plan(project_id: str) -> dict[str, object]:
    return animation_manager.render_plan(project_id)
