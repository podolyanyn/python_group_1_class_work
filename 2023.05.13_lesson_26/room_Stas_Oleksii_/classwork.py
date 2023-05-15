
"""This script generates two arrays, one with 100 random integers and another with 10,000 random integers. It then
performs linear search and binary search algorithms to find the numbers 50 and 5000 respectively. The search
operations are repeated three times, and the time taken for each search is recorded.

Finally, the script calculates the average search time for each algorithm and prints the results. The linear search
algorithm checks each element in the array one by one until the target is found or the end of the array is reached.
The binary search algorithm repeatedly divides the search space in half until the target is found or it determines
that the target is not present in the array.

The average search times provide an indication of the efficiency of the linear and binary search algorithms for the
given array sizes."""

import random
import time

# Generate two arrays of random integers
array_first = [random.randint(1, 100) for i in range(100)]
array_second = [random.randint(1, 10000) for j in range(10000)]


# Linear search algorithm
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


# Binary search algorithm
def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid == target]:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# Perform linear search for the number 50 in the first array
linear_search_times_100 = []
for _ in range(3):
    start_time = time.time()
    linear_search_100 = linear_search(array_first, 50)
    end_time = time.time()
    search_time = end_time - start_time
    linear_search_times_100.append(search_time)

# # Perform binary search for the number 5000 in the second array
binary_search_times_10000 = []
for _ in range(3):
    start_time = time.time()
    binary_search_10000 = binary_search(array_second, 5000)
    end_time = time.time()
    search_time = end_time - start_time
    binary_search_times_10000.append(search_time)

# Calculating the average search time
average_linear_search_time_100 = sum(linear_search_times_100) / len(linear_search_times_100)
average_binary_search_time_10000 = sum(binary_search_times_10000) / len(binary_search_times_10000)
# Print the average search times
print("Average binary search time (100 items):", average_linear_search_time_100)
print("Average binary search time (10000 items):", average_binary_search_time_10000)

# Складність алгоритмів лінійного та бінарного пошуку можна оцінити за допомогою нотації Big O, яка вказує на
# зростання часової складності алгоритму при збільшенні розміру вхідних даних.
#
# 1. Лінійний пошук: - У найгіршому випадку, коли шуканий елемент знаходиться в кінці масиву або його немає взагалі,
# лінійний пошук вимагає перевірки кожного елементу масиву. Тому його часова складність становить O(n),
# де n - кількість елементів у масиві.
#
# 2. Бінарний пошук: - Бінарний пошук базується на діленні пошукового простору навпіл на кожній ітерації. У кожній
# ітерації розмір пошукового простору зменшується вдвічі. Тому бінарний пошук має часову складність O(log n),
# де n - кількість елементів у відсортованому масиві.
#
# Отже, на основі нотації Big O можна зробити такі висновки: - Лінійний пошук має лінійну часову складність O(n),
# де n - кількість елементів у масиві. Його часова складність зростає пропорційно з розміром масиву. - Бінарний пошук
# має логарифмічну часову складність O(log n), де n - кількість елементів у відсортованому масиві. Його часова
# складність зростає набагато повільніше з розміром масиву, оскільки пошуковий простір зменшується вдвічі на кожній
# ітерації.
#
# В порівнянні з лінійним пошуком, бінарний пошук є значно більш ефективним, особливо при великому розмірі вхідних
# даних. Лінійний пошук має лінійну часову складність O(n), тобто час пошуку зростає пропорційно з кількістю
# елементів у масиві. З іншого боку, бінарний пошук має логарифмічну часову складність O(log n), що означає,
# що час пошуку зростає повільніше з кількістю елементів у відсортованому масиві. Таким чином, бінарний пошук є
# набагато швидшим у випадку великого масиву. Наприклад, при використанні масиву з 10 000 елементів, бінарний пошук
# забезпечує значно швидшу швидкість пошуку порівняно з лінійним пошуком. Тому, якщо масив відсортований,
# використання бінарного пошуку є бажаною стратегією для досягнення більшої ефективності.