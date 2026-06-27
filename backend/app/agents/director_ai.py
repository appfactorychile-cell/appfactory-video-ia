from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Director General IA",
        slug="director-ai",
        specialty="Coordinacion estrategica",
        objective="Coordinar agentes especializados y decidir si una mision editorial esta lista para avanzar.",
        input="Mision, oportunidad, estado de agentes y reglas de calidad.",
        output="Decision final, resumen ejecutivo y siguiente accion recomendada.",
        status="Trabajando",
        execution_time_seconds=2.4,
        confidence_level=94,
        last_execution="08:07",
    )
