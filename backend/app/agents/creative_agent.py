from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Creative Agent",
        slug="creative-agent",
        specialty="Creatividad visual",
        objective="Definir estilo visual, ritmo, atmosfera y recursos creativos sin generar piezas reales todavia.",
        input="Guion, identidad del canal y reglas visuales.",
        output="Direccion creativa mock para storyboard y produccion futura.",
        status="Disponible",
        execution_time_seconds=2.1,
        confidence_level=87,
        last_execution="08:04",
    )
