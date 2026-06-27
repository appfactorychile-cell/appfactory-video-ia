from app.models.agent import AgentProfile


def build_agent(
    *,
    name: str,
    slug: str,
    specialty: str,
    objective: str,
    input: str,
    output: str,
    status: str,
    execution_time_seconds: float,
    confidence_level: int,
    last_execution: str,
) -> AgentProfile:
    return AgentProfile(
        name=name,
        slug=slug,
        specialty=specialty,
        objective=objective,
        input=input,
        output=output,
        status=status,
        execution_time_seconds=execution_time_seconds,
        confidence_level=confidence_level,
        last_execution=last_execution,
    )
