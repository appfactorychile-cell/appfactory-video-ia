from dataclasses import dataclass


@dataclass(slots=True)
class AgentProfile:
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


@dataclass(slots=True)
class AgentStatus:
    name: str
    status: str
    availability: str
    average_time_seconds: float
    load_percentage: int


@dataclass(slots=True)
class AgentTimelineStep:
    time: str
    agent: str
    action: str
    status: str
    confidence_level: int


@dataclass(slots=True)
class AgentSimulationResult:
    mission: str
    director_summary: str
    timeline: list[AgentTimelineStep]
    final_result: str
    quality_score: int
    confidence_score: int
    next_action: str
