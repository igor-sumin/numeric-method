from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, 
	QSizePolicy, QVBoxLayout, QTableView, QTableWidgetItem, 
	QTableWidget, QHeaderView, QListWidget, 
	QListWidgetItem, QLabel, QGraphicsColorizeEffect
)

from MyDesign import Ui_MainWindow
from MyTable import PdTable, WinDescr
from MyNonStationary import NonStat

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Подключить mpl
# Подключить table
# Вставить картинку в описание работы
# Настроить label'ы, spin'ы, lay'ы

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.setWindowTitle('Десятая задача / Игорь Сумин')

		self.initUi()
		self.widgetAdjust()

	def initUi(self):
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.font.setPointSize(12)
		self.font.setBold(False)
		self.font.setWeight(50)

		self.font2 = QtGui.QFont()
		self.font2.setFamily("Arial")
		self.font2.setPointSize(13)
		self.font2.setBold(False)
		self.font2.setWeight(50)

	def initLab(self, lab, font, text):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)
		lab.setText(text)

	def initSpinBox(self, lab, font, text=''):
		# lab.setMaximumHeight(30)
		# lab.setMinimumHeight(30)
		lab.setMinimumWidth(150)
		lab.setFont(font)
		lab.setRange(0, 1000000)
		# lab.setValue(500)
		lab.setSuffix(text)

	def initBut(self, lab, font, lay, text):
		style = """
		QPushButton {
			background-color : #11999e; 
			font-weight: bold; 
			color: #feffff; 
			border-color: #40514e;
		}

		QPushButton::hover {
			background-color: #30e3ca; 
		}
		"""

		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setMinimumWidth(350)

		lab.setFont(font)
		lab.setText(text)
		
		lab.setCursor(Qt.PointingHandCursor)
		lab.setStyleSheet(style)

	def initCheckBox(self, lab, font, text):
		style = """
		QCheckBox::indicator:checked {
			background-color : #11999e;
		}

		QCheckBox::indicator:hover {
			background-color : #30e3ca;
		}
		"""

		lab.setText(text)
		lab.setFont(font)
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)

		lab.setCursor(Qt.PointingHandCursor)
		lab.setStyleSheet(style)

	def myAddWidget(self, lab, spin, lay):
		pass
		# lay.addWidget(lab, alignment=QtCore.Qt.AlignRight)
		# lay.addWidget(spin, alignment=QtCore.Qt.AlignLeft)

	# Подключение кнопки вызова условия задачи
	def showDescr(self):
		self.win_descr = WinDescr()
		self.win_descr.show()

	def widgetAdjust(self):
		# Настраиваем label'ы
		self.texts = ['T - Правая граница по времени:', 'n - Число разбиений по пространству:', 'm - Число разбиений по времени:']
		self.labels = [self.label_T, self.label_n, self.label_m]
		self.lays = [self.lay_T, self.lay_n, self.lay_m]
		self.spins = [self.doubleSpinBox_T, self.spinBox_n, self.spinBox_m]

		for label, text in zip(self.labels, self.texts):
			self.initLab(label, self.font, text)

		# Настраиваем spinBox'ы
		text = ['', '', '']
		for spins, txt in zip(self.spins, text):
			self.initSpinBox(spins, self.font, txt)
		self.doubleSpinBox_T.setValue(5)
		self.spinBox_n.setValue(10)
		self.spinBox_m.setValue(500)

		# Настраиваем кнопки
		self.initBut(self.pushButton_task, self.font, self.lay_buttons, "Получить решение")
		self.initBut(self.pushButton_descr, self.font, self.lay_buttons, "Показать описание задачи")
		self.pushButton_task.clicked.connect(self.callFunc)
		self.pushButton_descr.clicked.connect(self.showDescr)

		# Настраиваем radioBox
		self.initCheckBox(self.checkBox_lays, self.font2, 'Выводим в таблицу все слои?')

		# Настраиваем виджеты
		for label, spin, lay in zip(self.labels, self.spins, self.lays):
			self.myAddWidget(label, spin, lay)
		self.lay_buttons.addWidget(self.checkBox_lays, alignment=QtCore.Qt.AlignCenter)
		self.lay_buttons.addWidget(self.pushButton_task, alignment=QtCore.Qt.AlignCenter)
		self.lay_buttons.addWidget(self.pushButton_descr, alignment=QtCore.Qt.AlignCenter)


		# Настраиваем таблицу с данными
		self.PdTable.setMaximumWidth(700)

		# Настраиваем график
		self.MplGraph.setMinimumSize(1000, 865)
		# self.MplGraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Вызываем начальные функции построения
		self.empty3dGraph()

	def getsValue(self):
		""" Получить значения со спинов """

		self.params = [0., 0, 0]
		for idx, spin in enumerate(self.spins):
			self.params[idx] = spin.value()

	def callFunc(self):
		self.getsValue()

		self.f = True if self.checkBox_lays.isChecked() else False
		self.result = NonStat(*self.params, self.f)
		self.ndata, self.df = self.result.output()

		self.plot3dGraph()
		PdTable(self, self.df, self.f, self.params)

	# создаем пустой график
	def empty3dGraph(self):
		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.figure.suptitle(
			'Изменение температуры стержня с течением времени\nT = {0}, n = {1}, m = {2}'. format(*['?', '?', '?']), 
			fontsize=13, fontweight='bold'
		)

		self.MplGraph.canvas.axes.zaxis.set_major_locator(LinearLocator(10))
		self.MplGraph.canvas.axes.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))

		self.MplGraph.canvas.axes.set_xlabel('?')
		self.MplGraph.canvas.axes.set_ylabel('?')
		self.MplGraph.canvas.axes.set_zlabel('?')

		# empty graph for visualize colorbar
		X, Y = np.meshgrid([0], [0])
		Z = X + Y
		surf = self.MplGraph.canvas.axes.plot_surface(X, Y, Z, cmap='coolwarm')
		cb = self.MplGraph.canvas.axes.figure.colorbar(surf, shrink=0.75, aspect=20)
		cb.set_label('Градиент температуры стержня')

	def plot3dGraph(self):
		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.figure.suptitle(
			'Изменение температуры стержня с течением времени\nT = {0}, n = {1}, m = {2}'. format(*self.params), 
			fontsize=13, fontweight='bold'
		)

		self.MplGraph.canvas.axes.zaxis.set_major_locator(LinearLocator(10))
		self.MplGraph.canvas.axes.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))

		self.MplGraph.canvas.axes.set_xlabel('x - координата сечения стержня')
		self.MplGraph.canvas.axes.set_ylabel('t - время')
		self.MplGraph.canvas.axes.set_zlabel('u(x, t) - температура стержня')

		surf = self.MplGraph.canvas.axes.plot_surface(*self.ndata, rstride=self.params[1] + 1, cstride=self.params[2] + 1, \
			antialiased=False, cmap='coolwarm')

		self.MplGraph.canvas.draw()
