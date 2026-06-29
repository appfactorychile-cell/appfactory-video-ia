from dataclasses import asdict

from app.ai import ai_logger, cache_manager, conversation_manager, cost_manager, provider_registry, provider_router, response_validator, token_counter, usage_manager
from app.models.ai_provider import AIRequest, AIResponse
from app.providers.openai_provider import from_env


def list_providers() -> list[dict[str, object]]:
    openai = from_env()
    return [asdict(item) for item in provider_registry.providers(openai.model, bool(openai.api_key))]


def active_provider() -> dict[str, object]:
    provider = from_env()
    return provider.health()


def generate(request: AIRequest) -> AIResponse:
    provider = provider_router.route(request.provider)
    model = request.model or getattr(provider, "model", "")
    key = conversation_manager.conversation_key(request.task, request.prompt, provider.name, model)
    cached = cache_manager.get(key)
    if cached:
        usage_manager.record(cached.provider, cached.model, cached.task, True, 0)
        return cached
    ai_logger.log_prompt(request.task, provider.name, request.prompt)
    try:
        response = provider.generate(request)
        if response.input_tokens == 0:
            response.input_tokens = token_counter.estimate_tokens(request.prompt + request.system_prompt)
        if response.output_tokens == 0:
            response.output_tokens = token_counter.estimate_tokens(response.content)
        response.parsed = response_validator.parse_json_object(response.content)
        cost_manager.record(response)
        usage_manager.record(response.provider, response.model, response.task, True, response.response_time_ms)
        cache_manager.set(key, response)
        return response
    except Exception:
        usage_manager.record(provider.name, model, request.task, False, 0)
        raise


def usage_summary() -> dict[str, object]:
    return usage_manager.summary(cost_manager.summary())


def costs() -> dict[str, object]:
    return {"summary": cost_manager.summary(), "items": cost_manager.list_costs()}


def logs() -> list[dict[str, object]]:
    return ai_logger.list_logs()

