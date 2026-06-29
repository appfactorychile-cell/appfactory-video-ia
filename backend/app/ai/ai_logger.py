from dataclasses import asdict

from app.models.ai_provider import PromptLog

_PROMPTS: list[PromptLog] = []


def log_prompt(task: str, provider: str, prompt: str) -> None:
    _PROMPTS.append(PromptLog(task=task, provider=provider, prompt_preview=prompt[:240]))


def list_logs() -> list[dict[str, object]]:
    return [asdict(item) for item in _PROMPTS]

