def build_timing(segments: list[dict[str, object]]) -> dict[str, object]:
    cursor = 0.0
    timed_segments = []
    for segment in segments:
        duration = float(segment.get("duration_seconds", 2.4))
        start = round(cursor, 2)
        end = round(start + duration, 2)
        words = int(segment.get("words", 0))
        timed_segments.append(
            {
                **segment,
                "start": start,
                "end": end,
                "duration": duration,
                "words_per_second": round(words / max(duration, 0.1), 2),
                "time_per_scene": duration,
            }
        )
        cursor = end + 0.25
    return {
        "segments": timed_segments,
        "total_duration_seconds": round(max(cursor - 0.25, 0), 2),
        "average_words_per_second": round(
            sum(item["words_per_second"] for item in timed_segments) / max(len(timed_segments), 1),
            2,
        ),
    }
