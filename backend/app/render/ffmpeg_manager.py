import os
import shutil
import subprocess
from pathlib import Path


KNOWN_FFMPEG_PATH = Path("C:/ffmpeg-8.1.2-essentials_build/bin/ffmpeg.exe")


def _candidate_paths() -> list[Path]:
    candidates: list[Path] = []
    configured = os.getenv("FFMPEG_PATH") or os.getenv("FFMPEG_BINARY")
    if configured:
        candidates.append(Path(configured))
    from_path = shutil.which("ffmpeg")
    if from_path:
        candidates.append(Path(from_path))
    candidates.append(KNOWN_FFMPEG_PATH)
    unique: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = str(candidate).lower()
        if key not in seen:
            seen.add(key)
            unique.append(candidate)
    return unique


def _version_for(path: Path) -> str:
    try:
        result = subprocess.run(
            [str(path), "-version"],
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    if result.returncode != 0:
        return ""
    return (result.stdout.splitlines() or [""])[0].strip()


def detect_ffmpeg() -> dict[str, object]:
    for candidate in _candidate_paths():
        if candidate.exists() and candidate.is_file():
            version = _version_for(candidate)
            if version:
                return {
                    "installed": True,
                    "version": version,
                    "path": str(candidate),
                    "available": True,
                }
    return {
        "installed": False,
        "version": "FFmpeg no encontrado",
        "path": "",
        "available": False,
    }
