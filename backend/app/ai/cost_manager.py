from dataclasses import asdict

from app.models.ai_provider import AIResponse, CostLog

_COSTS: list[CostLog] = []

MODEL_PRICES = {
    "gpt-4.1-mini": {"input": 0.0000004, "output": 0.0000016},
    "gpt-4.1": {"input": 0.000002, "output": 0.000008},
}


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    price = MODEL_PRICES.get(model, MODEL_PRICES["gpt-4.1-mini"])
    return round(input_tokens * price["input"] + output_tokens * price["output"], 6)


def record(response: AIResponse) -> AIResponse:
    response.estimated_cost_usd = estimate_cost(response.model, response.input_tokens, response.output_tokens)
    _COSTS.append(
        CostLog(
            provider=response.provider,
            model=response.model,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            estimated_cost_usd=response.estimated_cost_usd,
            response_time_ms=response.response_time_ms,
        )
    )
    return response


def list_costs() -> list[dict[str, object]]:
    return [asdict(item) for item in _COSTS]


def summary() -> dict[str, object]:
    return {
        "requests": len(_COSTS),
        "input_tokens": sum(item.input_tokens for item in _COSTS),
        "output_tokens": sum(item.output_tokens for item in _COSTS),
        "cost_daily_usd": round(sum(item.estimated_cost_usd for item in _COSTS), 6),
        "cost_monthly_estimated_usd": round(sum(item.estimated_cost_usd for item in _COSTS) * 30, 6),
    }

