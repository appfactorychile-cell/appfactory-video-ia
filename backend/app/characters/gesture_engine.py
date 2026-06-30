GESTURE_KEYWORDS = {
    "dinero": "Señalando",
    "negocio": "Explicando",
    "ia": "Señalando",
    "historia": "Explicando",
    "tecnología": "Señalando",
    "tecnologia": "Señalando",
    "educación": "Explicando",
    "educacion": "Explicando",
}


def suggest_gesture(text: str) -> dict[str, object]:
    normalized = (text or "").lower()
    for keyword, gesture in GESTURE_KEYWORDS.items():
        if keyword in normalized:
            return {"keyword": keyword, "gesture": gesture, "reason": f"Detectada palabra clave: {keyword}"}
    return {"keyword": "", "gesture": "Frente", "reason": "Sin palabra clave; gesto neutral."}

