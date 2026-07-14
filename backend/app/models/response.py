from pydantic import BaseModel

from backend.app.models.analysis import ResumeAnalysis
from backend.app.models.resume import Resume


class ResumeIntelligenceResponse(BaseModel):
    resume: Resume
    analysis: ResumeAnalysis