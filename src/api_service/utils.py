def valid_target(target: str) -> bool:
    targets = ["field_1", "author", "description"]

    return target.lower() in targets
