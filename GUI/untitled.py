
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout,QHBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys
import csv
from PyQt5.QtGui import QPixmap
import functions as func
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Main window"
        self.top = 55
        self.left = 7
        self.width = 950
        self.height = 450
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout =QFormLayout()
        groupBox = QGroupBox("This Is Group Box")

        labelLis = []
        comboList = []
        for i in  range(25):
            labelLis.append(QLabel("Label"))
            comboList.append(QPushButton("Click Me"))
            formLayout.addRow(labelLis[i], comboList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)


        ##

        formLayout1 = QFormLayout()
        groupBox1 = QGroupBox("This Is Group Box2")

        comboList1 = []
        for i in range(0):
            #comboList1.append(QPushButton("Click Me"))
            sign = func.buyOrder("limit", "Bit", "20", "25")
            Order = QtWidgets.QPushButton()
            Order.setStyleSheet("""QPushButton { text-align: left; 
                        background-color: rgb(176, 224, 230);};
                        """)
            Order.setText(sign)
            formLayout1.addWidget(Order)

        with open("userHistory.csv") as file:
            reader = csv.reader(file)
            for r in reader:
                if len(r):
                    sign = func.buyOrder(r[1], r[2], r[3], r[4])
                    Order = QtWidgets.QPushButton()
                    Order.setStyleSheet("""QPushButton { text-align: left; 
                                            background-color: rgb(176, 224, 230);};
                                            """)
                    Order.setText(sign)
                    formLayout1.addWidget(Order)

        groupBox1.setLayout(formLayout1)
        scroll2 = QScrollArea()
        scroll2.setWidget(groupBox1)
        scroll2.setWidgetResizable(True)
        scroll2.setFixedHeight(400)



        rightArea = QVBoxLayout()
        labelLayout = QHBoxLayout()
        label1 = QtWidgets.QLabel("Orders Pos!")
        label2 = QtWidgets.QLabel("Orders History!")
        labelLayout.addWidget(label1)
        labelLayout.addWidget(label2)
        twoScrolls = QHBoxLayout()
        twoScrolls.addWidget(scroll)
        twoScrolls.addWidget(scroll2)
        rightArea.addLayout(labelLayout)
        rightArea.addLayout(twoScrolls)

        leftArea = QVBoxLayout()

        BuySell = QHBoxLayout()
        buyButton = QtWidgets.QPushButton("BUY")
        BuySell.addWidget(buyButton)
        sellButton = QtWidgets.QPushButton("SELL")
        BuySell.addWidget(sellButton)

        buyButton.clicked.connect(lambda : addOrderHistoryBuy())


        leftArea.addLayout(BuySell)

        labelPIC = QtWidgets.QLabel()
        labelPIC.setPixmap(QPixmap("1.JPG").scaled(590, 390))

        leftArea.addWidget(labelPIC)

        Mainlayout = QHBoxLayout(self)
        Mainlayout.addLayout(leftArea)
        Mainlayout.addLayout(rightArea)
        self.show()

        def addOrderHistoryBuy():
            from random import randrange
            productsTest = ["Bitcoin", "Hsecoin", "Nuggets", "Jypyter Task"]
            t = ["Limit", "FOK"]
            order_type = t[randrange(0,2)]
            product = productsTest[randrange(0,4)]
            amount = str(randrange(0,100))
            price = str(randrange(0,100)) +"$"
            sign = func.buyOrder(order_type,product,amount,price)
            newOrder = QtWidgets.QPushButton()
            newOrder.setStyleSheet("""QPushButton { text-align: left; 
            background-color: rgb(176, 224, 230);};
            """)
            newOrder.setText(sign)
            formLayout1.addWidget(newOrder)
            func.addToHis("Buy", order_type, product,amount, price)






App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())