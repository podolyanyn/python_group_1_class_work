#!/usr/bin/env python3
"""
Задача 1.
Однонаправлений список.
Пошук всіх співпадінь шуканого значення, тобто метод повертає список індексів.
"""

class Node:

    def __init__(self, value, _next = None):
        self.value = value
        self.next = _next

    
class LinkedList:

    def __init__(self, arr):
        self.head = None
        arr.reverse()
        for i in arr:
            self.push(i)


    def seek(self, value):
        result = []
        index = 0

        current = self.head
        while current:
            if current.value == value:
                result.append(index)
            index += 1
            current = current.next

        return result
    

    def set_at(self, index, value):
        node = Node(value)
        list_index = 0 
        current = self.head

        while current and list_index <= index:
            if list_index == index:
                node.next = current.next
                current.next = node
            current = current.next
            list_index += 1
        


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
    
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value) + " "
            current = current.next
        return result


link_list = LinkedList([1, 2, 3, 4, 1, 1, 1, 1, 2, 1, 1, 3, 1])
link_list.push(109)
print(link_list.seek(11))
print(link_list)
link_list.set_at(0, 69)
print(link_list)
link_list.set_at(1, 67)
print(link_list)

