from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Research Agent",
        slug="research-agent",
        specialty="Investigacion",
        objective="Organizar contexto seguro, verificar supuestos y resumir informacion util para una idea original.",
        input="Tema, pais, idioma, nicho y reglas editoriales.",
        output="Resumen de investigacion, hallazgos y puntos que requieren verificacion futura.",
        status="Disponible",
        execution_time_seconds=1.8,
        confidence_level=91,
        last_execution="08:00",
    )
