# -*- coding: utf-8 -*
from tkinter import *
import tkinter.messagebox as toast
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='please input ip here')
        self.helloLabel.pack()
        self.ip=Entry(self)
        self.ip.pack()
        self.alertButton = Button(self, text='sure', command=self.check_ip)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def check_ip(self):
        toast.showinfo('Message','ip set to %s success'% self.ip.get())
    
app = Application()
# 设置窗口标题:
app.master.title('net debugger')
# 主消息循环:
app.mainloop()