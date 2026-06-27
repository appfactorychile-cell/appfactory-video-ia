from app.models.content_brain import ContentIdea, RankedIdea


def rank_ideas(ideas: list[ContentIdea]) -> list[RankedIdea]:
    ranked: list[RankedIdea] = []
    for index, idea in enumerate(ideas):
        curiosity = min(98, 78 + ((len(idea.title) + index * 3) % 18))
        conversation = min(96, 74 + ((len(idea.angle) + index * 5) % 20))
        monetization = min(94, 70 + ((idea.target_duration_seconds + index * 4) % 21))
        score = round(curiosity * 0.42 + conversation * 0.34 + monetization * 0.24)
        ranked.append(
            RankedIdea(
                rank=0,
                title=idea.title,
                score=score,
                curiosity_score=curiosity,
                conversation_score=conversation,
                monetization_score=monetization,
                reason="Balances curiosity, usefulness and responsible monetization potential.",
            )
        )
    ranked.sort(key=lambda item: item.score, reverse=True)
    for rank, item in enumerate(ranked, start=1):
        item.rank = rank
    return ranked
