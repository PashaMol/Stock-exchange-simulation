
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import plotly.express as px
import numpy as np
import data
from matplotlib import dates, ticker
import matplotlib as mpl
from mpl_finance import candlestick_ohlc, candlestick2_ochl
import functions as func

import data
import random
import mplcursors
from numpy import quantile
from time import time, strftime
#import bigGraph
from PyQt5 import QtWidgets
possibilities = [u'seaborn-darkgrid', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh', u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test', u'seaborn-colorblind', u'seaborn-deep', u'seaborn-whitegrid', u'seaborn-bright', u'seaborn-poster', u'seaborn-muted', u'seaborn-paper', u'seaborn-white', u'seaborn-pastel', u'seaborn-dark', u'seaborn', u'seaborn-dark-palette']

cols = ["purple", "lime", "magenta", "red", "blue", "orange"]
test_titles = ["Bitcoin", "Hsecoin", "Hsecoin", "Jupyter Task"]


#
import matplotlib.pyplot as plt
# from warnings import simplefilter
# simplefilter("ignore")
#
#print(plt.style.available)
plt.style.use("tableau-colorblind10")

xUP = []
yUP = []
xLOW = []
yLOW = []

def show_annotationUP(sel):
    xi, yi = sel.target
    xi = int(round(xi))
    sel.annotation.set_text(f'{data.xUP[xi]}\nvalue: {yi:.3f}')

def show_annotationDOWN(sel):
    xi, yi = sel.target
    xi = int(round(xi))
    sel.annotation.set_text(f'{data.xDOWN[xi]}\nvalue: {yi:.3f}')


def closeALL():
    plt.close("all")

#


def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

# def onclick1(event):
#     data.bg1 = xUP
#     data.bg2 = yUP
#     data.col = "green"
#     Dialog = QtWidgets.QDialog()
#     ui = bigGraph.GraphWindow()
#     ui.setupUi(Dialog)
#     Dialog.exec_()
#
# def onclick2(event):
#     data.bg1 = xLOW
#     data.bg2 = yLOW
#     data.col = "red"
#     Dialog = QtWidgets.QDialog()
#     ui = bigGraph.GraphWindow()
#     ui.setupUi(Dialog)
#     Dialog.exec_()


def enter_figure(event):
   # print('enter_figure', event.canvas.figure)


    if data.mode != "Dark":
        event.canvas.figure.patch.set_facecolor('#CACACA')
    else:
        event.canvas.figure.patch.set_facecolor('#41002E')
    event.canvas.draw()

def leave_figure(event):
    #print('leave_figure', event.canvas.figure)
    if data.mode != "Dark":
        event.canvas.figure.patch.set_facecolor('#BFBFBF')
    else:
        event.canvas.figure.patch.set_facecolor('#000000')
    event.canvas.draw()


#####################################################


# self.figure.patch.set_facecolor('#BFBFBF')
# self.figure.patch.set_facecolor('#000000')

##############################



