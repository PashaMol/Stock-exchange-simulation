
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import time
from reg import Ui_DialogREG
import userVerification as uv
import data
import random
import mainWindow
import functions
import client
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QScrollArea, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MyThread(QThread):
    try:
        # Create a counter thread
        change_value = pyqtSignal(int)
        timeToSleep = pyqtSignal(int)
        def run(self):
            try:
                cnt = 0
                while True:
                    #cnt += 1
                    #print(cnt)

                    self.change_value.emit(cnt)
                    time.sleep(self.timeToSleep)
            except:
                print("MyThread error")
    except: pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.x = 403
        self.y = 329
        Dialog.resize(self.x, self.y)
        Dialog.setStyleSheet("background: rgba(210, 210, 210, 255);")
        Dialog.setWindowIcon(QtGui.QIcon('icon1.ico'))
        #MainLayout = QVBoxLayout(Dialog)
        self.L = QGridLayout(Dialog)
        self.uNameLine = QLineEdit()
        self.idLine = QLineEdit()
        self.IPline = QLineEdit()
        self.uPasswordLine = QLineEdit()
        self.signInButton = QPushButton("Sign In")
        self.signInButton.clicked.connect(lambda : self.signingIn())
        self.RegBut = QPushButton("Sign Up")
        self.RegBut.clicked.connect(lambda : self.signingUp())
        self.L.addWidget(QtWidgets.QLabel("Name"), 0,0)
        self.L.addWidget(self.uNameLine, 0,1)
       # L.addWidget(QtWidgets.QLabel("ID"), 1, 0)
        #L.addWidget(self.idLine, 1, 1)
        self.L.addWidget(QtWidgets.QLabel("IP"), 2, 0)
        self.L.addWidget(self.IPline, 2,1)
        self.L.addWidget(QtWidgets.QLabel("Password"), 3, 0)
        self.L.addWidget(self.uPasswordLine, 3, 1)
        self.IPline.setText(client.IP)
        self.L.addWidget(self.RegBut, 4, 0)
        self.L.addWidget(self.signInButton, 4, 1)
        self.infLabel = QtWidgets.QLabel("                      ")
        self.infLabel.setFixedHeight(15)
        self.L.addWidget(self.infLabel, 5, 1)
        self.uPasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        #L.addWidget()
        #MainLayout.addLayout(L)
       # MainLayout.addWidget(self.infLabel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.thread = MyThread()  # time
        self.thread.timeToSleep = 3600
        self.thread.change_value.connect(lambda: functions.getNews())
        self.thread.start()                                                              # TODO START IT

    def callRegWin(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogREG()

        self.ui.setupUi(self.Dialog)
        self.Dialog.exec_()
        #self.Dialog.show()





######################

    def clearWin(self):
        # def clicked():
        #     exit()

        for i in reversed(range(self.L.count())):
            self.L.itemAt(i).widget().setParent(None)
        # finish = QPushButton("EXIT")
        # finish.setFixedSize(self.x*0.5, self.y*0.5)
        # finish.setStyleSheet(" background: red;")
        # finish.clicked.connect(lambda : clicked())
        # self.L.addWidget(finish)
        #pic = QtWidgets.QLabel()


    def signingIn(self):


        uName = self.uNameLine.text()
        uPassword = self.uPasswordLine.text()
        ip = self.IPline.text()
        #id_ = self.idLine.text()
        data.username = uName
        #data.userid = id_
        data.password = uPassword

        client.IP = ip
        #os.system("python mainWindow.py")
        if not client.known_user(uName, uPassword):
            self.infLabel.setText("Wrong login/password")
            return



        if len(data.username)!=0 and len(data.userid)!=0 and len(data.password)!=0 and len( client.IP)!=0 and functions.is_number(data.userid):
            print("start")
            try:
                 data.userid = client.get_id(uName)
                 data.balance = (client.get_balance(uName), "$")
                 functions.putPersonalData()
                 #self.Dialog.close()
                 mainWindow.runGUI()
                 #print("singIn")

            except:
                print("Error while starting app")
                self.clearWin()
                self.closewin()
                #self.Dialog.close()
        else:
            self.infLabel.setText("Error. Try Again!")

        return
    def signingUp(self):


        uName = self.uNameLine.text()
        uPassword = self.uPasswordLine.text()
        print("1")
        if client.known_user(uName, False):
            self.infLabel.setText("Cannot use this login!")
            return
        print("2")
        client.register(uName,uPassword)
        print("3")

        ip = self.IPline.text()
       #id_ = self.idLine.text()
        data.username = uName
       # data.userid = id_
        data.password = uPassword

        client.IP = ip
        print("4")
        if len(data.username)!=0 and len(data.userid)!=0 and len(data.password)!=0 and len( client.IP)!=0 and functions.is_number(data.userid):
            print("start")
            try:
                data.userid = client.get_id(uName)
                data.balance = (client.get_balance(uName), "$")
                functions.putPersonalData()
                #self.Dialog.close()
                mainWindow.runGUI()
                #print("signUp")
                #mainWindow.runGUI()
            except:
                print("Error while starting app")
                self.clearWin()
                self.closewin()
                #self.Dialog.close()
        else:
            self.infLabel.setText("Error. Try Again!")

        return

    def closewin(self):
        self.thread.terminate()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Verification"))
        # self.label.setText(_translate("Dialog", "    USERNAME"))
        # self.label_2.setText(_translate("Dialog", "  PASSWORD"))
        # self.signInButton.setText(_translate("Dialog", "Sign In"))
        # self.newAccButton.setText(_translate("Dialog", "Create new account"))
        # self.label_3.setText(_translate("Dialog", "     First time here?"))

