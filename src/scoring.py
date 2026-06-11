# -----------------------------------
# lead scoring engine
# -----------------------------------

def rule_score(message: str) -> int:

    msg = message.lower().strip()

    score = 0

    # -----------------------------------
    # urgency signals
    # -----------------------------------

    urgency_keywords = [
        "urgent",
        "asap",
        "immediately",
        "right away",
        "this week",
        "today",
        "tomorrow",
        "quickly"
    ]

    for keyword in urgency_keywords:
        if keyword in msg:
            score += 3

    # -----------------------------------
    # purchase / meeting intent
    # -----------------------------------

    purchase_keywords = [
        "pricing",
        "price",
        "cost",
        "quote",
        "quotation",
        "proposal",
        "budget",
        "demo",
        "book a call",
        "schedule a call",
        "consultation",
        "meeting",
        "connect",
        "call",
        "discussion"
    ]

    for keyword in purchase_keywords:
        if keyword in msg:
            score += 3

    # -----------------------------------
    # solution intent
    # -----------------------------------

    solution_keywords = [
        "need",
        "looking for",
        "require",
        "want",
        "interested",
        "interested in",
        "searching for",
        "exploring solutions",
        "resolve",
        "solve",
        "help with"
    ]

    for keyword in solution_keywords:
        if keyword in msg:
            score += 1

    # -----------------------------------
    # business problem intent
    # -----------------------------------

    problem_keywords = [
        "business problem",
        "problem",
        "challenge",
        "pain point",
        "issue",
        "bottleneck",
        "manual process",
        "struggling",
        "need help"
    ]

    for keyword in problem_keywords:
        if keyword in msg:
            score += 2

    # -----------------------------------
    # medium business intent
    # -----------------------------------

    medium_intent_keywords = [
        "more details",
        "details",
        "information",
        "services",
        "evaluating",
        "vendors",
        "learn more",
        "use case",
        "solution",
        "platform"
    ]

    for keyword in medium_intent_keywords:
        if keyword in msg:
            score += 2

    # -----------------------------------
    # AI / automation intent
    # -----------------------------------

    ai_keywords = [
        "automation",
        "ai system",
        "ai solution",
        "artificial intelligence",
        "chatbot",
        "lead qualification",
        "customer support",
        "workflow automation",
        "agentic ai",
        "ai agent",
        "autonomous ai"
    ]

    for keyword in ai_keywords:
        if keyword in msg:
            score += 2

    # -----------------------------------
    # implementation signals
    # -----------------------------------

    implementation_keywords = [
        "deployment",
        "implementation",
        "integration",
        "rollout",
        "production",
        "setup",
        "implement"
    ]

    for keyword in implementation_keywords:
        if keyword in msg:
            score += 2

    # -----------------------------------
    # business growth signals
    # -----------------------------------

    business_keywords = [
        "scaling",
        "growing fast",
        "team",
        "company",
        "business",
        "startup",
        "clients",
        "customers"
    ]

    for keyword in business_keywords:
        if keyword in msg:
            score += 1

    # -----------------------------------
    # cold curiosity signals
    # only reduce score, do not force COLD
    # -----------------------------------

    cold_keywords = [
        "just browsing",
        "browsing",
        "just exploring",
        "what do you do",
        "who are you",
        "tell me more",
        "checking out",
        "saw your page"
    ]

    for keyword in cold_keywords:
        if keyword in msg:
            score -= 2

    return score


# -----------------------------------
# label assignment
# -----------------------------------

def rule_based_label(score: int) -> str:

    if score >= 6:
        return "HOT"

    elif score >= 2:
        return "WARM"

    return "COLD"