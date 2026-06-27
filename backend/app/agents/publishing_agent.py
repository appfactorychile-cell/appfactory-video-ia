from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Publishing Agent",
        slug="publishing-agent",
        specialty="Publicacion futura",
        objective="Preparar una cola de publicacion para APIs oficiales en fases posteriores.",
        input="Plan aprobado, calendario y plataformas conectadas.",
        output="Programacion mock sin publicar contenido real.",
        status="Esperando",
        execution_time_seconds=1.6,
        confidence_level=83,
        last_execution="08:07",
    )
