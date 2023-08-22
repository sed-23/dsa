# There are 3 different ways of implementing queue data structure in python

# Features of stack enqueue, dequeue, isEmpty, peek, size

# 1. Using built in Lists
# 2. Using collections.deque
# 3. Custom Implementation using doubly linked list


# 1. Using built in Lists

que = []

class Queue:
    def __init__(self):
        self.que = []

    def enqueue(self, item):
        self.que.append(item)

    def deque(self):
        if not self.is_empty(): 
            return self.que.pop(0)
        else: 
            return 'Queue is empty so nothing to deque'

    def is_empty(self):
        return False if len(self.que) else True
    
    def peek(self):
        return self.que[0]
    
    def size(self):
        return len(self.que)
    
# # Creating a Queue
# queue = Queue()
# # is Queue empty 
# print(f'Is queue empty - {queue.is_empty()}')
# # Dequeuing an empty queue
# print(f'{queue.deque()}')
# # Enqueuing
# queue.enqueue('a')
# queue.enqueue('b')
# queue.enqueue('c')
# queue.enqueue('d')
# queue.enqueue('e')
# # checking the size of Queue
# print(f'Size of the queue is - {queue.size()}')
# # Peek into Queue 
# print(f'Peek at queue - {queue.peek()}')
# # Dequeuing 
# print(f'Dequeuing queue is - {queue.deque()}')
# print(f'Size of the queue is - {queue.size()}')


# 2. Using collections.deque

from collections import deque

class Queue2:
    def __init__(self):
        self.que = deque()

    def enqueue(self, item):
        self.que.append(item)

    def deque(self):
        if not self.is_empty(): 
            return self.que.popleft()
        else: 
            return 'Queue is empty so nothing to deque'

    def is_empty(self):
        return False if len(self.que) else True
    
    def peek(self):
        return self.que[0]
    
    def size(self):
        return len(self.que)

# # Creating a Queue
# queue2 = Queue2()
# # is Queue empty 
# print(f'Is queue empty - {queue2.is_empty()}')
# # Dequeuing an empty queue
# print(f'{queue2.deque()}')
# # Enqueuing
# queue2.enqueue('a')
# queue2.enqueue('b')
# queue2.enqueue('c')
# queue2.enqueue('d')
# queue2.enqueue('e')
# # checking the size of Queue
# print(f'Size of the queue is - {queue2.size()}')
# # Peek into Queue 
# print(f'Peek at queue - {queue2.peek()}')
# # Dequeuing 
# print(f'Dequeuing queue is - {queue2.deque()}')
# print(f'Size of the queue is - {queue2.size()}')

# 3. Custom Implementation using doubly linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        self.length = 1


    def append(self, val):
        node = Node(val)
        if not self.length:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1


    def add_at_head(self, val):
        node = Node(val)
        if not self.length:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
            self.length += 1

    def pop(self):
        if not self.length:
            return 'List is empty nothing to pop'
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.length = 0
            return data
        else:
            tail = self.tail
            self.tail = tail.previous
            self.tail.next = None
            self.length -= 1
            return tail.data

    def print_list(self, custom_message=None):
        list_val = f'{self.head.data}'
        next_node = self.head.next
        while next_node:
            
            list_val += f' <--> {next_node.data}'
            next_node = next_node.next
        if custom_message:
            return f'{custom_message} -- {list_val}'
        else:
            return f'Linked List is - {list_val} with length - {self.length}'

class Queue3:
    def __init__(self, val):
        self.que = DoublyLinkedList(val)

    def enqueue(self, item):
        self.que.add_at_head(item)

    def deque(self):
        if not self.is_empty(): 
            return self.que.pop()
        else: 
            return 'Queue is empty so nothing to deque'

    def is_empty(self):
        return False if self.que.head else True
    
    def peek(self):
        return self.que.tail.data
    
    def size(self):
        return self.que.length

    def print_queue(self):
        return self.que.print_list()
    
# Creating a Queue
queue3 = Queue3(0)
# is Queue empty 
print(f'Is queue empty - {queue3.is_empty()}')
# Dequeuing an empty queue
print(f'{queue3.deque()}')
# Enqueuing
queue3.enqueue('a')
queue3.enqueue('b')
queue3.enqueue('c')
queue3.enqueue('d')
queue3.enqueue('e')
# checking the size of Queue
print(f'Size of the queue is - {queue3.size()} and queue - {queue3.print_queue()}')
# Peek into Queue 
print(f'Peek at queue - {queue3.peek()} and queue - {queue3.print_queue()}')
# Dequeuing 
print(f'Dequeuing queue is - {queue3.deque()} and queue - {queue3.print_queue()}')
print(f'Size of the queue is - {queue3.size()} and queue - {queue3.print_queue()}')
