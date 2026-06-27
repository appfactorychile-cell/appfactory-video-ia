from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="Storyboard Agent",
        slug="storyboard-agent",
        specialty="Storyboard",
        objective="Dividir la historia en escenas simples, visuales y faciles de revisar.",
        input="Guion, direccion creativa y duracion objetivo.",
        output="Storyboard mock con escenas, narracion y subtitulos planeados.",
        status="Esperando",
        execution_time_seconds=2.5,
        confidence_level=86,
        last_execution="08:05",
    )
