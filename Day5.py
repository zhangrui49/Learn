# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:05:35 2017

@author: zhangrui
"""
import os

a = "insert"

if a == "insert":
    print "insert"
elif a == "update":
    print "update"
elif a == "delete":
    print "delete"
elif a == "modify":
    print "modify"
else:
    print "unknown oprate"

if a in ('insert', 'delete', 'update', "modify"):
    print  '%s' % a
else:
    print "unknown oprate"
def bigger(ax,ay):
    if(ax < ay):
        return ay
    else :
        return ax
x, y = 10, 20
smaller = x if x < y else y  # 三元运算符
print smaller
larger = bigger(x,y)
print larger
print range(2, 19, 2)  # start,end ,step



def func1():
    pass  # no operation

if not os._exists("mkdir"):
    os.mkdir("mkdir")
    os.chdir("mkdir")
    print os.getcwd()

try:
    1 / 0
except Exception, e:
    print  e

assert 2==3
