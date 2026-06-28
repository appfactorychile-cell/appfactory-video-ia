from dataclasses import asdict

from app.schemas.content_brain_schema import (
    ContentBrainAnalysisResponse,
    ContentBrainRecommendationResponse,
    ContentBrainRequest,
    ContentBrainStoryboardResponse,
    ProductionPlanSchema,
    StoryboardSceneSchema,
)
from app.projects import project_library
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


def analyze(payload: ContentBrainRequest) -> ContentBrainAnalysisResponse:
    source_mode, project_context = _source_context()
    research = research_service.research_opportunity(payload)
    ideas = idea_generator_service.generate_ideas(research)
    ranking = idea_ranking_service.rank_ideas(ideas)
    best_idea = ranking[0]
    audience = audience_service.build_audience_profile(payload)
    hooks = hook_service.generate_hooks(best_idea)
    story_strategy = story_strategy_service.build_story_strategy(best_idea, audience)
    production_plan = production_plan_service.build_production_plan(story_strategy, payload.language)

    return ContentBrainAnalysisResponse(
        source_mode=source_mode,
        project_context=project_context,
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
            subtitles="What would you test first?",
        ),
        narration="Hook, context, practical example and responsible conversation close.",
        subtitles=["Clear hook", "Useful example", "Responsible CTA"],
        cta="What would you try first in your own work?",
        duration_seconds=result.story_strategy.recommended_duration_seconds,
    )


def production_plan(payload: ContentBrainRequest) -> ProductionPlanSchema:
    return analyze(payload).production_plan


