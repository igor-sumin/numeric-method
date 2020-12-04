from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, QSizePolicy, 
	QVBoxLayout, QTableView, QTableWidgetItem, QTableWidget, QHeaderView
)

from matplotlib.figure import Figure 
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

# График приложения
class MyGraph(QWidget): 
	def __init__(self, parent=None): 
		QWidget.__init__(self, parent)

		self.canvas = FigureCanvas(Figure()) 
		self.toolbar = NavigationToolbar2QT(self.canvas, parent)

		self.vertical_layout = QVBoxLayout()
		self.vertical_layout.addWidget(self.canvas)
		self.vertical_layout.addWidget(self.toolbar) 
		
		self.canvas.axes = self.canvas.figure.add_subplot(111)
		self.canvas.axes1 = self.canvas.figure.add_subplot(121)
		self.canvas.axes2 = self.canvas.figure.add_subplot(122)