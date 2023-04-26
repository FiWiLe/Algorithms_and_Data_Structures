def selection_sort(values: list[int]) -> list[int]:
    """
    Searching for minimal number in values list
    Then appending it to a new list and deleting it from the old list
    Returns the new sorted list
    """

    sorted_list = []

    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))

    return sorted_list


def index_of_min(values: list[int]) -> int:
    """
    Searching the minimal number in values list
    Returns the index of the minimal number
    """

    min_index = 0

    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i

    return min_index
