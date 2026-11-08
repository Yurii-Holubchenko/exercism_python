def find(search_list, value):
    left_pointer = 0
    right_pointer = len(search_list) - 1

    while left_pointer <= right_pointer:
        index = left_pointer + (right_pointer - left_pointer) // 2
        elem = search_list[index]

        if elem > value:
            right_pointer = index - 1
        elif elem < value:
            left_pointer = index + 1
        else:
            return index
            

    raise ValueError("value not in array")
    