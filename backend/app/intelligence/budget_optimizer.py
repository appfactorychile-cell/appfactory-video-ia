def optimize_budget(daily_budget_usd: float, candidates: list[dict[str, object]]) -> dict[str, object]:
    selected: list[dict[str, object]] = []
    used = 0.0
    for item in sorted(candidates, key=lambda x: x["opportunity_score"], reverse=True):
        cost = float(item["estimated_cost_usd"])
        if used + cost <= daily_budget_usd:
            selected.append(item)
            used += cost
    return {
        "daily_budget_usd": daily_budget_usd,
        "used_budget_usd": round(used, 2),
        "remaining_budget_usd": round(daily_budget_usd - used, 2),
        "selected_videos": selected,
        "rejected_videos": [item for item in candidates if item not in selected],
        "strategy": "Priorizar videos con mayor Opportunity Score y ROI esperado.",
    }

