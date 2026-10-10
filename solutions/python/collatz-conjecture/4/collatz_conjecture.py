def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_counter = 0

    while number != 1:
        steps_counter += 1
        
        if number % 2:
            number = number * 3 + 1
        else:
            number /= 2

    return steps_counter