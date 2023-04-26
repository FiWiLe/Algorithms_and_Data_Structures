def merge_sort(values: list[int]) -> list[int]:
    """
    Sorts a list in ascending order
    Returns new list
    """

    if len(values) <= 1:
        return values

    left_half, right_half = split(values)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(values: list[int]) -> tuple[list[int], list[int]]:
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right halfs
    """

    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    return left, right


def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merges two lists (arrays) and sorting them
    Returns a new merged list
    """

    res_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            res_list.append(left[i])
            i += 1
        else:
            res_list.append(right[j])
            j += 1

    while i < len(left):
        res_list.append(left[i])
        i += 1

    while j < len(right):
        res_list.append(right[j])
        j += 1

    return res_list
