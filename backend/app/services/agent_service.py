from dataclasses import asdict

from app.agents import (
    analytics_agent,
    creative_agent,
    director_ai,
    editorial_agent,
    idea_agent,
    learning_agent,
    publishing_agent,
    quality_agent,
    research_agent,
    script_agent,
    seo_agent,
    storyboard_agent,
    trend_agent,
    video_agent,
    voice_agent,
)
from app.models.agent import AgentTimelineStep
from app.projects import project_library
from app.schemas.agent_schema import (
    AgentProfileSchema,
    AgentSimulationRequest,
    AgentSimulationResponse,
    AgentStatusOverviewResponse,
    AgentStatusSchema,
    AgentTimelineStepSchema,
)

_AGENT_BUILDERS = [
    director_ai.get_agent,
    research_agent.get_agent,
    trend_agent.get_agent,
    editorial_agent.get_agent,
    idea_agent.get_agent,
    script_agent.get_agent,
    creative_agent.get_agent,
    storyboard_agent.get_agent,
    seo_agent.get_agent,
    voice_agent.get_agent,
    video_agent.get_agent,
    quality_agent.get_agent,
    learning_agent.get_agent,
    publishing_agent.get_agent,
    analytics_agent.get_agent,
]

_STATUS_MAP = {
    "Disponible": "Disponible",
    "Trabajando": "Trabajando",
    "Esperando": "Esperando",
    "Error": "Error",
}


def list_agents() -> list[AgentProfileSchema]:
    return [AgentProfileSchema(**asdict(builder())) for builder in _AGENT_BUILDERS]


def get_agent(agent_name: str) -> AgentProfileSchema:
    normalized = agent_name.lower().strip().replace("_", "-")
    for agent in list_agents():
        candidates = {agent.slug.lower(), agent.name.lower().replace(" ", "-"), agent.name.lower()}
        if normalized in candidates:
            return agent
    raise KeyError(agent_name)


def get_status() -> AgentStatusOverviewResponse:
    agents = list_agents()
    statuses = [
        AgentStatusSchema(
            name=agent.name,
            status=_STATUS_MAP.get(agent.status, agent.status),
            availability="Operativo" if agent.status != "Error" else "Requiere revision",
            average_time_seconds=agent.execution_time_seconds,
            load_percentage=min(96, max(12, int(agent.execution_time_seconds * 22))),
        )
        for agent in agents
    ]
    avg_time = round(sum(item.average_time_seconds for item in statuses) / len(statuses), 2)
    avg_load = round(sum(item.load_percentage for item in statuses) / len(statuses))
    return AgentStatusOverviewResponse(
        status="Operativo en modo mock",
        availability="15 agentes simulados disponibles para coordinacion futura",
        average_time_seconds=avg_time,
        load_percentage=avg_load,
        agents=statuses,
    )


def simulate(payload: AgentSimulationRequest) -> AgentSimulationResponse:
    active_project = project_library.get_active_project()
    source_mode = "Proyecto vinculado" if active_project else "Contenido global"
    mode_action = f"Define modo proyecto usando solo fuentes autorizadas de {active_project.name}" if active_project else "Define modo global sin usar proyectos vinculados"
    steps = [
        AgentTimelineStep("08:00", "Director General IA", mode_action, "Trabajando", 94),
        AgentTimelineStep("08:01", "Research Agent", "Resume contexto seguro y puntos de investigacion", "Completado", 91),
        AgentTimelineStep("08:02", "Trend Agent", "Evalua oportunidad por pais, idioma y nicho", "Completado", 89),
        AgentTimelineStep("08:03", "Editorial Agent", "Decide enfoque responsable y original", "Completado", 93),
        AgentTimelineStep("08:04", "Idea Agent", "Genera ideas con curiosidad y utilidad", "Completado", 90),
        AgentTimelineStep("08:05", "Script Agent", "Propone estructura de guion corto", "Completado", 88),
        AgentTimelineStep("08:06", "Storyboard Agent", "Ordena escenas y subtitulos planeados", "Completado", 86),
        AgentTimelineStep("08:06", "SEO Agent", "Prepara metadatos seguros para descubrimiento", "Completado", 85),
        AgentTimelineStep("08:07", "Quality Agent", "Revisa calidad, seguridad y cumplimiento", "Completado", 95),
        AgentTimelineStep("08:07", "Director General IA", "Aprueba resultado mock y siguiente accion", "Completado", 94),
    ]
    return AgentSimulationResponse(
        source_mode=source_mode,
        active_project_name=active_project.name if active_project else None,
        mission=payload.mission,
        director_summary="El Director General IA coordino agentes especializados y aprobo una estrategia editorial mock, original y responsable.",
        timeline=[AgentTimelineStepSchema(**asdict(step)) for step in steps],
        final_result="Mision lista para pasar a Content Brain o Workflow MVP sin generar video, audio, imagenes ni publicar.",
        quality_score=92,
        confidence_score=94,
        next_action="Enviar la estrategia aprobada al flujo guiado de creacion de contenido.",
    )



