from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class AIProvider:
    name: str
    slug: str
    status: str
    model: str
    functional: bool
    priority: int
    description: str


@dataclass(slots=True)
class AIRequest:
    task: str
    prompt: str
    system_prompt: str
    provider: str = "openai"
    model: str = ""
    temperature: float = 0.7
    max_output_tokens: int = 1400
    metadata: dict[str, object] = field(default_factory=dict)


@dataclass(slots=True)
class AIResponse:
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
    cached: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class UsageLog:
    provider: str
    model: str
    task: str
    success: bool
    response_time_ms: int
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class CostLog:
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float
    response_time_ms: int
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class PromptLog:
    task: str
    provider: str
    prompt_preview: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

