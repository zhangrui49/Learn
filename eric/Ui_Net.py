# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\eric\Net.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(890, 625)
        Dialog.setSizeGripEnabled(True)
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(540, 430, 75, 23))
        self.exit.setObjectName("exit")
        self.send = QtWidgets.QPushButton(Dialog)
        self.send.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.send.setObjectName("send")
        self.request_body = QtWidgets.QTextEdit(Dialog)
        self.request_body.setGeometry(QtCore.QRect(280, 140, 351, 71))
        self.request_body.setObjectName("request_body")
        self.request_label = QtWidgets.QLabel(Dialog)
        self.request_label.setGeometry(QtCore.QRect(200, 170, 54, 12))
        self.request_label.setObjectName("request_label")
        self.response_label = QtWidgets.QLabel(Dialog)
        self.response_label.setGeometry(QtCore.QRect(200, 270, 54, 12))
        self.response_label.setObjectName("response_label")
        self.response_body = QtWidgets.QTextEdit(Dialog)
        self.response_body.setGeometry(QtCore.QRect(280, 240, 351, 161))
        self.response_body.setObjectName("response_body")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(210, 80, 54, 12))
        self.ip_label.setObjectName("ip_label")
        self.port_label = QtWidgets.QLabel(Dialog)
        self.port_label.setGeometry(QtCore.QRect(490, 80, 54, 12))
        self.port_label.setObjectName("port_label")
        self.ip = QtWidgets.QLineEdit(Dialog)
        self.ip.setGeometry(QtCore.QRect(280, 80, 171, 20))
        self.ip.setObjectName("ip")
        self.port = QtWidgets.QLineEdit(Dialog)
        self.port.setGeometry(QtCore.QRect(530, 80, 101, 20))
        self.port.setObjectName("port")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 19, 201, 41))
        font = QtGui.QFont()
        font.setFamily("AngsanaUPC")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.exit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "网络调试"))
        self.exit.setText(_translate("Dialog", "exit"))
        self.send.setText(_translate("Dialog", "send"))
        self.request_label.setText(_translate("Dialog", "request"))
        self.response_label.setText(_translate("Dialog", "response"))
        self.ip_label.setText(_translate("Dialog", "ip"))
        self.port_label.setText(_translate("Dialog", "port"))
        self.label.setText(_translate("Dialog", "网络调试助手"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

