from pydantic import BaseModel, Field


class SkillMatch(BaseModel):
    matched: list[str] = Field(default_factory=list)
    missing: list[str] = Field(default_factory=list)


class SemanticMatchResult(BaseModel):

    match_score: int

    required: SkillMatch

    preferred: SkillMatch

    recommendations: list[str] = Field(default_factory=list)