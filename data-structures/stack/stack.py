# There are 3 different ways of implementing stack data structure in python

# Features of stack push, pop, isEmpty, peek, size

# 1. Using built in Lists
# 2. Using collections.deque
# 3. Custom Implementation ( Using Linked List )


# 1. Using built in Lists
class Stack1:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty(): 
            return self.stack.pop()
        else: 
            return 'Stack is empty so nothing to deque'
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return False if self.size() else True
    
    def size(self):
        return len(self.stack)
    
# Creating a stack
# stack = Stack1()
# # is stack empty 
# print(f'Is stack empty - {stack.is_empty()}')
# print(f'Stack is - {stack.stack}')
# # Dequeuing an empty stack
# print(f'{stack.pop()}')
# # Enqueuing
# stack.push('a')
# stack.push('b')
# stack.push('c')
# stack.push('d')
# stack.push('e')
# # checking the size of stack
# print(f'Size of the stack is - {stack.size()}')
# print(f'Stack is - {stack.stack}')
# # Peek into stack 
# print(f'Peek at stack - {stack.peek()}')
# print(f'Stack is - {stack.stack}')
# # Dequeuing 
# print(f'Dequeuing stack is - {stack.pop()}')
# print(f'Stack is - {stack.stack}')
# print(f'Size of the stack is - {stack.size()}')
# print(f'Stack is - {stack.stack}')


# 2. Using collections.deque
from collections import deque
class Stack2:
    def __init__(self):
        self.stack = deque()
        self.length = 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty(): 
            return self.stack.pop()
        else: 
            return 'Stack is empty so nothing to deque'
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return False if self.size() else True
    
    def size(self):
        return len(self.stack)
    
# # Creating a stack
# stack2 = Stack2()
# # is stack empty 
# print(f'Is stack empty - {stack2.is_empty()}')
# print(f'Stack is - {stack2.stack}')
# # Dequeuing an empty stack
# print(f'{stack2.pop()}')
# # Enqueuing
# stack2.push('a')
# stack2.push('b')
# stack2.push('c')
# stack2.push('d')
# stack2.push('e')
# # checking the size of stack
# print(f'Size of the stack is - {stack2.size()}')
# print(f'Stack is - {stack2.stack}')
# # Peek into stack 
# print(f'Peek at stack - {stack2.peek()}')
# print(f'Stack is - {stack2.stack}')
# # Dequeuing 
# print(f'Dequeuing stack is - {stack2.pop()}')
# print(f'Stack is - {stack2.stack}')
# print(f'Size of the stack is - {stack2.size()}')
# print(f'Stack is - {stack2.stack}')


# 3. Custom Implementation ( Using linked list )
class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        

class Stack3:
    def __init__(self, node=None) -> None:
        self.head = node
        self.length = 1 if node else 0

    def push(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if self.length:
            node = self.head
        else:
            return 'Stack is Empty nothing to pop.'
        if node.next: self.head = node.next
        self.length -= 1
        return node.data
    
    def peek(self):
        return self.head.data if self.length else 'Notihing to peek from an empty stack'
    
    def is_empty(self):
        return True if not self.length else False
    
    def size(self):
        return self.length
    
    def print_stack(self):
        if self.length: 
            stack = f'{self.head.data}' 
            if self.head.next:
                node = self.head.next
            else:
                return stack  
        else:
            return 'Stack is empty...'
        
        while node:
            stack += f'--> {node.data}' 
            if node.next:
                node = node.next
            else: 
                break

        return stack

    
# Creating a stack
stack3 = Stack3()
# is stack empty 
print(f'Is stack empty - {stack3.is_empty()}')
print(f'Stack is - {stack3.print_stack()}')
# Dequeuing an empty stack
print(f'{stack3.pop()}')
# Enqueuing
stack3.push(Node('a'))
stack3.push(Node('b'))
stack3.push(Node('c'))
stack3.push(Node('d'))
stack3.push(Node('e'))
# checking the size of stack
print(f'Size of the stack is - {stack3.size()}')
print(f'Stack is - {stack3.print_stack()}')
# Peek into stack 
print(f'Peek at stack - {stack3.peek()}')
print(f'Stack is - {stack3.print_stack()}')
# Dequeuing 
print(f'Dequeuing stack is - {stack3.pop()}')
print(f'Stack is - {stack3.print_stack()}')
print(f'Size of the stack is - {stack3.size()}')
print(f'Stack is - {stack3.print_stack()}')
    
        
    