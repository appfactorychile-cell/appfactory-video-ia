from dataclasses import asdict

from app.ai import prompt_builder, provider_manager
from app.intelligence import global_intelligence
from app.models.content_brain import ContentIdea, HookProposal, RankedIdea
from app.projects import project_library
from app.schemas.content_brain_schema import (
    ContentBrainAnalysisResponse,
    ContentBrainRecommendationResponse,
    ContentBrainRequest,
    ContentBrainStoryboardResponse,
    ProductionPlanSchema,
    StoryboardSceneSchema,
)
from app.services import (
    audience_service,
    hook_service,
    idea_generator_service,
    idea_ranking_service,
    production_plan_service,
    research_service,
    story_strategy_service,
)


def _source_context() -> tuple[str, str]:
    active_project = project_library.get_active_project()
    if active_project is None:
        return "Contenido global", "Sin proyecto activo. La IA trabaja con tendencias globales y locales simuladas."
    return "Proyecto vinculado", f"Proyecto activo: {active_project.name}. Usar solo informacion autorizada de este proyecto."


def _content_idea_from_ai(item: dict[str, object], index: int) -> ContentIdea:
    return ContentIdea(
        title=str(item.get("title") or f"Idea IA {index}"),
        angle=str(item.get("angle") or "Angulo practico y localizado"),
        emotion=str(item.get("emotion") or "Curiosidad"),
        value_promise=str(item.get("value_promise") or "Explicar una oportunidad con valor real"),
        target_duration_seconds=int(item.get("target_duration_seconds") or 38),
    )


def _ranked_idea_from_ai(item: dict[str, object], index: int) -> RankedIdea:
    return RankedIdea(
        rank=index,
        title=str(item.get("title") or f"Idea IA {index}"),
        score=int(item.get("score") or item.get("curiosity_score") or 86),
        curiosity_score=int(item.get("curiosity_score") or 86),
        conversation_score=int(item.get("conversation_score") or 82),
        monetization_score=int(item.get("monetization_score") or 80),
        reason=str(item.get("reason") or "Buena combinacion de utilidad, curiosidad y bajo riesgo."),
    )


def _hook_from_ai(item: dict[str, object], index: int) -> HookProposal:
    return HookProposal(
        hook=str(item.get("hook") or f"Hook IA {index}"),
        score=int(item.get("score") or 86),
        emotion=str(item.get("emotion") or "Curiosidad"),
        expected_retention=str(item.get("expected_retention") or "Alta"),
    )


def _ai_ideas(payload: ContentBrainRequest) -> tuple[list[ContentIdea], list[RankedIdea]] | None:
    try:
        request = prompt_builder.build_request(
            "ideas",
            topic=payload.topic,
            country=payload.country,
            language=payload.language,
            niche=payload.niche,
            idea="",
            hook="",
            script="",
        )
        response = provider_manager.generate(request)
        parsed = response.parsed if isinstance(response.parsed, dict) else {}
        items = parsed.get("ideas", []) if isinstance(parsed, dict) else []
        if not isinstance(items, list) or not items:
            return None
        ideas = [_content_idea_from_ai(item if isinstance(item, dict) else {}, index) for index, item in enumerate(items[:10], start=1)]
        ranking = [_ranked_idea_from_ai(item if isinstance(item, dict) else {}, index) for index, item in enumerate(items[:10], start=1)]
        return ideas, ranking
    except Exception:
        return None


def _ai_hooks(payload: ContentBrainRequest, best_idea: RankedIdea) -> list[HookProposal] | None:
    try:
        request = prompt_builder.build_request(
            "hooks",
            topic=payload.topic,
            country=payload.country,
            language=payload.language,
            niche=payload.niche,
            idea=best_idea.title,
            hook="",
            script="",
        )
        response = provider_manager.generate(request)
        parsed = response.parsed if isinstance(response.parsed, dict) else {}
        items = parsed.get("hooks", []) if isinstance(parsed, dict) else []
        if not isinstance(items, list) or not items:
            return None
        return [_hook_from_ai(item if isinstance(item, dict) else {}, index) for index, item in enumerate(items[:5], start=1)]
    except Exception:
        return None


def _ai_script(payload: ContentBrainRequest, title: str, hook: str) -> dict[str, object] | None:
    try:
        request = prompt_builder.build_request(
            "script",
            topic=payload.topic,
            country=payload.country,
            language=payload.language,
            niche=payload.niche,
            idea=title,
            hook=hook,
            script="",
        )
        response = provider_manager.generate(request)
        return response.parsed if isinstance(response.parsed, dict) else None
    except Exception:
        return None


