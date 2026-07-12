from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {
        "application": "HireSense",
        "message": "Welcome to HireSense",
        "status": "running",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "backend",
    }