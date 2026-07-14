from pydantic import BaseModel

from backend.app.models.response import ResumeIntelligenceResponse


class UploadResponse(BaseModel):
    resume_id: str
    filename: str
    analysis: ResumeIntelligenceResponse