import json

from backend.app.ai.providers.groq_provider import GroqProvider
from backend.app.ai.utils import load_prompt
from backend.app.models.response import ResumeIntelligenceResponse


class IntelligenceService:

    def __init__(self):
        self.provider = GroqProvider()

    def analyze_resume(
        self,
        resume_text: str,
    ) -> ResumeIntelligenceResponse:

        prompt = load_prompt("resume_extraction")

        prompt = prompt.replace(
            "{{resume}}",
            resume_text,
        )

        response = self.provider.generate(
            prompt
        )

        try:
            parsed = json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON returned by AI:\n\n{response}"
            ) from e

        return ResumeIntelligenceResponse.model_validate(
            parsed
        )