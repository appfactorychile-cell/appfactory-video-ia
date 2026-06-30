EFFECTS_LIBRARY: list[dict[str, object]] = [
    {"id": "whoosh", "name": "Whoosh", "use": "Entrada o transicion", "frequency": 660, "duration": 0.18},
    {"id": "pop", "name": "Pop", "use": "Aparicion de texto", "frequency": 820, "duration": 0.11},
    {"id": "click", "name": "Click", "use": "Cambio de dato", "frequency": 980, "duration": 0.07},
    {"id": "impact", "name": "Impact", "use": "Momento clave", "frequency": 150, "duration": 0.16},
    {"id": "rise", "name": "Rise", "use": "Construccion de expectativa", "frequency": 520, "duration": 0.28},
    {"id": "transition", "name": "Transition", "use": "Cambio de escena", "frequency": 720, "duration": 0.14},
    {"id": "notification", "name": "Notification", "use": "Dato importante", "frequency": 880, "duration": 0.10},
    {"id": "sparkle", "name": "Sparkle", "use": "Resultado positivo", "frequency": 1200, "duration": 0.09},
    {"id": "glitch", "name": "Glitch", "use": "Tecnologia o error visual", "frequency": 440, "duration": 0.12},
    {"id": "soft-hit", "name": "Soft Hit", "use": "Enfasis suave", "frequency": 240, "duration": 0.13},
]


def list_effects() -> list[dict[str, object]]:
    return EFFECTS_LIBRARY


def get_effect(effect_id: str) -> dict[str, object]:
    return next((effect for effect in EFFECTS_LIBRARY if effect["id"] == effect_id), EFFECTS_LIBRARY[0])
