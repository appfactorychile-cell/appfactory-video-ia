from uuid import uuid4

from app.animation import scene_composer


TIMELINE_STORE: dict[str, dict[str, object]] = {}


def _keyframes(scene_index: int, layer: dict[str, object], scene_start: int, scene_end: int) -> list[dict[str, object]]:
    layer_type = str(layer.get("type") or "layer")
    return [
        {
            "time": scene_start,
            "layer": layer.get("name"),
            "property": "opacity",
            "value": 0,
            "easing": "ease-out",
            "event": f"Entrada {layer_type}",
        },
        {
            "time": scene_start + 1,
            "layer": layer.get("name"),
            "property": "opacity",
            "value": 1,
            "easing": "ease-out",
            "event": "Visible",
        },
        {
            "time": max(scene_start + 2, scene_end - 2),
            "layer": layer.get("name"),
            "property": "transform",
            "value": f"translateY({-2 - scene_index}px) scale(1.02)",
            "easing": "ease-in-out",
            "event": "Movimiento sutil",
        },
        {
            "time": scene_end,
            "layer": layer.get("name"),
            "property": "opacity",
            "value": 0,
            "easing": "ease-in",
            "event": f"Salida {layer_type}",
        },
    ]


def _timeline_scene(scene: dict[str, object], index: int, start_time: int) -> dict[str, object]:
    duration = int(scene.get("duration_seconds") or 10)
    end_time = start_time + duration
    layers = scene.get("layers") if isinstance(scene.get("layers"), list) else []
    keyframes = []
    for layer in layers:
        if isinstance(layer, dict):
            keyframes.extend(_keyframes(index, layer, start_time, end_time))
    return {
        "scene_id": scene.get("scene_id") or f"scene-{index + 1}",
        "title": scene.get("title") or f"Escena {index + 1}",
        "start_time": start_time,
        "end_time": end_time,
        "duration_seconds": duration,
        "layers": layers,
        "keyframes": keyframes,
        "entry_animation": "Fade in por capas con desplazamiento vertical",
        "exit_animation": "Fade out y compresion suave",
        "zoom": {"from": 1.0, "to": round(1.05 + index * 0.01, 2), "start": start_time, "end": end_time},
        "pan": {"direction": "derecha" if index % 2 == 0 else "izquierda", "amount": 6, "start": start_time, "end": end_time},
        "transition": {
            "type": "crossfade luminoso" if index % 2 == 0 else "slide vertical suave",
            "duration_seconds": 1,
            "starts_at": max(start_time, end_time - 1),
        },
        "subtitles": [
            {"time": start_time + 1, "text": scene.get("subtitle") or "Subtitulo sincronizado"},
            {"time": max(start_time + 2, end_time - 3), "text": scene.get("main_text") or "Texto principal"},
        ],
        "camera_events": [
            {"time": start_time, "event": "camera_start", "description": "Plano vertical completo 9:16"},
            {"time": start_time + duration // 2, "event": "camera_zoom", "description": "Zoom lento hacia texto principal"},
            {"time": end_time, "event": "camera_cut", "description": "Preparar transicion a siguiente escena"},
        ],
        "text_events": [
            {"time": start_time + 1, "event": "title_reveal", "description": "Aparece titulo principal"},
            {"time": start_time + 3, "event": "caption_pop", "description": "Aparece subtitulo inferior"},
        ],
    }


def build_timeline(payload: dict[str, object]) -> dict[str, object]:
    timeline_id = str(payload.get("timeline_id") or uuid4())
    scenes = payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        scenes = scene_composer.compose_video_scenes({}).get("scenes", [])
    timeline_scenes = []
    cursor = 0
    for index, scene in enumerate(scenes):
        if not isinstance(scene, dict):
            continue
        item = _timeline_scene(scene, index, cursor)
        timeline_scenes.append(item)
        cursor = int(item["end_time"])
    timeline = {
        "timeline_id": timeline_id,
        "status": "Timeline animado preparado",
        "total_duration_seconds": cursor,
        "scene_count": len(timeline_scenes),
        "scenes": timeline_scenes,
        "global_transitions": [
            {"from_scene": timeline_scenes[index]["scene_id"], "to_scene": timeline_scenes[index + 1]["scene_id"], "type": timeline_scenes[index]["transition"]["type"], "duration_seconds": 1}
            for index in range(max(len(timeline_scenes) - 1, 0))
        ],
        "preview": {
            "aspect_ratio": "9:16",
            "resolution": "1080x1920 futuro",
            "note": "Preview temporal mock. No renderiza MP4 ni usa FFmpeg.",
        },
    }
    TIMELINE_STORE[timeline_id] = timeline
    return timeline


def get_timeline(timeline_id: str) -> dict[str, object]:
    if timeline_id not in TIMELINE_STORE:
        return build_timeline({"timeline_id": timeline_id})
    return TIMELINE_STORE[timeline_id]


def preview_timeline(payload: dict[str, object]) -> dict[str, object]:
    timeline = build_timeline(payload)
    return {
        "timeline_id": timeline["timeline_id"],
        "status": "Preview de timeline listo",
        "total_duration_seconds": timeline["total_duration_seconds"],
        "frames": [
            {
                "time": scene["start_time"],
                "scene_id": scene["scene_id"],
                "title": scene["title"],
                "camera": scene["camera_events"][0],
                "text": scene["text_events"][0],
                "transition": scene["transition"],
            }
            for scene in timeline["scenes"]
        ],
    }
