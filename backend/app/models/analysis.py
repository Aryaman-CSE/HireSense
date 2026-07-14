from pydantic import BaseModel, Field


class ScoreBreakdown(BaseModel):
    technical_skills: int = 0
    projects: int = 0
    experience: int = 0
    education: int = 0
    certifications: int = 0
    languages: int = 0


class ResumeAnalysis(BaseModel):

    overall_score: int = 0

    score_breakdown: ScoreBreakdown = Field(
        default_factory=ScoreBreakdown
    )

    ats_score: int = 0

    strengths: list[str] = Field(
        default_factory=list
    )

    weaknesses: list[str] = Field(
        default_factory=list
    )

    missing_skills: list[str] = Field(
        default_factory=list
    )

    recommendations: list[str] = Field(
        default_factory=list
    )

    recruiter_summary: str | None = None