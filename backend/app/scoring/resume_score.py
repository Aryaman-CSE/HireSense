from backend.app.models.resume import Resume


class ResumeScorer:

    def score(
        self,
        resume: Resume,
    ) -> dict:

        score = 0

        breakdown = {}

        technical = min(
            len(resume.technical_skills),
            20,
        )

        technical *= 2

        breakdown["technical_skills"] = technical

        score += technical

        projects = min(
            len(resume.projects),
            5,
        ) * 6

        breakdown["projects"] = projects

        score += projects

        experience = min(
            len(resume.experience),
            5,
        ) * 5

        breakdown["experience"] = experience

        score += experience

        education = 10 if resume.education else 0

        breakdown["education"] = education

        score += education

        certifications = min(
            len(resume.certifications),
            2,
        ) * 5

        breakdown["certifications"] = certifications

        score += certifications

        languages = 5 if resume.languages else 0

        breakdown["languages"] = languages

        score += languages

        return {

            "overall_score": min(
                score,
                100,
            ),

            "breakdown": breakdown,
        }