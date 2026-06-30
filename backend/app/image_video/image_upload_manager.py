import base64
from pathlib import Path
from uuid import uuid4


PROJECT_ROOT = Path(__file__).resolve().parents[3]
UPLOAD_DIR = PROJECT_ROOT / "storage" / "uploads" / "images"
UPLOAD_STORE: dict[str, dict[str, object]] = {}

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def _extension_for(filename: str, content_type: str) -> str:
    suffix = Path(filename or "").suffix.lower()
    if suffix in ALLOWED_EXTENSIONS:
        return suffix
    if "png" in content_type:
        return ".png"
    if "webp" in content_type:
        return ".webp"
    if "gif" in content_type:
        return ".gif"
    return ".jpg"


def _decode_data_url(data_url: str) -> tuple[str, bytes]:
    if "," in data_url and data_url.strip().lower().startswith("data:"):
        header, encoded = data_url.split(",", 1)
        content_type = header.split(";", 1)[0].replace("data:", "") or "image/jpeg"
    else:
        content_type = "image/jpeg"
        encoded = data_url
    return content_type, base64.b64decode(encoded)


def save_uploaded_image(payload: dict[str, object]) -> dict[str, object]:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    filename = str(payload.get("filename") or "uploaded-image.jpg")
    data_url = str(payload.get("data_url") or "")
    if not data_url:
        raise ValueError("No se recibio imagen para subir.")

    content_type, data = _decode_data_url(data_url)
    upload_id = str(uuid4())
    extension = _extension_for(filename, content_type)
    path = UPLOAD_DIR / f"{upload_id}{extension}"
    path.write_bytes(data)

    record = {
        "upload_id": upload_id,
        "filename": filename,
        "content_type": content_type,
        "path": str(path),
        "size_bytes": path.stat().st_size,
        "status": "uploaded",
    }
    UPLOAD_STORE[upload_id] = record
    return record


def get_upload(upload_id: str | None = None) -> dict[str, object]:
    if upload_id and upload_id in UPLOAD_STORE:
        return UPLOAD_STORE[upload_id]
    if UPLOAD_STORE:
        return list(UPLOAD_STORE.values())[-1]
    raise ValueError("No existe una imagen subida para crear video.")

