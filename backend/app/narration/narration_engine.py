from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from app.narration.script_segmenter import DEFAULT_SCRIPT, segment_script
from app.narration.speech_timeline import build_speech_timeline


PROJECT_ROOT = Path(__file__).resolve().parents[3]
NARRATION_DIR = PROJECT_ROOT / "generated" / "narration"
JOBS: dict[str, dict[str, object]] = {}


def analyze_script(payload: dict[str, object]) -> dict[str, object]:
    script = str(payload.get("script") or DEFAULT_SCRIPT)
    segments = segment_script(script)
    return {
        "script": script,
        "scene_count": len(segments),
        "segments": segments,
        "status": "script_segmented",
    }


def plan_narration(payload: dict[str, object]) -> dict[str, object]:
    script_result = analyze_script(payload)
    voice = str(payload.get("voice") or "Narrador Local Mock")
    speech = build_speech_timeline(script_result["segments"], voice)
    return {
        **script_result,
        "voice_plan": speech["voice_plan"],
        "timing": speech["timing"],
        "subtitles": speech["subtitles"],
        "speech_timeline": speech["tracks"],
        "status": "narration_planned",
    }


def generate_narration(payload: dict[str, object]) -> dict[str, object]:
    job_id = str(payload.get("job_id") or uuid4())
    plan = plan_narration(payload)
    NARRATION_DIR.mkdir(parents=True, exist_ok=True)
    mock_audio_path = NARRATION_DIR / f"{job_id}.mock.txt"
    mock_audio_path.write_text(
        "\n".join(
            [
                "APP FACTORY VIDEO IA - MOCK NARRATION",
                f"job_id={job_id}",
                f"voice={plan['voice_plan']['voice']}",
                f"duration={plan['timing']['total_duration_seconds']}",
                "",
                str(plan["script"]),
            ]
        ),
        encoding="utf-8",
    )
    job = {
        **plan,
        "job_id": job_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "mock_audio_generated",
        "audio": {
            "provider": "local_mock",
            "path": str(mock_audio_path),
            "format": "mock.txt",
            "real_audio": False,
        },
    }
    JOBS[job_id] = job
    return job


def list_jobs() -> list[dict[str, object]]:
    return [
        {
            "job_id": job["job_id"],
            "status": job["status"],
            "created_at": job["created_at"],
            "duration_seconds": job["timing"]["total_duration_seconds"],
            "voice": job["voice_plan"]["voice"],
        }
        for job in JOBS.values()
    ]


def get_job(job_id: str) -> dict[str, object]:
    if job_id not in JOBS:
        return generate_narration({"job_id": job_id})
    return JOBS[job_id]
