
from PyQt5 import QtCore, QtGui, QtWidgets
import data
import functions as func
import styles
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QComboBox, QScrollArea, QVBoxLayout,QHBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QCheckBox

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

import client
import functions
import mainWindow

#FOR SEARCHING
class Ui_DialogOrder(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(data.orderResolution[0], data.orderResolution[1])
        #Dialog.setStyleSheet(" background: qlineargradient(spread:pad, x1:0.0568182, y1:0.126, x2:0.75, y2:0.227, stop:0.0738636 rgba(192, 192, 192, 255), stop:0.840909 rgba(210, 210, 210, 255));")
        MainLayout = QVBoxLayout(Dialog)
        searchLine = QHBoxLayout()
        sLine = QtWidgets.QLineEdit()
        sBut = QPushButton("Search")
        sBut.clicked.connect(lambda:  test1())
        searchLine.addWidget(sLine)
        searchLine.addWidget(sBut)
        filter = QHBoxLayout()
        ordertype = QComboBox()
        ordertype.addItem("All")
        ordertype.addItem("Limit")
        ordertype.addItem("Fill or Kill")
        filter.addWidget(ordertype)

        reqq = QComboBox()
        reqq.addItem("All")
        reqq.addItem("Buy")
        reqq.addItem("Sell")
        filter.addWidget(reqq)

        filter.addWidget(QLabel("Amount: "))
        amount = QtWidgets.QLineEdit()
        filter.addWidget(amount)

        filter.addWidget(QLabel("Price: "))
        price = QtWidgets.QLineEdit()
        filter.addWidget(price)




        formLayout0 = QFormLayout()
        groupBox0 = QGroupBox()
        labelLis = []
        comboList = []
        for i in range(0):
            labelLis.append(QLabel("Label"))
            comboList.append(QPushButton("Click Me"))
            formLayout0.addRow(labelLis[i], comboList[i])

        groupBox0.setLayout(formLayout0)
        scroll0 = QScrollArea()
        scroll0.setWidget(groupBox0)
        scroll0.setWidgetResizable(True)
        MainLayout.addLayout(searchLine)
        MainLayout.addLayout(filter)
        MainLayout.addWidget(scroll0)









        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def test1():
            if sLine.text().strip() != "":
                prd =  "SELECT * FROM orders WHERE product='{}'".format(sLine.text().strip())
            else:
                prd = "SELECT * FROM orders"
            try:
                raise Exception
                res = client.exe(prd)
            except:
                res = functions.getOrder()



            print(res)
            for i in reversed(range(formLayout0.count())):
                formLayout0.itemAt(i).widget().deleteLater()
            groupBox0.setTitle(f"Available orders: {sLine.text()}")

            ordersAvailable = res
            # print(sLine.text(), ordertype.currentText(),
            #       reqq.currentText().lower(),
            #       amount.text(),
            #       price.text())
            for order in ordersAvailable:
                # comboList.append(QPushButton("Click Me"))
                thisorder = QPushButton()
                if order[3] == "buy":
                    sign = func.buyOrder(order[2], order[4], order[5], order[6])
                    thisorder.setStyleSheet(styles.buybutton)
                else:
                    thisorder.setStyleSheet(styles.sellbutton)
                    sign = func.sellOrder(order[2], order[4], order[5], order[6])
                thisorder.setText(sign)
                formLayout0.addRow(thisorder)

        def search():
            for i in reversed(range(formLayout0.count())):
                formLayout0.itemAt(i).widget().deleteLater()
            groupBox0.setTitle(f"Available orders: {sLine.text()}")

            ordersAvailable = func.findOrder(sLine.text(),
                                             ordertype.currentText().lower(),
                                             reqq.currentText().lower(),
                                             amount.text(),
                                             price.text())
            print(sLine.text(),ordertype.currentText(),
                                             reqq.currentText().lower(),
                                             amount.text(),
                                             price.text())
            for order in ordersAvailable:
                # comboList.append(QPushButton("Click Me"))
                thisorder = QPushButton()
                if order[3] == "buy":
                    sign = func.buyOrder(order[2], order[4], order[5], order[6])
                    thisorder.setStyleSheet(styles.buybutton)
                else:
                    thisorder.setStyleSheet(styles.sellbutton)
                    sign = func.sellOrder(order[2], order[4], order[5], order[6])
                thisorder.setText(sign)
                formLayout0.addRow(thisorder)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog","Searching"))

