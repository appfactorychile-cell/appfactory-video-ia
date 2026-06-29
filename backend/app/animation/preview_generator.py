from app.models.animation import AnimationScene


def generate_preview(project_id: str, scenes: list[AnimationScene]) -> dict[str, object]:
    return {
        "project_id": project_id,
        "status": "Preview mock disponible",
        "frames": [
            {
                "scene_id": scene.id,
                "title": scene.title,
                "visual": f"{scene.layers[0]} + {scene.layers[1]} + subtitulos animados",
                "timecode": f"{scene.start_seconds:02d}s-{scene.end_seconds:02d}s",
            }
            for scene in scenes
        ],
    }
