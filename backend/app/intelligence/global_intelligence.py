from app.intelligence import (
    audience_analyzer,
    competition_analyzer,
    country_selector,
    executive_decision,
    language_selector,
    market_analyzer,
    opportunity_ranker,
    roi_estimator,
    trend_analyzer,
    viral_score,
)


def analyze_global_opportunity(
    topic: str,
    country: str,
    language: str,
    niche: str,
    daily_budget_usd: float = 20.0,
) -> dict[str, object]:
    trend = trend_analyzer.analyze_trends(topic, country, language, niche)
    competition = competition_analyzer.analyze_competition(topic, niche)
    audience = audience_analyzer.analyze_audience(country, language, niche)
    market = market_analyzer.analyze_market(country, language, niche)
    viral = viral_score.calculate_viral_score(
        int(trend["popularity"]),
        int(trend["growth_speed"]),
        int(audience["audience_fit"]),
        int(competition["saturation"]),
    )
    risk_level = 28 if int(competition["saturation"]) < 50 else 52
    roi = roi_estimator.estimate_roi(daily_budget_usd, int(viral["viral_probability"]), int(market["market_demand"]))
    score = opportunity_ranker.rank_opportunity(
        int(trend["popularity"]),
        int(competition["competition"]),
        float(roi["ai_cost_usd"]),
        float(roi["roi_percentage"]),
        risk_level,
    )
    decision = executive_decision.make_executive_decision(
        int(score["opportunity_score"]),
        float(roi["roi_percentage"]),
        risk_level,
    )
    country_choice = country_selector.select_country(country, int(market["market_demand"]), int(competition["competition"]))
    language_choice = language_selector.select_language(language, country)
    return {
        "topic": topic,
        "country": country,
        "language": language,
        "niche": niche,
        "trend_analysis": trend,
        "competition_analysis": competition,
        "audience_analysis": audience,
        "market_analysis": market,
        "viral_analysis": viral,
        "roi_dashboard": roi,
        "score_breakdown": score,
        "opportunity_score": score["opportunity_score"],
        "risk_level": risk_level,
        "recommended_country": country_choice["recommended_country"],
        "recommended_language": language_choice["recommended_language"],
        "executive_decision": decision,
        "country_selection": country_choice,
        "language_selection": language_choice,
    }


def executive_dashboard() -> dict[str, object]:
    return {
        "active_channels": 248,
        "approved_videos": 37,
        "rejected_videos": 9,
        "detected_opportunities": 126,
        "used_budget_usd": 14.75,
        "ai_cost_usd": 6.4,
        "estimated_roi_percentage": 186.5,
        "top_country": "Mexico",
        "recommended_language": "Espanol",
        "fastest_growing_topic": "IA practica para pequenas empresas",
        "summary": "El Director Ejecutivo IA prioriza oportunidades con demanda alta, riesgo bajo y retorno esperado positivo.",
    }

