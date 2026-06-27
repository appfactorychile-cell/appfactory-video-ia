from dataclasses import asdict

from app.data.mock_store import STORE
from app.models.content import ContentIdea, ContentScript
from app.schemas.content_schema import (
    ContentIdeaRequest,
    ContentIdeaResponse,
    ContentScriptRequest,
    ContentScriptResponse,
)


def generate_idea(payload: ContentIdeaRequest) -> ContentIdeaResponse:
    idea = ContentIdea(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        title=f"Why {payload.topic} is becoming impossible to ignore",
        hook="This looks like a small trend, but it may change what people talk about next.",
        angle=f"A culturally adapted {payload.niche} story for {payload.country}, built to be useful and entertaining.",
    )
    STORE.ideas.append(idea)
    return ContentIdeaResponse(**asdict(idea))


def generate_script(payload: ContentScriptRequest) -> ContentScriptResponse:
    duration = min(45, max(20, payload.target_duration_seconds))
    script = ContentScript(
        idea_title=payload.idea_title,
        language=payload.language,
        estimated_duration_seconds=duration,
        script=(
            f"Hook: {payload.idea_title}. In the first seconds, we show the surprising fact. "
            "Then we explain why it matters, using one clear example and one practical takeaway. "
            "We close with an open question that invites comments without exaggerating or inventing facts."
        ),
        scenes=[
            "Fast opening visual with the main question.",
            "Context scene showing the trend or problem.",
            "Simple explanation with one concrete example.",
            "Responsible closing with a conversation prompt.",
        ],
    )
    STORE.scripts.append(script)
    return ContentScriptResponse(**asdict(script))
