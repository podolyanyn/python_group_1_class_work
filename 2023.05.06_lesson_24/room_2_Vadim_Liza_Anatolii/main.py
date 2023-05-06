# my_list = []

# def enqueue(my_list, a):
#     return my_list.append(a)
#
# def dequeue(my_list):
#     return my_list.pop()
#
# def isEmpty(my_list):
#     return not bool(my_list)
#
# def size(my_list):
#     return len(my_list)
#
# enqueue(my_list, 2)
# enqueue(my_list, 3)
# enqueue(my_list, 4)
# dequeue(my_list)
# print(size(my_list))
# print(isEmpty(my_list))
# print(my_list)

my_list = []

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue_right(self, a):
        return self.queue.append(a)

    def enqueue_left(self, a):
        return self.queue.insert(0,a)

    def dequeue_right(self):
        return self.queue.pop(-1)

    def dequeue_left(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue_right(2)
queue.enqueue_right(6)
queue.enqueue_right(8)
queue.enqueue_right(9)
queue.enqueue_left(33)
# queue.dequeue_right()
# queue.dequeue_left()
print(queue.queue)
