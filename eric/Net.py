# -*- coding: utf-8 -*-

"""
Module implementing Net.
"""

from PyQt5.QtCore import pyqtSlot,QThread,pyqtSignal
from PyQt5.QtWidgets import QDialog
import socket
import time

from Ui_Net import Ui_Dialog

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip,port,request="","",""

class Sendthread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        for i in range(20):
            print("ip:%s port: %s request: %s" % (ip, port, request))
            print(i)
            s.sendto(request.encode('utf-8'),(ip,int(port)))
            data, addr = s.recvfrom(1024)
            #print('receive %s from %s' % (data, addr))
                #self.response_body.insertPlainText(data.decode('utf-8'))
            self.breakSignal.emit(data.decode('utf-8'))
            time.sleep(1)

thread = Sendthread()
#def receive(window):
 #   while True:
  #      data = s.recv(1024)
  #      print('receive %s' % (data))
   #     window.response_body.setText(str(data)+"\n")
            
# def send(window):
#     ip = window.ip.toPlainText()
#     port = window.port.toPlainText()
#     request = window.request_body.toPlainText()
#     print("ip:%s port: %s request: %s" % (ip, port, request))
#     for i in range(20):
#         print(i)
#         s.sendto(request.encode('utf-8'),(ip,int(port)))
#         data, addr = s.recvfrom(1024)
#         print('receive %s from %s' % (data, addr))
#         window.response_body.setText(str(i))
#         time.sleep(1)


class Net(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Net, self).__init__(parent)
        self.setupUi(self)
                    
    @pyqtSlot()
    def on_exit_clicked(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_send_clicked(self):
        """
        Slot documentation goes here.
        """
        global ip,port,request
        ip = self.ip.text()
        port = self.port.text()
        request = self.request_body.toPlainText()
        thread.breakSignal.connect(self.show_receive)
        thread.start()

    def show_receive(self,s):
        self.response_body.insertPlainText(s)
        print(s)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Net()
    dlg.show()
    #t_receive = threading.Thread(target=receive, args=(dlg,))
    #t_receive.start()
    sys.exit(app.exec_())
   
