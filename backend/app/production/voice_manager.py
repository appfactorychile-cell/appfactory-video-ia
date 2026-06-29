from app.models.production import Narration


def prepare_narration(script: str, language: str) -> Narration:
    return Narration(
        voice=f"Voz IA natural en {language}",
        tone="Claro, ejecutivo y cercano",
        script=script,
        duration_seconds=38,
    )

