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

		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		vertical_layout.addWidget(self.toolbar) 
		
		self.canvas.axes = self.canvas.figure.add_subplot(111)
		self.canvas.figure.autofmt_xdate()

		self.setLayout(vertical_layout)