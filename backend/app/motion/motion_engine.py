from app.motion.animation_library import animation_catalog, scene_animation
from app.motion.camera_engine import camera_catalog, camera_for_scene
from app.motion.layout_engine import layout_catalog, layout_for_scene
from app.motion.transition_library import transition_catalog, transition_for_scene


def motion_catalog() -> dict[str, object]:
    return {
        "animations": animation_catalog(),
        "camera": camera_catalog(),
        "layouts": layout_catalog(),
        "transitions": transition_catalog(),
    }


def motion_plan(scene_count: int = 4) -> dict[str, object]:
    scenes = []
    for index in range(scene_count):
        scenes.append(
            {
                "scene": index + 1,
                "animation": scene_animation(index),
                "transition": transition_for_scene(index),
                "camera": camera_for_scene(index),
                "layout": layout_for_scene(index),
                "duration_seconds": 3,
            }
        )
    return {
        "name": "TikTok/Reels Motion Pack",
        "style": "Motion Graphics vertical premium",
        "resolution": "720x1280",
        "aspect_ratio": "9:16",
        "total_duration_seconds": scene_count * 3,
        "scenes": scenes,
        "catalog": motion_catalog(),
    }


def scene_motion(index: int) -> dict[str, object]:
    return motion_plan(index + 1)["scenes"][index]
