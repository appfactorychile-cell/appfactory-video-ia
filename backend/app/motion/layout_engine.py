LAYOUTS = [
    "Titulo grande",
    "Titulo + subtitulo",
    "Lista",
    "Comparacion",
    "Dato curioso",
    "Top 5",
    "Estadistica",
]


def layout_catalog() -> list[str]:
    return LAYOUTS


def layout_for_scene(index: int) -> dict[str, object]:
    name = LAYOUTS[index % len(LAYOUTS)]
    positions = {
        "Titulo grande": {"title_y": 230, "main_y": 548, "subtitle_y": 1078},
        "Titulo + subtitulo": {"title_y": 214, "main_y": 572, "subtitle_y": 1078},
        "Lista": {"title_y": 200, "main_y": 520, "subtitle_y": 1078},
        "Comparacion": {"title_y": 220, "main_y": 590, "subtitle_y": 1078},
        "Dato curioso": {"title_y": 244, "main_y": 572, "subtitle_y": 1078},
        "Top 5": {"title_y": 206, "main_y": 540, "subtitle_y": 1078},
        "Estadistica": {"title_y": 226, "main_y": 560, "subtitle_y": 1078},
    }
    return {"name": name, "positions": positions[name]}

