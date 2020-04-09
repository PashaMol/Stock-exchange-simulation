#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QPixmap
# import sys
# import time
# from reg import Ui_DialogREG
# import userVerification as uv
#
#
#
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
#
# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
#
# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(403, 329)
#         Dialog.setStyleSheet("background: rgba(210, 210, 210, 255);")
#         self.uNameLine = QtWidgets.QLineEdit(Dialog)
#         self.uNameLine.setGeometry(QtCore.QRect(150, 90, 113, 20))
#         self.uNameLine.setObjectName("uNameLine")
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setGeometry(QtCore.QRect(25, 80, 110, 31))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setGeometry(QtCore.QRect(25, 140, 110, 31))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#         self.uPasswordLine = QtWidgets.QLineEdit(Dialog)
#         self.uPasswordLine.setGeometry(QtCore.QRect(150, 150, 113, 20))
#         self.uPasswordLine.setObjectName("uPasswordLine")
#         self.signInButton = QtWidgets.QPushButton(Dialog)
#         self.signInButton.setGeometry(QtCore.QRect(160, 190, 91, 20))
#         self.signInButton.setObjectName("signInButton")
#         self.signInButton.clicked.connect(self.signingIn)
#         self.newAccButton = QtWidgets.QPushButton(Dialog)
#         self.newAccButton.setGeometry(QtCore.QRect(140, 250, 145, 25))
#         self.newAccButton.setObjectName("newAccButton")
#         self.newAccButton.clicked.connect(self.callRegWin)
#         self.label_3 = QtWidgets.QLabel(Dialog)
#         self.label_3.setGeometry(QtCore.QRect(125, 230, 175, 20))
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(Dialog)
#         self.label_4.setGeometry(QtCore.QRect(155, 55, 200, 20))
#         self.label_4.setObjectName("label_4")
#
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def callRegWin(self):
#         self.Dialog = QtWidgets.QDialog()
#         self.ui = Ui_DialogREG()
#
#         self.ui.setupUi(self.Dialog)
#         self.Dialog.exec_()
#         #self.Dialog.show()
#
#
#     def signingIn(self):
#         uv.c =uv.conn.cursor()
#         uName = self.uNameLine.text()
#         uPassword = self.uPasswordLine.text()
#         status = uv.checkUser(uName,uPassword)
#         uv.verdict(status) ##
#         if status[0]:
#             print("There is such a user")
#             if status[1]:
#                 self.label_4.setText("Accepted!")
#             else:
#                 self.label_4.setText("Wrong password")
#         else:
#             self.label_4.setText("There is NO such a user")
#         uv.c.close()
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "User Verification"))
#         self.label.setText(_translate("Dialog", "    USERNAME"))
#         self.label_2.setText(_translate("Dialog", "  PASSWORD"))
#         self.signInButton.setText(_translate("Dialog", "Sign In"))
#         self.newAccButton.setText(_translate("Dialog", "Create new account"))
#         self.label_3.setText(_translate("Dialog", "     First time here?"))
#
