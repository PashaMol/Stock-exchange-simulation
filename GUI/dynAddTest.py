import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)



class ExampleWidget(QGroupBox):
    def __init__(self, numAddWidget):
        QGroupBox.__init__(self)
        self.numAddWidget = numAddWidget
        self.numAddItem   = 1
        self.setTitle("Title {}".format(self.numAddWidget))
        self.initSubject()
        self.organize()

    def initSubject(self):
        self.lblName = QLabel("Label Title {}".format(self.numAddWidget), self)
        self.lblSelectItem = QLabel(self)



    def organize(self):
        grid = QGridLayout(self)
        self.setLayout(grid)
        grid.addWidget(self.lblName,        0, 0, 1, 3)
        grid.addWidget(self.lblSelectItem,  1, 0, 1, 2)
        #grid.addWidget(self.teachersselect, 1, 2)
        #grid.addWidget(self.addbtn,         3, 2)




class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.numAddWidget = 1
        self.initUi()

    def initUi(self):
        self.layoutV = QVBoxLayout(self)

        self.area = QScrollArea(self)
        self.area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 200, 100)

        self.layoutH = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        self.layoutH.addLayout(self.gridLayout)

        self.area.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QPushButton("Add Widget")
        self.layoutV.addWidget(self.area)
        self.layoutV.addWidget(self.add_button)
        self.add_button.clicked.connect(self.addWidget)

        self.widget = ExampleWidget(self.numAddWidget)
        self.gridLayout.addWidget(self.widget)
        self.setGeometry(700, 200, 350, 300)

    def addWidget(self):
        self.numAddWidget += 1
        self.widget = ExampleWidget(self.numAddWidget)
        self.gridLayout.addWidget(self.widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())