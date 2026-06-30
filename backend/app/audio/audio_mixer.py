from datetime import datetime, timezone
from uuid import uuid4

from app.audio.audio_timeline import build_audio_timeline

JOBS: dict[str, dict[str, object]] = {}


def prepare_mix(payload: dict[str, object]) -> dict[str, object]:
    timeline = payload.get("audio_timeline") if isinstance(payload.get("audio_timeline"), dict) else build_audio_timeline(payload)
    job_id = str(payload.get("job_id") or uuid4())
    mix = {
        "job_id": job_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "audio_mix_ready",
        "duration_seconds": timeline["duration_seconds"],
        "music_volume": 0.24,
        "narration_volume": 0.82,
        "effects_volume": 0.46,
        "fade_in": timeline["music_track"]["fade_in"],
        "fade_out": timeline["music_track"]["fade_out"],
        "ducking": timeline["ducking"],
        "normalization": "basic_peak_mock",
        "compatible_with_video": True,
        "audio_timeline": timeline,
        "output": {
            "format": "synthetic_audio",
            "real_music_file": False,
            "copyright_safe": True,
        },
    }
    JOBS[job_id] = mix
    return mix


def list_audio_jobs() -> list[dict[str, object]]:
    return [
        {
            "job_id": job["job_id"],
            "status": job["status"],
            "created_at": job["created_at"],
            "duration_seconds": job["duration_seconds"],
            "style": job["audio_timeline"]["music_track"]["style"],
        }
        for job in JOBS.values()
    ]


def get_audio_job(job_id: str) -> dict[str, object]:
    if job_id not in JOBS:
        return prepare_mix({"job_id": job_id})
    return JOBS[job_id]
