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

    # business-friendly confidence calibration

    if label == "HOT":

        if score >= 6:
            return 0.95

        elif score >= 4:
            return 0.88

        return 0.8

    elif label == "WARM":

        if score >= 4:
            return 0.78

        elif score >= 2:
            return 0.7

        return 0.6

    else:

        if score == 0:
            return 0.45

        return 0.55


# -----------------------------------
# lead classification
# -----------------------------------

def classify_lead(message: str):

    msg = message.lower().strip()

    # -----------------------------------
    # low quality detection
    # -----------------------------------

    if is_low_quality(message):

        return "COLD", 0.4

    # -----------------------------------
    # curiosity / informational intent
    # -----------------------------------

    curiosity_patterns = [

        "what do you do",
        "tell me more",
        "just exploring",
        "checking out",
        "saw your page",
        "who are you",
        "how does this work"
    ]

    if any(pattern in msg for pattern in curiosity_patterns):

        return "COLD", 0.5

    # -----------------------------------
    # high-intent detection
    # -----------------------------------

    high_intent_patterns = [

        "pricing",
        "demo",
        "book a call",
        "schedule a call",
        "get started",
        "need immediately",
        "urgent",
        "asap"
    ]

    if any(pattern in msg for pattern in high_intent_patterns):

        return "HOT", 0.92

    # -----------------------------------
    # rule engine
    # -----------------------------------

    score = rule_score(message)

    rule_label = rule_based_label(score)

    # confident enough → skip LLM

    if score >= 2:

        confidence = compute_confidence(
            score,
            rule_label
        )

        return rule_label, confidence

    # -----------------------------------
    # fallback to LLM
    # -----------------------------------

    try:

        prompt = CLASSIFICATION_PROMPT.format(
            message=message
        )

        result = call_llm(prompt).upper()

        match = re.search(
            r"\b(HOT|WARM|COLD)\b",
            result
        )

        label = match.group(1) if match else "WARM"

        confidence = 0.55

        return label, confidence

    except:

        return "WARM", 0.5


# -----------------------------------
# response generation
# -----------------------------------

def generate_response(message: str, label: str):

    try:

        prompt = RESPONSE_PROMPT.format(
            message=message,
            label=label
        )

        result = call_llm(prompt)

        # retry once

        if not result:

            result = call_llm(prompt)

        # -----------------------------------
        # fallback handling
        # -----------------------------------

        if not result or len(result.split()) < 6:

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