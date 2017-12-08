# -*- coding: utf-8 -*-
map1 = {}
map2 = dict((["x", 1], ["y", 2]))
map3 = {}.fromkeys(["x", "y"], 1)
map5 = {}.fromkeys("xyz")
map4 = dict(x=1, y=2)
print map1
print map2
print map3
print map4
print map5
map3.has_key("x")
a = "x" in map3

s=set("uvwxyzabdc")
print s
t=frozenset("abcdefg")
print t
s.add(1)
s.add(a)
print s
#list1=list("11aabb")
#print list1
print set("push")==set("shup")

st = s|t # 并 或
ts=s&t # 与 交
tts=s^t # 非  

print st
print ts
print tts

print s.issubset(t)
print s.issuperset(t)
print s.union(t)
print s.intersection(t)
print s.difference(t)
print s.symmetric_difference(t)