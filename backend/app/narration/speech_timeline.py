from app.narration.subtitle_planner import build_subtitles
from app.narration.timing_engine import build_timing
from app.narration.voice_planner import plan_voice


def build_speech_timeline(segments: list[dict[str, object]], voice: str = "Narrador Local Mock") -> dict[str, object]:
    timing = build_timing(segments)
    timed_segments = timing["segments"]
    return {
        "voice_plan": plan_voice(segments, voice),
        "timing": timing,
        "subtitles": build_subtitles(timed_segments),
        "tracks": [
            {
                "scene": segment["scene"],
                "scene_id": segment["scene_id"],
                "start": segment["start"],
                "end": segment["end"],
                "duration": segment["duration"],
                "event": "mock_speech",
                "status": "planned_without_tts",
            }
            for segment in timed_segments
        ],
    }
