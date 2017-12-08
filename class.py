# -*- coding: utf-8 -*
from enum import Enum, unique


class Student(object):
    #__slots__ = ('name', '__grade')  # 限定绑定的属性

    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade  # 私有
 
    def get_grade(self):
        print('%s grade is %s' % (self.name, self.__grade))

    def __len__(self):
        return self.name.__len__()

    def __str__(self):
        return "Student name: %s" % self.name
    __repr = __str__


tom = Student("tom", "grade 1")
tom.get_grade()
print(tom.name)
print(tom)
# print(tom.__grade)
# print(tom._Student__grade) #慎用

print(dir(tom))
print(len(tom))

print(hasattr(tom, 'name'))
setattr(tom, 'name', "Tom")
print(tom.name)
print(getattr(tom, 'age', 18))
fn = getattr(tom, 'get_grade')
fn()


def set_age(self, age):
    self.age = age


Student.set_age = set_age  # 动态添加属性和方法
tom.set_age(25)
print(tom.age)


class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height * self.__width


sc = Screen()
sc.height = 180
sc.width = 2
print(sc.height)
print(sc.resolution)


class Animal(object):
    pass


class Runnable(object):
    pass


class Cat(Animal, Runnable):  # 多重继承

    def run(self):
        print("cat running...")


cat = Cat()
cat.run()


class Fab(object):
    def __init__(self, maxValue):
        self.a, self.b = 0, 1
        self.maxValue = maxValue

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.maxValue:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            if start is None:
                start = 0
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L


fab = Fab(10000)
# for n in fab:
#     print(n)
print(fab[10])
print(fab[:10])

def fabyeild(max):
    a , b = 1,1
    while b < max:
        yield b
        a ,b =b ,a+b
for i in fabyeild(1000):
    print(i)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().date.event.list)

month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.__members__)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday(1))
print(Weekday['Sun'])
print(Weekday['Sun'].value)

for name, member in Weekday.__members__.items():
    print(name, "=>", member)
