from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Editorial Agent",
        slug="editorial-agent",
        specialty="Direccion editorial",
        objective="Evaluar si una oportunidad merece transformarse en contenido original y responsable.",
        input="Investigacion, tendencia, audiencia y politicas de contenido.",
        output="Recomendacion editorial, riesgo, valor para el usuario y enfoque sugerido.",
        status="Trabajando",
        execution_time_seconds=2.0,
        confidence_level=93,
        last_execution="08:02",
    )
