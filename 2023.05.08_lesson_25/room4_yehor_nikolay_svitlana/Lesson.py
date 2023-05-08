class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, elem):
        current = self.head
        previos = None
        while current is not None:
            if current.data == elem:
                previos.next = current.next
                print(elem, 'removed')
                return
            previos = current
            current = current.next
        print(elem, 'not removed')

    def find(self, elem):
        current = self.head
        while current is not None:
            if current.data == elem:
                return True
            current = current.next
        return False

    def findall(self, elem):
        index = 0
        index_list = []
        current = self.head
        while current is not None:
            if current.data == elem:
                index_list.append(index)
            index += 1
            current = current.next
        return index_list

    # def insert(self, data, index):
    #     new_node = Node(data)
    #     i = 0
    #     last_node = self.head
    #     while i < index:
    #         last_node = last_node.next
    #         i += 1
    #     last_node.next = new_node
# не доробив :(


linked_list = LinkedList()
linked_list.append(1)
linked_list.append("2")
linked_list.append(1)
linked_list.append("Stas")
linked_list.print_list()
# linked_list.insert(44, 1)
linked_list.print_list()
# print(linked_list.findall(1))