class CanvasUp(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=50):
        if data.mode == "Dark":
            plt.style.use('dark_background')
        else:
            plt.style.use('classic')

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.fig.tight_layout()
        self.plot()


    def upd(self):
        if data.mode == "Dark":
            plt.style.use('dark_background')
        else:
            plt.style.use('classic')

        if data.mode != "Dark":
            self.figure.patch.set_facecolor('#BFBFBF')
        else:
            self.figure.patch.set_facecolor('#000000')

        self.clear()
        self.reloading()

    def clicked(self, event):
        print("THIS BRO WAS CLICKED1")





    def plot_joint(self):


        try:
            if len(data.graphsData) * len(data.graphsData_1)!= 0:
                XY = func.getXY(data.graphsData)
                XY1 = func.getXY(data.graphsData_1)
                x1 = XY[0]
                y1 = XY[1]
                x2 = XY1[0]                                                          #TODO FINISH IT
                y2 = XY1[1]
                m = min(len(x1), len(y1), len(y2))
                #print(m)
                x1 = x1[:m]
                y1 = y1[:m]
                y2 = y2[:m]
                #y1,y2 =[], []
                # for i in range(min(len(x1), len(x2))):


            else:
                print("NOTHING TO PLOT")

            data.xDOWN = x1

            self.figure.tight_layout()
            #
            # self.figure.canvas.mpl_connect('figure_enter_event', enter_figure)
            # self.figure.canvas.mpl_connect('figure_leave_event', leave_figure)
            #self.figure.canvas.mpl_connect('button_press_event', onclick)

            ax = self.figure.add_subplot(111)
            ax.set_ylim([0, max(max(y1), max(y2)) * 1.15])

            self.figure.text(0.5, 0.5, f'{data.graphsData_1[0][0]}', transform=ax.transAxes,
                             fontsize=40, color='gray', alpha=0.5,
                             ha='center', va='center')

            c1 = "lime"
            c2 = "red"

            if data.mode == "Dark":
                print("switched dark")
                c1 = lighten_color("lime",0.7)
                c2 = lighten_color("red",0.9)


            ax.fill_between(x1, y1=y1, y2=0, alpha=0.7, color= c1, linewidth=2)
            ax.fill_between(x1, y1=y2, y2=0,alpha=0.7, color= c2, linewidth=2)
            if len(x1) > 10:
                ax.set_xticks(ax.get_xticks()[::len(x1) // 20])
                self.figure.autofmt_xdate()
            # dt1 = ax.plot(x1, y1, color="lime")
            # dt2 = ax.plot(x1, y2, color="red")
            # cursor = mplcursors.cursor([dt1, dt2],  hover=True)
            # cursor.connect('add', show_annotationDOWN)
            ax.grid()
            #mplcursors.cursor(ax, hover=True)
            self.draw_idle()
        except: pass


    def no_data(self):
        ax = self.figure.add_subplot(111)

        self.figure.text(0.5, 0.5, 'NO DATA', transform=ax.transAxes,
                         fontsize=40, color='gray', alpha=0.5,
                         ha='center', va='center')

        ax.plot(0, 0, color="red")
        self.draw_idle()


    def reloading(self):
        ax = self.figure.add_subplot(111)

        self.figure.text(0.5, 0.5, 'LOADING', transform=ax.transAxes,
                         fontsize=40, color='gray', alpha=0.5,
                         ha='center', va='center')

        ax.plot(0, 0, color="red")
        self.draw_idle()


    def clear(self):
        self.fig.clf()


    def plot(self):


        try:
            if len(data.graphsData)!=0:
                XY = func.getXY(data.graphsData)
                x1 = XY[0]
                y1 = XY[1]

                # global xUP, yUP
                # xUP, yUP = x1, y1
                # for i in range(len(x1)):
                #     x1[i] = func.getTime(x1[i])

                # print("X:")
                # print(x1)
                # print("Y:")
                # print(y1)
               # print(data.graphsData)
                #print()
                lab = "    " + str(data.graphsData[0][0] + "    " + data.graphsData[0][-1])
            else:
                lab = ""
               # x1   = np.arange(0.0, 2.0, 0.21)
                ran_floats = np.random.rand(10) * (7.3 - 0.5) + 0.5
                #y1 = (1 + np.sin(2 * np.pi * ran_floats))

            data.xUP = x1

            self.figure.tight_layout()

            # self.figure.canvas.mpl_connect('figure_enter_event', enter_figure)
            # self.figure.canvas.mpl_connect('figure_leave_event', leave_figure)
            #self.figure.canvas.mpl_connect('button_press_event', onclick1)
            self.figure.canvas.mpl_connect('button_press_event', self.clicked)

            ax = self.figure.add_subplot(111)
            ax.set_ylim([0, max(y1)*1.15])


            self.figure.text(0.5, 0.5, f'{data.graphsData[0][0]}', transform=ax.transAxes,
                             fontsize=40, color='gray', alpha=0.5,
                             ha='center', va='center')
            ax.fill_between(x1, y1=y1, label='psavert', alpha=0.5, color='tab:green', linewidth=2)
            if len(x1)>10:
                ax.set_xticks(ax.get_xticks()[::len(x1)//20])
                self.figure.autofmt_xdate()
            dt = ax.plot(x1, y1, color= cols[random.randrange(0, len(cols))])
            ax.set_title(lab, loc='left')
            cursor = mplcursors.cursor(dt, hover=True)
            cursor.connect('add', show_annotationUP)
            ax.grid()
            self.draw_idle()

        except:
            ax = self.figure.add_subplot(111)

            self.figure.text(0.5, 0.5, 'NO DATA', transform=ax.transAxes,
                             fontsize=40, color='gray', alpha=0.5,
                             ha='center', va='center')

            ax.plot(0, 2, color=cols[random.randrange(0, len(cols))])
            ax.set_title("", loc='left')

            print("Bad graphs")



class CanvasLow(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=50):
        if data.mode == "Dark":
            plt.style.use('dark_background')
        else:
            plt.style.use('classic')

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.fig.tight_layout()
        self.plot()

    def upd(self):
        if data.mode == "Dark":
            plt.style.use('dark_background')
        else:
            plt.style.use('classic')

        if data.mode != "Dark":
            self.figure.patch.set_facecolor('#BFBFBF')
        else:
            self.figure.patch.set_facecolor('#000000')

        self.clear()
        self.reloading()

    def clicked(self, event):
        print("THIS BRO WAS CLICKED")


    def candels(self):
        # data1 = [('2017-01-02 02:00:00', '1.05155', '1.05197', '1.05155', '1.0519'),
        #         ('2017-01-02 02:01:00', '1.05209', '1.05209', '1.05177', '1.05179'),
        #         ('2017-01-02 02:02:00', '1.05177', '1.05198', '1.05177', '1.05178'),
        #         ('2017-01-02 02:03:00', '1.05188', '1.052', '1.05188', '1.052'),
        #         ('2017-01-02 02:04:00', '1.05196', '1.05204', '1.05196', '1.05203'),
        #         ('2017-01-02 02:06:00', '1.05196', '1.05204', '1.05196', '1.05204'),
        #         ('2017-01-02 02:07:00', '1.05205', '1.0521', '1.05205', '1.05209'),
        #         ('2017-01-02 02:08:00', '1.0521', '1.0521', '1.05209', '1.05209'),
        #         ('2017-01-02 02:09:00', '1.05208', '1.05209', '1.05208', '1.05209'),
        #         ('2017-01-02 02:10:00', '1.05208', '1.05211', '1.05207', '1.05209'),
        #         ('2017-01-02 02:11:00', '1.05196', '1.05204', '1.05196', '1.05204'),
        #         ('2017-01-02 02:12:00', '1.05205', '1.0521', '1.05205', '1.05209'),
        #         ('2017-01-02 02:13:00', '1.0521', '1.0521', '1.05209', '1.05209'),
        #         ('2017-01-02 02:14:00', '1.05208', '1.05209', '1.05208', '1.05209'),
        #         ('2017-01-02 02:15:00', '1.05208', '1.05211', '1.05207', '1.05209')]
        # data0 = data.bx
        # print("HERE WEGOAGAIN", data0)
        # q0 = min(data0)
        # q1 = quantile(data0, 0.25)
        # q2 = quantile(data0, 0.5)
        # q3 = quantile(data0, 0.75)
        # q4 = max(data0)
        #
        #
        # print("THIS GUY GOES YES1",data.bx1)
        # tm = str(strftime("%H:%M:%S"))
        # print(tm)
        # data.bx1.append((  tm,str(q0),str(q1),str(q3),str(q4)))
        # print("THIS GUY GOES YES2",data.bx1)
        #
        #
        # opens_ = []
        # closes_ = []
        # lows_ = []
        # highs_ = []
        #
        # ohlc_data = []
        #
        # for line in data.bx1:
        #     ohlc_data.append((dates.datestr2num(line[0]), np.float64(line[2]), np.float64(line[1]), np.float64(line[4]),
        #                       np.float64(line[3])))
        #
        #     ##
        #     opens_.append(np.float64(line[1]))
        #     closes_.append(np.float64(line[2]))
        #     lows_.append(np.float64(line[3]))
        #     highs_.append(np.float64(line[4]))
        #
        # self.figure.tight_layout()
        #
        # # self.figure.canvas.mpl_connect('button_press_event', self.clicked)
        # # self.figure.canvas.mpl_connect('figure_leave_event', leave_figure)
        #
        # ax1 = self.figure.add_subplot(111)
        # ax1.set_ylim([q0*0.9, q4 * 1.15])
        # ax1.xaxis_date()
        # print("something wrong. i can feel it")
        # print(ohlc_data)
        # candlestick_ohlc(ax1, ohlc_data, width=len(data.bx1)+10, colorup=cols[random.randint(0, len(cols)-1)], colordown='red', alpha=0.65) #TODO FINISH CANDELS
        # #candlestick2_ochl(ax1, opens=opens_, closes=closes_, lows=lows_, highs=highs_)
        # ax1.grid()
        # self.figure.autofmt_xdate()
        # ax1.xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y %H:%M'))
        # ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
        #
        #
        #
        # ax1.plot()
        # self.draw_idle()
        #
        # # plt.xticks(rotation=30)
        # # plt.grid()
        # # plt.xlabel('Date')
        # # plt.ylabel('Price')
        # # plt.title('Historical Data EURUSD')
        # # plt.tight_layout()
        # # plt.show()

        dark = True

        # data = [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0,
        #         135.0, 135.0, 135.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0,
        #         136.0, 160.67, 160.67, 160.67, 160.67, 160.67, 162.74, 162.74, 162.74, 162.74, 162.74, 165.82, 165.82,
        #         166.48, 166.48, 174.09, 174.09, 174.09, 174.09, 175.0, 175.0, 218.51, 218.51, 218.51, 218.51, 225.07,
        #         241.31]
        #
        # data2 = [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0,
        #          135.0, 135.0, 135.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 136.0, 47, 19, 20, 136.0, 160.67,
        #          160.67, 160.67, 160.67, 160.67, 162.74, 162.74, 162.74, 162.74, 162.74, 165.82, 165.82, 166.48, 166.48,
        #          174.09, 174.09, 174.09, 174.09, 175.0, 175.0, 218.51, 254, 29, 30, 225.07, 241.31]

        mpl.use('agg')
        mpl.rcParams['boxplot.whiskerprops.linestyle'] = '-'

       # label_size = 8
        #mpl.rcParams['xtick.labelsize'] = label_size

        ax1 = self.figure.add_subplot(111)

        c2 = "red"
        c = 'green'
        #print("_________________")
        # to_build = []
        # to_build1 = []
        # labelList = []
        # for i in range(len(data.bx)):
        #     if i%2==0:
        #         to_build.append(data.bx[i])
        #     else:
        #         to_build.append([])
        # for i in range(len(data.bx1)):
        #     if i % 2 == 0:
        #         to_build1.append(data.bx1[i])
        #     else:
        #         to_build1.append([])
        # for i in range(len(data.bx_lab)):
        #     if i % 2 == 0:
        #         labelList.append(func.sec_to_time(data.bx_lab[i]))
        #     else:
        #         labelList.append("")

        to_build = [List for List in data.bx]
        to_build1 = [List for List in data.bx1]

      # print(to_build)
       # print("^^^^^^^^^^")
        c1 = [0, 1, 0, 0.69]
        c2 = [1, 0 ,0 , 0.69]
        labelList = [func.sec_to_time(sec) for sec in data.bx_lab]
        labelList_emp = [" "]*len(labelList)
        #print(labelList)
        #print("HERE____GG", data.bx_lab)
        print(":: ", len(to_build), len(labelList))
        s = time()
        box1 = ax1.boxplot(to_build, positions= np.arange(len(to_build))-0.2 ,  labels=labelList_emp, notch=False, patch_artist=True,
                           widths=0.3, medianprops=dict(color='white'),
                           boxprops=dict(facecolor=c1, color=c1),
                           capprops=dict(color=c1),
                           whiskerprops=dict(color=c1),
                           flierprops=dict(color=c1, markeredgecolor=c1),
                           )

        box2 = ax1.boxplot(to_build1, positions= np.arange(len(to_build1))+0.2, labels=labelList, notch=False, patch_artist=True,
                           widths=0.3, medianprops=dict(color='white'),
                           boxprops=dict(facecolor=c2, color=c2),
                           capprops=dict(color=c2),
                           whiskerprops=dict(color=c2),
                           flierprops=dict(color=c2, markeredgecolor=c2)
                           )

        #mplcursors.cursor(ax1, hover=True)
        self.figure.autofmt_xdate()
        #self.figure.tight_layout()

        ax1.plot()

        self.draw_idle()
        print("gui go brrr", time() - s )


    def no_data(self):
        ax = self.figure.add_subplot(111)

        self.figure.text(0.5, 0.5, 'NO DATA', transform=ax.transAxes,
                         fontsize=40, color='gray', alpha=0.5,
                         ha='center', va='center')

        ax.plot(0, 0, color="red")
        self.draw_idle()


    def reloading(self):
        ax = self.figure.add_subplot(111)

        self.figure.text(0.5, 0.5, 'LOADING', transform=ax.transAxes,
                         fontsize=40, color='gray', alpha=0.5,
                         ha='center', va='center')

        ax.plot(0, 0, color="red")
        self.draw_idle()


    def clear(self):
        self.fig.clf()


    def plot(self):


        try:
            if len(data.graphsData_1)!=0:
                XY = func.getXY(data.graphsData_1)
                x1 = XY[0]
                y1 = XY[1]

                # global xUP, yUP
                # xUP, yUP = x1, y1
                # for i in range(len(x1)):
                #     x1[i] = func.getTime(x1[i])

                # print("X:")
                # print(x1)
                # print("Y:")
                # print(y1)
               # print(data.graphsData)
                #print()
                lab = "    " + str(data.graphsData_1[0][0] + "    " + data.graphsData_1[0][-1])
            else:
                lab = ""
               # x1   = np.arange(0.0, 2.0, 0.21)
                ran_floats = np.random.rand(10) * (7.3 - 0.5) + 0.5
                #y1 = (1 + np.sin(2 * np.pi * ran_floats))

            data.xUP = x1

            self.figure.tight_layout()

            # self.figure.canvas.mpl_connect('figure_enter_event', enter_figure)
            # self.figure.canvas.mpl_connect('figure_leave_event', leave_figure)
            #self.figure.canvas.mpl_connect('button_press_event', onclick1)
            self.figure.canvas.mpl_connect('button_press_event', self.clicked)

            ax = self.figure.add_subplot(111)
            ax.set_ylim([0, max(y1)*1.15])


            self.figure.text(0.5, 0.5, f'{data.graphsData_1[0][0]}', transform=ax.transAxes,
                             fontsize=40, color='gray', alpha=0.5,
                             ha='center', va='center')
            ax.fill_between(x1, y1=y1, label='psavert', alpha=0.5, color='tab:red', linewidth=2)
            if len(x1)>10:
                ax.set_xticks(ax.get_xticks()[::len(x1)//20])
                self.figure.autofmt_xdate()
            dt = ax.plot(x1, y1, color= cols[random.randrange(0, len(cols))])
            ax.set_title(lab, loc='left')
            cursor = mplcursors.cursor(dt, hover=True)
            cursor.connect('add', show_annotationUP)
            ax.grid()
            self.draw_idle()

        except:
            ax = self.figure.add_subplot(111)

            self.figure.text(0.5, 0.5, 'NO DATA', transform=ax.transAxes,
                             fontsize=40, color='gray', alpha=0.5,
                             ha='center', va='center')

            ax.plot(0, 2, color=cols[random.randrange(0, len(cols))])
            ax.set_title("", loc='left')

            print("Bad graphs2")

########################

# class CanvasJOINT(FigureCanvas):
#     def __init__(self, parent=None, width=5, height=5, dpi=50):
#         if data.mode == "Dark":
#             plt.style.use('dark_background')
#         else:
#             plt.style.use('classic')
#
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#         self.plot()
#
#
#
#     def plot(self):
#
#         try:
#             if len(data.graphsData) * len(data.graphsData_1)!= 0:
#                 XY = func.getXY(data.graphsData)
#                 XY1 = func.getXY(data.graphsData_1)
#                 x1 = XY[0]
#                 y1 = XY[1]
#                 x2 = XY1[0]
#                 y2 = XY1[1]
#                 m = min(len(x1), len(y1), len(y2))
#                 #print(m)
#                 x1 = x1[:m]
#                 y1 = y1[:m]
#                 y2 = y2[:m]
#                 #y1,y2 =[], []
#                 # for i in range(min(len(x1), len(x2))):
#
#
#             else:
#                 print("NOTHING TO PLOT")
#
#             data.xDOWN = x1
#
#             self.figure.tight_layout()
#
#             self.figure.canvas.mpl_connect('figure_enter_event', enter_figure)
#             self.figure.canvas.mpl_connect('figure_leave_event', leave_figure)
#             #self.figure.canvas.mpl_connect('button_press_event', onclick)
#
#             ax = self.figure.add_subplot(111)
#             ax.set_ylim([0, max(max(y1), max(y2)) * 1.15])
#
#             self.figure.text(0.5, 0.5, f'{data.graphsData_1[0][0]}', transform=ax.transAxes,
#                              fontsize=40, color='gray', alpha=0.5,
#                              ha='center', va='center')
#
#             ax.fill_between(x1, y1=y1, y2=0, alpha=0.5, color="green", linewidth=2)
#             ax.fill_between(x1, y1=y2, y2=0,alpha=0.5, color="red", linewidth=2)
#             if len(x1) > 30:
#                 ax.set_xticks(ax.get_xticks()[::len(x1) // 20])
#                 self.figure.autofmt_xdate()
#             #dt = ax.plot(x1, y1, color=cols[random.randrange(0, len(cols))])
#             cursor = mplcursors.cursor(hover=True)
#             cursor.connect('add', show_annotationDOWN)
#             ax.grid()
#
#
#
#         except:
#             ax = self.figure.add_subplot(111)
#
#             self.figure.text(0.5, 0.5, 'NO JOINT DATA', transform=ax.transAxes,
#         fontsize=40, color='gray', alpha=0.5,
#         ha='center', va='center')
#
#             ax.plot(0, 0, color=cols[random.randrange(0, len(cols))])
#             ax.set_title("", loc='left')
#             print("Bad graphs2")





class Candlestick(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=50):
        if data.mode == "Dark":
            plt.style.use('dark_background')
        else:
            plt.style.use('classic')

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()



    def plot(self):

        try:
            if len(data.box1)!= 0:
                pass


            else:
                print("NOTHING TO PLOT")

            self.figure = px.box(data.box1, x="day", y="total_bill", color="smoker")
            self.figure.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
            self.figure.show()




        except:
        #     ax = self.figure.add_subplot(111)
        #
        #     self.figure.text(0.5, 0.5, 'NO BOX DATA', transform=ax.transAxes,
        # fontsize=40, color='gray', alpha=0.5,
        # ha='center', va='center')
        #
        #     ax.plot(0, 0, color=cols[random.randrange(0, len(cols))])
        #     ax.set_title("", loc='left')
           print("Bad BOXES")





