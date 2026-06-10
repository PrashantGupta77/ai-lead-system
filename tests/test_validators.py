from src.validators import is_low_quality


def test_low_quality_short_text():

    assert is_low_quality("hi") is True


def test_low_quality_symbols():

    assert is_low_quality("!!!!") is True


def test_good_quality_message():

    assert is_low_quality(
        "Need AI automation for customer support"
    ) is False