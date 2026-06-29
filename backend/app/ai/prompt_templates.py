TEMPLATES = {
    "ideas": (
        "Genera 10 ideas originales para videos cortos sobre '{topic}'. Pais: {country}. "
        "Idioma: {language}. Nicho: {niche}. Devuelve JSON con clave ideas, cada item con "
        "title, angle, emotion, value_promise, target_duration_seconds, curiosity_score, "
        "conversation_score, monetization_score y reason."
    ),
    "hooks": (
        "Genera 5 hooks originales para la idea '{idea}' sobre '{topic}'. Pais: {country}. "
        "Idioma: {language}. Devuelve JSON con clave hooks, cada item con hook, score, emotion "
        "y expected_retention."
    ),
    "script": (
        "Escribe un guion original de 20 a 45 segundos para '{topic}'. Idea: {idea}. Hook: {hook}. "
        "Pais: {country}. Idioma: {language}. Nicho: {niche}. Devuelve JSON con title, hook, "
        "duration_seconds, narration, subtitles y cta."
    ),
    "storyboard": (
        "Crea un storyboard de 4 escenas para '{topic}' en {language}. Devuelve JSON con scenes, "
        "cada escena con title, visual, narration, subtitles y duration_seconds."
    ),
    "narration": "Adapta esta narracion para voz natural en {language}: {script}",
    "seo": "Genera SEO responsable para '{topic}' en {language}. Devuelve title, description y keywords.",
    "description": "Genera una descripcion breve y segura para un video sobre '{topic}' en {language}.",
    "hashtags": "Genera hashtags seguros para '{topic}' en {language}.",
}

