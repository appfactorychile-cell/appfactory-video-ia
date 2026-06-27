from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Trend Agent",
        slug="trend-agent",
        specialty="Tendencias",
        objective="Detectar senales de oportunidad por pais, idioma, nicho y ventana horaria.",
        input="Senales simuladas de mercado, pais, idioma y competencia.",
        output="Nivel de tendencia, demanda estimada y oportunidad editorial.",
        status="Disponible",
        execution_time_seconds=1.5,
        confidence_level=89,
        last_execution="08:01",
    )
