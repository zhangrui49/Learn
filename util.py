from datetime import datetime, timedelta
from collections import namedtuple, defaultdict, OrderedDict
import struct
import hashlib
import itertools
import urllib
from urllib import request
import sys
from contextlib import closing

print(datetime.fromtimestamp(datetime.timestamp(datetime.now())))
print(datetime.utcfromtimestamp(datetime.timestamp(datetime.now())))
print(datetime.now().strftime('%a,%b %d %H:%M'))
now = datetime.now()
new_time = now - timedelta(days=60)
print(new_time)

Ponit = namedtuple('Ponit', ['x', 'y'])
p1 = Ponit(15, 20)
print(p1.y)

Circle = namedtuple('Circle', ['r', 'x', 'y'])

dd = defaultdict(lambda: 'NaN')
dd['a'] = 1
dd['b'] = 2
print(dd['x'])

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # 按插入顺序排列
print(od)

print(struct.pack('>I', 59))

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

natual = itertools.count(1)
# for i in natual:
#     print(i)
cs = itertools.cycle('A')
# for c in cs:
#     print(c)
ns = itertools.repeat('R', 50)
for n in ns:
    print(n)

nst = itertools.takewhile(lambda x: x < 10, natual)
for n in list(nst):
    print(n)

for key ,group in itertools.groupby('ABCAABBCCabc'):
    print(key,list(group))

try:
    f = open('setting.txt')
    for line in f.readlines():
        print(line)
finally:
    f.close()

with open('setting.txt') as f:
    for line in f.readlines():
        print(line)

with closing(request.urlopen('https://api.douban.com/v2/book/2129650')) as f:
        data = f.read()
        print('status:',f.status,f.reason)
        for key,value in f.getheaders():
            print('%s : %s' % (key,value))
        print('data:',data.decode('utf8'))