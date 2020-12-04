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
		parent.PdTable.setColumnWidth(2, parent.PdTable.width() // 5)
		for i in range(3, 10):
			parent.PdTable.setColumnWidth(i, parent.PdTable.width() // 4)

		parent.PdTable.horizontalHeader().setStretchLastSection(True)

	def getToolTips(self, parent):
		# ['n', 'x', 'u(1)', 'u(2)', 'v(1)', 'v(2)', 'exp(-1000*x)', 'exp(-0.01*x)', 'E(1)', 'E(2)']
		parent.PdTable.horizontalHeaderItem(0).setToolTip('Номер шага')
		parent.PdTable.horizontalHeaderItem(1).setToolTip('Координата приближенной траектории, вычесленная методом РК-2 с текущим шагом')
		parent.PdTable.horizontalHeaderItem(2).setToolTip('Координата точной траектории для 1ой компоненты (точное решение 1ой компоненты)')
		parent.PdTable.horizontalHeaderItem(3).setToolTip('Координата точной траектории для 2ой компоненты (точное решение 2ой компоненты)')
		parent.PdTable.horizontalHeaderItem(4).setToolTip('Координата приближенной траектории, вычисленная методом РК-2 с текущим шагом, для 1ой компоненты (численное решение 1ой компоненты)')
		parent.PdTable.horizontalHeaderItem(5).setToolTip('Координата приближенной траектории, вычисленная методом РК-2 с текущим шагом, для 2ой компоненты (численное решение 2ой компоненты)')
		parent.PdTable.horizontalHeaderItem(6).setToolTip('Часть точного решения, показывающая скорость изменения компоненты')
		parent.PdTable.horizontalHeaderItem(7).setToolTip('Часть точного решения, показывающая скорость изменения компоненты')
		parent.PdTable.horizontalHeaderItem(8).setToolTip('Глобальная погрешность 1ой компоненты')
		parent.PdTable.horizontalHeaderItem(9).setToolTip('Глобальная погрешность 2ой компоненты')

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
		pixmap = QPixmap("./ksusha.jpg")
		self.setWindowTitle('Условие задачи')

		lab = QLabel(self)
		lab.setPixmap(pixmap)

		hbox.addWidget(lab)
		self.setLayout(hbox)
