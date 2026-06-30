def _lines(text: str, max_chars: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) > max_chars and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines[:3]


def build_subtitles(timed_segments: list[dict[str, object]], max_chars_per_line: int = 34) -> list[dict[str, object]]:
    subtitles = []
    for segment in timed_segments:
        subtitles.append(
            {
                "scene": segment["scene"],
                "scene_id": segment["scene_id"],
                "text": segment["text"],
                "lines": _lines(str(segment["text"]), max_chars_per_line),
                "start": segment["start"],
                "end": segment["end"],
                "position": "inferior centrado",
                "max_chars_per_line": max_chars_per_line,
            }
        )
    return subtitles
