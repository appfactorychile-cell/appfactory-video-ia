ENTRY_ANIMATIONS = [
    "Fade",
    "Slide Left",
    "Slide Right",
    "Slide Up",
    "Slide Down",
    "Scale",
    "Zoom In",
    "Zoom Out",
    "Bounce",
    "Pop",
]

EXIT_ANIMATIONS = ["Fade", "Scale Down", "Slide", "Blur Out"]

TEXT_ANIMATIONS = [
    "Escribir letra por letra",
    "Fade",
    "Bounce",
    "Highlight",
    "Glow",
    "Escala",
]

PARTICLES = ["circulos", "lineas", "brillos", "formas geometricas", "grids"]


def animation_catalog() -> dict[str, list[str]]:
    return {
        "entradas": ENTRY_ANIMATIONS,
        "salidas": EXIT_ANIMATIONS,
        "textos": TEXT_ANIMATIONS,
        "particulas": PARTICLES,
    }


def scene_animation(index: int) -> dict[str, str]:
    return {
        "entrada": ENTRY_ANIMATIONS[index % len(ENTRY_ANIMATIONS)],
        "salida": EXIT_ANIMATIONS[index % len(EXIT_ANIMATIONS)],
        "texto": TEXT_ANIMATIONS[index % len(TEXT_ANIMATIONS)],
        "particula": PARTICLES[index % len(PARTICLES)],
    }

