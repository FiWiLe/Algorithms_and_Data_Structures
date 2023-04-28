def quicksort(values: list[int]) -> list[int]:
    """
    1) Selects the first element of the original values array as pivot. [4,5,8,1,7,3,2] -> 4
    2) Then splits the values array into two sub-arrays:
     less_than_pivot containing elements less than or equal to pivot,
     and greater_than_pivot containing elements greater than pivot. [1,3,2], [5,8,7]
    3) Then recursively executes starting from 1) until it reaches subarrays of 1 element.
     [1,3,2] -> 1 -> [], [3,2] -> 3 -> [2], []; [5,8,7] -> 5 -> [], [7,8] -> 7 -> [], [8].
    4) Then recursively merges the sub-arrays together in sorted form (less_than_pivot, pivot, greater_than_pivot)
     until it reaches the final sorted array. [1,2,3], 4, [5,7,8] -> [1,2,3,4,5,7,8]
    Returns a new sorted array
    """

    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
