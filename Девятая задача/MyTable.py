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
		parent.PdTable.setColumnWidth(0, parent.PdTable.width() // 20)
		parent.PdTable.setColumnWidth(1, parent.PdTable.width() // 10)
		for i in range(2, 7):
			parent.PdTable.setColumnWidth(i, parent.PdTable.width() // 4)

		parent.PdTable.setColumnWidth(7, parent.PdTable.width() // 10)
		parent.PdTable.setColumnWidth(8, parent.PdTable.width() // 10)
		parent.PdTable.setColumnWidth(9, parent.PdTable.width() // 4)
		parent.PdTable.setColumnWidth(10, parent.PdTable.width() // 4)
		parent.PdTable.setColumnWidth(11, parent.PdTable.width() // 4)

		parent.PdTable.horizontalHeader().setStretchLastSection(True)

	def getToolTips(self, parent):
		# cols = ['n', 'x', 'Ij', 'I2j', 'Ij - I2j', '|ОЛП|', 'Hj', 'C1', 'C2', 'uj', '|uj - Ij|', 'yj']
		parent.PdTable.horizontalHeaderItem(0).setToolTip('Номер шага')
		parent.PdTable.horizontalHeaderItem(1).setToolTip('Координата x<sub>j</sub> приближенной траектории с текущим шагом')
		parent.PdTable.horizontalHeaderItem(2).setToolTip('Координата v<sub>j</sub> приближенной траектории с текущим шагом')
		parent.PdTable.horizontalHeaderItem(3).setToolTip('Координата v<sub>2j</sub> приближенной траектории с половинным шагом')
		parent.PdTable.horizontalHeaderItem(4).setToolTip('Разница координат с текущим шагом v<sub>j</sub> и с половинным шагом v<sub>2j</sub>')
		parent.PdTable.horizontalHeaderItem(5).setToolTip('Модуль оценки локальной погрешности')
		parent.PdTable.horizontalHeaderItem(6).setToolTip('Шаг интегрирования')
		parent.PdTable.horizontalHeaderItem(7).setToolTip('Счетчик удвоений шага')
		parent.PdTable.horizontalHeaderItem(8).setToolTip('Счетчик деления шага')
		parent.PdTable.horizontalHeaderItem(9).setToolTip('Координата u<sub>j</sub> точной траектории')
		parent.PdTable.horizontalHeaderItem(10).setToolTip('Разница между точным и численным решением')
		parent.PdTable.horizontalHeaderItem(11).setToolTip('Процесс установления тока в цепи с самоиндукцией')

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
		pixmap = QPixmap("./lera.jpg")
		self.setWindowTitle('Условие задачи')

		lab = QLabel(self)
		lab.setPixmap(pixmap)

		hbox.addWidget(lab)
		self.setLayout(hbox)


| Задача | Решение | Авторы решения | Примечание |
|---| ----- | -------- |-----|
|1ая лабораторная| [C++](./numeric/numeric-method/Первая лабораторная/Тестовая и основная задача/ZedGraph)| Игорь Сумин |Тестовая и основная задача. Лабораторная работа|
|9 задача| [Python](./numeric/numeric-method/Девятая задача)| Валерия Алексеева / Игорь Сумин | ... . Практическая работа |
|11 задача| *В процессе* | Никита Мешалкин | ... . Практическая работа |
|Жесткая система ОДУ| [Python](./numeric/numeric-method/Жесткая система ОДУ)| Ксения Белова / Игорь Сумин | ... . Практическая работа |
|2ая лабораторная| [Python](./numeric/numeric-method/Вторая лабораторная/Тестовая и основная задача)| Валерия Алексеева / Игорь Сумин |Тестовая и основная задача. Лабораторная работа|
|3я лабораторная| *В процессе* | Дмитрий Сиротин | ... . Лабораторная работа |