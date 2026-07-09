from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def evaluate(model, x_test, y_test):

    predictions = model.predict(x_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions,
        output_dict=True
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    return {
        "accuracy": accuracy,
        "classification_report": report,
        "confusion_matrix": matrix.tolist(),
    }