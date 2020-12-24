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

		self.setWindowTitle('Девятая задача / Валерия Алексеева, Игорь Сумин')

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
		self.font2.setPointSize(14)
		self.font2.setBold(False)
		self.font2.setWeight(50)

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
		spin.setRange(1, 1000000)
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
		par_main = '<strong>Параметры для расчета силы тока:</strong>'
		par_top = '<strong>общие параметры для уравнения силы тока:</strong>'
		par_center = '<strong>параметры для переменного тока:</strong>'
		par_bottom = '<strong>параметры для тока с самоиндукцией:</strong>'

		for item, text in zip([self.label_params_enter, self.label_top, self.label_center, self.label_bottom, \
			self.label_L, self.label_R, self.label_E0, self.label_w, \
			self.label_I0, self.label_V], \
			[
			par_main, par_top, par_center, par_bottom, 'L - индуктивность:', 'R - сопротивление:', \
			'E<sub>o</sub> - нач. напряженность:', 'w - угловая частота:', \
			'I<sub>o</sub> - нач. ток:', 'V - напряжение в цепи:' \
			]
		):
			self.initLab(item, self.font, text)

		par_enter2 = '<strong>Параметры для расчета методом Рунге-Кутты(3):</strong>'
		for item,text in zip([self.label_params_enter2, self.label_h0, self.label_n, self.label_eps, \
			self.label_xmax, self.label_xeps],
			[
			par_enter2, 'h<sub>o</sub> - начальный шаг:', 'n<sub>max</sub> - максимальное количество шагов:', 'eps - параметр для контроля лок. погрешности:', \
		 	'X<sub>max</sub> - максимальная координата x:', 'eps<sub>x</sub> - параметр выхода на границу: '
			]
		):
			self.initLab(item, self.font, text)

		# Настраиваем spinBox'ы
		for item, text in zip([self.doubleSpinBox_L, self.doubleSpinBox_R, self.doubleSpinBox_E0, self.doubleSpinBox_w, self.doubleSpinBox_I0, \
			self.doubleSpinBox_V], \
			[' Гн', ' Ом', ' В/м', ' 1/c', ' A', ' В']
		):
			self.initSpinBox(item, self.font, text)

		for item in [self.doubleSpinBox_h0, self.doubleSpinBox_eps, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps]:
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
			[self.label_h0, self.label_eps, self.label_xmax, self.label_xeps],
			[self.doubleSpinBox_h0, self.doubleSpinBox_eps, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps],
			[self.lay_h0, self.lay_eps, self.lay_xmax, self.lay_xeps]
		):
			self.myAddWidget2(label, dSpin, lay)

		self.label_params_enter2.setAlignment(QtCore.Qt.AlignCenter)

		self.label_params_enter.setFont(self.font2)
		self.label_params_enter2.setFont(self.font2)

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
		self.params_rk = np.empty(5, dtype=np.double)

		for idx, spin in enumerate(
			[self.doubleSpinBox_L, self.doubleSpinBox_R, self.doubleSpinBox_E0, self.doubleSpinBox_w, self.doubleSpinBox_I0, self.doubleSpinBox_V]
		):
			self.params_phys[idx] = spin.value()

		for idx, spin in enumerate(
			[self.doubleSpinBox_h0, self.spinBox_n, self.doubleSpinBox_eps, self.doubleSpinBox_xmax, self.doubleSpinBox_xeps]
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

		self.MplGraph.canvas.axes.set_title('Зависимость переменных токов I, I1\n и тока с самоиндукцией I2 от времени x') 
		self.MplGraph.canvas.axes.set_ylabel('I, A') 
		self.MplGraph.canvas.axes.set_xlabel('x, c')

		self.MplGraph.canvas.draw()

	def plotGraph(self):
		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.set_title('Зависимость переменных токов I, I1\n и тока с самоиндукцией I2 от времени x')
		self.MplGraph.canvas.axes.set_ylabel('I, A')
		self.MplGraph.canvas.axes.set_xlabel('x, c')

		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['I'], label='численное решение для переменного тока')
		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['I1'], label='точное решение для переменного тока')
		self.MplGraph.canvas.axes.plot(self.ndata['x'], self.ndata['I2'], label='точное решение для тока с самоиндукцией')
		self.MplGraph.canvas.axes.legend(loc='best')

		self.MplGraph.canvas.draw()

	# создаем пустую таблицу
	def emptyTable(self):
		cols = ['n', 'x', 'I', 'I2n', 'I - I2n', '|ОЛП|', 'h', 'C1', 'C2', 'I1', '| I1 - I |', 'I2']
		ndata = pd.DataFrame(columns=cols)

		self.emptyTable = PdTable(self, ndata)