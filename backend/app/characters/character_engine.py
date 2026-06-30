from app.characters.character_animator import animate_character
from app.characters.character_library import character_library, get_character
from app.characters.expression_library import expression_library
from app.characters.pose_library import pose_library


ASSIGNMENTS: dict[str, dict[str, object]] = {}


def list_characters() -> list[dict[str, object]]:
    return character_library()


def character_detail(character_id: str) -> dict[str, object]:
    return get_character(character_id)


def library() -> dict[str, object]:
    return {
        "characters": character_library(),
        "expressions": expression_library(),
        "poses": pose_library(),
        "animations": get_character("narrador-hombre")["animaciones_soportadas"],
    }


def assign_character(payload: dict[str, object]) -> dict[str, object]:
    scene_id = str(payload.get("scene_id") or "composed-scene-1")
    character_id = str(payload.get("character_id") or "narrador-hombre")
    character = get_character(character_id)
    assignment = {
        "scene_id": scene_id,
        "character": character,
        "expression": str(payload.get("expression") or "Feliz"),
        "pose": str(payload.get("pose") or "Explicando"),
        "animation": str(payload.get("animation") or "Hablar"),
        "status": "personaje_asignado",
    }
    ASSIGNMENTS[scene_id] = assignment
    return assignment


def animate(payload: dict[str, object]) -> dict[str, object]:
    return animate_character(payload)
