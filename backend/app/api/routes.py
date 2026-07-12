from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.schemas.resume import ResumeUploadResponse
from backend.app.services.upload_service import UploadService

router = APIRouter()


@router.get("/")
async def root():
    return {
        "application": "HireSense",
        "status": "running",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
    }


@router.post(
    "/resumes/upload",
    response_model=ResumeUploadResponse,
)
async def upload_resume(file: UploadFile = File(...)):

    try:
        return await UploadService.save_resume(file)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )