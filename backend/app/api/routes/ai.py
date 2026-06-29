from dataclasses import asdict

from fastapi import APIRouter, HTTPException, status

from app.ai import prompt_builder, provider_manager
from app.models.ai_provider import AIRequest
from app.schemas.ai_schema import (
    AICostsResponse,
    AIGenerateRequest,
    AIProviderResponse,
    AIResponseSchema,
    AITestRequest,
    AIUsageResponse,
)

router = APIRouter(prefix="/ai", tags=["AI Provider Platform"])


def _response(response) -> dict[str, object]:
    return asdict(response)


def _safe_generate(request: AIRequest) -> dict[str, object]:
    try:
        return _response(provider_manager.generate(request))
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.get("/providers", response_model=list[AIProviderResponse], summary="AI Providers")
def providers() -> list[dict[str, object]]:
    return provider_manager.list_providers()


@router.get("/provider/active", summary="Active AI Provider")
def active_provider() -> dict[str, object]:
    return provider_manager.active_provider()


@router.post("/test", response_model=AIResponseSchema, summary="Test AI Provider")
def test_provider(payload: AITestRequest) -> dict[str, object]:
    request = AIRequest(task="test", prompt=payload.prompt, system_prompt="Responde solamente JSON valido.")
    return _safe_generate(request)


@router.get("/usage", response_model=AIUsageResponse, summary="AI Usage")
def usage() -> dict[str, object]:
    return provider_manager.usage_summary()


@router.get("/costs", response_model=AICostsResponse, summary="AI Costs")
def costs() -> dict[str, object]:
    return provider_manager.costs()


@router.get("/logs", summary="AI Prompt Logs")
def logs() -> list[dict[str, object]]:
    return provider_manager.logs()


@router.post("/generate/ideas", response_model=AIResponseSchema, summary="Generate Ideas")
def generate_ideas(payload: AIGenerateRequest) -> dict[str, object]:
    request = prompt_builder.build_request("ideas", **payload.model_dump())
    return _safe_generate(request)


@router.post("/generate/hooks", response_model=AIResponseSchema, summary="Generate Hooks")
def generate_hooks(payload: AIGenerateRequest) -> dict[str, object]:
    request = prompt_builder.build_request("hooks", **payload.model_dump())
    return _safe_generate(request)


@router.post("/generate/script", response_model=AIResponseSchema, summary="Generate Script")
def generate_script(payload: AIGenerateRequest) -> dict[str, object]:
    request = prompt_builder.build_request("script", **payload.model_dump())
    return _safe_generate(request)
