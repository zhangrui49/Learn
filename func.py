# -*- coding: utf-8 -*-
from functools import reduce
import functools
import time
from datetime import datetime
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def squr(x):
    return x * x

r = map(squr, a)
print(list(r))

def sum(x, y):
    return x + y

sum = reduce(sum, a)
print(sum)

def toInt(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

result = reduce(toInt, map(char2num, "12345"))
print('type of result %d is %s' % (result, type(result)))
result2 = int('12345')
print('type of result2 %d is %s' % (result2, type(result2)))


def format(string):
    if isinstance(string, str):
        return string.capitalize()


def format2(string):
    if isinstance(string, str):
        a = string.lower()
        b = a.replace(a[0], a[0].upper(), 1)
    return b

formats = map(format, ["xxx", "zhangrui", "xu", "aaAA", "AAads"])
print(format('abc'))
print(list(formats))

def is_odd(x):
    return x % 2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

f=lambda x:x*x
print(f(11111))

def now():
    #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(datetime.now())

f=now
f()

print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print("call %s(): " % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now_time():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

now_time()

def int2(x,base=16):
    return int(x,base)
print(int2('100'))
print(hex(100))

int3=functools.partial(int,base=16)

print(int3('100'))

max2=functools.partial(max,10)
print(max2(2,5,5,7))