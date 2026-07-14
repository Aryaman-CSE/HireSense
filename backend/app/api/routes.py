import json

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from backend.app.db.database import SessionLocal
from backend.app.repositories.job_repository import JobRepository
from backend.app.repositories.resume_repository import ResumeRepository
from backend.app.schemas.job import JobUploadResponse
from backend.app.schemas.upload import UploadResponse
from backend.app.services.job_service import JobService
from backend.app.services.upload_service import UploadService

router = APIRouter()

upload_service = UploadService()
job_service = JobService()


class JobRequest(BaseModel):
    description: str


@router.get("/")
async def root():
    return {
        "application": "HireSense",
        "status": "running",
        "version": "0.2.0",
    }


@router.get("/health")
async def health():
    return {"status": "healthy"}


@router.get("/ai/health")
async def ai_health():
    return {
        "provider": "Groq",
        "status": "connected",
        "model": "llama-3.3-70b-versatile",
    }


# ----------------------------
# Resume APIs
# ----------------------------

@router.post(
    "/resumes/upload",
    response_model=UploadResponse,
)
async def upload_resume(file: UploadFile = File(...)):
    try:
        return await upload_service.process_resume(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/resumes")
async def list_resumes():

    db = SessionLocal()

    try:
        repository = ResumeRepository(db)

        return [
            {
                "id": r.id,
                "original_filename": r.original_filename,
                "stored_filename": r.stored_filename,
                "created_at": r.created_at,
            }
            for r in repository.list()
        ]

    finally:
        db.close()


@router.get("/resumes/{resume_id}")
async def get_resume(resume_id: str):

    db = SessionLocal()

    try:
        repository = ResumeRepository(db)

        resume = repository.get(resume_id)

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
            "analysis": json.loads(resume.analysis_json),
        }

    finally:
        db.close()


@router.delete("/resumes/{resume_id}")
async def delete_resume(resume_id: str):

    db = SessionLocal()

    try:
        repository = ResumeRepository(db)

        if not repository.delete(resume_id):
            raise HTTPException(
                status_code=404,
                detail="Resume not found.",
            )

        return {
            "message": "Resume deleted successfully."
        }

    finally:
        db.close()


# ----------------------------
# Job APIs
# ----------------------------

@router.post(
    "/jobs/upload",
    response_model=JobUploadResponse,
)
async def upload_job(
    request: JobRequest,
):
    try:
        return job_service.process_job(
            request.description
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get("/jobs")
async def list_jobs():

    db = SessionLocal()

    try:

        repository = JobRepository(db)

        jobs = repository.list()

        return [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "created_at": job.created_at,
            }
            for job in jobs
        ]

    finally:

        db.close()


@router.get("/jobs/{job_id}")
async def get_job(
    job_id: str,
):

    db = SessionLocal()

    try:

        repository = JobRepository(db)

        job = repository.get(job_id)

        if job is None:
            raise HTTPException(
                status_code=404,
                detail="Job not found.",
            )

        return {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "created_at": job.created_at,
            "analysis": json.loads(
                job.analysis_json
            ),
        }

    finally:

        db.close()


@router.delete("/jobs/{job_id}")
async def delete_job(
    job_id: str,
):

    db = SessionLocal()

    try:

        repository = JobRepository(db)

        if not repository.delete(job_id):
            raise HTTPException(
                status_code=404,
                detail="Job not found.",
            )

        return {
            "message": "Job deleted successfully."
        }

    finally:

        db.close()