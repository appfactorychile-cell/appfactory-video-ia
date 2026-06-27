from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Script Agent",
        slug="script-agent",
        specialty="Guion",
        objective="Convertir la idea elegida en una estructura breve, clara y con valor real.",
        input="Idea, hook, tono, idioma y duracion objetivo.",
        output="Guion mock de formato corto con inicio, desarrollo y cierre.",
        status="Esperando",
        execution_time_seconds=2.8,
        confidence_level=88,
        last_execution="08:04",
    )
