from app.models.content_brain import AudienceProfile
from app.schemas.content_brain_schema import ContentBrainRequest


def build_audience_profile(payload: ContentBrainRequest) -> AudienceProfile:
    return AudienceProfile(
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        target_audience="Curious digital viewers, creators and small business operators aged 24 to 44.",
        motivations=[
            "Learn something useful quickly.",
            "Understand why the topic is being discussed.",
            "Find a practical next step without feeling overwhelmed.",
        ],
        objections=[
            "Avoid hype and exaggerated promises.",
            "Do not use generic examples that ignore local context.",
            "Keep the explanation simple and visually clear.",
        ],
        preferred_tone="Smart, clear, energetic and culturally localized.",
    )
