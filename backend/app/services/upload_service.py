from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from backend.app.pipeline.resume_pipeline import ResumePipeline
from backend.app.services.extraction_service import ExtractionService

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class UploadService:

    def __init__(self):
        self.pipeline = ResumePipeline()

    async def process_resume(self, file: UploadFile):

        extension = file.filename.split(".")[-1].lower()

        if extension not in {"pdf", "docx"}:
            raise ValueError("Only PDF and DOCX files are allowed.")

        resume_id = str(uuid4())

        filename = f"{resume_id}.{extension}"

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = ExtractionService.extract_text(
            str(destination)
        )

        intelligence = self.pipeline.process(
            extracted_text
        )

        return {
            "resume_id": resume_id,
            "filename": filename,
            "analysis": intelligence,
        }