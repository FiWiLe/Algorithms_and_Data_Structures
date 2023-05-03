class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, data):
        if self.is_full():
            print('The queue is full')
            return
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data

    def dequeue(self):
        if self.is_empty():
            print('The queue is empty')
            return
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp

    def peek(self):
        return self.queue[self.head]

    def peek_tail(self):
        return self.queue[self.tail]

    def __repr__(self):
        if self.head == -1:
            return '[ ]'
        elif self.tail >= self.head:
            repr_list = [str(self.queue[i]) for i in range(self.head, self.tail + 1)]
            return f'[ {" ".join(repr_list)} ]'
        else:
            repr_list = [str(self.queue[i]) for i in range(self.head, self.size)] + \
                [str(self.queue[i]) for i in range(self.tail + 1)]
            return f'[ {" ".join(repr_list)} ]'
