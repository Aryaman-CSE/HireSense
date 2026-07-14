import json

from sqlalchemy.orm import Session

from backend.app.db.job_models import JobRecord
from backend.app.models.job import JobDescription


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(
        self,
        job: JobDescription,
        raw_description: str,
    ) -> JobRecord:

        record = JobRecord(
            title=job.title or "Unknown",
            company=job.company or "Unknown",
            raw_description=raw_description,
            analysis_json=job.model_dump_json(indent=2),
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record

    def get(
        self,
        job_id: str,
    ) -> JobRecord | None:

        return self.db.get(
            JobRecord,
            job_id,
        )

    def list(self) -> list[JobRecord]:

        return (
            self.db.query(JobRecord)
            .order_by(JobRecord.created_at.desc())
            .all()
        )

    def delete(
        self,
        job_id: str,
    ) -> bool:

        record = self.get(job_id)

        if record is None:
            return False

        self.db.delete(record)
        self.db.commit()

        return True

    def get_analysis(
        self,
        job_id: str,
    ) -> dict | None:

        record = self.get(job_id)

        if record is None:
            return None

        return json.loads(record.analysis_json)