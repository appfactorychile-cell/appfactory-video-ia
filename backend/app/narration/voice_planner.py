def plan_voice(segments: list[dict[str, object]], voice: str = "Narrador Local Mock") -> dict[str, object]:
    total_words = sum(int(segment.get("words", 0)) for segment in segments)
    average_speed = round(
        sum(float(segment.get("speed", 0)) for segment in segments) / max(len(segments), 1),
        2,
    )
    energy = "media-alta" if total_words > 45 else "media"
    return {
        "voice": voice,
        "provider": "local_mock",
        "tone": "claro, cercano y profesional",
        "energy": energy,
        "speed": average_speed,
        "pauses": [
            {"after_scene": segment["scene"], "duration_seconds": 0.25 if segment["scene"] < len(segments) else 0.0}
            for segment in segments
        ],
        "emphasis": [
            {"word": "IA", "style": "ligero enfasis"},
            {"word": "oportunidad", "style": "pausa breve antes"},
            {"word": "video", "style": "cierre claro"},
        ],
        "future_providers": ["OpenAI", "ElevenLabs", "Azure Speech", "Google TTS"],
    }
