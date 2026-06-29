def effect_plan(video_type: str) -> list[str]:
    if video_type in {"Motion Graphics", "Infographic"}:
        return ["Glow sutil", "Contadores animados", "Lineas de conexion"]
    return ["Sombras suaves", "Entrada por opacidad", "Pulso en palabras clave"]
