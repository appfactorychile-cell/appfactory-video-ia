from app.ai import provider_factory, provider_selector


def route(preferred_provider: str | None = None):
    slug = provider_selector.select_provider(preferred_provider)
    return provider_factory.create_provider(slug)

