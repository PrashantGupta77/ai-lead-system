from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


def calculate_metrics(
    y_true,
    y_pred
):
    return {
        "accuracy": float(
            accuracy_score(
                y_true,
                y_pred
            )
        ),

        "precision": float(
            precision_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0
            )
        ),

        "recall": float(
            recall_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0
            )
        ),

        "f1_score": float(
            f1_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0
            )
        ),

        "classification_report":
        classification_report(
            y_true,
            y_pred,
            output_dict=True,
            zero_division=0
        ),

        "confusion_matrix":
        confusion_matrix(
            y_true,
            y_pred
        ).tolist()
    }