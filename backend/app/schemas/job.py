from pydantic import BaseModel

from backend.app.models.job import JobDescription


class JobUploadResponse(BaseModel):
    job_id: str
    job: JobDescription