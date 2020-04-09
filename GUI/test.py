from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QPushButton,QTabWidget, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
from numpy import quantile
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_finance import candlestick_ohlc, candlestick2_ochl
x1 =[]
y1 = []
colors = ["purple", "lime", "magenta", "red", "blue", "orange"]

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=50):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.candels()

    def clear(self):
        self.fig.clf()

    def candels(self):
        data0 = [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26, 0.26]
        q0 = min(data0)
        q1 = quantile(data0, 0.25)
        q2 = quantile(data0, 0.5)
        q3 = quantile(data0, 0.75)
        q4 = max(data0)
        bx1 = []
        bx1.append((str(q0),str(q1),str(q2),str(q3),str(q4)))
        ohlc_data = []
        for line in bx1:
            ohlc_data.append( (np.float64(line[1]), np.float64(line[2]), np.float64(line[3]),
                              np.float64(line[4])))
        self.figure.tight_layout()


        ax1 = self.figure.add_subplot(111)
        #candlestick_ohlc(ax1, ohlc_data, colorup=cols[random.randint(0, len(cols)-1)], colordown='red', alpha=0.65) #TODO FINISH CANDELS
        ax1.grid()
        self.figure.autofmt_xdate()

        ax1.plot()
        self.draw_idle()


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(7, 55,600, 600)
        graphsArea = QVBoxLayout(self)
        bbb = QPushButton("UPDATE GRAPHS")
        bbb.clicked.connect(lambda : self.testf())
        graphsArea.addWidget(bbb)
        self.graph1 = Canvas()
        self.tabs = QTabWidget()
        self.graph = QWidget()
        self.graph.layout = QVBoxLayout( self.graph)
        self.graph.layout.addWidget(self.graph1)
        self.tabs.addTab(self.graph, "Graph1")
        graphsArea.addWidget(self.tabs)
        self.show()
        self.testf()
    def testf(self):
        self.graph1.clear()
        self.graph1.candels()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = MainWindow()
    sys.exit(App.exec())
