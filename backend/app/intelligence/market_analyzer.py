def analyze_market(country: str, language: str, niche: str) -> dict[str, object]:
    return {
        "country": country,
        "language": language,
        "niche": niche,
        "market_demand": 92,
        "recommended_country": country or "Mexico",
        "recommended_language": language or "Espanol",
        "best_window": "13:00 hora local",
        "market_summary": "Mercado con interes alto, competencia controlable y espacio para contenido original de valor.",
    }

