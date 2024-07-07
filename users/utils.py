from db import DB


def generate_id() -> int:
    ids = list(DB.keys())

    if len(ids) == 0:
        return 1
    return ids[-1] + 1