def analyze(payload: ContentBrainRequest) -> ContentBrainAnalysisResponse:
    source_mode, project_context = _source_context()
    executive_audit = global_intelligence.analyze_global_opportunity(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
    )
    research = research_service.research_opportunity(payload)
    ai_ideas = _ai_ideas(payload)
    if ai_ideas:
        ideas, ranking = ai_ideas
    else:
        ideas = idea_generator_service.generate_ideas(research)
        ranking = idea_ranking_service.rank_ideas(ideas)
    best_idea = ranking[0]
    audience = audience_service.build_audience_profile(payload)
    hooks = _ai_hooks(payload, best_idea) or hook_service.generate_hooks(best_idea)
    story_strategy = story_strategy_service.build_story_strategy(best_idea, audience)
    production_plan = production_plan_service.build_production_plan(story_strategy, payload.language)

    return ContentBrainAnalysisResponse(
        source_mode=source_mode,
        project_context=project_context,
        executive_decision=executive_audit["executive_decision"],
        opportunity_score=best_idea.score,
        research_summary=asdict(research),
        ideas=[asdict(idea) for idea in ideas],
        ranking=[asdict(item) for item in ranking],
        best_idea=asdict(best_idea),
        audience_profile=asdict(audience),
        hooks=[asdict(hook) for hook in hooks],
        story_strategy=asdict(story_strategy),
        production_plan=asdict(production_plan),
    )


def recommend(payload: ContentBrainRequest) -> ContentBrainRecommendationResponse:
    result = analyze(payload)
    best = result.best_idea
    strategy = result.story_strategy
    return ContentBrainRecommendationResponse(
        source_mode=result.source_mode,
        project_context=result.project_context,
        executive_decision=result.executive_decision,
        best_idea=best.title,
        why_this_idea_is_better=best.reason,
        target_emotion=strategy.emotional_goal,
        recommended_duration_seconds=strategy.recommended_duration_seconds,
        recommended_character=strategy.character,
        recommended_visual_style=strategy.visual_style,
        recommended_tone=strategy.tone,
        curiosity_level=best.curiosity_score,
        conversation_potential=best.conversation_score,
        monetization_potential=best.monetization_score,
    )


def storyboard(payload: ContentBrainRequest) -> ContentBrainStoryboardResponse:
    result = analyze(payload)
    title = result.best_idea.title
    hook = result.hooks[0].hook
    ai_script = _ai_script(payload, title, hook)
    if ai_script:
        subtitles = ai_script.get("subtitles", [])
        subtitle_lines = subtitles if isinstance(subtitles, list) else [str(subtitles)]
        narration = str(ai_script.get("narration") or "Guion generado por Provider Manager.")
        return ContentBrainStoryboardResponse(
            title=str(ai_script.get("title") or title),
            hook=str(ai_script.get("hook") or hook),
            scene_1=StoryboardSceneSchema(
                scene="Scene 1",
                visual="Hook visual localizado.",
                narration=narration[:220],
                subtitles=str(subtitle_lines[0]) if subtitle_lines else "Inicio claro.",
            ),
            scene_2=StoryboardSceneSchema(
                scene="Scene 2",
                visual="Ejemplo practico.",
                narration="Desarrollo del valor central.",
                subtitles=str(subtitle_lines[1]) if len(subtitle_lines) > 1 else "Valor practico.",
            ),
            scene_3=StoryboardSceneSchema(
                scene="Scene 3",
                visual="Cierre seguro.",
                narration="CTA responsable.",
                subtitles=str(subtitle_lines[2]) if len(subtitle_lines) > 2 else "Cierre responsable.",
            ),
            narration=narration,
            subtitles=[str(item) for item in subtitle_lines],
            cta=str(ai_script.get("cta") or "Que aplicarias primero?"),
            duration_seconds=int(ai_script.get("duration_seconds") or result.story_strategy.recommended_duration_seconds),
        )
    return ContentBrainStoryboardResponse(
        title=title,
        hook=hook,
        scene_1=StoryboardSceneSchema(
            scene="Scene 1",
            visual="Close-up of the main problem with bold kinetic text.",
            narration=f"{hook} Today we are looking at {payload.topic} in a way that feels practical, not generic.",
            subtitles="A clear problem appears in the first three seconds.",
        ),
        scene_2=StoryboardSceneSchema(
            scene="Scene 2",
            visual="Realistic example, localized to the selected country and niche.",
            narration="One simple example shows why this opportunity matters and how people can understand it quickly.",
            subtitles="One example. One useful idea. No hype.",
        ),
        scene_3=StoryboardSceneSchema(
            scene="Scene 3",
            visual="Clean summary, CTA and platform-safe closing frame.",
            narration="The takeaway is simple: use the trend responsibly, verify claims and ask what problem it solves.",
            subtitles="What would you try first?",
        ),
        narration="Hook, context, practical example and responsible conversation close.",
        subtitles=["Clear hook", "Useful example", "Responsible CTA"],
        cta="What would you try first in your own work?",
        duration_seconds=result.story_strategy.recommended_duration_seconds,
    )


def production_plan(payload: ContentBrainRequest) -> ProductionPlanSchema:
    return analyze(payload).production_plan
