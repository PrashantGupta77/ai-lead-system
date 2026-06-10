from src.evaluation.evaluator import evaluate


def test_evaluator_runs():

    result = evaluate()

    assert "accuracy" in result

    assert "precision" in result