from app.models.content_brain import HookProposal, RankedIdea


def generate_hooks(best_idea: RankedIdea) -> list[HookProposal]:
    return [
        HookProposal("Nobody is explaining this part clearly...", 94, "curiosity", "Very strong first 3 seconds"),
        HookProposal("This looks small, but it changes the whole story...", 91, "surprise", "Strong retention through contrast"),
        HookProposal("Here is the reason people are starting to talk about this...", 88, "context", "Good for educational audiences"),
        HookProposal("Before you ignore this trend, watch the next 20 seconds...", 86, "urgency", "Useful when the payoff is practical"),
        HookProposal("This is the simple example that makes it finally make sense...", 92, "clarity", "High completion potential"),
    ]
