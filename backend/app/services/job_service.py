from backend.app.ai.job_intelligence_service import JobIntelligenceService
from backend.app.db.database import SessionLocal
from backend.app.repositories.job_repository import JobRepository


class JobService:

    def __init__(self):
        self.intelligence = JobIntelligenceService()

    def process_job(
        self,
        job_description: str,
    ):

        analysis = self.intelligence.analyze_job(
            job_description
        )

        db = SessionLocal()

        try:

            repository = JobRepository(db)

            record = repository.save(
                job=analysis,
                raw_description=job_description,
            )

        finally:

            db.close()

        return {
            "job_id": record.id,
            "job": analysis,
        }