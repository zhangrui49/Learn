import chardet
import psutil
print(chardet.detect(b'hello'))
print(chardet.detect('卧槽'.encode('gb2312')))
print(chardet.detect('卧槽'.encode('utf-8')))

print('cpu count: %d' % psutil.cpu_count())
print(psutil.cpu_times())

# for x in range(100):
#     print(psutil.cpu_percent(interval=1,percpu=True))

print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())
print(psutil.disk_usage('E:\\'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())
# print(psutil.net_connections())
print(psutil.pids())
p=psutil.Process(7524)
print('name:',p.name())
print('exe:',p.exe())
print('cmdline:',p.cmdline())
print('ppid:',p.ppid())
print('status:',p.status())
print('user:',p.username())
print('create:',p.create_time())
#print('terminal:',p.terminal())
print('cpu:',p.cpu_times())
print('memory:',p.memory_info())
print('thread:',p.threads())
print('child:',p.children())
print('conn:',p.connections())
print('threads:',p.num_threads())
print('env:',p.environ())
p.test() #ps 



