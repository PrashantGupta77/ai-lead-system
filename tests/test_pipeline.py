from src.pipeline import classify_lead


def test_hot_classification():

    label, confidence = classify_lead(
        "Need AI chatbot implementation ASAP"
    )

    assert label == "HOT"

    assert confidence >= 0.80


def test_warm_classification():

    label, confidence = classify_lead(
        "Can you share information about your services?"
    )

    assert label == "WARM"


def test_cold_classification():

    label, confidence = classify_lead(
        "Just browsing your website"
    )

    assert label == "COLD"


def test_confidence_range():

    label, confidence = classify_lead(
        "Need AI automation urgently"
    )

    assert 0.0 <= confidence <= 1.0