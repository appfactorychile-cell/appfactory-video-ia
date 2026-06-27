from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Analytics Agent",
        slug="analytics-agent",
        specialty="Analitica",
        objective="Interpretar metricas simuladas para orientar aprendizaje y decisiones futuras.",
        input="Datos mock de rendimiento por canal, pais e idioma.",
        output="Lectura ejecutiva, alertas y oportunidad siguiente.",
        status="Disponible",
        execution_time_seconds=1.8,
        confidence_level=88,
        last_execution="08:07",
    )
