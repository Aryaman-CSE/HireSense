from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from backend.app.ai.intelligence_service import IntelligenceService
from backend.app.db.database import SessionLocal
from backend.app.repositories.resume_repository import ResumeRepository
from backend.app.services.extraction_service import ExtractionService

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class UploadService:

    def __init__(self):
        self.intelligence_service = IntelligenceService()

    async def process_resume(
        self,
        file: UploadFile,
    ):

        extension = file.filename.split(".")[-1].lower()

        if extension not in {"pdf", "docx"}:
            raise ValueError(
                "Only PDF and DOCX files are allowed."
            )

        filename = f"{uuid4()}.{extension}"

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        extracted_text = ExtractionService.extract_text(
            str(destination)
        )

        analysis = self.intelligence_service.analyze_resume(
            extracted_text
        )

        db = SessionLocal()

        try:

            repository = ResumeRepository(
                db
            )

            record = repository.save(
                original_filename=file.filename,
                stored_filename=filename,
                extracted_text=extracted_text,
                analysis=analysis,
            )

        finally:

            db.close()

        return {
            "resume_id": record.id,
            "filename": record.stored_filename,
            "analysis": analysis,
        }