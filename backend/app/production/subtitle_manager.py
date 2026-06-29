from app.models.production import Subtitle


def prepare_subtitles(language: str) -> Subtitle:
    return Subtitle(
        language=language,
        lines=[
            "No basta con tener una idea.",
            "La IA primero valida oportunidad, costo y retorno.",
            "Solo después prepara guion, escenas y calidad.",
            "Crear mejor vale más que crear más.",
        ],
    )

