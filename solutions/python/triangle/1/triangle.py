def equilateral(sides: list) -> bool:
    a, b, c = sides

    if zero_sides(a, b, c) or inequality_triangle(a, b, c):
        return False

    return a == b == c
    

def isosceles(sides: list) -> bool:
    a, b, c = sides

    if zero_sides(a, b, c) or inequality_triangle(a, b, c):
        return False

    return a == b or a == c or b == c

def scalene(sides: list) -> bool:
    a, b, c = sides

    if zero_sides(a, b, c) or inequality_triangle(a, b, c):
        return False
    
    return (a != b) and (a != c) and (b != c)


def zero_sides(a: int, b: int, c: int) -> bool:
    return a == 0 or b == 0 or c == 0


def inequality_triangle(a: int, b: int, c: int) -> bool:
    return not(a + b >= c and b + c >=a and a + c >= b)