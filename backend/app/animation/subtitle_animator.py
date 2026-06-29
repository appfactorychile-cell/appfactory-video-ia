def subtitle_plan(language: str, style: str, scene_count: int) -> list[list[str]]:
    return [
        [
            f"{language}: idea clave de la escena {index + 1}",
            f"{language}: cierre breve con valor para el usuario",
            f"Estilo: {style}",
        ]
        for index in range(scene_count)
    ]
