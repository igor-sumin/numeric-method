from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
	QApplication, QWidget, QMainWindow, 
	QSizePolicy, QVBoxLayout, QTableView, QTableWidgetItem, 
	QTableWidget, QHeaderView, QListWidget, 
	QListWidgetItem, QLabel, QGraphicsColorizeEffect
)

from DesignerRigid import Ui_MainWindow
from MyTable import PdTable, WinDescr
from MyRigid import RigidSystem
from MyGraph import MyGraph


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Подключить mpl
# Подключить table
# Связать кнопку с действием
# Сделать рабочими спины
# Заполнить label'ы

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)

		self.setWindowTitle("Жесткая система / Ксения Белова, Игорь Сумин")

		self.initUi()
		self.widgetAdjust()

	def initUi(self):

		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.font.setPointSize(11)
		self.font.setBold(False)
		self.font.setWeight(50)

		self.font_bold = QtGui.QFont()
		self.font_bold.setFamily("Arial")
		self.font_bold.setPointSize(13)
		self.font_bold.setBold(False)
		self.font_bold.setWeight(50)

	def initLab(self, lab, font, text):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)
		lab.setText(text)

	def initSpinBox(self, lab, font):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)

	def initBut(self, lab, font, text):
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
		
		lab.clicked.connect(self.call_func)

		lab.setCursor(Qt.PointingHandCursor)
		lab.setStyleSheet(style)

	def widgetAdjust(self):

		# Настраиваем label'ы
		for item, text in zip(
			[self.label_n, self.label_h, self.label_eps], ['кол-во шагов:', 'шаг интегр-ния:', 'eps - параметр контроля лок. погрешности']
		):
			self.initLab(item, self.font, text)

		for item, text in zip([self.label_u0, self.label_nres, self.label_hres], \
			['(u(1), u(2)) = <strong>(?, ?)</strong>', 'при n = <strong>?</strong>', 'шаг h = <strong>?</strong>']):
			self.initLab(item, self.font_bold, text)	

		# Настраиваем spinBox'ы
		for item in [self.spinBox_n, self.doubleSpinBox_h, self.doubleSpinBox_eps]:
			self.initSpinBox(item, self.font)

		self.spinBox_n.setRange(1, 1000000)

		self.doubleSpinBox_h.setRange(0., 1000000.)
		self.doubleSpinBox_h.setSpecialValueText("0")
		self.doubleSpinBox_h.setDecimals(7)
		self.doubleSpinBox_h.setSingleStep(0.00001)

		self.doubleSpinBox_eps.setRange(0., 1000000.)
		self.doubleSpinBox_eps.setSpecialValueText("0")
		self.doubleSpinBox_eps.setDecimals(7)
		self.doubleSpinBox_eps.setSingleStep(0.00001)

		# Настраиваем кнопки
		for item, text in zip([self.button_numeric, self.button_exact, self.button_eps, self.button_numeric_exact, self.button_descr], \
			['Численное решение', 'Точное решение', 'Глобальная погрешность', 'Точное и численное решение', 'Показать описание задачи']):
			self.initBut(item, self.font, text)

		# Настраиваем таблицу с данными
		self.PdTable.setMinimumSize(400, 300)
		self.PdTable.setMaximumWidth(1000)

		# Настраиваем график
		self.MplGraph.setMinimumSize(400, 200)
		self.MplGraph.setMaximumSize(1200, 800)
		self.MplGraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Настраиваем radioBox
		self.checkBox_lp.setText('Считаем с локальной погрешностью?')
		self.checkBox_lp.setFont(self.font_bold)

		# Добавляем виджеты
		self.hlayout_res.addWidget(self.label_u0, alignment=QtCore.Qt.AlignCenter)
		self.hlayout_res.addWidget(self.label_nres, alignment=QtCore.Qt.AlignCenter)
		self.hlayout_res.addWidget(self.label_hres, alignment=QtCore.Qt.AlignCenter)
		self.lay_rr.addWidget(self.button_descr, alignment=QtCore.Qt.AlignCenter)
		self.lay_rr.addWidget(self.checkBox_lp, alignment=QtCore.Qt.AlignCenter)



		# Вызываем начальные функции построения
		self.emptyGraph()
		self.emptyTable()


	# Показать описание задачи
	def showDescr(self):
		self.win_descr = WinDescr()
		self.win_descr.show()

	# Выбор работы алгоритма
	def call_func(self):
		source = self.sender()

		if source.text() == 'Показать описание задачи':
			self.showDescr(); return

		self.n = self.spinBox_n.value()
		self.h = self.doubleSpinBox_h.value()
		self.eps = self.doubleSpinBox_eps.value()
		self.f = False if self.checkBox_lp.isChecked() else True

		self.result = RigidSystem(self.n, self.h, self.eps, self.f)
		self.ndata = self.result.output()

		t = ' ' * 50

		# ['n', 'x', 'h', 'u(1)', 'u(2)', 'v(1)', 'v(2)', 'exp(-1000*x)', 'exp(-0.01*x)', '|ОЛП(1)|', '|ОЛП(2)|', 'c1', 'c2' 'E(1)', 'E(2)']
		text = source.text() + ' жестокой системы ОДУ'
		if source.text() == 'Численное решение':
			self.plotGraph(self.ndata.iloc[:, 5:7], text)
		elif source.text() == 'Точное решение':
			self.plotGraph(self.ndata.iloc[:, 3:5], text)
		elif source.text() == 'Глобальная погрешность':
			self.plotGraph(self.ndata.iloc[:, -2:], text)
		elif source.text() == 'Точное и численное решение':
			self.plotGraphSub(self.ndata.iloc[:, 3:5], self.ndata.iloc[:, 5:7], t + text)
		else:
			raise Exception()

		self.label_u0.setText('(u(1), u(2)) = <strong>({0}, {1})</strong>'.format('7', '13'))
		self.label_nres.setText('при n = <strong>{0}</strong>'.format(str(self.n)))
		self.label_hres.setText('шаг h = <strong>{0}</strong>'.format(str(self.h)))

		self.table = PdTable(self, self.ndata)

	def plotGraph(self, data, text):

		named1, named2 = data.columns

		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.set_visible(True)
		self.MplGraph.canvas.axes1.set_visible(False)
		self.MplGraph.canvas.axes2.set_visible(False)

		self.MplGraph.canvas.axes.set_title(text)
		self.MplGraph.canvas.axes.set_ylabel('Значения {0} и {1}'.format(named1, named2))
		self.MplGraph.canvas.axes.set_xlabel('Значение x')

		self.MplGraph.canvas.axes.plot(self.ndata['x'], data[named1], label=named1)
		self.MplGraph.canvas.axes.plot(self.ndata['x'], data[named2], label=named2)

		self.MplGraph.canvas.axes.legend(loc='best') 

		self.MplGraph.canvas.draw()
		self.MplGraph.setLayout(self.MplGraph.vertical_layout)

	def plotGraphSub(self, dataExact, dataNumeric, text):

		namedE1, namedE2 = dataExact.columns
		namedN1, namedN2 = dataNumeric.columns

		self.MplGraph.canvas.axes1.clear()
		self.MplGraph.canvas.axes2.clear()

		self.MplGraph.canvas.axes.set_visible(False)
		self.MplGraph.canvas.axes1.set_visible(True)
		self.MplGraph.canvas.axes2.set_visible(True)
		

		self.MplGraph.canvas.axes1.set_title(text)
		self.MplGraph.canvas.axes1.plot(self.ndata['x'], dataExact[namedE1], label=namedE1)
		self.MplGraph.canvas.axes1.plot(self.ndata['x'], dataNumeric[namedN1], label=namedN1)
		self.MplGraph.canvas.axes1.set_ylabel('Значения ' + '{0} и {1}, {2} и {3}'.format(namedE1, namedN1, namedE2, namedN2))
		self.MplGraph.canvas.axes1.set_xlabel('Значения x')

		self.MplGraph.canvas.axes2.plot(self.ndata['x'], dataExact[namedE2], label=namedE2)
		self.MplGraph.canvas.axes2.plot(self.ndata['x'], dataNumeric[namedN2], label=namedN2)
		self.MplGraph.canvas.axes2.set_xlabel('Значения x')

		self.MplGraph.canvas.figure.autofmt_xdate() 
		self.MplGraph.canvas.figure.autofmt_xdate() 

		self.MplGraph.canvas.axes1.legend(loc='best')
		self.MplGraph.canvas.axes2.legend(loc='best')

		self.MplGraph.canvas.draw()
		self.MplGraph.setLayout(self.MplGraph.vertical_layout)

	# создаем пустой график
	def emptyGraph(self):

		self.MplGraph.canvas.axes.clear()

		self.MplGraph.canvas.axes.set_visible(True)
		self.MplGraph.canvas.axes1.set_visible(False)
		self.MplGraph.canvas.axes2.set_visible(False)

		self.MplGraph.canvas.axes.set_title('Модельная задача') 
		self.MplGraph.canvas.axes.set_ylabel('Значения v(x), u(x), E(x)') 
		self.MplGraph.canvas.axes.set_xlabel('Значение x')

		self.MplGraph.canvas.draw()
		self.MplGraph.setLayout(self.MplGraph.vertical_layout)

	# создаем пустую таблицу
	def emptyTable(self):
		columns = ['n', 'x', 'h', 'u(1)', 'u(2)', 'v(1)', 'v(2)', 'exp(-1000*x)', 'exp(-0.01*x)', '|ОЛП|(1)', '|ОЛП|(2)', 'c1', 'c2', 'E(1)', 'E(2)']
		ndata = pd.DataFrame(columns=columns)

		self.emptyTable = PdTable(self, ndata)
