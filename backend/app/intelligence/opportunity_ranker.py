def rank_opportunity(popularity: int, competition: int, ai_cost: float, roi_percentage: float, risk_level: int) -> dict[str, object]:
    cost_score = max(0, 100 - round(ai_cost * 4))
    roi_score = max(0, min(100, round(roi_percentage + 55)))
    opportunity_score = round(
        popularity * 0.30
        + (100 - competition) * 0.18
        + cost_score * 0.14
        + roi_score * 0.28
        + (100 - risk_level) * 0.10
    )
    return {
        "popularity_score": popularity,
        "competition_score": competition,
        "cost_score": cost_score,
        "roi_score": roi_score,
        "risk_score": risk_level,
        "opportunity_score": max(0, min(100, opportunity_score)),
    }

