class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        """
        Creates a representation of the Node in the '<Node data: data>' format
        """

        return f'<Node data: {self.data}>'


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if the LinkedList doesn't contain any item
        """

        return self.head is None

    def size(self):
        """
        Finds the size of the LinkedList
        """

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node

        return count

    def prepend(self, data):
        """
        Adds a new Node at the head of the LinkedList
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):
        """
        Inserts a new Node at index position
        """

        if index == 0:
            self.prepend(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the Node or None if key doesn't exist
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current

    def search(self, key):
        """
        Searches the first Node containing data that matches the key
        Returns the node or 'None' if not found
        """

        current = self.head

        while current:
            if current.data == key:
                return current

            else:
                current = current.next_node

        return None

    def find_by_index(self, index):
        """
        Finding a node at the index position in a linked list
        Returns the node if index is valid, None if index is invalid
        """

        if index == 0:
            return self.head

        elif index > self.size() - 1:
            return None

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
        Creates a representation of the LinkedList in '[Head: data] -> [data] -> ... -> [Tail: data]' format
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.data}]')

            elif current.next_node is None:
                nodes.append(f'[Tail: {current.data}]')

            else:
                nodes.append(f'[{current.data}]')

            current = current.next_node

        return ' -> '.join(nodes)
