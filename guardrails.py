def validate_input(user_input):
    blocked_words = ["hack", "fraud", "attack"]

    if any(word in user_input.lower() for word in blocked_words):
        return "⚠️ Request blocked due to safety policy."

    return None