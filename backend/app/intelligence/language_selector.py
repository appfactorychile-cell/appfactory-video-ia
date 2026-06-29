def select_language(language: str, country: str) -> dict[str, object]:
    recommended = language or ("Portugues" if country.lower() == "brasil" else "Espanol")
    return {
        "recommended_language": recommended,
        "language_score": 90,
        "localization_note": "Adaptar culturalmente el guion; no traducir de forma literal.",
        "supported_languages": ["Espanol", "Ingles", "Portugues", "Frances", "Italiano", "Aleman"],
    }

