class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = head
        self.length = 1


    def append(self, val):
        node = Node(val)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1


    def add_at_head(self, val):
        node = Node(val)
        self.head.previous = node
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
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
            print(f'{custom_message} -- {list_val}')
        else:
            print(f'Linked List is - {list_val} with length - {self.length}')

# Creating nodes

node1 = Node('a')
# node2 = Node('b')
# node3 = Node('c')
# node4 = Node('d')
# node5 = Node('e')
# node6 = Node('f')

# Linking Nodes
doubly_linked_list = DoublyLinkedList(node1)


# Printing doubly_linked_list
doubly_linked_list.print_list()


doubly_linked_list.add_at_head('b')
doubly_linked_list.add_at_head('c')
doubly_linked_list.add_at_head('d')
doubly_linked_list.add_at_head('e')
doubly_linked_list.add_at_head('f')
doubly_linked_list.add_at_head('g')

doubly_linked_list.print_list()

doubly_linked_list.add_at_head('0')

doubly_linked_list.print_list()

doubly_linked_list.pop()

doubly_linked_list.print_list()




doubly_linked_list.append('b')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.append('f')
doubly_linked_list.append('g')

doubly_linked_list.print_list()

doubly_linked_list.pop()

doubly_linked_list.print_list()

# Inserting after a certain node
# doubly_linked_list.insert_after('a', 7)
# doubly_linked_list.print_list()
# doubly_linked_list.insert_after('z', 4)


# Inserting before a certain node
# doubly_linked_list.insert_before('d', 2)
# doubly_linked_list.print_list()
# doubly_linked_list.insert_before('x', 3)


# Add at head
# doubly_linked_list.add_at_head('A')
# doubly_linked_list.print_list()

# Add at end
# doubly_linked_list.add_at_end('A')
# doubly_linked_list.print_list()