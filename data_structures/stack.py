class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.stack[self.size - 1] is not None

    def push(self, data):
        if self.is_full():
            return

        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            return

        elem = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return elem

    def peek(self):
        if self.is_empty():
            return

        return self.stack[self.top]

    def __repr__(self):
        return ' - '.join([str(elem) if elem else 'None' for elem in self.stack])
