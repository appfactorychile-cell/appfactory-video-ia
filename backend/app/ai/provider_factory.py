from app.providers.openai_provider import from_env


def create_provider(slug: str):
    if slug == "openai":
        return from_env()
    raise RuntimeError(f"Provider {slug} is registered as placeholder only.")

