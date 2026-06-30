def validate_audio_mix(mix: dict[str, object], video_duration: float) -> dict[str, object]:
    timeline = mix.get("audio_timeline") if isinstance(mix.get("audio_timeline"), dict) else {}
    duration = float(mix.get("duration_seconds") or timeline.get("duration_seconds") or 0)
    checks = {
        "music_assigned": bool(timeline.get("music_track")),
        "effects_assigned": bool(timeline.get("effects_track")),
        "narration_available": bool(timeline.get("narration_track")),
        "mix_valid": mix.get("status") == "audio_mix_ready",
        "duration_compatible": abs(duration - float(video_duration or duration)) <= 1.0,
    }
    return {
        "checks": checks,
        "approved": all(checks.values()),
        "score": 96 if all(checks.values()) else 64,
        "notes": ["Audio mock local compatible con render MP4."] if all(checks.values()) else ["La mezcla no esta completa."],
    }
