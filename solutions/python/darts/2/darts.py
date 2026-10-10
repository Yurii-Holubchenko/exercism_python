import math

def score(x, y):
    point_radius = math.hypot(x, y)
    
    if point_radius <= 1:
        return 10

    if point_radius <= 5:
        return 5

    if point_radius <= 10:
        return 1

    return 0
