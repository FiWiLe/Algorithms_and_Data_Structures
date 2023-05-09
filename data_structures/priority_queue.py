class Node:
    def __init__(self, item=None, priority=None):
        self.item = item
        self.priority = priority
        self.next = None
        self.previous = None


class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        if self.is_full():
            return
        elif self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return
        highest = self.head
        current = self.head.next
        while current:
            if highest.priority < current.priority:
                highest = current
            current = current.next

        item = highest.item
        highest.previous.next = highest.next
        highest.next = highest.previous
        if self.is_empty():
            self.tail = None
        return item

    def peek(self):
        highest = self.head
        current = self.head.next
        while current:
            if highest.priority < current.priority:
                highest = current
            current = current.next

        return highest.item

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.item} (Priority: {current.priority})]')

            elif current is self.tail:
                nodes.append(f'[Tail: {current.item} (Priority: {current.priority})]')

            else:
                nodes.append(f'[{current.item} (Priority: {current.priority})]')

            current = current.next

        return ' - '.join(nodes)
