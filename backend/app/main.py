from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes import router
from backend.app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\n========== REGISTERED ROUTES ==========")

    for route in app.routes:
        if hasattr(route, "path"):
            print(route.path)

    print("=======================================\n")

    print("🚀 HireSense Backend Started")

    yield

    print("🛑 HireSense Backend Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="AI Resume Intelligence Platform",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix=settings.API_PREFIX,
    tags=["API"],
)