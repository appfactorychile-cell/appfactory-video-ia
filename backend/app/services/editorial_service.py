from app.schemas.opportunity_schema import (
    EditorialRecommendationRequest,
    EditorialRecommendationResponse,
)


def recommend_content(payload: EditorialRecommendationRequest) -> EditorialRecommendationResponse:
    confidence = min(96, max(50, payload.opportunity_score + 8))
    return EditorialRecommendationResponse(
        topic=payload.topic,
        recommendation="Produce a short original video with a strong curiosity hook and practical value.",
        ai_confidence_score=confidence,
        reasons=[
            f"The simulated opportunity score is {payload.opportunity_score}/100.",
            f"The topic fits the {payload.niche} niche for {payload.country}.",
            "The content can be localized instead of translated literally.",
            "The format supports retention through curiosity, clarity and responsible storytelling.",
        ],
        risks=[
            "Avoid unverified claims or rumors.",
            "Do not reuse copyrighted visuals, scripts or formats.",
            "Keep the final script culturally appropriate for the selected language.",
        ],
        final_decision="recommended_for_mock_production",
    )
