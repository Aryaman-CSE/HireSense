from pydantic import BaseModel, Field


class JobRequirement(BaseModel):
    skill: str
    required: bool = True


class JobDescription(BaseModel):

    title: str | None = None

    company: str | None = None

    location: str | None = None

    employment_type: str | None = None

    experience: str | None = None

    education: str | None = None

    responsibilities: list[str] = Field(default_factory=list)

    required_skills: list[JobRequirement] = Field(default_factory=list)

    preferred_skills: list[JobRequirement] = Field(default_factory=list)

    technologies: list[str] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)