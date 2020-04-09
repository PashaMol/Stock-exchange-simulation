#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton
# from PyQt5.QtWidgets import QApplication,QGridLayout, QWidget, QTabWidget,QScrollArea, QVBoxLayout,QHBoxLayout,QCheckBox, QGroupBox, QLabel, QPushButton, QFormLayout, QCheckBox,QComboBox
#
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QSize
#
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import random
# import data
# import mplcursors
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#
# cols = ["purple", "lime", "magenta", "red", "blue", "orange"]
#
#
#
#
# def show_annotation(sel):
#     xi, yi = sel.target
#     xi = int(round(xi))
#     sel.annotation.set_text(f'{data.bg1[xi]}\nvalue: {yi:.3f}')
#
#
#
# class GraphWindow(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.setWindowIcon(QtGui.QIcon('bgicon.ico'))
#         Dialog.resize(data.reso[0], data.reso[1])
#         mainWin = QVBoxLayout(Dialog)
#
#         plot = WidgetPlot()
#
#         mainWin.addWidget(plot)
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "GRAPH"))
#
# class WidgetPlot(QWidget):
#     def __init__(self, *args, **kwargs):
#         try:
#             QWidget.__init__(self, *args, **kwargs)
#             self.setLayout(QVBoxLayout())
#             self.canvas = PlotCanvas(self, width=10, height=8)
#             self.toolbar = NavigationToolbar(self.canvas, self)
#             self.layout().addWidget(self.toolbar)
#             self.layout().addWidget(self.canvas)
#         except:
#             pass
#
# class PlotCanvas(FigureCanvas):
#     try:
#         def __init__(self, parent=None, width=10, height=8, dpi=100):
#             fig = Figure(figsize=(width, height), dpi=dpi)
#             FigureCanvas.__init__(self, fig)
#             self.setParent(parent)
#             FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
#             FigureCanvas.updateGeometry(self)
#             self.plot()
#
#         def plot(self):
#             #x = ['11:16:15 22-02', '15:31:54 22-02', '15:32:30 22-02', '15:32:45 22-02', '15:33:57 22-02', '15:34:13 22-02', '15:34:46 22-02', '15:34:53 22-02', '15:42:59 22-02', '15:43:08 22-02', '15:56:10 22-02', '15:56:18 22-02', '15:56:36 22-02', '15:56:43 22-02', '08:59:05 23-02', '08:59:35 23-02', '09:05:16 23-02', '09:05:22 23-02', '09:28:40 23-02', '09:28:57 23-02', '09:31:57 23-02', '09:32:04 23-02', '09:32:41 23-02', '10:11:21 23-02', '10:11:30 23-02', '10:15:01 23-02', '10:15:31 23-02', '10:15:31 23-02', '10:15:49 23-02', '10:30:28 23-02', '10:30:50 23-02', '10:31:09 23-02', '10:31:21 23-02', '10:53:02 23-02', '10:53:09 23-02', '10:53:14 23-02', '11:50:25 23-02', '11:50:25 23-02', '11:51:06 23-02', '10:33:48 24-02', '10:33:49 24-02', '10:33:50 24-02', '10:33:50 24-02', '10:33:51 24-02', '11:16:30 24-02', '11:16:48 24-02', '11:17:00 24-02', '14:10:08 24-02', '14:10:24 24-02', '12:39:10 25-02', '12:40:11 25-02', '12:41:52 25-02', '12:45:33 25-02', '12:45:35 25-02', '12:45:35 25-02', '12:45:36 25-02', '12:45:42 25-02', '12:46:14 25-02', '12:51:45 25-02', '12:53:22 25-02', '12:53:30 25-02', '12:53:57 25-02', '12:54:01 25-02', '12:54:18 25-02', '13:02:21 25-02', '13:02:25 25-02', '13:02:31 25-02', '13:05:51 25-02', '13:06:01 25-02']
#             #y = [1.0, 1.0, 3.0, 4.0, 5.0, 3.0, 2.3333333333333335, 4.0, 3.0, 5.0, 3.6666666666666665, 6.0, 4.333333333333333, 7.0, 1.0, 2.0, 3.0, 4.0, 6.0, 4.5, 3.3333333333333335, 3.0, 5.0, 4.0, 5.4, 4.666666666666667, 4.142857142857143, 3.75, 3.4444444444444446, 3.2, 2.9545454545454546, 2.708341666666667, 79.42308461538461, 1.0, 0.75, 1.0, 0.75, 2.5, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9285714285714286, 1.0, 0.9166666666666666, 1.3, 1.0, 2.0, 5.0, 3.0, 2.3333333333333335, 2.0, 1.8, 2.5, 3.6666666666666665, 6.0, 13.0, 7.0, 5.0, 8.0, 5.666666666666667, 1.0, 2.5, 4.0, 1.0, 2.0]
#             x =data.bg1
#             y =data.bg2
#
#             ax = self.figure.add_subplot(111)
#             ax.fill_between(x, y1=y, label='psavert', alpha=0.5, color=data.col, linewidth=2)
#             ax.set_ylim([0, max(y) * 1.15])
#             self.figure.tight_layout()
#             dt = ax.plot(x,y, linewidth=1, color = cols[random.randint(0, len(cols)-1)])
#             if len(x) > 30:
#                 ax.set_xticks(ax.get_xticks()[::len(x) // 20])
#                 self.figure.autofmt_xdate()
#             cursor = mplcursors.cursor(dt, hover=True)
#             cursor.connect('add', show_annotation)
#             ax.grid()
#
#
#             self.draw()
#
#     except:
#         pass
