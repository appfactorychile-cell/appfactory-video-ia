from app.models.ai_provider import AIResponse

_CACHE: dict[str, AIResponse] = {}


def get(key: str) -> AIResponse | None:
    cached = _CACHE.get(key)
    if cached:
        cached.cached = True
    return cached


def set(key: str, response: AIResponse) -> None:
    _CACHE[key] = response

