from app.models.ai_provider import AIProvider


def providers(openai_model: str, openai_ready: bool) -> list[AIProvider]:
    return [
        AIProvider("OpenAI", "openai", "Disponible" if openai_ready else "Falta OPENAI_API_KEY", openai_model, openai_ready, 1, "Primer proveedor real de texto."),
        AIProvider("Gemini", "gemini", "Placeholder", "pendiente", False, 2, "Preparado para fase futura."),
        AIProvider("Claude", "claude", "Placeholder", "pendiente", False, 3, "Preparado para fase futura."),
        AIProvider("DeepSeek", "deepseek", "Placeholder", "pendiente", False, 4, "Preparado para fase futura."),
        AIProvider("Ollama", "ollama", "Placeholder", "local", False, 5, "Preparado para modelos locales futuros."),
    ]

