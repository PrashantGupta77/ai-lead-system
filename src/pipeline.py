import re

from src.llm import call_llm

from src.prompts import (
    CLASSIFICATION_PROMPT,
    RESPONSE_PROMPT
)

from src.scoring import (
    rule_score,
    rule_based_label
)

from src.validators import is_low_quality


# -----------------------------------
# fallback responses
# -----------------------------------

FALLBACK_RESPONSE_BY_LABEL = {

    "HOT":
    (
        "Thanks for reaching out. "
        "This sounds urgent — would you be open to a quick discussion today?"
    ),

    "WARM":
    (
        "That sounds like a valuable use case for AI automation. "
        "Are you mainly looking to improve lead qualification, customer engagement, or operational efficiency?"
    ),

    "COLD":
    (
        "We help businesses automate lead engagement and customer interactions using AI systems. "
        "What kind of solution are you exploring currently?"
    )
}


# -----------------------------------
# confidence calculation
# -----------------------------------

def compute_confidence(score: int, label: str) -> float:

    if label == "HOT":

        if score >= 6:
            return 0.95

        elif score >= 4:
            return 0.88

        return 0.80

    elif label == "WARM":

        if score >= 4:
            return 0.78

        elif score >= 2:
            return 0.70

        return 0.60

    else:

        if score <= 0:
            return 0.50

        return 0.55


# -----------------------------------
# lead classification
# -----------------------------------

def classify_lead(message: str):

    msg = message.lower().strip()

    # -----------------------------------
    # low-quality detection
    # -----------------------------------

    if is_low_quality(message):
        return "COLD", 0.40

    # -----------------------------------
    # high-intent signals first
    # -----------------------------------

    high_intent_patterns = [
        "pricing",
        "demo",
        "book a call",
        "schedule a call",
        "get started",
        "need immediately",
        "urgent",
        "asap",
        "proposal",
        "quotation",
        "quote",
        "cost",
        "connect",
        "today",
        "tomorrow",
        "business problem",
        "resolve my business problem",
        "solve my business problem"
    ]

    if any(pattern in msg for pattern in high_intent_patterns):
        score = rule_score(message)

        if score >= 6:
            return "HOT", 0.92

        return "WARM", 0.75

    # -----------------------------------
    # rule engine
    # -----------------------------------

    score = rule_score(message)

    rule_label = rule_based_label(score)

    confidence = compute_confidence(
        score,
        rule_label
    )

    # -----------------------------------
    # curiosity signals
    # do not override strong business intent
    # -----------------------------------

    curiosity_patterns = [
        "what do you do",
        "tell me more",
        "just exploring",
        "checking out",
        "who are you",
        "how does this work",
        "just browsing",
        "browsing",
        "linkedin page",
        "saw your linkedin",
        "visited your website",
        "your website"
    ]

    has_curiosity = any(
        pattern in msg
        for pattern in curiosity_patterns
    )

    if has_curiosity and score < 2:
        return "COLD", 0.55

    # -----------------------------------
    # strong rule signals
    # -----------------------------------

    if score >= 2:
        return rule_label, confidence

    # -----------------------------------
    # definitely cold
    # -----------------------------------

    if score < 0:
        return "COLD", 0.50

    # -----------------------------------
    # ambiguous case: use LLM
    # -----------------------------------

    try:
        prompt = CLASSIFICATION_PROMPT.format(
            message=message
        )

        result = call_llm(
            prompt
        ).upper()

        match = re.search(
            r"\b(HOT|WARM|COLD)\b",
            result
        )

        label = (
            match.group(1)
            if match
            else "WARM"
        )

        return label, 0.60

    except:
        return "WARM", 0.50

# -----------------------------------
# response generation
# -----------------------------------

def generate_response(
    message: str,
    label: str
):

    try:

        prompt = RESPONSE_PROMPT.format(
            message=message,
            label=label
        )

        result = call_llm(
            prompt
        )

        # retry once

        if not result:

            result = call_llm(
                prompt
            )

        # -----------------------------------
        # fallback handling
        # -----------------------------------

        if (

            not result

            or

            len(
                result.split()
            ) < 6

        ):

            return FALLBACK_RESPONSE_BY_LABEL.get(
                label,
                FALLBACK_RESPONSE_BY_LABEL["WARM"]
            )

        return result.strip()

    except:

        return FALLBACK_RESPONSE_BY_LABEL.get(
            label,
            FALLBACK_RESPONSE_BY_LABEL["WARM"]
        )