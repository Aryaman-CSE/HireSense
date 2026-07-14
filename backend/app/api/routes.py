import json

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.db.database import SessionLocal
from backend.app.repositories.resume_repository import ResumeRepository
from backend.app.schemas.upload import UploadResponse
from backend.app.services.upload_service import UploadService

router = APIRouter()

upload_service = UploadService()


@router.get("/")
async def root():
    return {
        "application": "HireSense",
        "status": "running",
        "version": "0.1.0",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
    }


@router.get("/ai/health")
async def ai_health():
    return {
        "provider": "Groq",
        "status": "connected",
        "model": "llama-3.3-70b-versatile",
    }


@router.post(
    "/resumes/upload",
    response_model=UploadResponse,
)
async def upload_resume(
    file: UploadFile = File(...)
):
    try:
        return await upload_service.process_resume(file)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get("/resumes")
async def list_resumes():

    db = SessionLocal()

    try:

        repository = ResumeRepository(db)

        resumes = repository.list()

        return [
            {
                "id": resume.id,
                "original_filename": resume.original_filename,
                "stored_filename": resume.stored_filename,
                "created_at": resume.created_at,
            }
            for resume in resumes
        ]

    finally:

        db.close()


@router.get("/resumes/{resume_id}")
async def get_resume(
    resume_id: str,
):

    db = SessionLocal()

    try:

        repository = ResumeRepository(db)

        resume = repository.get(
            resume_id
        )

        if resume is None:
            raise HTTPException(
                status_code=404,
                detail="Resume not found.",
            )

        return {
            "id": resume.id,
            "original_filename": resume.original_filename,
            "stored_filename": resume.stored_filename,
            "created_at": resume.created_at,
            "analysis": json.loads(
                resume.analysis_json
            ),
        }

    finally:

        db.close()


@router.delete("/resumes/{resume_id}")
async def delete_resume(
    resume_id: str,
):

    db = SessionLocal()

    try:

        repository = ResumeRepository(db)

        deleted = repository.delete(
            resume_id
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Resume not found.",
            )

        return {
            "message": "Resume deleted successfully."
        }

    finally:

        db.close()