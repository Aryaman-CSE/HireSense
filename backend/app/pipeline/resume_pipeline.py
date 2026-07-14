from backend.app.ai.intelligence_service import IntelligenceService
from backend.app.models.response import ResumeIntelligenceResponse


class ResumePipeline:

    def __init__(self):
        self.intelligence_service = IntelligenceService()

    def process(
        self,
        extracted_text: str,
    ) -> ResumeIntelligenceResponse:

        intelligence = self.intelligence_service.analyze_resume(
            extracted_text
        )

        return intelligence