from app.models.content_brain import ProductionPlan, StoryStrategy


def build_production_plan(strategy: StoryStrategy, language: str) -> ProductionPlan:
    return ProductionPlan(
        narrator="Natural AI narrator, confident but warm",
        visual_style=strategy.visual_style,
        camera_type="Vertical 9:16, simulated handheld plus slow push-in shots",
        lighting="High-contrast studio lighting with soft cyan accents",
        music="Modern light pulse, low volume, no copyrighted tracks",
        transitions="Fast cuts, clean zooms and caption-led scene changes",
        format="Shorts/Reels/TikTok vertical explainer",
        platforms=["YouTube Shorts", "Instagram Reels", "TikTok", "Facebook Reels"],
        duration_seconds=strategy.recommended_duration_seconds,
        language=language,
    )
