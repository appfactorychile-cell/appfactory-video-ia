def build_ffmpeg_plan(project_id: str) -> dict[str, object]:
    return {
        "project_id": project_id,
        "status": "Preparado, no ejecutado",
        "ffmpeg_ready": False,
        "steps": [
            "Componer capas por escena",
            "Sincronizar narracion mock",
            "Sincronizar subtitulos animados",
            "Aplicar transiciones",
            "Mezclar musica",
            "Exportar MP4 vertical 1080x1920",
        ],
        "output_format": "MP4 H.264 1080x1920",
        "note": "Arquitectura preparada para FFmpeg. Esta fase no ejecuta render real.",
    }
