import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.core.logging import get_logger
from app.schemas.wine import (
    PredictionResponse,
    WineRequest,
)
from app.services.predictor import predict

router = APIRouter()

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parents[2]

METADATA = BASE_DIR / "ml" / "metadata.json"


@router.get("/health")
def health():
    return {"status": "Healthy"}


@router.get("/ready")
def ready():
    return {"status": "Ready"}


@router.get("/metadata")
def metadata():

    with open(METADATA) as f:
        return json.load(f)


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict_wine(request: WineRequest):

    try:
        return predict(request)

    except Exception as ex:

        logger.exception(ex)

        raise HTTPException(
            status_code=500,
            detail="Prediction failed",
        )