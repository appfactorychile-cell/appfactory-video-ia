from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Video Agent",
        slug="video-agent",
        specialty="Video futuro",
        objective="Preparar requisitos de generacion visual para una fase posterior sin crear video real.",
        input="Storyboard, estilo visual, formato y plataforma.",
        output="Plan tecnico mock para render futuro.",
        status="Esperando",
        execution_time_seconds=3.1,
        confidence_level=82,
        last_execution="08:06",
    )
