from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    APP_NAME: str = "Azure AI/MLOps Wine Quality API"
    API_VERSION: str = "v1"
    MODEL_PATH: str = str(BASE_DIR / "ml" / "model.pkl")
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()