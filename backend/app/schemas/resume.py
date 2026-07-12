from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    id: str
    filename: str
    original_filename: str
    content_type: str
    size: int