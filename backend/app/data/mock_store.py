from app.models.channel import Channel
from app.models.content import ContentIdea, ContentScript
from app.models.opportunity import OpportunityAnalysis
from app.models.pipeline import PipelineRun


class MockStore:
    def __init__(self) -> None:
        self.channels: list[Channel] = [
            Channel(
                name="Ciencia Global",
                target_country="Chile",
                language="Spanish",
                timezone="America/Santiago",
                niche="Science",
                visual_style="Cinematic documentary",
                ai_voice="Calm natural narrator",
                daily_video_count=8,
                publishing_times=["08:00", "13:00", "17:00", "21:00"],
                connected_platforms=["YouTube", "TikTok"],
                content_rules=["Original content only", "Verify factual claims"],
            ),
            Channel(
                name="World Curiosity Lab",
                target_country="United States",
                language="English",
                timezone="America/New_York",
                niche="Curiosities",
                visual_style="Premium editorial",
                ai_voice="Energetic narrator",
                daily_video_count=8,
                publishing_times=["08:00", "13:00", "17:00", "21:00"],
                connected_platforms=["YouTube", "Instagram"],
                content_rules=["No rumors", "No copyrighted copying"],
            ),
        ]
        self.opportunities: list[OpportunityAnalysis] = []
        self.ideas: list[ContentIdea] = []
        self.scripts: list[ContentScript] = []
        self.pipeline_runs: list[PipelineRun] = []


STORE = MockStore()
