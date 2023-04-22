def range_between(a: int, b: int):
    x, y = min(a, b), max(a, b)

    return range(x + 1, y)
