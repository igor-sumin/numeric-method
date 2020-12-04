from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, QSizePolicy, QVBoxLayout, 
	QTableView, QTableWidgetItem, QTableWidget, QHeaderView
)

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure 
	
class MplWidget(QWidget): 
	def __init__(self, parent=None): 
		QWidget.__init__( self, parent)
		
		self.canvas = FigureCanvas(Figure()) 
		self.toolbar = NavigationToolbar2QT(self.canvas, parent)

		vertical_layout = QVBoxLayout() 
		vertical_layout.addWidget(self.canvas)
		vertical_layout.addWidget(self.toolbar) 
		
		self.canvas.axes = self.canvas.figure.add_subplot(111) 
		self.setLayout(vertical_layout)