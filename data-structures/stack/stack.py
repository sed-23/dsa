# There are 3 different ways of implementing stack data structure in python

# Features of stack push, pop, isEmpty, peek, size

# 1. Using built in Lists
# 2. Using collections.deque
# 3. Custom Implementation


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
stack = Stack1()
# is stack empty 
print(f'Is stack empty - {stack.is_empty()}')
print(f'Stack is - {stack.stack}')
# Dequeuing an empty stack
print(f'{stack.pop()}')
# Enqueuing
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
stack.push('e')
# checking the size of stack
print(f'Size of the stack is - {stack.size()}')
print(f'Stack is - {stack.stack}')
# Peek into stack 
print(f'Peek at stack - {stack.peek()}')
print(f'Stack is - {stack.stack}')
# Dequeuing 
print(f'Dequeuing stack is - {stack.pop()}')
print(f'Stack is - {stack.stack}')
print(f'Size of the stack is - {stack.size()}')
print(f'Stack is - {stack.stack}')
