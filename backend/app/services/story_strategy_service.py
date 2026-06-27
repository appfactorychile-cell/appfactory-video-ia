from app.models.content_brain import AudienceProfile, RankedIdea, StoryStrategy


def build_story_strategy(best_idea: RankedIdea, audience: AudienceProfile) -> StoryStrategy:
    return StoryStrategy(
        selected_idea=best_idea.title,
        emotional_goal="Create curiosity first, then relief by making the idea feel simple and useful.",
        narrative_arc="Hook with a surprising problem, explain one concrete example, close with a practical question.",
        tone=audience.preferred_tone,
        character="A calm expert narrator with a relatable operator or creator as the visual anchor.",
        visual_style="Premium dark editorial, kinetic captions, clean data overlays and realistic scenes.",
        recommended_duration_seconds=38,
    )
