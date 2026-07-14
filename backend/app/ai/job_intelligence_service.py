import json

from backend.app.ai.providers.groq_provider import GroqProvider
from backend.app.ai.utils import load_prompt

from backend.app.models.job import JobDescription


class JobIntelligenceService:

    def __init__(self):
        self.provider = GroqProvider()

    def analyze_job(
        self,
        job_description: str,
    ) -> JobDescription:

        prompt = load_prompt(
            "job_extraction"
        )

        prompt = prompt.replace(
            "{{job}}",
            job_description,
        )

        response = self.provider.generate(
            prompt
        )

        try:

            parsed = json.loads(
                response
            )

        except json.JSONDecodeError as e:

            raise ValueError(
                f"Invalid JSON returned by AI:\n\n{response}"
            ) from e

        return JobDescription.model_validate(
            parsed
        )