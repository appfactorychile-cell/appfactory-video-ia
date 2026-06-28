SUPPORTED_EXTENSIONS = {
    "PDF", "DOCX", "TXT", "MARKDOWN", "MD", "CSV", "JSON", "HTML", "PNG", "JPG", "JPEG", "WEBP", "MP4", "MP3"
}


def normalize_file_type(file_type: str) -> str:
    value = file_type.strip().replace(".", "").upper()
    if value == "MD":
        return "Markdown"
    if value == "JPEG":
        return "JPG"
    return value


def is_supported(file_type: str) -> bool:
    return file_type.strip().replace(".", "").upper() in SUPPORTED_EXTENSIONS
