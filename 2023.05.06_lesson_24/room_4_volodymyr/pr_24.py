# # ---------------Queue---------------
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
#
# print(my_list.pop(0))
# print(my_list.pop(0))
# print(my_list.pop(0))
#
# class Queue:
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items == []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         if len(self.items) < 1:
#             return None
#         else:
#             return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#

# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue('dog')
#     q.enqueue(True)
#     print(q.size())
#     print(q.dequeue())
#     print(q.dequeue())
#     print(q.dequeue())
#
# # ---------------Deque---------------
#
# my_list1 = []
# # add front
# my_list1.append(1)
# my_list1.append(2)
# my_list1.append(3)
# # add rear
# my_list1.insert(0, 4)
# my_list1.insert(0, 5)
#
# print(my_list1)
#
# # remove_front
# print('remove_front', my_list1.pop())
# # remove_rear
# print('remove_rear', my_list1.pop(0))
#
#
# class Deque:
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items == []
#
#     def add_front(self, item):
#         self.items.append(item)
#
#     def add_rear(self, item):
#         self.items.insert(0, item)
#
#     def remove_front(self):
#         self.items.pop()
#
#     def remove_rear(self):
#         self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#
#
# if __name__ == '__main__':
#     d = Deque()
#     print(d.is_empty())
#     d.add_rear(4)
#     d.add_rear('dog')
#     d.add_front('cat')
#     d.add_front(True)
#     print(d.size())
#     print(d.is_empty())
#     d.add_rear(8.4)
#     print(d.remove_rear())
#     print(d.remove_front())