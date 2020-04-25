
from PyQt5 import QtCore, QtGui, QtWidgets
import data
import functions as func
import styles
import engine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from client import bug_log
#import mainWindow
import client


from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication,QGridLayout, QWidget, QTabWidget,QScrollArea, QVBoxLayout,QHBoxLayout,QCheckBox, QGroupBox, QLabel, QPushButton, QFormLayout, QCheckBox,QComboBox

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)





class Ui_DialogConfig(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(data.orderResolution[0], data.orderResolution[1])
        #Dialog.setStyleSheet(" background: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(192, 192, 192, 255), stop:0.840909 rgba(210, 210, 210, 255));")
        addingToBox = []
        mainWin = QVBoxLayout(Dialog)
        tabs = QTabWidget()
        mainWin.addWidget(tabs)
        apply = QPushButton("Apply and Close")
        apply.clicked.connect(lambda : applyClose())
        mainWin.addWidget(apply)
        apply.setFixedWidth(data.orderResolution[0]/5)
        Dialog.setWindowIcon(QtGui.QIcon('gear.ico'))
        tabs.resize(data.orderResolution[0], data.orderResolution[1])
        tab1 = QWidget()
        tab1.layout = QGridLayout(tab1)
        deleteHisButton = QPushButton("DELETE HISTORY")
        deleteHisButton.clicked.connect(lambda : deleteHis())
        deleteHisButton.setFixedWidth(data.orderResolution[0]/5)

        darkModeBut = QPushButton()
        if data.mode == "Light":
            darkModeBut.setText("DARK MODE")
        else:
            darkModeBut.setText("Light MODE")

        darkModeBut.clicked.connect(lambda: switchToDark())
        tab1.layout.addWidget(deleteHisButton)
        tab1.layout.addWidget(darkModeBut)
        darkModeBut.setFixedWidth(data.orderResolution[0] / 5)

        tab1.layout.addWidget(QLabel("Find bag? Say about it:"), 2, 0)
        space = QtWidgets.QTextEdit()
        tab1.layout.addWidget(space,3,0)
        sendBag = QPushButton("Send")
        sendBag.clicked.connect(lambda: send_bug())
        tab1.layout.addWidget(sendBag, 3, 1)




        tabs.addTab(tab1, "General")

       # tab2 = QWidget()
        #tab2.layout = QVBoxLayout(tab2)
        #tabs.addTab(tab2, "Graph Settings")


        # searchLine = QHBoxLayout()
        # sLine = QtWidgets.QLineEdit()
        # sBut = QPushButton("Search")
        # sBut.clicked.connect(lambda: search())
        # searchLine.addWidget(sLine)
        # searchLine.addWidget(sBut)


        joinGraphs = QCheckBox("Join Buy and Sell Graphs?")
        if data.joinG[1] == True:
            joinGraphs.setChecked(True)
        joinGraphs.stateChanged.connect(self.joinGraphs)
        tab1.layout.addWidget(joinGraphs, 0, 1)
       # tab2.layout.addLayout(searchLine)

        # formLayout0 = QFormLayout()
        # groupBox0 = QGroupBox()
        # labelLis = []
        # comboList = []
        # #butlist = []
        # for i in range(1):
        #     but = QPushButton("Click Me"+ str(i))
        #     labelLis.append(QLabel("Label" + str(i)))
        #     comboList.append(but)
        #     formLayout0.addRow(labelLis[i], comboList[i])
        #
        # groupBox0.setLayout(formLayout0)
        # groupBox0.setTitle("Your Graphs:     Click to delete from Your Graphs.")
        # scroll0 = QScrollArea()
        # scroll0.setWidget(groupBox0)
        # scroll0.setWidgetResizable(True)

        #tab2.layout.addWidget(scroll0)



        # tab3 = QWidget()
        # tab3.layout = QGridLayout(tab3)
        # PIC = QtWidgets.QLabel()
        # PIC.setPixmap(QPixmap("3.JPG").scaled(200, 200))
        # tab3.layout.addWidget(PIC, 0, 0)
        # info = QLabel()
        # info.setText(func.barInfo().replace("    ", "\n"))
        # tab3.layout.addWidget(info, 0, 1)
        #
        # tab3.layout.addWidget(QPushButton("3"), 1, 0)
        # tab3.layout.addWidget(QPushButton("4"), 1, 1)
        #
        # tab3.layout.addWidget(QPushButton("6"), 2, 0)
        # tab3.layout.addWidget(QPushButton("7"), 2, 1)
        #
        # tabs.addTab(tab3, "Profile")



        tab4 = QWidget()
        tab4.layout = QVBoxLayout(tab4)
        tabs.addTab(tab4, "Products")
        tab4.layout.addWidget(QLabel("Find products you want to add."))
        searchLine1 = QHBoxLayout()
        sLine1 = QtWidgets.QLineEdit()
        sBut1 = QPushButton("Add")
        sBut1.clicked.connect(lambda: addPrd())
        searchLine1.addWidget(sLine1)
        searchLine1.addWidget(sBut1)
        tab4.layout.addLayout(searchLine1)

        formLayout1 = QFormLayout()

        groupBox1 = QGroupBox()
        i = 0
        for prod in data.pref_prd:
            i +=1
            t = QPushButton("    "+prod, clicked=lambda _, n=i: remove_prd(n-1))
            t.setFixedWidth(data.orderResolution[0] / 5)
            t.setStyleSheet("text-align: left;")
            formLayout1.insertRow(0, t)


        groupBox1.setLayout(formLayout1)
        groupBox1.setTitle("Your products:     Click to delete from Your Products.")
        scroll1 = QScrollArea()
        scroll1.setWidget(groupBox1)
        scroll1.setWidgetResizable(True)

        tab4.layout.addWidget(scroll1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def addPrd():
            prd = sLine1.text()
            data.pref_prd.append(prd)
            t = QPushButton("    "+str(prd))
            t.setFixedWidth(data.orderResolution[0] / 5)
            t.setStyleSheet("text-align: left;")
            formLayout1.addRow(t)
            addingToBox.append(prd)
            data.addToBox = [True, addingToBox]


        def send_bug():
            text = space.toPlainText()
            sendBag.setText("DONE")
            sendBag.setDisabled(True)
            bug_log(text)





        def applyClose():
            if data.joinG[0] == True:
                data.joinG = [True, True]
            if len(addingToBox) != 0:
                client.add_star(addingToBox,data.username,data.password)
            Dialog.close()

        def switchToDark():
            darkModeBut.setText("Click 'Apply and Close'")
            darkModeBut.setDisabled(True)
            if data.mode == "Light":
                data.mode = "Dark"
            else:
                data.mode = "Light"

        def deleteHis():
            data.clearHis = True
            func.clearHis()
            client.delete_history(data.username, data.password)
            deleteHisButton.setText("DONE")
            deleteHisButton.setDisabled(True)

        # def search():
        #     text = str(sLine.text().lower().strip())
        #     if text in data.graphs.keys():
        #         for i in reversed(range(formLayout0.count())):
        #             formLayout0.itemAt(i).widget().deleteLater()
        #         formLayout0.insertRow(0, QPushButton(text))
        #         groupBox0.setTitle("Click to add to Your Graphs")
        #     elif text == "":
        #         groupBox0.setTitle("Your Graphs:     Click to delete from Your Graphs.")
        def remove_prd(index):
            print("DLETE THIS NIBO", data.pref_prd[index])
            client.remove_star(data.pref_prd[index], data.username, data.password)
            del data.pref_prd[index]
            for i in reversed(range(formLayout1.count())):
                formLayout1.itemAt(i).widget().deleteLater()
            i = 0
            for prod in data.pref_prd:
                i += 1
                t = QPushButton("    "+prod, clicked=lambda _, n=i: remove_prd(n - 1))
                t.setFixedWidth(data.orderResolution[0] / 5)
                t.setStyleSheet("text-align: left;")
                formLayout1.insertRow(0, t)
            print(data.pref_prd)

            data.addToBox = [True, ""]

    def joinGraphs(self, state):
        if state == QtCore.Qt.Checked:
            #print('Checked')
            data.joinG = [True, False]
        else:
            data.joinG = [False, False]

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Config"))



