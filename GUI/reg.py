# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import userVerification as uv

class Ui_DialogREG(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 329)
        Dialog.setStyleSheet("background-color: rgb(225, 223, 252);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.uNameLine = QtWidgets.QLineEdit(Dialog)
        self.uNameLine.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.uNameLine.setObjectName("uNameLine")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.uPasswordLine = QtWidgets.QLineEdit(Dialog)
        self.uPasswordLine.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.uPasswordLine.setObjectName("uPasswordLine")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.uPasswordLine_2 = QtWidgets.QLineEdit(Dialog)
        self.uPasswordLine_2.setGeometry(QtCore.QRect(140, 210, 113, 20))
        self.uPasswordLine_2.setObjectName("uPasswordLine_2")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 50, 200, 31))

        self.confirmButton = QtWidgets.QPushButton("CONFIRM",Dialog)
        self.confirmButton.setGeometry(QtCore.QRect(160, 240, 91, 20))
        self.confirmButton.setObjectName("CONFIRM")
        #self.confirmButton.clicked.connect(self.createNewUser)
        self.confirmButton.clicked.connect(lambda: self.createNewUser(Dialog))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def createNewUser(self, Dialog):
        uv.c = uv.conn.cursor()
        uName = self.uNameLine.text()
        uPassword1 = self.uPasswordLine.text()
        uPassword2 = self.uPasswordLine_2.text()
        status = uv.checkUser(uName, uPassword1)
        if status[0] == True:
            self.label_5.setText("The name is not available")
            return
        if uPassword1 != uPassword2:
            self.label_5.setText("The passwords differ")
            return
        self.label_5.setText("OK")
        uv.createNewUser(uName,uPassword1)
        uv.c.close()
        Dialog.hide()




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Create new profile"))
        self.label_2.setText(_translate("Dialog", "    USERNAME"))
        self.label_3.setText(_translate("Dialog", " ENTER\n"
" NEW\n"
" PASSWORD"))
        self.label_4.setText(_translate("Dialog", " CONFIRM \n"
" PASSWORD"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
