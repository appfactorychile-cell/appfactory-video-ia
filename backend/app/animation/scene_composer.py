from uuid import uuid4

from app.characters.character_animator import animate_character
from app.characters.character_library import get_character
from app.narration.narration_engine import plan_narration


SCENE_STORE: dict[str, dict[str, object]] = {}


def _layer(layer_type: str, name: str, x: int, y: int, width: int, height: int, animation: str) -> dict[str, object]:
    return {
        "type": layer_type,
        "name": name,
        "position": {"x": x, "y": y},
        "size": {"width": width, "height": height},
        "animation": animation,
    }


def compose_scene(payload: dict[str, object]) -> dict[str, object]:
    scene_id = str(payload.get("scene_id") or uuid4())
    title = str(payload.get("title") or "Una idea simple puede cambiar el flujo de trabajo")
    main_text = str(payload.get("main_text") or "La IA ayuda a transformar una oportunidad en contenido claro y util.")
    subtitle = str(payload.get("subtitle") or "Escena preparada para preview animado.")
    narration_segment = payload.get("narration_segment") if isinstance(payload.get("narration_segment"), dict) else {}
    subtitle_plan = payload.get("subtitle_plan") if isinstance(payload.get("subtitle_plan"), dict) else {}
    speech_track = payload.get("speech_track") if isinstance(payload.get("speech_track"), dict) else {}
    duration = round(float(narration_segment.get("duration") or narration_segment.get("duration_seconds") or payload.get("duration_seconds") or 10), 2)
    tone = str(payload.get("tone") or "premium")
    accent = "violeta" if tone == "storytelling" else "azul"
    character_id = str(payload.get("character_id") or "narrador-hombre")
    character = get_character(character_id)
    character_animation = animate_character(
        {
            "character_id": character_id,
            "scene_id": scene_id,
            "text": f"{title} {main_text}",
            "expression": payload.get("expression") or "Feliz",
            "animation": payload.get("character_animation") or "Hablar",
            "speech_start": narration_segment.get("start", 0),
            "speech_duration": narration_segment.get("duration", duration),
        }
    )
    scene = {
        "scene_id": scene_id,
        "title": title,
        "main_text": main_text,
        "subtitle": subtitle,
        "duration_seconds": duration,
        "narration": {
            "text": narration_segment.get("text") or main_text,
            "start": narration_segment.get("start", 0),
            "end": narration_segment.get("end", duration),
            "duration": narration_segment.get("duration", duration),
            "words": narration_segment.get("words", len(main_text.split())),
            "words_per_second": narration_segment.get("words_per_second", 0),
            "source": "Narration Engine Mock",
        },
        "subtitle_plan": subtitle_plan or {
            "text": subtitle,
            "lines": [subtitle],
            "start": 0,
            "end": duration,
            "position": "inferior centrado",
            "max_chars_per_line": 34,
        },
        "speech_track": speech_track or {
            "start": 0,
            "end": duration,
            "duration": duration,
            "event": "mock_speech",
            "status": "planned_without_tts",
        },
        "background": {
            "name": "Fondo degradado global",
            "style": f"Azul profundo con acento {accent}",
            "animation": "Desplazamiento lento de luces y profundidad",
        },
        "character": {
            "id": character["id"],
            "name": character["nombre"],
            "style": character["estilo"],
            "color": character["color_principal"],
            "position": character["posicion_por_defecto"],
            "expression": character_animation["expression"],
            "pose": character_animation["pose"],
            "animation": character_animation["animation"],
            "gesture": character_animation["gesture"],
            "lip_sync": character_animation["lip_sync"],
        },
        "icons": [
            {"name": "Cerebro IA", "position": {"x": 12, "y": 20}, "animation": "Pulso suave"},
            {"name": "Grafico", "position": {"x": 75, "y": 23}, "animation": "Escala progresiva"},
            {"name": "Check", "position": {"x": 82, "y": 68}, "animation": "Aparece con rebote sutil"},
        ],
        "layers": [
            _layer("background", "Degradado oscuro", 0, 0, 100, 100, "pan lento"),
            _layer("shape", "Panel luminoso", 8, 10, 84, 72, "fade + scale"),
            _layer("character", "Narrador 2D", 52, 38, 34, 38, "slide up"),
            _layer("title", "Titulo principal", 10, 13, 78, 11, "fade in"),
            _layer("text", "Texto principal", 12, 56, 76, 16, "type reveal"),
            _layer("subtitle", "Subtitulo inferior", 10, 84, 80, 8, "caption pop"),
        ],
        "suggested_animation": "Entrada por capas, camara con zoom lento y subtitulos sincronizados.",
        "aspect_ratio": "9:16",
        "status": "Composicion lista para preview",
    }
    SCENE_STORE[scene_id] = scene
    return scene


def compose_video_scenes(payload: dict[str, object]) -> dict[str, object]:
    storyboard = payload.get("storyboard")
    narration_plan = plan_narration({"script": payload.get("script")}) if payload.get("script") or not storyboard else None
    if not isinstance(storyboard, list) or not storyboard:
        storyboard = [
            {"title": "Hook visual", "main_text": "Esto parece simple, pero cambia como se crea contenido.", "subtitle": "La oportunidad aparece antes que el video."},
            {"title": "Problema", "main_text": "Crear contenido sin estrategia consume tiempo y recursos.", "subtitle": "Primero se decide si vale la pena producir."},
            {"title": "Solucion animada", "main_text": "El motor transforma el storyboard en capas visuales editables.", "subtitle": "Fondos, personaje, iconos y textos."},
            {"title": "Cierre", "main_text": "Todo queda listo para una futura fase de render real.", "subtitle": "Sin FFmpeg ni APIs externas todavia."},
        ]
    scenes = []
    for index, item in enumerate(storyboard[:4], start=1):
        narration_segment = {}
        subtitle_plan = {}
        speech_track = {}
        if narration_plan:
            narration_segment = narration_plan["timing"]["segments"][index - 1]
            subtitle_plan = narration_plan["subtitles"][index - 1]
            speech_track = narration_plan["speech_timeline"][index - 1]
        if isinstance(item, dict):
            scene_payload = item
        else:
            scene_payload = {"title": f"Escena {index}", "main_text": str(item)}
        scene_payload = {
            "scene_id": f"composed-scene-{index}",
            "title": scene_payload.get("title") or f"Escena {index}",
            "main_text": narration_segment.get("text") or scene_payload.get("main_text") or "Mensaje principal de la escena animada.",
            "subtitle": " ".join(subtitle_plan.get("lines", [])) or scene_payload.get("subtitle") or "Subtitulo mock sincronizado.",
            "duration_seconds": narration_segment.get("duration") or scene_payload.get("duration_seconds") or 10,
            "tone": scene_payload.get("tone") or "premium",
            "character_id": scene_payload.get("character_id") or "narrador-hombre",
            "expression": scene_payload.get("expression") or "Feliz",
            "character_animation": scene_payload.get("character_animation") or "Hablar",
            "narration_segment": narration_segment,
            "subtitle_plan": subtitle_plan,
            "speech_track": speech_track,
        }
        scenes.append(compose_scene(scene_payload))
    return {
        "video_id": str(payload.get("video_id") or uuid4()),
        "status": "Escenas animadas compuestas",
        "scene_count": len(scenes),
        "scenes": scenes,
        "narration_plan": narration_plan,
    }


def get_scene_preview(scene_id: str) -> dict[str, object]:
    if scene_id not in SCENE_STORE:
        compose_scene({"scene_id": scene_id, "title": "Preview de escena", "main_text": "Composicion mock generada bajo demanda."})
    return SCENE_STORE[scene_id]
