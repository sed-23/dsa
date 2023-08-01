class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head):
        self.head = head

    def print_list(self):
        list_val = f'{self.head.data}'
        next_node = self.head.next
        while next_node:
            list_val += f'-->{next_node.data}'
            next_node = next_node.next
        
        print(f'Linked List is - {list_val}')

# Creating nodes

node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')
node6 = Node('f')

# Linking Nodes
linked_list = SinglyLinkedList(node1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


# Printing linked_list
linked_list.print_list()