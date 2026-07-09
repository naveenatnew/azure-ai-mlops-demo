from pathlib import Path

import pandas as pd

from ml.constants import FEATURE_COLUMNS
from ml.constants import TARGET_COLUMN


def load_dataset(path: Path):

    df = pd.read_csv(path, sep=";")

    df[TARGET_COLUMN] = (
        df[TARGET_COLUMN] >= 7
    ).astype(int)

    X = df[FEATURE_COLUMNS]

    y = df[TARGET_COLUMN]

    return X, y