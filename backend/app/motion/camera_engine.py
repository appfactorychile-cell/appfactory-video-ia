CAMERA_MOVEMENTS = ["Zoom lento", "Pan horizontal", "Pan vertical", "Dolly", "Shake muy suave"]


def camera_catalog() -> list[str]:
    return CAMERA_MOVEMENTS


def camera_for_scene(index: int) -> dict[str, str]:
    movement = CAMERA_MOVEMENTS[index % len(CAMERA_MOVEMENTS)]
    filters = {
        "Zoom lento": "scale=760:1352,crop=720:1280:x=20:y=36",
        "Pan horizontal": "scale=760:1280,crop=720:1280:x='20+18*sin(t*0.9)':y=0",
        "Pan vertical": "scale=720:1340,crop=720:1280:x=0:y='30+20*sin(t*0.8)'",
        "Dolly": "scale=780:1387,crop=720:1280:x=30:y=54",
        "Shake muy suave": "scale=740:1316,crop=720:1280:x='10+3*sin(t*9)':y='18+3*cos(t*8)'",
    }
    return {"name": movement, "ffmpeg_filter": filters[movement]}

