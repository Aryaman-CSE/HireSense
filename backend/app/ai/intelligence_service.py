import json

from backend.app.ai.providers.groq_provider import GroqProvider
from backend.app.ai.utils import load_prompt

from backend.app.models.analysis import ResumeAnalysis, ScoreBreakdown
from backend.app.models.response import ResumeIntelligenceResponse

from backend.app.scoring.resume_score import ResumeScorer


class IntelligenceService:

    def __init__(self):
        self.provider = GroqProvider()
        self.scorer = ResumeScorer()

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

        result = ResumeIntelligenceResponse.model_validate(
            parsed
        )

        score = self.scorer.score(
            result.resume
        )

        result.analysis.overall_score = score["overall_score"]

        result.analysis.score_breakdown = ScoreBreakdown(
            **score["breakdown"]
        )

        result.analysis.ats_score = self._calculate_ats_score(
            result
        )

        return result

    def _calculate_ats_score(
        self,
        result: ResumeIntelligenceResponse,
    ) -> int:

        score = 100

        if len(result.resume.projects) == 0:
            score -= 20

        if len(result.resume.technical_skills) < 8:
            score -= 15

        if len(result.resume.experience) == 0:
            score -= 20

        if result.resume.candidate.summary is None:
            score -= 10

        if len(result.resume.certifications) == 0:
            score -= 5

        return max(score, 0)