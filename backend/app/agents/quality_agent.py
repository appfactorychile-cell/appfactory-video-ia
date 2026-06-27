from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Quality Agent",
        slug="quality-agent",
        specialty="Calidad y cumplimiento",
        objective="Revisar originalidad, claridad, seguridad, derechos de autor y valor para la audiencia.",
        input="Guion, storyboard, metadatos y reglas de contenido.",
        output="Score de calidad, riesgos y aprobacion mock.",
        status="Trabajando",
        execution_time_seconds=2.2,
        confidence_level=95,
        last_execution="08:06",
    )
