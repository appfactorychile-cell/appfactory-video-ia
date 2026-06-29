def select_country(country: str, market_demand: int, competition: int) -> dict[str, object]:
    alternatives = ["Mexico", "Chile", "Brasil", "Estados Unidos", "Espana"]
    return {
        "recommended_country": country or "Mexico",
        "country_score": round(market_demand * 0.7 + (100 - competition) * 0.3),
        "alternatives": alternatives,
        "reason": "Mejor balance entre demanda, costo de produccion y oportunidad local.",
    }

