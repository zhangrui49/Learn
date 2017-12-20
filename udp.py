import socket
import threading,time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def receive():
    while True:
        data = s.recvfrom(1024)
        print('receive from %s' % (data))

def send():
    for i in range(20):
        print(i)
        s.sendto(b'',('116.62.62.140',5551))
        time.sleep(1)
        # address = s.recv(1024)
        # print('receive from %s' % (address))

t_send = threading.Thread(target=send,name='send_thread')
t_receive = threading.Thread(target=receive,name='receive_thread')

t_send.start()
t_receive.start()