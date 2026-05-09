def rule_score(message: str) -> int:

    msg = message.lower()

    score = 0

    # urgency
    if "urgent" in msg:
        score += 3

    if "asap" in msg:
        score += 3

    if "immediately" in msg:
        score += 2

    # intent
    if "need" in msg:
        score += 1

    if "looking for" in msg:
        score += 1

    if "automation" in msg:
        score += 2

    if "ai solution" in msg:
        score += 2

    # growth/business signals
    if "scaling" in msg:
        score += 2

    if "growing fast" in msg:
        score += 2

    return score


def rule_based_label(score: int) -> str:

    if score >= 5:
        return "HOT"

    elif score >= 2:
        return "WARM"

    return "COLD"