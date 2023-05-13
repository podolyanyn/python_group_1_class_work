from random import shuffle
from time import time
#
# def linear_search(some_list, key):
#     i = 0
#     while i < len(some_list):
#         if some_list[i] == key:
#             return i
#         i += 1
#
#
#
# # list_1 = [randint(1,100) for i in range(100)]
# list_1 = [i for i in range(100)]
# shuffle(list_1)
# list_2 = [j for j in range(10000)]
# shuffle(list_2)
#
# # print(list_1)
# t1 = 0
# for i in range(3):
#     start = time()
#     linear_search(list_1, 50)
#     end = time()
#     t1 += end - start
#
# print(t1/3)
#
# t2 = 0
# for i in range(3):
#     start = time()
#     linear_search(list_2, 5000)
#     end = time()
#     t2 += end - start
#
# print(t2/3)
# #----------------------------------------
# list_1 = [i for i in range(100)]
# list_2 = [j for j in range(10000)]
#
# def bin_search(some_list, key):
#     l = 0
#     r = len(some_list) - 1
#     while l < r:
#         m = int((l + r)/2)
#         if some_list[m] < key:
#             l = m + 1
#         else:
#             r = m
#     if some_list[r] == key:
#         return r
#     else:
#         return 'not in list'
#
#
# t1 = 0
# for i in range(3):
#     start = time()
#     bin_search(list_1, 50)
#     end = time()
#     t1 += end - start
#
# print(t1/3)
#
# t2 = 0
# for i in range(3):
#     start = time()
#     bin_search(list_2, 5000)
#     end = time()
#     t2 += end - start
#
# print(t2/3)
# #----------------------------------------
class SomeClass:
    def __init__(self, a):
        self.a = a



sm1 = SomeClass(1)
sm2 = SomeClass(2)
sm3 = SomeClass(3)






