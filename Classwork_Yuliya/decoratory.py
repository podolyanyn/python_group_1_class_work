import time
from functools import wraps
def decor_repeat(k):
  def decor(func):
    @wraps(func)
    def inner(*arg):
      '''decorator - add before and after'''
      print('before '*k)
      func(*arg)
      print('after '*k)
    return inner
  return decor

def decor_time(func):
    @wraps(func)
    def inner1(*arg):
        '''decorator - time'''
        start = time.time()
        #print(start)
        rez = func(*arg)
        time.sleep(0.1)
        end = time.time()
        #print(end)
        print(end - start)
        return rez
    return inner1

def test():
    print('Hello, I am test')


@decor_time
@decor_repeat(3)
def test1(n):
    '''func'''
    print('Hello, I am test1',n)

test1(5)
print((test1.__doc__, test1.__name__))




#dec = decor(test)
#dec()

#dec1 = decor_time(test1)
#dec1(3)
