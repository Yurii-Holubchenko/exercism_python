def correct_triangle(func):
    def inner_func(sides: list):
        # Using > instead of >= to also cover the check for 0
        # sum(sides) > 2 * max(sides) if the shortcut for sum(sides) - max(sides) > max(sides)
        return sum(sides) > 2 * max(sides) and func(sides)

    return inner_func


@correct_triangle
def equilateral(sides: list) -> bool:
    return len(set(sides)) == 1
    

@correct_triangle
def isosceles(sides: list) -> bool:
    return len(set(sides)) < 3

@correct_triangle
def scalene(sides: list) -> bool:
    return len(set(sides)) == 3

