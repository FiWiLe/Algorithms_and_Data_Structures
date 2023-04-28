def binary_search(collection: list, target):
    # list should be sorted

    first = 0
    last = len(collection) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if collection[midpoint] == target:
            return midpoint

        elif collection[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return -1
