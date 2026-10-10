def score(x, y):
    coords_sum = abs(x) ** 2 + abs(y) ** 2
    
    if 0 <= coords_sum <= 1 ** 2:
        return 10

    if 1 ** 2 < coords_sum <= 5 ** 2:
        return 5

    if 5 ** 2 < coords_sum <= 10 ** 2:
        return 1

    return 0
