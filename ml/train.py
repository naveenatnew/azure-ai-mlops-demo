from datetime import datetime
from pathlib import Path
import json

import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ml.constants import (
    DATASET_NAME,
    FEATURE_COLUMNS,
    MODEL_VERSION,
)
from ml.evaluate import evaluate
from ml.preprocess import load_dataset

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "dataset.csv"

MODEL_PATH = BASE_DIR / "model.pkl"

METADATA_PATH = BASE_DIR / "metadata.json"


def train():

    print("Loading dataset...")

    X, y = load_dataset(DATASET_PATH)

    print(f"Dataset size : {len(X)}")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
    )

    print("Training model...")

    model.fit(
        X_train,
        y_train,
    )

    metrics = evaluate(
        model,
        X_test,
        y_test,
    )

    joblib.dump(
        model,
        MODEL_PATH,
    )

    metadata = {
        "model_version": MODEL_VERSION,
        "dataset": DATASET_NAME,
        "trained_at": datetime.utcnow().isoformat(),
        "algorithm": "RandomForestClassifier",
        "accuracy": metrics["accuracy"],
        "features": FEATURE_COLUMNS,
    }

    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            metadata,
            f,
            indent=4,
        )

    print()

    print("=" * 50)

    print("Training Complete")

    print("=" * 50)

    print(f"Accuracy : {metrics['accuracy']:.4f}")

    print(f"Model saved : {MODEL_PATH}")

    print(f"Metadata saved : {METADATA_PATH}")


if __name__ == "__main__":
    train()