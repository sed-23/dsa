class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head):
        self.head = head

    def append(self, val):
        node = Node(val)
        self.get_tail().next = node

        
    def get_tail(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def add_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def add_at_end(self, val):
        node = Node(val)
        temp_node = self.head

        while temp_node.next:
            temp_node = temp_node.next
        else:
            temp_node.next = node


    def insert_after(self, ref_val, val):
        node = Node(val)
        temp_node = self.head
        ref_node = None

        while temp_node and temp_node.data != ref_val:
            temp_node = temp_node.next
        else:
            ref_node = temp_node

        if ref_node:
            node.next = temp_node.next
            temp_node.next = node
        else:
            self.print_list("The node you are looking for doesn't exist please select a node in the following existing nodes")

    def insert_before(self, ref_val, val):
        node = Node(val)
        invalid_node = True
        previous_node = self.head
        if not previous_node.next:
            if previous_node.data == ref_val:
                node.next = previous_node
                self.head = node
        
        temp_node = previous_node.next

        while temp_node:
            if temp_node.data == ref_val:
                node.next = temp_node
                previous_node.next = node
            previous_node = temp_node
            if previous_node.next:
                temp_node = previous_node.next
            else:
                break

        
        if invalid_node:
            self.print_list("The node you are looking for doesn't exist please select a node in the following existing nodes")
             

        temp_node = previous_node

        def prepend(node0, node1, node2):
            if node0:
                node2.next = node0.next
                node0.next = node2

    def print_list(self, custom_message=None):
        list_val = f'{self.head.data}'
        next_node = self.head.next
        while next_node:
            list_val += f' --> {next_node.data}'
            next_node = next_node.next
        if custom_message:
            print(f'{custom_message} -- {list_val}')
        else:
            print(f'Linked List is - {list_val}')

# Creating nodes

node1 = Node('a')
# node2 = Node('b')
# node3 = Node('c')
# node4 = Node('d')
# node5 = Node('e')
# node6 = Node('f')

# Linking Nodes
linked_list = SinglyLinkedList(node1)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6


# Printing linked_list
# linked_list.print_list()


linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
linked_list.append('f')
linked_list.append('g')

linked_list.print_list()


# Inserting after a certain node
# linked_list.insert_after('a', 7)
# linked_list.print_list()


# Inserting before a certain node
# linked_list.insert_before('d', 2)
# linked_list.print_list()


# Add at head
# linked_list.add_at_head('A')
# linked_list.print_list()

# Add at end
linked_list.add_at_end('A')
linked_list.print_list()