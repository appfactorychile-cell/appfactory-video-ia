from uuid import uuid4

from app.audio.audio_ducking import build_ducking_curve
from app.audio.music_library import get_music
from app.audio.sound_effects_library import get_effect


def build_audio_timeline(payload: dict[str, object]) -> dict[str, object]:
    duration = float(payload.get("duration_seconds") or 12)
    scene_count = int(payload.get("scene_count") or 4)
    style = str(payload.get("music_style") or "educativa").lower()
    selected_effects = payload.get("effects") if isinstance(payload.get("effects"), list) else ["whoosh", "pop", "transition", "soft-hit"]
    scene_duration = round(duration / max(scene_count, 1), 2)
    narration_track = []
    effects_track = []

    for index in range(scene_count):
        start = round(index * scene_duration, 2)
        end = round(min(duration, start + scene_duration), 2)
        narration_track.append(
            {
                "scene": index + 1,
                "start": start,
                "end": end,
                "duration": round(end - start, 2),
                "volume": 0.82,
                "source": "narracion_mock",
            }
        )
        effect = get_effect(str(selected_effects[index % len(selected_effects)]))
        effects_track.append(
            {
                "scene": index + 1,
                "effect": effect["name"],
                "effect_id": effect["id"],
                "start": round(start + 0.18, 2),
                "end": round(start + 0.18 + float(effect["duration"]), 2),
                "volume": 0.46,
                "frequency": effect["frequency"],
            }
        )

    return {
        "timeline_id": str(payload.get("timeline_id") or uuid4()),
        "duration_seconds": duration,
        "music_track": {
            "style": style,
            "track": get_music(style),
            "start": 0,
            "end": duration,
            "volume": 0.24,
            "fade_in": 0.8,
            "fade_out": 1.0,
            "source": "synthetic_tone",
        },
        "effects_track": effects_track,
        "narration_track": narration_track,
        "ducking": build_ducking_curve(narration_track),
        "status": "audio_timeline_ready",
    }
