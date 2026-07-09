from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings
from app.core.logging import get_logger
from app.models.loader import load_model

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Loading ML model...")
    load_model()
    logger.info("Application started.")
    yield
    logger.info("Application stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(
    router,
    prefix=f"/api/{settings.API_VERSION}",
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": "1.0.0",
        "status": "Running"
    }