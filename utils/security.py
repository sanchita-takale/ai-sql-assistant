def is_safe_query(query):

    query = query.lower()

    blocked_words = [
        "drop",
        "delete",
        "truncate",
        "update",
        "insert",
        "alter"
    ]

    for word in blocked_words:

        if word in query:
            return False

    return True