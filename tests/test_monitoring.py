from src.monitoring.performance import (
    confidence_stats
)


def test_confidence_stats():

    predictions = [

        {"confidence": 0.9},

        {"confidence": 0.8},

        {"confidence": 0.7}
    ]

    stats = confidence_stats(
        predictions
    )

    assert stats["avg_confidence"] == 0.8

    assert stats["max_confidence"] == 0.9

    assert stats["min_confidence"] == 0.7