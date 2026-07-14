from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None


class Candidate(BaseModel):
    full_name: str | None = None
    headline: str | None = None
    summary: str | None = None

    contact: Contact = Field(default_factory=Contact)


class Education(BaseModel):
    institution: str | None = None
    degree: str | None = None
    field: str | None = None
    start_year: int | None = None
    end_year: int | None = None
    grade: str | None = None


class Experience(BaseModel):
    company: str | None = None
    title: str | None = None
    duration: str | None = None

    responsibilities: list[str] = Field(default_factory=list)

    technologies: list[str] = Field(default_factory=list)


class Project(BaseModel):
    title: str | None = None
    description: str | None = None

    technologies: list[str] = Field(default_factory=list)

    impact: list[str] = Field(default_factory=list)

    github: str | None = None

    live_demo: str | None = None


class Certification(BaseModel):
    name: str | None = None

    issuer: str | None = None

    year: int | None = None


class Resume(BaseModel):

    candidate: Candidate

    education: list[Education] = Field(default_factory=list)

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    technical_skills: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    certifications: list[Certification] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)