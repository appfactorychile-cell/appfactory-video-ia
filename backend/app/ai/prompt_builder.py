from app.ai.prompt_templates import TEMPLATES
from app.ai.system_prompts import SYSTEM_PROMPT
from app.models.ai_provider import AIRequest


def build_request(task: str, **kwargs: object) -> AIRequest:
    template = TEMPLATES[task]
    prompt = template.format(**{key: str(value) for key, value in kwargs.items()})
    return AIRequest(task=task, prompt=prompt, system_prompt=SYSTEM_PROMPT, metadata=kwargs)

