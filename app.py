import sys

from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
import os

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.filename = ''
        self.mdiArea1 = QmdiArea1Area()
        self.mdiArea2 = QmdiArea1Area()

        self.widget1 = QWidget(self)
        self.layout1 = QHBoxLayout(self.widget1)

        self.widget2 = QWidget(self)
        self.layout2 = QHBoxLayout(self.widget2)


        self.ScatterButton = QPushButton('Plot scatter point', self.mdiArea1)
        self.ScatterButton.resize(250, 50)
        self.ScatterButton.move(50, 50)
        self.ScatterButton.clicked.connect(self.ScatterPlotFn)

        self.ScatterSmoothButton = QPushButton('Plot scatter point with smooth lines',self.mdiArea1)
        self.ScatterSmoothButton.resize(250, 50)
        self.ScatterSmoothButton.move(300, 50)
        self.ScatterSmoothButton.clicked.connect(self.SmoothScatterPlotFn)

        self.LinesButton = QPushButton('Plot lines', self.mdiArea1)
        self.LinesButton.resize(250, 50)
        self.LinesButton.move(550, 50)
        self.LinesButton.clicked.connect(self.SmoothLinePlotFn)

        self.model = QStandardItemModel(self)
        self.tableView = QTableView(self.mdiArea2)
        self.tableView.setModel(self.model)

        self.tableView.clicked.connect(self.cell_was_clicked)

        self.layout1.addWidget(self.ScatterButton)
        self.layout1.addWidget(self.ScatterSmoothButton)
        self.layout1.addWidget(self.LinesButton)

        self.layout2.addWidget(self.tableView)

        self.central_widget = QWidget(self)
        self.VerticalLayout = QVBoxLayout(self.central_widget)
        self.VerticalLayout.addWidget(self.widget1)
        self.VerticalLayout.addWidget(self.widget2)

        self.setCentralWidget(self.central_widget)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.rows = []
        self.win = QmdiArea1SubWindow()
        self.MiddleWidget = QWidget()
        self.layout2 = QVBoxLayout(self.MiddleWidget)
        self.layout2.addWidget(self.toolbar)
        self.layout2.addWidget(self.canvas)

        self.win.setWidget(self.MiddleWidget)

        self.MenuBar = self.menuBar()
        self.FileMenu = self.MenuBar.addMenu("self.FileMenu")
        self.FileMenu.addAction("Load")
        self.EditMenu = self.MenuBar.addMenu("self.EditMenu")
        self.EditMenu.addAction("self.EditMenu data")
        self.FileMenu.addAction("Add data")
        self.FileMenu.addAction("Save")
        self.FileMenu.addAction("Save as PNG")
        self.setWindowTitle("Main Window")
        self.FileMenu.triggered[QAction].connect(self.windowaction)


    def cell_was_clicked(self,index):
        self.rows = []
        for i in range(1,self.model.rowCount()):
            self.rows.append(float(index.sibling(i,index.column()).data()))
        print(self.rows)

    def ScatterPlotFn(self):
        self.win.setWindowTitle('Scatter Plot')
        ax = self.figure.add_subplot(111)
        ax.clear()
        x = [int(x) for x in range(len(self.rows))]
        y = self.rows
        ax.plot(x,y,'ro')
        ax.set_title('Scatter Plot')
        self.canvas.draw()
        self.win.show()

    def SmoothScatterPlotFn(self):
        self.win.setWindowTitle('Scatter Plot with Smooth Line')
        ax = self.figure.add_subplot(111)
        ax.clear()
        x = [int(x) for x in range(len(self.rows))]
        y = self.rows
        ax.plot(x, y,'-o')
        ax.set_title('Scatter Plot with Smooth Line')
        self.canvas.draw()
        self.win.show()

    def SmoothLinePlotFn(self):
        self.win.setWindowTitle('Smooth Line Plot')
        ax = self.figure.add_subplot(111)
        ax.clear()
        x = [int(x) for x in range(len(self.rows))]
        y = self.rows
        ax.plot(x, y)
        ax.set_title('Smooth Line Plot')
        self.canvas.draw()
        self.win.show()


    def writeCsv(self, fileName):
        with open(fileName, "w",newline='') as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber,columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                print(fields)
                writer.writerow(fields)

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def windowaction(self, q):
        if q.text() == "Load":
            filename = QFileDialog.getOpenFileName(self, 'Open self.FileMenu',os.getcwd(), "CSV files (*.csv)")
            print(filename)
            self.filename = filename
            self.loadCsv(self.filename)
            data = pandas.read_csv(self.filename)
        elif q.text() == "self.EditMenu data":
            self.filename = filename
            self.writeCsv(self.filename)
        elif q.text() == "Add data":
            self.model.appendRow([])
        elif q.text() == "Save":
            self.writeCsv(self.filename)
        elif q.text()=="Save as PNG":
            self.take_screenshot()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


main()