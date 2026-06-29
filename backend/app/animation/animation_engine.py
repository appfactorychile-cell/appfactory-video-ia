from uuid import uuid4

from app.animation import asset_library, preview_generator, scene_animator, template_manager
from app.animation.animation_renderer import prepare_render
from app.animation.timeline_builder import build_timeline
from app.models.animation import AnimationProject


def create_animation_project(payload: dict[str, object]) -> AnimationProject:
    project_id = str(uuid4())
    template = template_manager.get_template(str(payload.get("template_slug") or "explain-2d"))
    title = str(payload.get("title") or "Video animado APP FACTORY")
    topic = str(payload.get("topic") or title)
    language = str(payload.get("language") or "Espanol")
    scenes = scene_animator.build_scenes(template, topic, language)
    assets = asset_library.select_assets_for_video(template.video_type)
    timeline = build_timeline(project_id, scenes)
    preview = preview_generator.generate_preview(project_id, scenes)
    render_pipeline = prepare_render(project_id)
    return AnimationProject(project_id, title, template.video_type, template, scenes, assets, timeline, preview, render_pipeline)
