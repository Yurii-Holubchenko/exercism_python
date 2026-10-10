def is_armstrong_number(number):
    initial_number = number
    number_length = len(str(number))
    result = 0    

    while number % 10 > 0:
        result += (number % 10) ** number_length
        number //= 10

    return initial_number == result