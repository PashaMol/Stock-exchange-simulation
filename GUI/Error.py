
from PyQt5 import QtCore, QtGui, QtWidgets
import data
import functions as func
import styles
import engine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
import client
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout,QHBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QCheckBox,QComboBox

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
from PyQt5.QtCore import QThread, Qt, pyqtSignal, QPoint
import sys
import time
class MyThread(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    timeToSleep = pyqtSignal(int)
    def run(self):
        try:
            cnt = 0
            while True:
                #cnt += 1
                #print(cnt)
                time.sleep(self.timeToSleep)
                self.change_value.emit(cnt)
        except:
            print("MyThread error")

class Error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.setGeometry(data.coord[0], data.coord[1], data.orderResolution[0]/4, data.orderResolution[1]/6)
        Dialog.resize(data.orderResolution[0]/4, data.orderResolution[1]/6)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setWindowFlags(flags)
        MainLayout = QVBoxLayout(Dialog)
        MainLayout.addWidget(QLabel("Trying to connect to server"))
        self.load = QLabel()
        self.load.setAlignment(Qt.AlignCenter)
        if data.mode != "Dark":
            movie = QtGui.QMovie("loading.gif")
        else:
            movie = QtGui.QMovie("loadingDark.gif")
        self.load.setMovie(movie)
        movie.start()
        MainLayout.addWidget(self.load)

        self.thread = MyThread()  # time
        self.thread.timeToSleep = 5
        self.thread.change_value.connect(lambda: setProgressVal())
        self.thread.start()


        def setProgressVal():
            try:
                r = client.update()
                Dialog.close()
                data.error =False
            except:
                pass



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CONFIRM"))



