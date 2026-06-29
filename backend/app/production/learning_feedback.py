def build_learning_feedback(topic: str, hook: str) -> dict[str, object]:
    return {
        "what_worked": ["Hook directo", "Estructura de problema-solucion", "Duracion breve"],
        "what_did_not_work": ["Evitar exceso de datos en la primera escena"],
        "what_to_improve": ["Probar una version mas emocional del cierre"],
        "future_recommendations": [
            "Mantener apertura bajo 3 segundos",
            "Usar ejemplos locales",
            "Medir retencion antes de repetir formato",
        ],
        "principle": f"Para {topic}, el hook '{hook}' funciona como principio general, no como contenido a copiar.",
    }

