from pydantic import BaseModel, Field


class WineRequest(BaseModel):

    fixed_acidity: float = Field(..., gt=0)
    volatile_acidity: float = Field(..., gt=0)
    citric_acid: float
    residual_sugar: float = Field(..., gt=0)
    chlorides: float = Field(..., gt=0)
    free_sulfur_dioxide: float = Field(..., ge=0)
    total_sulfur_dioxide: float = Field(..., ge=0)
    density: float = Field(..., gt=0)
    pH: float = Field(..., gt=0)
    sulphates: float = Field(..., gt=0)
    alcohol: float = Field(..., gt=0)


class PredictionResponse(BaseModel):

    prediction: int
    label: str