import json

from sqlalchemy.orm import Session

from backend.app.db.models import ResumeRecord
from backend.app.models.response import ResumeIntelligenceResponse


class ResumeRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(
        self,
        original_filename: str,
        stored_filename: str,
        extracted_text: str,
        analysis: ResumeIntelligenceResponse,
    ) -> ResumeRecord:

        record = ResumeRecord(
            original_filename=original_filename,
            stored_filename=stored_filename,
            extracted_text=extracted_text,
            analysis_json=analysis.model_dump_json(
                indent=2
            ),
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record

    def get(
        self,
        resume_id: str,
    ) -> ResumeRecord | None:

        return self.db.get(
            ResumeRecord,
            resume_id,
        )

    def list(self) -> list[ResumeRecord]:

        return (
            self.db.query(ResumeRecord)
            .order_by(
                ResumeRecord.created_at.desc()
            )
            .all()
        )

    def delete(
        self,
        resume_id: str,
    ) -> bool:

        record = self.get(
            resume_id
        )

        if record is None:
            return False

        self.db.delete(record)

        self.db.commit()

        return True