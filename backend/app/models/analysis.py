from pydantic import BaseModel, Field


class ResumeAnalysis(BaseModel):

    overall_score: int

    technical_depth: int

    communication: int

    project_quality: int

    impact: int

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)

    recommendations: list[str] = Field(default_factory=list)