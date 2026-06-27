from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Idea Agent",
        slug="idea-agent",
        specialty="Generacion de ideas",
        objective="Proponer ideas originales con curiosidad, utilidad y potencial de conversacion.",
        input="Recomendacion editorial, audiencia y nicho.",
        output="Lista priorizada de ideas de contenido originales.",
        status="Disponible",
        execution_time_seconds=1.7,
        confidence_level=90,
        last_execution="08:03",
    )
