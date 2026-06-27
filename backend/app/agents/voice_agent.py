from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Voice Agent",
        slug="voice-agent",
        specialty="Voz IA",
        objective="Recomendar tipo de voz, velocidad y energia para una narracion futura.",
        input="Idioma, audiencia, tono y duracion.",
        output="Perfil de voz mock y ritmo recomendado.",
        status="Esperando",
        execution_time_seconds=1.4,
        confidence_level=84,
        last_execution="08:05",
    )
