from abc import ABC, abstractmethod

from app.models.ai_provider import AIRequest, AIResponse


class BaseProvider(ABC):
    name = "base"

    @abstractmethod
    def generate(self, request: AIRequest) -> AIResponse:
        raise NotImplementedError

    def health(self) -> dict[str, object]:
        return {"provider": self.name, "status": "placeholder"}

