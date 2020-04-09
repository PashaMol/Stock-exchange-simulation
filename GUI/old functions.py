def addOrderHistoryBuy():
    from random import randrange
    productsTest = ["Bitcoin", "Hsecoin", "Nuggets", "Jupyter Task"]
    t = ["Limit", "FOK"]
    order_type = t[randrange(0, 2)]
    product = productsTest[randrange(0, 4)]
    amount = str(randrange(0, 100))
    price = str(randrange(0, 100)) + "$"
    sign = func.buyOrder(order_type, product, amount, price)
    newOrder = QtWidgets.QPushButton()
    newOrder.setStyleSheet(styles.buybutton)
    newOrder.setDisabled(True)
    newOrder.setText(sign)
    # formLayout1.addWidget(newOrder)
    self.formLayout1.insertRow(0, newOrder)

    func.addToHis("Buy", order_type, product, amount, price)


def addOrderHistorySell():
    from random import randrange
    productsTest = ["Bitcoin", "Hsecoin", "Nuggets", "Jypyter Task"]
    t = ["Limit", "FOK"]
    order_type = t[randrange(0, 2)]
    product = productsTest[randrange(0, 4)]
    amount = str(randrange(0, 100))
    price = str(randrange(0, 100)) + "$"
    sign = func.sellOrder(order_type, product, amount, price)
    newOrder = QtWidgets.QPushButton()
    newOrder.setStyleSheet(styles.sellbutton)
    newOrder.setDisabled(True)
    newOrder.setText(sign)
    # formLayout1.addWidget(newOrder)
    self.formLayout1.insertRow(1, newOrder)

    func.addToHis("Sell", order_type, product, amount, price)


def clearHis():
    # print("csv is empty now")
    func.clearHis()
    try:
        for i in reversed(range(self.formLayout1.count())):
            self.formLayout1.itemAt(i).widget().deleteLater()
    except:
        pass
    # restart()


def restart():
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)


def callOrderWindow(type):
    data.orderResolution[0], data.orderResolution[1] = self.width / 3.7, self.height / 3
    data.orderType = str(type)
    Dialog = QtWidgets.QDialog()
    ui = ord.Ui_DialogOrder()
    ui.setupUi(Dialog)
    Dialog.exec_()
    if data.addToHis[0]:  ### ALSO CHECKS FOR SUCCESS
        # print("tt")
        sign = func.Order(data.addToHis[1][0], data.addToHis[1][1],
                          data.addToHis[1][2], data.addToHis[1][3], data.addToHis[1][4])
        newOrder = QtWidgets.QPushButton()
        newOrder.setStyleSheet(styles.buybutton)
        if data.addToHis[1][0].lower() == "sell":
            newOrder.setStyleSheet(styles.sellbutton)
        newOrder.setDisabled(True)
        newOrder.setText(sign)
        # formLayout1.addWidget(newOrder)
        self.formLayout1.insertRow(1, newOrder)

        bar.setText(func.barInfo())  # CHEANGE BALANCE
        func.putPersonalData()  # reamber balance
        # RELOADING AVALIABLE ORDERS
        self.reloadData()
        # ordersAvailable = func.getOrder()
        # if data.addToHis[1][0].lower() == "buy":
        #     try:
        #         for i in reversed(range(self.formLayout.count())):
        #             self.formLayout.itemAt(i).widget().deleteLater()
        #     except: pass
        #
        #     for order in ordersAvailable:
        #         # comboList.append(QPushButton("Click Me"))
        #        # print(order[4] + '!')
        #         if order[3] == "sell" and order[4] == self.MainProduct.currentText():
        #             thisorder = QPushButton()
        #             sign = func.buyOrder(order[2], order[4], order[5], order[6])
        #             thisorder.setText(sign)
        #             thisorder.setStyleSheet(styles.buybutton)
        #             self.formLayout.addRow(thisorder)
        # else:
        #     try:
        #         for i in reversed(range(self.formLayout0.count())):
        #             self.formLayout0.itemAt(i).widget().deleteLater()
        #     except: pass
        #
        #     for order in ordersAvailable:
        #         # comboList.append(QPushButton("Click Me"))
        #         #print(order[4] + '!')
        #         if order[3] == "buy"  and order[4] == self.MainProduct.currentText():
        #             thisorder = QPushButton()
        #             sign = func.sellOrder(order[2], order[4], order[5], order[6])
        #             thisorder.setText(sign)
        #             thisorder.setStyleSheet(styles.sellbutton)
        #             self.formLayout0.addRow(thisorder)
    elif data.addToOrd[0]:
        self.reloadData()
        # if data.addToOrd[1].lower() == "buy":
        #     thisorder = QPushButton()
        #     thisorder.setText(" Sell"+ data.addToOrd[2][4:])
        #     thisorder.setStyleSheet(styles.sellbutton)
        #     self.formLayout0.insertRow(1, thisorder)
        # else:
        #     thisorder = QPushButton()
        #     thisorder.setText(" Buy" + data.addToOrd[2][5:])
        #     thisorder.setStyleSheet(styles.buybutton)
        #     self.formLayout.insertRow(1, thisorder)

    data.addToHis = (False, [])
    data.addToOrd = (False, "Buy", "")


