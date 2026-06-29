from app.animation.background_manager import choose_backgrounds
from app.animation.camera_motion import camera_plan
from app.animation.character_manager import select_character
from app.animation.subtitle_animator import subtitle_plan
from app.models.animation import AnimationScene, AnimationTemplate


def build_scenes(template: AnimationTemplate, topic: str, language: str) -> list[AnimationScene]:
    backgrounds = choose_backgrounds(template.video_type)
    camera = camera_plan(template.camera_motion, template.scene_count)
    subtitles = subtitle_plan(language, template.subtitles, template.scene_count)
    character = select_character(template.video_type)
    scenes: list[AnimationScene] = []
    for index in range(template.scene_count):
        start = index * template.seconds_per_scene
        end = start + template.seconds_per_scene
        scenes.append(
            AnimationScene(
                id=f"scene-{index + 1}",
                title=f"Escena {index + 1}: {topic}",
                start_seconds=start,
                end_seconds=end,
                layers=[backgrounds[index % len(backgrounds)], character["name"], "Iconografia", "Texto principal"],
                animations=[template.animations[index % len(template.animations)], camera[index]],
                narration=f"Guion mock para {topic}. La escena {index + 1} explica una parte simple, util y visual.",
                subtitles=subtitles[index],
                music="Base electronica suave sin derechos - mock",
            )
        )
    return scenes
