# def fib_iterative(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
#
# print(fib_iterative(3))
#
# def fib_recursive(n):
#     if n == 0 or n == 1:
#         return n
#     return fib_recursive(n-1) + fib_recursive(n-2)
#
# print(fib_recursive(5))
#
# import sys
# sys.setrecursionlimit(3000)
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(1000))


# def f1(n):
#     print('f1')
#     return n+1
#
# def f2(n):
#     print('f2')
#     return f1(n) + 2
#
# def f3(n):
#     print('f3')
#     return f2(n) + 3
# # зворотний порядок, мають відпрацювати всі функції поки не почнуть повертатись значення
# # print(f3(0))
#
# def f(n):
#     if n < 5:
#         print(n)
#         f(n+1)
#         print(n)
#
# # f(0)
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# # print(fact(10))
#
# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(5))

''' Задача 1.
 Визначте функцію print_to, яка приймає одне натуральне число n і роздруковує на
екрані послідовність цілих чисел від 1 до n до включно. Кожне число необхідно виводити в окремому рядку.'''

def print_to(n):
    if n > 0:
        print_to(n-1)
        print(n)

# print_to(5)


'''Задача 2.
Дано натуральне число N і послідовність з N елементів. Потрібно вивести цю послідовність у зворотному порядку.
Вхідні дані:
Програма приймає на вхід натуральне число N (N ≤ 1000). У другому рядку через пропуск йдуть N цілих чисел, 
які за модулем не перевищують 1000 - елементи послідовності.
Вихідні дані:
Ваше завдання вивести задану послідовність у зворотному порядку.'''

a = '1 5 1 2 3'
# n = 4

def f(n, m: str):
    test = len(m)
    if test == 1 or n == 1:
        print(m)
        return
    space = m.rindex(' ')
    print(m[space+1:])
    return f(n-1, m[:space])

# f(5, a)


''' Задача 4.
Напишіть функцію, яка приймає на вхід список із цілих чисел і повертає суму елементів переданого списку.'''

a = [1, 2, 3, 4]

def func(my_list):
    if len(my_list) == 1:
        return my_list[0]
    return my_list[0] + func(my_list[1:])

# print(func(a))


'''Задача 5.
Уявіть, що у нас є список цілих чисел необмеженої вкладеності. 
Тобто наш список може складатися зі списків, усередині яких також можуть бути списки. 
Ваше завдання перетворити все це на лінійний список за допомогою функції flatten
flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
flatten([[[[9]], [1, 2], [[8]]]) => [9, 1, 2, 8]'''



def flatten(my_list):
    res = []
    for i in my_list:
        if isinstance(i, list):
            # res.extend(flatten(i))
            res += flatten(i)
        else:
            res.append(i)
    return res

print(flatten([1, [2, 3, [4]], 5]))

print(flatten([[[[9]], [1, 2], [[8]]]]))


