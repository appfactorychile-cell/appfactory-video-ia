TRANSITIONS = ["Cross Fade", "Push", "Slide", "Zoom", "Flash"]


def transition_catalog() -> list[str]:
    return TRANSITIONS


def transition_for_scene(index: int) -> dict[str, object]:
    name = TRANSITIONS[index % len(TRANSITIONS)]
    return {
        "name": name,
        "duration_seconds": 0.35,
        "description": f"Transicion {name} preparada para clips verticales.",
    }

