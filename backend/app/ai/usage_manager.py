from dataclasses import asdict

from app.models.ai_provider import UsageLog

_USAGE: list[UsageLog] = []


def record(provider: str, model: str, task: str, success: bool, response_time_ms: int) -> None:
    _USAGE.append(UsageLog(provider=provider, model=model, task=task, success=success, response_time_ms=response_time_ms))


def list_usage() -> list[dict[str, object]]:
    return [asdict(item) for item in _USAGE]


def summary(cost_summary: dict[str, object]) -> dict[str, object]:
    total = len(_USAGE)
    errors = len([item for item in _USAGE if not item.success])
    ok = total - errors
    avg = round(sum(item.response_time_ms for item in _USAGE) / total, 1) if total else 0
    return {
        **cost_summary,
        "requests": total,
        "successful_requests": ok,
        "errors": errors,
        "average_response_time_ms": avg,
    }
