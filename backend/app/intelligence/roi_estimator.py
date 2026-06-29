def estimate_roi(daily_budget_usd: float, viral_probability: int, market_demand: int) -> dict[str, object]:
    ai_cost = round(min(daily_budget_usd * 0.32, 8.0), 2)
    video_cost = round(ai_cost + 1.75, 2)
    channel_cost = round(video_cost * 0.18, 2)
    daily_cost = round(video_cost + channel_cost, 2)
    monthly_cost = round(daily_cost * 30, 2)
    estimated_revenue = round((viral_probability * market_demand / 100) * 0.42, 2)
    roi = round(((estimated_revenue - daily_cost) / daily_cost) * 100, 1) if daily_cost else 0
    return {
        "ai_cost_usd": ai_cost,
        "video_cost_usd": video_cost,
        "channel_cost_usd": channel_cost,
        "daily_cost_usd": daily_cost,
        "monthly_cost_usd": monthly_cost,
        "estimated_revenue_usd": estimated_revenue,
        "roi_percentage": roi,
        "estimated_profit_usd": round(estimated_revenue - daily_cost, 2),
        "monetization_probability": min(96, round((viral_probability + market_demand) / 2)),
    }

