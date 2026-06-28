from pydantic import BaseModel, Field


class AgentProfileSchema(BaseModel):
    name: str
    slug: str
    specialty: str
    objective: str
    input: str
    output: str
    status: str
    execution_time_seconds: float
    confidence_level: int
    last_execution: str


class AgentStatusSchema(BaseModel):
    name: str
    status: str
    availability: str
    average_time_seconds: float
    load_percentage: int


class AgentStatusOverviewResponse(BaseModel):
    status: str
    availability: str
    average_time_seconds: float
    load_percentage: int
    agents: list[AgentStatusSchema]


class AgentSimulationRequest(BaseModel):
    mission: str = Field(
        default="Crear una estrategia editorial segura para una oportunidad global de contenido IA",
        examples=["Analizar una oportunidad de contenido para Mexico, Espanol, Tecnologia"],
    )


class AgentTimelineStepSchema(BaseModel):
    time: str
    agent: str
    action: str
    status: str
    confidence_level: int


class AgentSimulationResponse(BaseModel):
    source_mode: str
    active_project_name: str | None
    mission: str
    director_summary: str
    timeline: list[AgentTimelineStepSchema]
    final_result: str
    quality_score: int
    confidence_score: int
    next_action: str


