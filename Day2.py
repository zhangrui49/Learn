import os


ls = os.linesep
fName = "test.txt"
while True:
    if os.path.exists(fName):
        print "ERROR: '%s' already exists" % fName
    else:
        break
all = []
print "\nEnter lines ('.' by itself to quit).\n"
while True:
    entry = raw_input(' > ')
    if entry == '.':
        break
    else:
        all.append(entry)
fobj = open(fName, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print "DONE!"


class Foo: pass


foo = Foo()
print type(foo)
print type(Foo)

num = raw_input("input a number")

def displayNumType(num):
    print num, "is",
    if type(num) == type(0):
        print 'an integer'
    elif type(num) == type(0L):
        print 'a long'
    elif type(num) == type(0.0):
        print 'a float'
    elif type(num) == type(0 + 0j):
        print 'a complex number'
    else:
        print 'not a number at all!! it is ',type(num)


displayNumType(num)
