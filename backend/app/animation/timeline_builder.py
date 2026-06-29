from app.models.animation import AnimationScene, AnimationTimeline


def build_timeline(project_id: str, scenes: list[AnimationScene]) -> AnimationTimeline:
    total = max((scene.end_seconds for scene in scenes), default=0)
    return AnimationTimeline(
        project_id=project_id,
        total_duration_seconds=total,
        scenes=scenes,
        music="Pista principal: ambiente tecnologico premium - mock",
        status="Timeline preparado",
    )
