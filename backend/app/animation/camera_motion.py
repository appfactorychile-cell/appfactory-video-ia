def camera_plan(camera_motion: str, scene_count: int) -> list[str]:
    return [f"{camera_motion} - escena {index + 1}" for index in range(scene_count)]
