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
	def __init__(self, parent, data, flag, params):
		super().__init__()

		self._data = data
		self._flag = flag
		self._lays = params

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

		temp = [''] * rows
		j = 0
		for i in range(0, rows, self._lays[1] + 1):
			temp[i] = 'Слой ' + str(j)
			j += 1

		# вызуил для предпослденего и послденего слоев
		temp[-self._lays[1] - 1] = 'Слой ' + str(self._lays[2])
		temp[(-self._lays[1] - 1) * 2] = 'Слой ' + str(self._lays[2] - 1)


		parent.PdTable.setVerticalHeaderLabels(temp)

		# data insertion
		for i in range(parent.PdTable.rowCount()):
			for j in range(parent.PdTable.columnCount()):
				parent.PdTable.setItem(i, j, QTableWidgetItem(str(self._data.iloc[i, j])))

	# Изменение рамеров колонок таблицы
	def resizeEvent(self, parent):
		# parent.PdTable.setColumnWidth(0, parent.PdTable.width() // 16)
		# parent.PdTable.setColumnWidth(1, parent.PdTable.width() // 8)
		# parent.PdTable.setColumnWidth(2, parent.PdTable.width() // 8)
		# parent.PdTable.setColumnWidth(3, parent.PdTable.width() // 14)
		# parent.PdTable.setColumnWidth(4, parent.PdTable.width() // 8)

		parent.PdTable.horizontalHeader().setStretchLastSection(True)

	def getToolTips(self, parent):
		# cols = ['№ Слоя', 'tj', 'i', 'xi', 'vij']

		parent.PdTable.horizontalHeaderItem(0).setToolTip('Координата времени на каждом слое')
		parent.PdTable.horizontalHeaderItem(1).setToolTip('Номер координаты по пространству')
		parent.PdTable.horizontalHeaderItem(2).setToolTip('Координата пространства на каждом слое')
		parent.PdTable.horizontalHeaderItem(3).setToolTip('Координата точного решения неявной схемы в узле (i, j)')

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
		parent.PdTable.verticalHeader().setVisible(True)

		header = parent.PdTable.horizontalHeader()
		vertical = parent.PdTable.verticalHeader()

		header.setDefaultAlignment(QtCore.Qt.AlignCenter)
		vertical.setDefaultAlignment(QtCore.Qt.AlignCenter)

# Окно с условием задачи
class WinDescr(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)
		pixmap = QPixmap("./igor.jpg")
		self.setWindowTitle('Условие задачи')

		lab = QLabel(self)
		lab.setPixmap(pixmap)

		hbox.addWidget(lab)
		self.setLayout(hbox)