from app.models.content_brain import ResearchResult
from app.schemas.content_brain_schema import ContentBrainRequest


def research_opportunity(payload: ContentBrainRequest) -> ResearchResult:
    return ResearchResult(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        summary=(
            f"Mock research for {payload.topic} in {payload.country}: audience interest is rising, "
            f"the {payload.niche} niche rewards practical examples, and the story should be localized in {payload.language}."
        ),
        key_findings=[
            "The topic has strong educational value when explained with one concrete daily-life example.",
            "The safest editorial angle is usefulness plus curiosity, not hype or unverified promises.",
            "Short vertical formats should open with a clear problem in the first three seconds.",
            "Local examples increase retention because the audience recognizes the situation faster.",
        ],
        safe_sources_policy="Mock mode: use only verified, permitted and non-copyrighted sources in future real integrations.",
    )
