from typing import Any

from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None


class ResumeAIResponse(BaseModel):

    candidate: Candidate

    summary: str | None = None

    technical_skills: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    education: list[Any] = Field(default_factory=list)

    experience: list[Any] = Field(default_factory=list)

    projects: list[Any] = Field(default_factory=list)

    certifications: list[Any] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)