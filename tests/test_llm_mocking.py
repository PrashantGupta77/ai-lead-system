from unittest.mock import patch

from src.pipeline import classify_lead


@patch("src.pipeline.call_llm")
@patch("src.pipeline.rule_score")
@patch("src.pipeline.is_low_quality")
def test_llm_returns_hot(
    mock_low_quality,
    mock_score,
    mock_llm
):
    mock_low_quality.return_value = False
    mock_score.return_value = 0
    mock_llm.return_value = "HOT"

    label, confidence = classify_lead("anything")

    assert label == "HOT"
    assert confidence == 0.60


@patch("src.pipeline.call_llm")
@patch("src.pipeline.rule_score")
@patch("src.pipeline.is_low_quality")
def test_llm_returns_warm(
    mock_low_quality,
    mock_score,
    mock_llm
):
    mock_low_quality.return_value = False
    mock_score.return_value = 0
    mock_llm.return_value = "WARM"

    label, confidence = classify_lead("anything")

    assert label == "WARM"
    assert confidence == 0.60


@patch("src.pipeline.call_llm")
@patch("src.pipeline.rule_score")
@patch("src.pipeline.is_low_quality")
def test_llm_returns_cold(
    mock_low_quality,
    mock_score,
    mock_llm
):
    mock_low_quality.return_value = False
    mock_score.return_value = 0
    mock_llm.return_value = "COLD"

    label, confidence = classify_lead("anything")

    assert label == "COLD"
    assert confidence == 0.60


@patch("src.pipeline.call_llm")
@patch("src.pipeline.rule_score")
@patch("src.pipeline.is_low_quality")
def test_llm_failure(
    mock_low_quality,
    mock_score,
    mock_llm
):
    mock_low_quality.return_value = False
    mock_score.return_value = 0

    mock_llm.side_effect = Exception(
        "Groq unavailable"
    )

    label, confidence = classify_lead("anything")

    assert label == "WARM"
    assert confidence == 0.50