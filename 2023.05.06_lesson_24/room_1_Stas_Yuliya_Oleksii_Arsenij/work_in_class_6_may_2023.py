# Данный класс Stack представляет структуру данных стека (англ. stack). Стек - это упорядоченный список элементов,
# где доступен только последний добавленный элемент (элемент на вершине стека), а все остальные элементы недоступны,
# пока не будет удален последний добавленный элемент.
class Stack:
    def __init__(self):
        self._items = []
        # В данном классе используется список self._items для хранения элементов стека.
        #
        # Метод __init__() используется для инициализации пустого стека при создании объекта класса.

    def is_empty(self):
        return bool(self._items)

    # Метод is_empty() проверяет, является ли стек пустым, и возвращает True, если стек пуст, и False, если стек не
    # пуст.

    def push(self, item):
        self._items.append(item)
        # Метод push(item) добавляет элемент item на вершину стека.

    def pop(self):
        return self._items.pop()

    # Метод push(item) добавляет элемент item на вершину стека.

    def peek(self):
        return self._items[len(self._items) - 1]

    # Метод peek() возвращает последний добавленный элемент (элемент на вершине стека), не удаляя его из стека.

    def size(self):
        return len(self._items)

    # Метод size() возвращает количество элементов в стеке.

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    # Метод __repr__() возвращает строковое представление объекта класса в виде нумерованного списка элементов стека.

    def __str__(self):
        return self.__repr__()
    # Метод __str__() вызывает метод __repr__(), чтобы получить строковое представление объекта класса.


class Queue:
    # Класс Queue представляет структуру данных очередь (англ. queue). Очередь - это упорядоченный список элементов,
    # где доступен только первый добавленный элемент (элемент в начале очереди), а все остальные элементы недоступны,
    # пока не будут удалены все элементы, добавленные ранее.
    def __init__(self):
        self._items = []
        # В данном классе используется список self._items для хранения элементов очереди.
        #
        # Метод __init__() используется для инициализации пустой очереди при создании объекта класса.

    def is_empty(self):
        return bool(self._items)

    # Метод is_empty() проверяет, является ли очередь пустой, и возвращает True, если очередь пуста, и False,
    # если очередь не пуста.

    def enqueue(self, item):
        self._items.insert(0, item)
        # Метод enqueue(item) добавляет элемент item в конец очереди.

    def dequeue(self):
        return self._items.pop()

    # Метод dequeue() удаляет и возвращает первый добавленный элемент (элемент в начале очереди).

    def size(self):
        return len(self._items)

    # Метод size() возвращает количество элементов в очереди.

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    # Метод __repr__() возвращает строковое представление объекта класса в виде нумерованного списка элементов очереди.

    def __str__(self):
        return self.__repr__()
    # Метод __str__() вызывает метод __repr__(), чтобы получить строковое представление объекта класса.


class Deque:
    # Данный класс Deque реализует структуру данных двусторонняя очередь (англ. deque), которая представляет собой
    # упорядоченный список элементов, к которому можно добавлять и удалять элементы с обоих концов.
    def __init__(self):
        self._items = []
        # Метод __init__() используется для инициализации пустой двусторонней очереди при создании объекта класса.

    def is_empty(self):
        return self._items == []
    # Метод is_empty() проверяет, является ли очередь пустой, и возвращает True, если очередь пуста, и False,
    # если очередь не пуста.

    def add_front(self, item):
        self._items.append(item)
        # Метод add_front(item) добавляет элемент item в начало очереди.

    def add_rear(self, item):
        self._items.insert(0, item)
        # Метод add_rear(item) добавляет элемент item в конец очереди.

    def remove_front(self):
        return self._items.pop()
    # Метод remove_front() удаляет и возвращает первый элемент (элемент в начале очереди).

    def remove_rear(self):
        return self._items.pop(0)
    # Метод remove_rear() удаляет и возвращает последний элемент (элемент в конце очереди).

    def size(self):
        return len(self._items)
    # Метод size() возвращает количество элементов в очереди.

    def __repr__(self):
        return f"<Deque: `rear` {self._items} `front`>"
    # Метод __repr__() возвращает строковое представление объекта класса в виде списка элементов двусторонней очереди
    # с пометками "rear" (конец очереди) и "front" (начало очереди).

    def __str__(self):
        return self.__repr__()
    # Метод __str__() вызывает метод __repr__(), чтобы получить строковое представление объекта класса.


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)
    print(s.pop())
    print(s)

    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
    print(d)
