from backend.app.models.job import JobDescription
from backend.app.models.resume import Resume


class SemanticMatchEngine:

    def match(
        self,
        resume: Resume,
        job: JobDescription,
    ) -> dict:

        resume_skills = {
            skill.lower()
            for skill in resume.technical_skills
        }

        required = {
            skill.skill.lower()
            for skill in job.required_skills
        }

        preferred = {
            skill.skill.lower()
            for skill in job.preferred_skills
        }

        matched_required = sorted(
            required & resume_skills
        )

        missing_required = sorted(
            required - resume_skills
        )

        matched_preferred = sorted(
            preferred & resume_skills
        )

        missing_preferred = sorted(
            preferred - resume_skills
        )

        total_weight = (
            len(required) * 2
            + len(preferred)
        )

        earned = (
            len(matched_required) * 2
            + len(matched_preferred)
        )

        score = (
            int((earned / total_weight) * 100)
            if total_weight
            else 100
        )

        return {

            "match_score": score,

            "matched_required": matched_required,

            "missing_required": missing_required,

            "matched_preferred": matched_preferred,

            "missing_preferred": missing_preferred,
        }