def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns new list
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right halfs
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
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
