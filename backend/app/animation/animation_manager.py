from app.animation import animation_engine, asset_library, template_manager
from app.models.animation import AnimationProject


class AnimationManager:
    def __init__(self) -> None:
        self._projects: dict[str, AnimationProject] = {}

    def list_video_types(self) -> list[str]:
        return template_manager.list_video_types()

    def list_templates(self):
        return template_manager.list_templates()

    def list_assets(self):
        return asset_library.grouped_assets()

    def create_project(self, payload: dict[str, object]) -> AnimationProject:
        project = animation_engine.create_animation_project(payload)
        self._projects[project.id] = project
        return project

    def list_projects(self) -> list[AnimationProject]:
        if not self._projects:
            self.create_project({})
        return list(self._projects.values())

    def get_project(self, project_id: str) -> AnimationProject:
        return self._projects.get(project_id) or self.list_projects()[0]

    def timeline(self, project_id: str):
        return self.get_project(project_id).timeline

    def preview(self, project_id: str) -> dict[str, object]:
        return self.get_project(project_id).preview

    def render_plan(self, project_id: str) -> dict[str, object]:
        return self.get_project(project_id).render_pipeline


animation_manager = AnimationManager()
