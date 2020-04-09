
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QTabWidget
import sys
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

def show_annotation(sel):
    xi, yi = sel.target
    xi = int(round(xi))
    sel.annotation.set_text(f'{x[xi]}\nvalue:{yi:.3f}')




class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=120):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()


    def plot(self):

            self.figure.tight_layout()
            self.figure.autofmt_xdate()
            #mplcursors.Cursor()

            ax = self.figure.add_subplot(111)
            x = ['22-02 11:16:15', '22-02 15:31:54', '22-02 15:32:30',
                 '22-02 15:32:45', '22-02 15:33:57', '22-02 15:34:13',
                 '22-02 15:34:46']
            y = [1, 4, 3, 4, 8, 9, 2]

            dt = ax.plot(x, y)
            cursor = mplcursors.cursor(dt, hover = True)
            cursor.connect('add', show_annotation)

            self.figure.tight_layout()



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.top = 255
        self.left = 150
        self.setGeometry(self.left, self.top, 900, 900)
        self.Mainlayout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.graphUP = QWidget()
        self.graphUP.layout = QVBoxLayout( self.graphUP)
        self.graphUP.layout.addWidget(Canvas())
        self.tabs.setFixedHeight(800)
        self.tabs.setFixedWidth(800)
        self.tabs.addTab(self.graphUP, "Graph1")
        self.Mainlayout.addWidget(self.tabs)
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
