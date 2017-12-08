# -*- coding: utf-8 -*-
print "cacca"
pty = "python"
print pty[2]
print pty[2:5]
aDic = {"name": "zhang"}
print aDic.keys()
aDic["age"] = 56
print aDic.keys()

for key in aDic:
    print key, aDic[key]

for item in ["email", "address", "name", "age"]:
    print item,
print
for i in range(len(pty)):
    print pty[i], '(%d)' % i
for i, ch in enumerate(pty):
    print ch, "(%d)" % i
square = [x ** 2 for x in range(8) if not x % 2]
print square

file = open('setting.txt')
for line in file:
    print line
file.close()

