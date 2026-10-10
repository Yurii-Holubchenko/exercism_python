def equilateral(sides: list) -> bool:
    side_a, side_b, side_c = sides

    if zero_sides(side_a, side_b, side_c) or inequality_triangle(side_a, side_b, side_c):
        return False

    return side_a == side_b == side_c
    

def isosceles(sides: list) -> bool:
    side_a, side_b, side_c = sides

    if zero_sides(side_a, side_b, side_c) or inequality_triangle(side_a, side_b, side_c):
        return False

    return side_a == side_b or side_a == side_c or side_b == side_c

def scalene(sides: list) -> bool:
    side_a, side_b, side_c = sides

    if zero_sides(side_a, side_b, side_c) or inequality_triangle(side_a, side_b, side_c):
        return False
    
    return (side_a != side_b) and (side_a != side_c) and (side_b != side_c)


def zero_sides(side_a: int, side_b: int, side_c: int) -> bool:
    return side_a == 0 or side_b == 0 or side_c == 0


def inequality_triangle(side_a: int, side_b: int, side_c: int) -> bool:
    return not(
        side_a + side_b >= side_c and 
        side_b + side_c >= side_a and 
        side_a + side_c >= side_b
    )