class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self):
        if self.head is not None:
            self.head = self.head.next

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert(data)
        else:
            new_node = self.Node(data)
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise Exception("Index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.delete()
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise Exception("Index out of range")
                current = current.next
            if current is None or current.next is None:
                raise Exception("Index out of range")
            current.next = current.next.next

    def search(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise Exception("Index out of range")
            current = current.next
        if current is None:
            raise Exception("Index out of range")
        return current.data

    def __str__(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return str(result)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        return self.search(index)

    def __bool__(self):
        return self.head is not None


class Stack:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.stack = []

    def push(self, data):
        if self.max_size is not None and len(self.stack) >= self.max_size:
            raise Exception("Stack is full")
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return len(self.stack) > 0


class Queue:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.queue = []

    def enqueue(self, data):
        if self.max_size is not None and len(self.queue) >= self.max_size:
            raise Exception("Queue is full")
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.queue)

    def __bool__(self):
        return len(self.queue) > 0


class Array:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.array)

    def __contains__(self, item):
        return item in self.array

    def __bool__(self):
        return bool(self.array)

    def append(self, item):
        self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def sort(self):
        sorted(self.array)

    def reverse(self):
        self.array.reverse()

