from datetime import datetime

from pydantic import BaseModel, Field


class AIGenerateRequest(BaseModel):
    topic: str = Field(..., examples=["Herramientas de IA para pequenas empresas"])
    country: str = Field("Mexico")
    language: str = Field("Espanol")
    niche: str = Field("Tecnologia")
    idea: str = Field("", description="Idea aprobada opcional")
    hook: str = Field("", description="Hook seleccionado opcional")


class AITestRequest(BaseModel):
    prompt: str = Field("Responde con JSON: {\"status\":\"ok\",\"message\":\"OpenAI conectado\"}")


class AIProviderResponse(BaseModel):
    name: str
    slug: str
    status: str
    model: str
    functional: bool
    priority: int
    description: str


class AIResponseSchema(BaseModel):
    id: str
    provider: str
    model: str
    task: str
    content: str
    parsed: dict[str, object] | list[object] | None
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float
    response_time_ms: int
    cached: bool
    created_at: datetime


class AIUsageResponse(BaseModel):
    requests: int
    successful_requests: int
    errors: int
    average_response_time_ms: float
    input_tokens: int
    output_tokens: int
    cost_daily_usd: float
    cost_monthly_estimated_usd: float


class AICostsResponse(BaseModel):
    summary: dict[str, object]
    items: list[dict[str, object]]

