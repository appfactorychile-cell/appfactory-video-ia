from app.characters.character_library import get_character
from app.characters.gesture_engine import suggest_gesture
from app.characters.lip_sync_planner import create_lip_sync_plan


def animate_character(payload: dict[str, object]) -> dict[str, object]:
    character_id = str(payload.get("character_id") or "narrador-hombre")
    scene_id = str(payload.get("scene_id") or "scene-preview")
    text = str(payload.get("text") or "La IA explica una idea de forma clara.")
    expression = str(payload.get("expression") or "Feliz")
    pose = str(payload.get("pose") or "")
    animation = str(payload.get("animation") or "Hablar")
    speech_start = float(payload.get("speech_start") or 0.0)
    speech_duration = payload.get("speech_duration")
    character = get_character(character_id)
    gesture = suggest_gesture(text)
    selected_pose = pose or str(gesture["gesture"])
    return {
        "character": character,
        "scene_id": scene_id,
        "expression": expression,
        "pose": selected_pose,
        "animation": animation,
        "gesture": gesture,
        "lip_sync": create_lip_sync_plan(
            character_id,
            scene_id,
            text,
            start=speech_start,
            duration_seconds=float(speech_duration) if speech_duration else None,
        ),
        "track": {
            "name": "character_track",
            "layer": "Personaje",
            "keyframes": [
                {"time": 0, "property": "opacity", "value": 0, "event": "Entrada"},
                {"time": 0.45, "property": "opacity", "value": 1, "event": animation},
                {"time": 1.2, "property": "pose", "value": selected_pose, "event": "Gesto"},
                {"time": 2.6, "property": "scale", "value": 1.03, "event": "Respirar"},
            ],
        },
    }
