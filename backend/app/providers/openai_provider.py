import json
import os
import time
import urllib.error
import urllib.request
from uuid import uuid4

from app.models.ai_provider import AIRequest, AIResponse
from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    name = "openai"

    def __init__(self, api_key: str, model: str, timeout: int) -> None:
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    def generate(self, request: AIRequest) -> AIResponse:
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")
        model = request.model or self.model
        started = time.perf_counter()
        payload = {
            "model": model,
            "input": [
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": request.prompt},
            ],
            "temperature": request.temperature,
            "max_output_tokens": request.max_output_tokens,
        }
        http_request = urllib.request.Request(
            "https://api.openai.com/v1/responses",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(http_request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI request failed: {exc.code} {detail}") from exc
        data = json.loads(raw)
        content = self._extract_text(data)
        usage = data.get("usage", {}) if isinstance(data, dict) else {}
        input_tokens = int(usage.get("input_tokens", 0) or 0)
        output_tokens = int(usage.get("output_tokens", 0) or 0)
        elapsed = int((time.perf_counter() - started) * 1000)
        return AIResponse(
            id=str(data.get("id") or uuid4()),
            provider=self.name,
            model=model,
            task=request.task,
            content=content,
            parsed=None,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            estimated_cost_usd=0.0,
            response_time_ms=elapsed,
        )

    def health(self) -> dict[str, object]:
        return {
            "provider": self.name,
            "status": "available" if bool(self.api_key) else "missing_api_key",
            "model": self.model,
            "timeout": self.timeout,
        }

    @staticmethod
    def _extract_text(data: dict[str, object]) -> str:
        text = data.get("output_text")
        if isinstance(text, str) and text.strip():
            return text.strip()
        chunks: list[str] = []
        for item in data.get("output", []) or []:
            if not isinstance(item, dict):
                continue
            for content in item.get("content", []) or []:
                if isinstance(content, dict) and content.get("type") in {"output_text", "text"}:
                    value = content.get("text")
                    if isinstance(value, str):
                        chunks.append(value)
        return "\n".join(chunks).strip()


def from_env() -> OpenAIProvider:
    return OpenAIProvider(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        timeout=int(os.getenv("OPENAI_TIMEOUT", "45")),
    )

