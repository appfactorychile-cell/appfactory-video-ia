def calculate_viral_score(popularity: int, growth_speed: int, audience_fit: int, saturation: int) -> dict[str, object]:
    probability = round((popularity * 0.32) + (growth_speed * 0.28) + (audience_fit * 0.26) + ((100 - saturation) * 0.14))
    return {
        "viral_probability": probability,
        "retention_signal": "Alta si el hook explica el beneficio en menos de 3 segundos",
        "shareability_signal": "Alta por utilidad practica y contexto local",
        "comment_signal": "Media alta por preguntas aplicables al nicho",
    }

