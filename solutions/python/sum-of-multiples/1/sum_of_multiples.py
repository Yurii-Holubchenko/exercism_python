def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0

    result = set()
    
    for element in multiples:
        if element == 0:
            break

        with_multiplier = element
        while with_multiplier < limit:
            result.add(with_multiplier)
            with_multiplier += element

    return sum(result)
