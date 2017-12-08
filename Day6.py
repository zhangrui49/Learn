# -*- coding: utf-8 -*-
import math
def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("type not support")
    if x>=0:
        return x
    else :
        return -x
print(myAbs(-58))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  
#其实返回的是一个值 tuple
print(move(115,120,10,math.pi/6))

# ax2 + bx + c = 0
def quadratic(a, b, c):
    if b*b-4*a*c < 0:
        raise ValueError("次方程无解")

    x1=(-b+math.sqrt(b*b-4*a*c))/2*a
    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
    return x1,x2
print(quadratic(2,3,1))

def power(x,n=2):#默认求平方
    s=1
    while n>0:
        n=n-1
        s=s*x

#平方和
def sumP(numbers):
    s=0
    for x in numbers:
        s=s+x*x
    return s

def sump2(*numbers): #可变参数
    s = 0
    for x in numbers:
        s = s+x*x
    return s
print(sumP([1,2,3])) 
print (sump2(*[1,2,3])) # 将列表或者元组转成可变参数
print (sump2(1,2,3))

list0 = [x*x for x in range(1,11)]
list1 = [m+n for m in "ABC" for n in "123"]
S = list("ABCDEFG")
[s.lower() for s in S]
print(S)
print(list0)
print(list1)
