def conversation_key(task: str, prompt: str, provider: str, model: str) -> str:
    return f"{provider}:{model}:{task}:{hash(prompt)}"

