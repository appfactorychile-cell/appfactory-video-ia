from app.agents.agent_factory import build_agent


def get_agent():
    return build_agent(
        name="SEO Agent",
        slug="seo-agent",
        specialty="SEO y descubrimiento",
        objective="Preparar titulo, descripcion y etiquetas responsables para plataformas futuras.",
        input="Idea, pais, idioma, nicho y plataforma objetivo.",
        output="Metadatos mock optimizados sin manipulacion ni promesas falsas.",
        status="Disponible",
        execution_time_seconds=1.3,
        confidence_level=85,
        last_execution="08:05",
    )
