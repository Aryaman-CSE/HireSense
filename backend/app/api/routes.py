from fastapi import APIRouter, File, HTTPException, UploadFile

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