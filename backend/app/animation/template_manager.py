from app.models.animation import AnimationTemplate


VIDEO_TYPES = [
    "Explain 2D",
    "Motion Graphics",
    "Whiteboard",
    "Vector Animation",
    "Isometric",
    "Infographic",
    "Timeline",
    "Educational",
    "Business",
    "Storytelling",
]


def list_video_types() -> list[str]:
    return VIDEO_TYPES


def list_templates() -> list[AnimationTemplate]:
    return [
        AnimationTemplate("explain-2d", "Explain 2D Premium", "Explain 2D", 42, 4, ["Fade limpio", "Slide lateral"], "Zoom suave hacia el concepto central", ["Entrada por capas", "Iconos con rebote sutil"], 10, "Narracion clara y cercana", "Subtitulos grandes con palabras clave"),
        AnimationTemplate("motion-graphics", "Motion Graphics Ejecutivo", "Motion Graphics", 36, 5, ["Corte dinamico", "Barrido luminoso"], "Paneo horizontal con foco por secciones", ["Graficos animados", "Numeros progresivos"], 7, "Narracion rapida y segura", "Subtitulos sincronizados por frase"),
        AnimationTemplate("whiteboard", "Whiteboard Educativo", "Whiteboard", 48, 4, ["Dibujo continuo"], "Camara fija con acercamientos puntuales", ["Trazo manual", "Marcadores visuales"], 12, "Narracion docente", "Subtitulos discretos"),
        AnimationTemplate("vector-animation", "Vector Animation Modular", "Vector Animation", 40, 4, ["Morph vectorial", "Push vertical"], "Movimiento de camara por profundidad", ["Personaje simple", "Objetos vectoriales"], 10, "Narracion conversacional", "Subtitulos con bloques de color"),
        AnimationTemplate("isometric", "Isometrico Operacional", "Isometric", 45, 5, ["Cambio de plano isometrico"], "Orbita leve sobre escenario", ["Edificios", "Procesos conectados"], 9, "Narracion institucional", "Subtitulos inferiores"),
        AnimationTemplate("infographic", "Infografia Global", "Infographic", 34, 4, ["Escala por datos", "Reveal"], "Zoom entre graficos", ["Barras", "Mapas", "Indicadores"], 8, "Narracion analitica", "Subtitulos con cifras destacadas"),
        AnimationTemplate("timeline", "Timeline Narrativo", "Timeline", 44, 6, ["Avance por linea temporal"], "Seguimiento lateral", ["Hitos", "Fechas", "Conectores"], 7, "Narracion cronologica", "Subtitulos por hito"),
        AnimationTemplate("educational", "Educativo Claro", "Educational", 50, 5, ["Pizarra digital", "Corte suave"], "Camara estable", ["Ejemplos", "Notas", "Resumen"], 10, "Narracion simple", "Subtitulos de aprendizaje"),
        AnimationTemplate("business", "Business Premium", "Business", 38, 4, ["Panel ejecutivo", "Fade tecnico"], "Zoom a metricas", ["Tarjetas", "KPIs", "Flechas"], 9, "Narracion profesional", "Subtitulos corporativos"),
        AnimationTemplate("storytelling", "Storytelling Animado", "Storytelling", 52, 5, ["Corte cinematografico suave"], "Camara acompana al personaje", ["Personaje", "Escenario", "Conflicto"], 10, "Narracion emocional", "Subtitulos expresivos"),
    ]


def get_template(slug: str | None) -> AnimationTemplate:
    templates = list_templates()
    for template in templates:
        if template.slug == slug:
            return template
    return templates[0]
