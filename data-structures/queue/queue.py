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
    
# Creating a Queue
queue = Queue()
# is Queue empty 
print(f'Is queue empty - {queue.is_empty()}')
# Dequeuing an empty queue
print(f'{queue.deque()}')
# Enqueuing
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.enqueue('d')
queue.enqueue('e')
# checking the size of Queue
print(f'Size of the queue is - {queue.size()}')
# Peek into Queue 
print(f'Peek at queue - {queue.peek()}')
# Dequeuing 
print(f'Dequeuing queue is - {queue.deque()}')
print(f'Size of the queue is - {queue.size()}')


# Using collections.deque

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

# Creating a Queue
queue2 = Queue2()
# is Queue empty 
print(f'Is queue empty - {queue2.is_empty()}')
# Dequeuing an empty queue
print(f'{queue2.deque()}')
# Enqueuing
queue2.enqueue('a')
queue2.enqueue('b')
queue2.enqueue('c')
queue2.enqueue('d')
queue2.enqueue('e')
# checking the size of Queue
print(f'Size of the queue is - {queue2.size()}')
# Peek into Queue 
print(f'Peek at queue - {queue2.peek()}')
# Dequeuing 
print(f'Dequeuing queue is - {queue2.deque()}')
print(f'Size of the queue is - {queue2.size()}')


class Node:
    def __init__(self, val):
        self.previous = None
        self.next = None
        self.data = val
    
class DoublyLinkedList:
    def __init__(self, val):
        self.previous = None
        self.next = None
        self.data = val

class Queue3:
    def __init__(self):
        self.que = None

    def enqueue(self, item):
        self.que.append(item)

    def deque(self):
        if not self.is_empty(): 
            return self.que.popleft()
        else: 
            return 'Queue is empty so nothing to deque'

    def is_empty(self):
        return False if self.que else True
    
    def peek(self):
        return self.que[0]
    
    def size(self):
        return len(self.que)
    
# Creating a Queue
queue3 = Queue3()
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
print(f'Size of the queue is - {queue3.size()}')
# Peek into Queue 
print(f'Peek at queue - {queue3.peek()}')
# Dequeuing 
print(f'Dequeuing queue is - {queue3.deque()}')
print(f'Size of the queue is - {queue3.size()}')
