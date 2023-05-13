import random
import time
gen = [random.randint(1,100) for i in range(1, 100)]
gen2 = [random.randint(1,10000) for i in range(1, 10000)]

def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

@timer_func
def lin(l, q):
    start = time.time()
    for i in l:
        if i == q:
            return i
@timer_func
def bin(l,q):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > q:
            high = mid - 1
        elif l[mid] < q:
            low = mid + 1
        else:
            return l[mid]
    return -1

print(lin(gen, 63))
print(bin(gen, 20))
print(lin(gen2, 63))
print(bin(gen2, 20))






