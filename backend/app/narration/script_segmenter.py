import re


DEFAULT_SCRIPT = (
    "La inteligencia artificial ya no solo crea contenido. "
    "Primero analiza si una idea merece convertirse en video. "
    "Luego organiza escenas, personajes, subtitulos y ritmo visual. "
    "El objetivo es producir menos contenido improvisado y mejores historias."
)


def _words(text: str) -> list[str]:
    return re.findall(r"\b[\wáéíóúÁÉÍÓÚñÑ]+\b", text, flags=re.UNICODE)


def _sentences(script: str) -> list[str]:
    parts = [part.strip() for part in re.split(r"(?<=[.!?])\s+", script.strip()) if part.strip()]
    if len(parts) >= 4:
        return parts
    words = _words(script)
    chunk_size = max(1, len(words) // 4)
    return [" ".join(words[index : index + chunk_size]) for index in range(0, len(words), chunk_size)]


def segment_script(script: str | None = None, target_scenes: int = 4) -> list[dict[str, object]]:
    source = (script or DEFAULT_SCRIPT).strip()
    sentences = _sentences(source)
    buckets = ["" for _ in range(target_scenes)]
    for index, sentence in enumerate(sentences):
        bucket_index = min(index * target_scenes // max(len(sentences), 1), target_scenes - 1)
        buckets[bucket_index] = f"{buckets[bucket_index]} {sentence}".strip()
    if not any(buckets):
        buckets[0] = DEFAULT_SCRIPT
    last_text = next((item for item in reversed(buckets) if item), DEFAULT_SCRIPT)
    segments = []
    for index, text in enumerate(buckets, start=1):
        scene_text = text or last_text
        words = _words(scene_text)
        duration = round(max(2.4, len(words) / 2.55), 2)
        segments.append(
            {
                "scene": index,
                "scene_id": f"narration-scene-{index}",
                "text": scene_text,
                "duration_seconds": duration,
                "words": len(words),
                "speed": round(len(words) / duration, 2),
            }
        )
    return segments
