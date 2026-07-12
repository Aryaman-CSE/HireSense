from pydantic import BaseModel


class Candidate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None


class ResumeAIResponse(BaseModel):
    candidate: Candidate

    summary: str | None = None

    technical_skills: list[str] = []

    soft_skills: list[str] = []

    education: list = []

    experience: list = []

    projects: list = []

    certifications: list = []

    languages: list[str] = []