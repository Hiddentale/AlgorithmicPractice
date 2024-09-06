first_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
second_array = [11, 67, 42, 4, 90, 42]


def find_if_common_element():
    for number in first_array:
        for second_number in second_array:
            if number == second_number:
                return True
    return False