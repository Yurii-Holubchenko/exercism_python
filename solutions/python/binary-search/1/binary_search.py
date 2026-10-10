def find(search_list, value):
    left_pointer = 0
    right_pointer = len(search_list) - 1
    
    while left_pointer <= right_pointer:
        middle_index = (right_pointer + left_pointer) // 2
        middle_element = search_list[middle_index]

        if middle_element > value:
            right_pointer = middle_index - 1
        elif middle_element < value:
            left_pointer = middle_index + 1
        else:
            return middle_index

    raise ValueError("value not in array")
