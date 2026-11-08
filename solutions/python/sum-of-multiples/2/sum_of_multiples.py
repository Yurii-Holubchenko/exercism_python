def sum_of_multiples(limit, multiples):
    result = set()
    
    for element in multiples:
        if element > 0:
            result.update({number for number in range(element, limit, element)})

    return sum(result)
