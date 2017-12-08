# -*- coding: utf-8 -*-
from io import StringIO, BytesIO
import os
import time
import random
import threading
from multiprocessing import Process, Pool

f = StringIO('Hello!\nHi!\nGoodbye!')
b = BytesIO('中国'.encode('utf-8'))
while True:
    s = f.readline()

    if s == '':
        break
    print(s.strip())

print(b.read())
print(os.name)
# print(os.uname())
# print(os.environ)
print(os.environ.get('JAVA_HOME'))
print([x for x in os.listdir() if os.path.isdir(x)])
print([x for x in os.listdir() if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py'])

# print("process (%s) start..." % os.getpid())
# windows 不支持
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start...')
#     p.start()
#     p.join()
#     print('Child process end.')

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     #time.sleep(20000)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# long_time_task('20 s')
# print('Parent process %s.' % os.getpid())
# p = Pool(4)
# for i in range(5):
#     p.apply_async(long_time_task, args=(i,))
# print('Waiting for all subprocesses done...')
# p.close()
# p.join()
# print('All subprocesses done.')


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print("thread %s >>> %s" % (threading.current_thread().name, i))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

count = 1000
lock = threading.Lock()


def change(n):
   # lock.acquire()
   # try:
    global count
    count = count + n
    count = count - n
  #  finally:
   #     lock.release()


def run_thread():
    for i in range(1000):
        change(i)


thread1 = threading.Thread(target=change, args=(5,))
thread2 = threading.Thread(target=change, args=(8,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
# change(1000)
print(count)

local = threading.local()
def process_count():
    count = local.count
    print("%s %d",threading.current_thread().name,count)

def process_thread(count):
    local.count = count
    process_count()

for i in range(10):
    thread = threading.Thread(target=process_thread,args=(random.random()*i,))
    thread.start()
