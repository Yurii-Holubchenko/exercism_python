def equilateral(sides: list) -> bool:
    if wrong_triangle(sides):
        return False
    
    return len(set(sides)) == 1
    

def isosceles(sides: list) -> bool:
    if wrong_triangle(sides):
        return False

    return len(set(sides)) < 3

def scalene(sides: list) -> bool:
    if wrong_triangle(sides):
        return False

    return len(set(sides)) == 3


def wrong_triangle(sides: list) -> bool:
    return sum(sides) == 0 or not (sum(sorted(sides)[0:2]) >= max(sides))

    