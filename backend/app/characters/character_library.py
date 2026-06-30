from app.characters.expression_library import expression_library
from app.characters.pose_library import pose_library


ANIMATIONS = [
    "Entrada",
    "Salida",
    "Idle",
    "Hablar",
    "Respirar",
    "Mover brazos",
    "Señalar",
    "Caminar corto",
    "Bounce suave",
    "Escala suave",
]


def _character(
    character_id: str,
    name: str,
    category: str,
    color: str,
    style: str,
    height: float,
    x: int,
    y: int,
) -> dict[str, object]:
    return {
        "id": character_id,
        "nombre": name,
        "categoria": category,
        "color_principal": color,
        "estilo": style,
        "altura_relativa": height,
        "posicion_por_defecto": {"x": x, "y": y},
        "expresiones_soportadas": expression_library(),
        "poses_soportadas": pose_library(),
        "animaciones_soportadas": ANIMATIONS,
    }


CHARACTERS = [
    _character("narrador-hombre", "Narrador Hombre", "Narrador", "0x38bdf8", "vector premium", 0.82, 510, 560),
    _character("narradora-mujer", "Narradora Mujer", "Narradora", "0xf472b6", "vector premium", 0.80, 505, 560),
    _character("profesor", "Profesor", "Educativo", "0x22c55e", "didactico", 0.84, 500, 555),
    _character("empresario", "Empresario", "Negocio", "0xf59e0b", "corporativo", 0.86, 500, 555),
    _character("presentador", "Presentador", "Media", "0xa855f7", "show vertical", 0.83, 505, 558),
    _character("estudiante", "Estudiante", "Educativo", "0x60a5fa", "juvenil", 0.76, 515, 584),
    _character("personaje-cartoon", "Personaje Cartoon", "Cartoon", "0xef4444", "amistoso", 0.78, 510, 576),
    _character("avatar-neutro", "Avatar Neutro", "General", "0x94a3b8", "minimalista", 0.80, 510, 570),
]


def character_library() -> list[dict[str, object]]:
    return CHARACTERS


def get_character(character_id: str) -> dict[str, object]:
    return next((character for character in CHARACTERS if character["id"] == character_id), CHARACTERS[0])
