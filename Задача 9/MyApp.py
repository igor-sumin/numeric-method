from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, 
	QSizePolicy, QVBoxLayout, QTableView, QTableWidgetItem, 
	QTableWidget, QHeaderView, QListWidget, 
	QListWidgetItem, QLabel, QGraphicsColorizeEffect
)

from MyDesigner import Ui_MainWindow
from MyTable import PdTable, WinDescr
from MyNineLab import NineLab

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Подключить mpl
# Подключить table
# Вставить картинку в описание работы

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.setWindowTitle('Девятая задача')

		self.initUi()
		self.widgetAdjust()

	def initUi(self):
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.font.setPointSize(13)
		self.font.setBold(False)
		self.font.setWeight(50)

	def initLab(self, lab, font, text):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)
		lab.setText(text)

	def initSpinBox(self, lab, font, text=''):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)
		lab.setRange(0., 9999999.)
		lab.setSuffix(text)
		lab.setDecimals(5)
		lab.setSingleStep(0.00001)
		lab.setMaximumWidth(150)

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
		lab.setFont(font)
		lab.setText(text)
		
		lab.setCursor(Qt.PointingHandCursor)
		lab.setStyleSheet(style)

		# lay.addWidget(lab, alignment=QtCore.Qt.AlignCenter)

	def myAddWidget(self, lab, dSpin, lay):
		lay.addWidget(lab, alignment=QtCore.Qt.AlignRight) 	
		lay.addWidget(dSpin, alignment=QtCore.Qt.AlignLeft)

	def myAddWidget2(self, lab, dSpin, lay):
		lay.addWidget(lab, alignment=QtCore.Qt.AlignCenter)
		lay.addWidget(dSpin, alignment=QtCore.Qt.AlignRight)

	def optionN(self, lab, spin, lay):
		spin.setRange(1, 9999999)
		spin.setMaximumHeight(30)
		spin.setMinimumHeight(30)
		spin.setFont(self.font)
		spin.setMinimumWidth(136)

		lay.addWidget(lab, alignment=QtCore.Qt.AlignCenter)
		lay.addWidget(spin, alignment=QtCore.Qt.AlignRight)

	def showDescr(self):
		self.win_descr = WinDescr()
		self.win_descr.show()

	def widgetAdjust(self):
		# Настраиваем label'ы
		par_enter = '<strong>Параметры для уравнения переменного тока:</strong>'
		for item, text in zip([self.label_params_enter, self.label_L, self.label_R, self.label_E0, self.label_w, self.label_I0, self.label_V], \
			[
			par_enter, 'L - индуктивность:', 'R - сопротивление:', \
			'E<sub>o</sub> - нач. напряженность:', 'w - угловая частота:', \
			'I<sub>o</sub> - нач. ток:', 'V - напряжение в цепи:' \
			]
		):
			self.initLab(item, self.font, text)

		par_enter2 = '<strong>Параметры для расчета методом РК-3:</strong>'
		for item,text in zip([self.label_params_enter2, self.label_h0, self.label_n, self.label_eps, \
			self.label_xmin, self.label_xmax, self.label_xeps],
			[
			par_enter2, 'h<sub>o</sub> - начальный шаг:', 'n - количество шагов:', 'eps - параметр контроля ЛП:', \
			'X<sub>min</sub> - начальная координата x:', 'X<sub>max</sub> - конечная координата x:', 'xeps - параметр выхода на границу: '
			]
		):
			self.initLab(item, self.font, text)

		# Настраиваем spinBox'ы
		for item, text in zip([self.doubleSpinBox_L, self.doubleSpinBox_R, self.doubleSpinBox_E0, self.doubleSpinBox_w, self.doubleSpinBox_I0, \
			self.doubleSpinBox_V], \
			[' Гн', ' Ом', ' В/м', ' 1/c', ' A', ' В']
		):
			self.initSpinBox(item, self.font, text)

		for item in [self.doubleSpinBox_h0, self.doubleSpinBox_eps, self.doubleSpinBox_xmin, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps]:
			self.initSpinBox(item, self.font)

		# (!) Настраиваем кнопки
		self.initBut(self.but_call, self.font, self.lay_buts, "Получить решение")
		self.initBut(self.but_descr, self.font, self.lay_buts, "Показать описание задачи")
		self.but_call.clicked.connect(self.callFunc)
		self.but_descr.clicked.connect(self.showDescr)

		# Настраиваем виджеты
		for label, dSpin, lay in zip(
			[self.label_L, self.label_R, self.label_E0, self.label_w, self.label_I0, self.label_V], 
			[self.doubleSpinBox_L, self.doubleSpinBox_R, self.doubleSpinBox_E0, self.doubleSpinBox_w, self.doubleSpinBox_I0, self.doubleSpinBox_V],
			[self.lay_L, self.lay_R, self.lay_E0, self.lay_w, self.lay_I0, self.lay_V]
		):
			self.myAddWidget(label, dSpin, lay)

		for label, dSpin, lay in zip(
			[self.label_h0, self.label_eps, self.label_xmin, self.label_xmax, self.label_xeps],
			[self.doubleSpinBox_h0, self.doubleSpinBox_eps, self.doubleSpinBox_xmin, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps],
			[self.lay_h0, self.lay_eps, self.lay_xmin, self.lay_xmax, self.lay_xeps]
		):
			self.myAddWidget2(label, dSpin, lay)

		self.label_params_enter.setAlignment(QtCore.Qt.AlignCenter)
		self.label_params_enter2.setAlignment(QtCore.Qt.AlignCenter)

		# Настраиваем таблицу с данными
		self.PdTable.setMinimumSize(400, 300)
		self.PdTable.setMaximumWidth(1100)

		# Настраиваем график
		self.MplGraph.setMinimumSize(400, 200)
		self.MplGraph.setMaximumSize(1200, 800)
		self.MplGraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Дополнительно
		self.optionN(self.label_n, self.spinBox_n, self.lay_n)
		self.doubleSpinBox_eps.setDecimals(9)
		self.doubleSpinBox_eps.setSingleStep(1e-9)
		self.doubleSpinBox_eps.setMaximumWidth(135)


		# Вызываем начальные функции построения
		self.emptyGraph()
		self.emptyTable()

	def getsValue(self):
		""" Получить значения со спинов """

		self.params_phys = np.empty(6, dtype=np.double)
		self.params_rk = np.empty(6, dtype=np.double)

		for idx, spin in enumerate(
			[self.doubleSpinBox_L, self.doubleSpinBox_R, self.doubleSpinBox_E0, self.doubleSpinBox_w, self.doubleSpinBox_I0, self.doubleSpinBox_V]
		):
			self.params_phys[idx] = spin.value()

		for idx, spin in enumerate(
			[self.doubleSpinBox_h0, self.spinBox_n, self.doubleSpinBox_eps, self.doubleSpinBox_xmin, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps]
		):
			self.params_rk[idx] = spin.value()

	def callFunc(self):
		self.getsValue()

		self.result = NineLab(self.params_phys, self.params_rk)
		self.ndata = self.result.output()

		self.plotGraph()
		PdTable(self, self.ndata)

	# создаем пустой график
	def emptyGraph(self):
		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.set_title('Зависимость переменного синусоидального тока от времени') 
		self.MplGraph.canvas.axes.set_ylabel('I(A) - сила тока') 
		self.MplGraph.canvas.axes.set_xlabel('x(сек) - время')

		self.MplGraph.canvas.draw()

	def plotGraph(self):
		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.set_title('Зависимость переменного синусоидального тока от времени')
		self.MplGraph.canvas.axes.set_ylabel('I(A) - сила тока') 
		self.MplGraph.canvas.axes.set_xlabel('x(сек) - время')

		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['Ij'], label='численное решение (I)')
		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['uj'], label='точное решение (u)')
		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['yj'], label='точное решение (y)')
		self.MplGraph.canvas.axes.legend(loc='best')

		self.MplGraph.canvas.draw()

	# создаем пустую таблицу
	def emptyTable(self):
		cols = ['n', 'x', 'Ij', 'I2j', 'Ij - I2j', '|ОЛП|', 'hj', 'C1', 'C2', 'uj', '| uj - Ij |', 'yj']
		ndata = pd.DataFrame(columns=cols)

		self.emptyTable = PdTable(self, ndata)