class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.counter = 1
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            self.counter += 1
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def index(self, elem):
        list_index = []
        current = self.head
        index = 0
        while current is not None:
            if current.data == elem:
                list_index.append(index)
            current = current.next
            index += 1
        return list_index

    def insert(self, index, data):
        node = Node(data)
        if index <= 0:
            node.next = self.head
            self.head = node
        else:
            if index > self.counter:
                index = self.counter
            current_id = 0
            current_node = self.head
            previous_node = None
            while current_node is not None and current_id < index:
                previous_node = current_node
                current_node = current_node.next
                current_id += 1
            node.next = current_node
            previous_node.next = node
            self.counter += 1


linked_list = LinkedList()
linked_list.append(1)
linked_list.append("2")
linked_list.append("Stas")
linked_list.append(1)
linked_list.append(1)
linked_list.append(1)
linked_list.print_list()
print(linked_list.index(1))
linked_list.insert(2,44)
linked_list.print_list()