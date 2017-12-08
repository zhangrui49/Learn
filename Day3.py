# -*- coding: utf-8 -*-
import copy

print chr(65)
print ord('A')
print "A89S".isdigit()
print "A89S".isalnum()
print "%x" % 108
print "%X" % 108
print "%#X" % 108

sql = '''CREATE TABLE users (login varchar(8), uid INTEGER , prid INTEGER) '''
a = (11, "22", 33L)
b = ("ddd", 0x78, 9 + 9j)
c = (["aa", "bb"], 0x78, 9 + 9j)
print id(a)
print id(b)
print id(c)
print c
c[0][1] = [1]
print id(c)
print c

person = ['name', ['savings', 100.00]]
hansband = person[:]
hansband[0] = "zhang"
hansband[1][1] = 150
wife = copy.deepcopy(person)
wife[0] = "ping"
wife[1][1] = 50
print hansband
print wife