def filtersell():
    prd = self.MainProduct.currentText()
    # print(prd)
    try:
        for i in reversed(range(self.formLayout0.count())):
            self.formLayout0.itemAt(i).widget().setParent(None)
    except:
        pass

    ordersAvailable = func.getOrder()
    for order in ordersAvailable:
        # print(order[4])
        # comboList.append(QPushButton("Click Me"))
        if order[3] == "buy" and order[4] == prd:
            thisorder = QPushButton()
            sign = func.sellOrder(order[2], order[4], order[5], order[6])
            thisorder.setText(sign)
            thisorder.setStyleSheet(styles.sellbutton)
            self.formLayout0.insertRow(1, thisorder)


def filterbuy():
    prd = self.MainProduct.currentText()
    # print(prd)
    try:
        for i in reversed(range(self.formLayout.count())):
            self.formLayout.itemAt(i).widget().setParent(None)
    except:
        pass

    ordersAvailable = func.getOrder()
    for order in ordersAvailable:
        # print(order[4])
        # comboList.append(QPushButton("Click Me"))
        if order[3] == "sell" and order[4] == prd:
            thisorder = QPushButton()
            sign = func.buyOrder(order[2], order[4], order[5], order[6])
            thisorder.setText(sign)
            thisorder.setStyleSheet(styles.buybutton)
            self.formLayout.insertRow(1, thisorder)



#############################################################################



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QScrollArea, QVBoxLayout,QHBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QMainWindow, QTabWidget
from PyQt5.QtCore import QThread, Qt, pyqtSignal, QPoint
import sys
import csv
import styles
from graphs import *
from random import randrange
from PyQt5.QtGui import QPixmap
import functions as func
import searchingWindow as src
import orderWindow as ord
import configWindow as cfg
import data
import time

