class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class Queue:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def enqueue(self, value):
        new_node = Node(value)
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
        item = self.head.item
        self.head = self.head.next
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return item

    def peek(self):
        return self.head.item

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.item}]')

            elif current is self.tail:
                nodes.append(f'[Tail: {current.item}]')

            else:
                nodes.append(f'[{current.item}]')

            current = current.next

        return ' - '.join(nodes)
