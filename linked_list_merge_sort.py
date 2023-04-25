from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists
    - Repeatedly merge the sublists to produce sorted sublists
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.find_by_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """

    # Create a new linked list contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head
    merged.prepend(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail
    while left_head or right_head:

        # If the head of the left is None, add the node from right to merged
        if left_head is None:
            current.next_node = right_head
            # Call next on right to end loop
            right_head = right_head.next_node

        # If the head of the right is None, add the node from left to merged
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to end loop
            left_head = left_head.next_node

        else:
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is less than on right, set current to left
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to the next node
                left_head = left_head.next_node

            # If data on left is greater than on right, set current to right
            else:
                current.next_node = right_head
                # Move right head to the next node
                right_head = right_head.next_node

        # Move current to the next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged
