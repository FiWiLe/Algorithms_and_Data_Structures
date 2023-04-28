def index_of_item(collection, target):
    for i in range(len(collection)):
        if target == collection[i]:
            return i

    return -1


def linear_search(collection: list, targets: list) -> list[int]:
    result_list = []
    for target in targets:
        index = index_of_item(collection, target)
        result_list.append(index)

    return result_list
