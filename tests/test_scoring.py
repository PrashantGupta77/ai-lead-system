from src.scoring import (
    rule_score,
    rule_based_label
)


def test_hot_score():

    score = rule_score(
        "Need AI automation urgently and want pricing"
    )

    assert score >= 6


def test_warm_score():

    score = rule_score(
        "Can you share information about your services?"
    )

    assert 2 <= score < 6


def test_cold_score():

    score = rule_score(
        "Just browsing your website"
    )

    assert score < 2


def test_hot_label():

    assert rule_based_label(8) == "HOT"


def test_warm_label():

    assert rule_based_label(3) == "WARM"


def test_cold_label():

    assert rule_based_label(1) == "COLD"