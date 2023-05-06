list1 = []

def enqueue(lis, item):
    return lis.append(item)

def dequeue(lis):
    return lis.pop(0)

def size(lis):
    return len(lis)

def isempty(lis):
    return len(lis) == 0

enqueue(list1, 5)
enqueue(list1, 1)
enqueue(list1, 9)
print(list1)

dequeue(list1)
print(list1)

print(size(list1))
print(isempty(list1))

class Queue:

    def __init__(self, value=None):
        if value:
            self.queue = [value]
        else:
            self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isempty(self):
        return len(self.queue) == 0

    def __str__(self):
        return f'{self.queue}'

que = Queue()

que.enqueue(8)
que.enqueue(5)
que.enqueue(3)
print(que)

que.dequeue()
print(que)

list1 = []

def add_right(lis, item):
    return lis.append(item)

def add_left(lis, item):
    return lis.insert(0, item)

def remove_right(lis):
    return lis.pop()

def remove_left(lis):
    return lis.pop(0)

def size(lis):
    return len(lis)

def isempty(lis):
    return len(lis) == 0

add_right(list1, 1)
add_right(list1, 2)
add_left(list1, 3)
add_left(list1, 4)
print(list1)

remove_right(list1)
remove_left(list1)
print(list1)

print(size(list1))
print(isempty(list1))

class Dequeue:

    def __init__(self, value=None):
        if value:
            self.dequeue = [value]
        else:
            self.dequeue = []

    def add_right(self, item):
        return self.dequeue.append(item)

    def add_left(self, item):
        return self.dequeue.insert(0, item)

    def remove_right(self):
        return self.dequeue.pop()

    def remove_left(self):
        return self.dequeue.pop(0)

    def size(self):
        return len(self.dequeue)

    def isempty(self):
        return len(self.dequeue) == 0

    def __str__(self):
        return f'{self.dequeue}'

dequeue = Dequeue()

dequeue.add_right(1)
dequeue.add_right(2)
dequeue.add_left(3)
dequeue.add_left(4)
print(dequeue)

dequeue.remove_left()
dequeue.remove_right()
print(dequeue)