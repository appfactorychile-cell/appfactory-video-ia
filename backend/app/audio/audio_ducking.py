def build_ducking_curve(narration_segments: list[dict[str, object]], base_volume: float = 0.24) -> list[dict[str, object]]:
    curve: list[dict[str, object]] = []
    for segment in narration_segments:
        start = float(segment.get("start", 0))
        end = float(segment.get("end", start + 3))
        curve.append(
            {
                "start": start,
                "end": end,
                "music_volume": round(base_volume * 0.42, 2),
                "reason": "Ducking automatico por narracion",
            }
        )
    return curve