import engine
import client

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class MyThread(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    timeToSleep = pyqtSignal(int)
    def run(self):
        cnt = 0
        while True:
            #cnt += 1
            #print(cnt)
            time.sleep(self.timeToSleep)
            self.change_value.emit(cnt)



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Main window"
        self.top = 55
        self.left = 7
        #self.width = 950
        w = 1.17
        h = 1.2
        self.width = App.primaryScreen().size().width()/w
        #self.height = 450
        self.height = App.primaryScreen().size().height()/h
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        data.graphResolution = [self.width/4.5, self.height/1.4]

       # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        ordersAvailable = func.getOrder()
        self.formLayout0 = QFormLayout()
        self.groupBox0 = QGroupBox("Available orders: SELL")


        # sellbox = QComboBox()
        # sellboxbut = QPushButton("Show")
        # sellboxbut.clicked.connect(lambda: filtersell())
        # sellboxLine = QHBoxLayout()
        # sellboxLine.addWidget(sellbox)
        # sellboxLine.addWidget(sellboxbut)
        # for prd in data.pref_prd:
        #     sellbox.addItem(prd)
        # formLayout0.insertRow(0, sellboxLine)
        # for order in ordersAvailable:
        #     break
        #     #comboList.append(QPushButton("Click Me"))
        #     if order[3] == "buy":
        #         thisorder = QPushButton()
        #         sign = func.sellOrder(order[2], order[4], order[5], order[6])
        #         thisorder.setText(sign)
        #         thisorder.setStyleSheet(styles.sellbutton)
        #         self.formLayout0.insertRow(1, thisorder)

        self.groupBox0.setLayout(self.formLayout0)
        scroll0 = QScrollArea()
        scroll0.setWidget(self.groupBox0)
        scroll0.setWidgetResizable(True)
        #scroll0.setFixedHeight(400)
        #

        self.formLayout =QFormLayout()
        self.groupBox = QGroupBox("Available orders: BUY")

        # self.buybox = QComboBox()
        # buyboxbut = QPushButton("Show")
        # buyboxbut.clicked.connect(lambda : filterbuy())
        # buyboxLine = QHBoxLayout()
        # buyboxLine.addWidget(self.buybox)
        # buyboxLine.addWidget(buyboxbut)
        #
        # for prd in data.pref_prd:
        #     self.buybox.addItem(prd)
        # formLayout.insertRow(0, buyboxLine)
        # for order in ordersAvailable:
        #     break
        #     #comboList.append(QPushButton("Click Me"))
        #     if order[3] == "sell":
        #         thisorder = QPushButton()
        #         sign = func.buyOrder(order[2], order[4], order[5], order[6])
        #         thisorder.setText(sign)
        #         thisorder.setStyleSheet(styles.buybutton)
        #         self.formLayout.insertRow(1, thisorder)

        self.groupBox.setLayout(self.formLayout)
        scroll = QScrollArea()
        scroll.setWidget(self.groupBox)
        scroll.setWidgetResizable(True)
        #scroll.setFixedHeight(self.height*0.98)





        ##
        self.formLayout3 = QFormLayout()
        self.groupBox3 = QGroupBox("Your orders")

        # sellbox = QComboBox()
        # sellboxbut = QPushButton("Show")
        # sellboxbut.clicked.connect(lambda: filtersell())
        # sellboxLine = QHBoxLayout()
        # sellboxLine.addWidget(sellbox)
        # sellboxLine.addWidget(sellboxbut)
        # for prd in data.pref_prd:
        #     sellbox.addItem(prd)
        # formLayout0.insertRow(0, sellboxLine)
        for order in ordersAvailable:

            # comboList.append(QPushButton("Click Me"))
            if True:
                thisorder = QPushButton()
                sign = func.sellOrder(order[2], order[4], order[5], order[6])
                thisorder.setText(sign)
                thisorder.setStyleSheet(styles.sellbutton)
                self.formLayout3.insertRow(1, thisorder)

        self.groupBox3.setLayout(self.formLayout3)
        scroll3 = QScrollArea()
        scroll3.setWidget(self.groupBox3)
        scroll3.setWidgetResizable(True)

            ##



        # global self.formLayout1
        self.formLayout1 = QFormLayout()
        self.groupBox1 = QGroupBox("Orders' History")

        # self.hisbox = QComboBox()
        # hisboxbut = QPushButton("Show")
        # hisboxLine = QHBoxLayout()
        # hisboxLine.addWidget(self.hisbox)
        # hisboxLine.addWidget(hisboxbut)
        # self.hisbox.addItem("All")
        # self.hisbox.addItem("Only BUY")
        # self.hisbox.addItem("Only SELL")

        #formLayout1.insertRow(0, hisboxLine)
        with open("userHistory.csv") as file:
            reader = csv.reader(file)
            for r in reader:
                if len(r):
                    Order = QtWidgets.QPushButton()
                    if r[0] == "Sell":
                        sign = func.sellOrder(r[1], r[2], r[3], r[4])
                        Order.setStyleSheet(styles.sellbutton)
                    else:
                        sign = func.buyOrder(r[1], r[2], r[3], r[4])
                        Order.setStyleSheet(styles.buybutton)
                    Order.setText(sign)
                    Order.setDisabled(True)
                    #formLayout1.addWidget(Order)
                    self.formLayout1.insertRow(1, Order)

        self.groupBox1.setLayout(self.formLayout1)
        scroll2 = QScrollArea()
        scroll2.setWidget(self.groupBox1)
        scroll2.setWidgetResizable(True)





        rightArea = QVBoxLayout()
       # labelLayout = QHBoxLayout()
       # label1 = QtWidgets.QLabel("Orders Pos!")
       # label2 = QtWidgets.QLabel("Orders History!")
        #labelLayout.addWidget(label1)
        #labelLayout.addWidget(label2)
        threeScrolls = QHBoxLayout()
        threeScrolls.addWidget(scroll0)
        threeScrolls.addWidget(scroll)
        Column = QVBoxLayout()
        Column.addWidget(scroll3)
        Column.addWidget(scroll2)
        threeScrolls.addLayout(Column)
        #rightArea.addLayout(labelLayout)
        rightArea.addLayout(threeScrolls)

        leftArea = QVBoxLayout()

        BuySell = QHBoxLayout()
        buyButton = QtWidgets.QPushButton("BUY")
        buyButton.setStyleSheet(styles.buybuttonFus.replace("text-align: left;",""))
       # buyButton.setFixedWidth(50)
       # buyButton.setFixedHeight(28)
        BuySell.addWidget(buyButton)
        sellButton = QtWidgets.QPushButton("SELL")
        sellButton.setStyleSheet(styles.sellbuttonFus.replace("text-align: left;",""))
        #sellButton.setFixedWidth(50)
        #sellButton.setFixedHeight(28)
        BuySell.addWidget(sellButton)
        searchButton = QtWidgets.QPushButton("SEARCH")
       # searchButton.setFixedWidth(50)
       # searchButton.setFixedHeight(28)
        #BuySell.addWidget(searchButton)
        settingsButton = QtWidgets.QPushButton("configuring".upper())
        BuySell.addWidget(settingsButton)
        self.MainProduct = QComboBox()
        #MainProduct.currentIndexChanged.connect(lambda : test())
        self.MainProduct.currentIndexChanged.connect(self.reloadData, self.MainProduct.currentIndex())
        self.MainProduct.addItem("No filter")
        for prd in data.pref_prd:
            self.MainProduct.addItem(prd)
        BuySell.addWidget(self.MainProduct)



        buyButton.clicked.connect(lambda : callOrderWindow("Buy"))
        sellButton.clicked.connect(lambda: callOrderWindow("Sell"))
        searchButton.clicked.connect(lambda: callSearchWindow())
        settingsButton.clicked.connect(lambda: callConfigWindow())

        leftArea.addLayout(BuySell)

        graphsArea = QVBoxLayout()
        #labelPIC = QtWidgets.QLabel()
        #labelPIC.setPixmap(QPixmap("2.JPG").scaled(400, 390))
        self.graph1 = Canvas2()

        self.graph2 = Canvas2() ##self


        tabs = QTabWidget()
        tabs.setFixedHeight(data.graphResolution[0])
        tabs.setFixedWidth(data.graphResolution[1])
        tabs.addTab(self.graph1, "Graph1")


        graphsArea.addWidget(tabs)

        tabs1 = QTabWidget()
        tabs1.setFixedHeight(data.graphResolution[0])
        tabs1.setFixedWidth(data.graphResolution[1])

        tabs1.addTab(self.graph2, "Graph2")

        graphsArea.addWidget(tabs1)

        ###

            ###
        leftArea.addLayout(graphsArea)

        global bar
        bar = QPushButton(func.barInfo())
        bar.setStyleSheet(styles.barstyle1)
        bar.setDisabled(True)

        lowBar = QPushButton("NEWS:  "+ data.news[randrange(0, len(data.news))])
        lowBar.setStyleSheet(styles.news)
        lowBar.setDisabled(True)



        Mainlayout = QVBoxLayout(self)
        ContentArea = QHBoxLayout()
        ContentArea.addLayout(leftArea)
        ContentArea.addLayout(rightArea)
        Mainlayout.addWidget(bar)
        Mainlayout.addLayout(ContentArea)
        Mainlayout.addWidget(lowBar)




        self.show()

        self.thread = MyThread()  #time
        self.thread.timeToSleep = 0.3
        self.thread.change_value.connect(lambda : setProgressVal())
        #self.thread.change_value.connect(lambda: test())
        self.thread.start()

        # self.thread1 = MyThread() # add possible orders
        # self.thread1.timeToSleep = 3
        # self.thread1.change_value.connect(lambda: test())
        # self.thread1.start()

        self.thread2 = MyThread() # update graphs
        self.thread2.timeToSleep = 2.3
        self.thread2.change_value.connect(lambda: updateGraphs())
        self.thread2.start()

        self.thread3 = MyThread()  # update news
        self.thread3.timeToSleep = 7
        self.thread3.change_value.connect(lambda: printNews())
        self.thread3.start()




        def setProgressVal():
            bar.setText(func.barInfo())
        def updateGraphs():
            tabs1.removeTab(0)
            self.graph2.setParent(None)
            self.graph2 = Canvas2(self)
            tabs1.addTab(self.graph2, "Graph2")
            #
            #tabs1.update()

            tabs.removeTab(0)
            self.graph1.setParent(None)
            self.graph1 = Canvas2(self)
            tabs.addTab(self.graph1, "Graph1")

        def callConfigWindow():

           ### QtWidgets.QApplication.instance().setPalette(self.style().standardPalette())  дефолт

            data.orderResolution[0], data.orderResolution[1] = self.width / 2.3, self.height / 1.7
            Dialog = QtWidgets.QDialog()
            ui = cfg.Ui_DialogConfig()
            ui.setupUi(Dialog)
            Dialog.exec_()
            if data.mode == "Dark":
                switchDark()
                bar.setStyleSheet(styles.barstyle2)
            if data.clearHis == True:
                try:
                    for i in reversed(range(self.formLayout1.count())):
                        self.formLayout1.itemAt(i).widget().deleteLater()
                except:
                    pass
            data.clearHis = False

            if data.addToBox[0]:
                for el in data.addToBox[1]:
                    self.MainProduct.addItem(el)

            data.addToBox = [False, []]



        def callOrderWindow(type):
            data.orderResolution[0], data.orderResolution[1] = self.width / 3.7, self.height / 3
            data.orderType = str(type)
            Dialog = QtWidgets.QDialog()
            ui = ord.Ui_DialogOrder()
            ui.setupUi(Dialog)
            Dialog.exec_()
            if data.addToHis[0]: ### ALSO CHECKS FOR SUCCESS
                #print("tt")
                sign = func.Order(data.addToHis[1][0], data.addToHis[1][1],
                                  data.addToHis[1][2], data.addToHis[1][3], data.addToHis[1][4])
                newOrder = QtWidgets.QPushButton()
                newOrder.setStyleSheet(styles.buybutton)
                if data.addToHis[1][0].lower() == "sell":
                    newOrder.setStyleSheet(styles.sellbutton)
                newOrder.setDisabled(True)
                newOrder.setText(sign)
                # formLayout1.addWidget(newOrder)
                self.formLayout1.insertRow(0, newOrder)

                bar.setText(func.barInfo())#CHEANGE BALANCE
                func.putPersonalData() #reamber balance
                #RELOADING AVALIABLE ORDERS
                self.reloadData()

            elif data.addToOrd[0]:
                self.reloadData()



            data.addToHis = (False, [])
            data.addToOrd = (False, "Buy", "")


        def callSearchWindow():
            data.orderResolution[0], data.orderResolution[1] = self.width/2.5, self.height/1.3
           # data.orderType = str(type)
            Dialog = QtWidgets.QDialog()
            ui = src.Ui_DialogOrder()
            ui.setupUi(Dialog)
            Dialog.exec_()


        def printNews():
            i = randrange(0, len(data.news))
            lowBar.setText("NEWS:  "+ data.news[i])





        def test():
            print("TESTING FUNCTION")






    def reloadData(self):
        text = self.MainProduct.currentText()
        print("IOI")
        flag = False
        if text == "No filter":
            try:
                if data.goLocal:
                    raise  Exception
                res = client.exe("SELECT * FROM orders")
                flag = True
            except:
                print("EXCEPTION OCCURRED: Local database is used instead ")
                res = func.getOrder()
                flag = True
        else:
            try:
                if data.goLocal:
                    raise  Exception
                res = client.exe("SELECT * FROM orders WHERE product='{}'".format(text))
            except:
                print("EXCEPTION OCCURRED: Local database is used instead ")
                res = func.findOrder(text)

        try:
            for i in reversed(range(self.formLayout.count())):
                self.formLayout.itemAt(i).widget().deleteLater()
        except:
            pass

        for order in res:
            # comboList.append(QPushButton("Click Me"))
            # print(order[4] + '!')
            if order[3] == "sell" and (order[4] == self.MainProduct.currentText() or flag) and str(order[-1]) != data.userid:
                thisorder = QPushButton()
                sign = func.buyOrder(order[2], order[4], order[5], order[6])
                thisorder.setText(sign)
                thisorder.setStyleSheet(styles.buybutton)
                self.formLayout.addRow(thisorder)
        try:
            for i in reversed(range(self.formLayout0.count())):
                self.formLayout0.itemAt(i).widget().deleteLater()
        except:
            pass

        for order in res:
            # comboList.append(QPushButton("Click Me"))
            # print(order[4] + '!')
            if order[3] == "buy" and (order[4] == self.MainProduct.currentText() or flag) and str(order[-1]) != data.userid:
                thisorder = QPushButton()
                sign = func.sellOrder(order[2], order[4], order[5], order[6])
                thisorder.setText(sign)
                thisorder.setStyleSheet(styles.sellbutton)
                self.formLayout0.addRow(thisorder)


def switchDark():

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, Qt.white)
    palette.setColor(QtGui.QPalette.Text, Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, Qt.red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, Qt.black)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    App.setPalette(palette)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')

    window = MainWindow()
    sys.exit(App.exec())


 def reloadData(self):
        text = self.MainProduct.currentText()
        ###v
        self.updateGraphs()

        #print("IOI")
        flag = False
        if text == "No filter":
            try:
                if data.goLocal:
                    raise  Exception
                res = client.exe("SELECT * FROM orders")
                flag = True
            except:
                print("EXCEPTION OCCURRED: Local database is used instead ")
                res = func.getOrder()
                flag = True
        else:
            try:
                if data.goLocal:
                    raise  Exception
                res = client.exe("SELECT * FROM orders WHERE product='{}' ORDER BY price".format(text))
            except:
                print("EXCEPTION OCCURRED: Local database is used instead ")
                res = func.findOrder(text)

        try:
            for i in reversed(range(self.formLayout.count())):
                self.formLayout.itemAt(i).widget().deleteLater()
        except:
            pass
        j2 = 0
        for order in res:
            # comboList.append(QPushButton("Click Me"))
            # print(order[4] + '!')
            j2+=1
            if order[3] == "sell":
                if order[-1] != float(data.userid) and (order[4] == self.MainProduct.currentText() or flag):
                    # thisorder = QPushButton()
                    # thisorder.setStyleSheet(styles.buybutton)
                    # sign = func.buyOrder(order[2], order[4], order[5], order[6])
                    # thisorder.setText(sign)
                    # self.formLayout.addRow(thisorder)
                    pass
                elif order[-1] == float(data.userid):
                    sys_ord = [order[2], order[3], order[4], str(order[5]), str(order[6]), str(order[0])]
                    if sys_ord not in data.system_ord:
                        data.system_ord.append(sys_ord)

                if order not in data.Orders:
                    data.Orders.append(order)

        try:
            for i in reversed(range(self.formLayout0.count())):
                self.formLayout0.itemAt(i).widget().deleteLater()
        except:
            pass
        j3 = 0
        for order in res:
            # comboList.append(QPushButton("Click Me"))
            # print(order[4] + '!')
            j3 +=1
            if order[3] == "buy":
                if order[-1] != float(data.userid)and (order[4] == self.MainProduct.currentText() or flag):
                    # thisorder = QPushButton()
                    # thisorder.setStyleSheet(styles.sellbutton)
                    # sign = func.sellOrder(order[2], order[4], order[5], order[6])
                    # thisorder.setText(sign)
                    # self.formLayout0.insertRow(0, thisorder)    #insert to show the the most expensive above
                    pass
                elif order[-1] == float(data.userid):
                    sys_ord = [order[2], order[3], order[4], str(order[5]), str(order[6]), str(order[0])]
                    if sys_ord not in data.system_ord:
                        data.system_ord.append(sys_ord)

            if order not in data.Orders:
                data.Orders.append(order)

        # print("v")
        # o = 0
        # for el in data.Orders:
        #     o+=1
        #     print(el)
        # print("^ " + str(o))


        self.reloadSystemOrders("")