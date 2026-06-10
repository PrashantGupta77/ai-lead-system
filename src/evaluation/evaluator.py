import json
from pathlib import Path

from src.pipeline import classify_lead
from src.evaluation.metrics import calculate_metrics
from src.monitoring.performance import confidence_stats


# -----------------------------------
# paths
# -----------------------------------

DATASET_PATH = (
    Path(__file__).parent /
    "dataset.json"
)

REPORT_PATH = (
    Path("reports") /
    "metrics.json"
)


# -----------------------------------
# evaluation runner
# -----------------------------------

def evaluate():

    with open(
        DATASET_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        dataset = json.load(f)

    y_true = []
    y_pred = []

    predictions = []

    for sample in dataset:

        # classify lead
        predicted_label, confidence = classify_lead(
            sample["message"]
        )

        # ground truth
        y_true.append(
            sample["expected_label"]
        )

        # prediction
        y_pred.append(
            predicted_label
        )

        # store for confidence analysis
        predictions.append(
            {
                "message": sample["message"],
                "expected_label": sample["expected_label"],
                "predicted_label": predicted_label,
                "confidence": confidence
            }
        )

    # classification metrics
    metrics = calculate_metrics(
        y_true,
        y_pred
    )

    # confidence metrics
    metrics["confidence"] = confidence_stats(
        predictions
    )

    return metrics


# -----------------------------------
# script entrypoint
# -----------------------------------

if __name__ == "__main__":

    results = evaluate()

    # create reports directory if missing
    REPORT_PATH.parent.mkdir(
        exist_ok=True
    )

    # save metrics
    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=4
        )

    print(
        json.dumps(
            results,
            indent=4
        )
    )

    print(
        f"\nMetrics saved to: {REPORT_PATH}"
    )