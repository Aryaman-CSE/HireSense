from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from backend.app.services.extraction_service import ExtractionService

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class UploadService:

    @staticmethod
    async def save_resume(file: UploadFile):

        extension = file.filename.split(".")[-1].lower()

        if extension not in {"pdf", "docx"}:
            raise ValueError("Only PDF and DOCX files are allowed.")

        filename = f"{uuid4()}.{extension}"

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = ExtractionService.extract_text(str(destination))

        preview = extracted_text[:500]

        return {
            "id": filename.split(".")[0],
            "filename": filename,
            "original_filename": file.filename,
            "content_type": file.content_type,
            "size": destination.stat().st_size,
            "text_preview": preview,
        }