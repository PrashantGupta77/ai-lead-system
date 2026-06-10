def confidence_stats(predictions):

    scores = [
        p["confidence"]
        for p in predictions
    ]

    if not scores:

        return {
            "avg_confidence": 0,
            "max_confidence": 0,
            "min_confidence": 0
        }

    return {

        "avg_confidence":
        round(
            sum(scores) / len(scores),
            4
        ),

        "max_confidence":
        round(
            max(scores),
            4
        ),

        "min_confidence":
        round(
            min(scores),
            4
        )
    }