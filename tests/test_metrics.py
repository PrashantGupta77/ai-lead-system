from src.evaluation.metrics import calculate_metrics


def test_metrics_calculation():

    y_true = ["HOT", "WARM", "COLD"]

    y_pred = ["HOT", "WARM", "COLD"]

    metrics = calculate_metrics(
        y_true,
        y_pred
    )

    assert metrics["accuracy"] == 1.0

    assert metrics["precision"] == 1.0

    assert metrics["recall"] == 1.0