from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, QSizePolicy, 
	QVBoxLayout, QTableView, QTableWidgetItem, QTableWidget, QHeaderView
)

import matplotlib.pyplot as plt

from matplotlib.figure import Figure 
from matplotlib.backends.backend_qt5agg import (
	FigureCanvas, FigureCanvasQTAgg, NavigationToolbar2QT
)

# plt.style.use('ggplot')
params = {
	'legend.fontsize': 'medium',
	'legend.handlelength': 2,
}
plt.rcParams.update(params)

# График приложения
class MyGraph(QWidget): 
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.canvas = FigureCanvas(Figure()) 
		self.toolbar = NavigationToolbar2QT(self.canvas, parent)

		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		vertical_layout.addWidget(self.toolbar) 
		
		self.canvas.axes = self.canvas.figure.add_subplot(111, projection='3d')

		self.canvas.figure.tight_layout()
		self.setLayout(vertical_layout)

