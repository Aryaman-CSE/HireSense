from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes import router
from backend.app.core.config import settings

from backend.app.db.database import Base, engine

# Import database models so SQLAlchemy registers them
from backend.app.db.models import ResumeRecord
from backend.app.db.job_models import JobRecord


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    print("\n========== REGISTERED ROUTES ==========")

    for route in app.routes:
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