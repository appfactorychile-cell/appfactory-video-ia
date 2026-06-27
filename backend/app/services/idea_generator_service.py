from app.models.content_brain import ContentIdea
from app.models.content_brain import ResearchResult


def generate_ideas(research: ResearchResult) -> list[ContentIdea]:
    base = research.topic
    country = research.country
    return [
        ContentIdea(f"The hidden reason {base} matters now", "Curiosity-led explainer", "curiosity", "Understand the change before it becomes obvious", 38),
        ContentIdea(f"How {base} can save one hour today", "Practical tutorial", "relief", "Give one useful action the viewer can imagine applying", 35),
        ContentIdea(f"What most people misunderstand about {base}", "Myth correction", "surprise", "Correct a common misconception responsibly", 42),
        ContentIdea(f"A simple story from {country} about {base}", "Localized story", "recognition", "Make the trend feel close to the viewer", 40),
        ContentIdea(f"Before you ignore {base}, watch this", "Attention reset", "urgency", "Explain why the topic deserves attention without fearmongering", 32),
        ContentIdea(f"The 3-second test for {base}", "Fast framework", "clarity", "Turn a complex topic into a simple decision tool", 28),
        ContentIdea(f"Why creators are talking about {base}", "Conversation context", "belonging", "Explain the social conversation around the topic", 34),
        ContentIdea(f"The safest way to try {base}", "Responsible how-to", "trust", "Offer a low-risk first step", 44),
        ContentIdea(f"This small detail changes {base}", "Micro insight", "surprise", "Reveal one memorable detail", 31),
        ContentIdea(f"What happens next with {base}", "Future-facing story", "anticipation", "Preview the next likely stage without making false claims", 41),
    ]
