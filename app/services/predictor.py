from ml.constants import FEATURE_COLUMNS

from app.models.loader import load_model


FEATURE_MAPPING = {
    "fixed acidity": "fixed_acidity",
    "volatile acidity": "volatile_acidity",
    "citric acid": "citric_acid",
    "residual sugar": "residual_sugar",
    "chlorides": "chlorides",
    "free sulfur dioxide": "free_sulfur_dioxide",
    "total sulfur dioxide": "total_sulfur_dioxide",
    "density": "density",
    "pH": "pH",
    "sulphates": "sulphates",
    "alcohol": "alcohol",
}


def predict(request):

    model = load_model()

    values = [
        getattr(
            request,
            FEATURE_MAPPING[column]
        )
        for column in FEATURE_COLUMNS
    ]

    prediction = int(
        model.predict([values])[0]
    )

    return {
        "prediction": prediction,
        "label": (
            "Good Wine"
            if prediction
            else "Average Wine"
        ),
    }