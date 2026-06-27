from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Learning Agent",
        slug="learning-agent",
        specialty="Aprendizaje",
        objective="Convertir resultados simulados en principios generales para mejorar futuras recomendaciones.",
        input="Metricas mock, decision editorial y resultado de calidad.",
        output="Principios aprendidos, no copias de videos ni guiones.",
        status="Disponible",
        execution_time_seconds=1.9,
        confidence_level=90,
        last_execution="08:07",
    )
