from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.Qt import QHBoxLayout
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, QSizePolicy, 
	QVBoxLayout, QTableView, QTableWidgetItem, QTableWidget, QHeaderView, QLabel
)

import numpy as np
import pandas as pd

# Таблица приложения
class PdTable(QWidget):
	def __init__(self, parent, data):
		super().__init__()

		self._data = data
		self.initUI(parent)

	def initUI(self, parent):
		self.createTable(parent)
		self.resizeEvent(parent)
		self.getStyle(parent)
		self.getToolTips(parent)

	# Заполнение таблицы пришедшими данными
	def createTable(self, parent):
		# set table dimension
		rows, cols = self._data.shape
		parent.PdTable.setRowCount(rows)
		parent.PdTable.setColumnCount(cols)
		parent.PdTable.setHorizontalHeaderLabels(self._data.columns)

		# data insertion
		for i in range(parent.PdTable.rowCount()):
			for j in range(parent.PdTable.columnCount()):
				parent.PdTable.setItem(i, j, QTableWidgetItem(str(self._data.iloc[i, j])))

	# Изменение рамеров колонок таблицы
	def resizeEvent(self, parent):
		parent.PdTable.setColumnWidth(0, parent.PdTable.width() // 24)
		parent.PdTable.setColumnWidth(1, parent.PdTable.width() // 8)
		parent.PdTable.setColumnWidth(2, parent.PdTable.width() // 4)
		parent.PdTable.setColumnWidth(3, parent.PdTable.width() // 4)
		parent.PdTable.setColumnWidth(4, parent.PdTable.width() // 4)

		parent.PdTable.horizontalHeader().setStretchLastSection(True)

	def getToolTips(self, parent):
		# cols = ['n', 'x', 'u(x)', 'v(x)', '| u(x) - v(x) |']
		parent.PdTable.horizontalHeaderItem(0).setToolTip('Номер шага')
		parent.PdTable.horizontalHeaderItem(1).setToolTip('Координата x<sub>j</sub> приближенной траектории с текущим шагом')
		parent.PdTable.horizontalHeaderItem(2).setToolTip('Координата u<sub>j</sub> точной траектории')
		parent.PdTable.horizontalHeaderItem(3).setToolTip('Координата v<sub>j</sub> приближенной траектории с текущим шагом')
		parent.PdTable.horizontalHeaderItem(4).setToolTip('Разница между точным и численным решением')

	# Добавление стилей
	def getStyle(self, parent):
		style = """
		QHeaderView {
			font-weight: bold; 
			color: #ffffff;
		}

		QHeaderView::section { 
			background-color: #11999e; 
			border: none; 
			border-left: 1px solid #ffffff; 
		}
		"""

		parent.PdTable.setStyleSheet(style)
		parent.PdTable.verticalHeader().setVisible(False)

		header = parent.PdTable.horizontalHeader()
		header.setDefaultAlignment(QtCore.Qt.AlignCenter)

# Окно с условием задачи
class WinDescr(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)
		pixmap = QPixmap("./Lera3.PNG")
		self.setWindowTitle('Описание задач')

		lab = QLabel(self)
		lab.setPixmap(pixmap)

		hbox.addWidget(lab)
		self.setLayout(hbox)