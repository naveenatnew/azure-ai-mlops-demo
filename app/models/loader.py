from pathlib import Path

import joblib

from app.core.config import settings

_model = None


def load_model():
    global _model

    if _model is None:
        model_path = Path(settings.MODEL_PATH)

        if not model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )

        _model = joblib.load(model_path)

    return _model