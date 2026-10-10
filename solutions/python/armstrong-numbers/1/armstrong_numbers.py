def is_armstrong_number(number):
    initial_number = number
    result = 0
    number_length = len(str(number))

    while number % 10 > 0:
        result += (number % 10) ** number_length
        number //= 10

    return initial_number == result