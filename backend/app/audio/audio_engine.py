from app.audio.audio_mixer import get_audio_job, list_audio_jobs, prepare_mix
from app.audio.audio_timeline import build_audio_timeline
from app.audio.music_library import list_music
from app.audio.sound_effects_library import list_effects


def music_library() -> list[dict[str, object]]:
    return list_music()


def effects_library() -> list[dict[str, object]]:
    return list_effects()


def plan_audio(payload: dict[str, object]) -> dict[str, object]:
    return build_audio_timeline(payload)


def mix_audio(payload: dict[str, object]) -> dict[str, object]:
    return prepare_mix(payload)


def audio_jobs() -> list[dict[str, object]]:
    return list_audio_jobs()


def audio_job(job_id: str) -> dict[str, object]:
    return get_audio_job(job_id)
