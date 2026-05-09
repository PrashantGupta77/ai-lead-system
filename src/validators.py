def is_low_quality(message: str) -> bool:

    if not message:
        return True

    words = message.split()

    # too short
    if len(words) < 3:
        return True

    # random garbage detection
    unique_chars = len(set(message.lower()))

    if unique_chars < 3:
        return True

    return False