from manipula import Array, Stack, Queue, LinkedList

def linked_list_test():
    array = [1, 2, 'gg', {'4': [6.7, (5)]}, 4, 5]

    linked_list = LinkedList()
    for i in array:
        linked_list.insert(i)
    print(linked_list)

    linked_list.delete()
    print(linked_list)

    linked_list.insert_at_index('hello', 3)
    print(linked_list)

    linked_list.delete_at_index(3)
    print(linked_list)

    print(linked_list.search(2))
    for item in linked_list:
        print(item)

    print(linked_list[2])
    print(len(linked_list))

    if linked_list:
        print('Linked list is not empty')

def stack_test():
    array = [1, 2, 'gg', {'4': [6.7, (5)]}, 4, 5]

    stack = Stack()
    print(stack.is_empty())

    for i in array:
        stack.push(i)
    print(stack)

    stack.pop()
    print(stack)

    stack.push('hello')
    print(stack)

    print(stack.peek())

    print(stack.is_empty())

    print(len(stack))

    if stack:
        print('Stack is not empty')


def queue_test():
    array = [1, 2, 'gg', {'4': [6.7, (5)]}, 4, 5]

    queue = Queue()
    print(queue.is_empty())

    for i in array:
        queue.enqueue(i)
    print(queue)

    queue.dequeue()
    print(queue)

    queue.enqueue('hello')
    print(queue)

    print(queue.peek())

    print(queue.is_empty())

    print(len(queue))

    if queue:
        print('Queue is not empty')


def array_test():
    array = Array()
    if array:
        print('Array is not empty')

    array = Array([1, 2, 3, 4, 5])
    print(array)

    array.reverse()
    print(array)

    array.sort()
    print(array)

    array.append(6)
    print(array)

    print(array[2])

    array[2] = 7
    print(array)

if __name__ == '__main__':
    array_test()
    stack_test()
    queue_test()
    linked_list_test()
