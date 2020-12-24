from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
	QSizePolicy, QVBoxLayout, QTableView, QTableWidgetItem, QTableWidget, QHeaderView, QListWidget, QListWidgetItem, QLabel, QGraphicsColorizeEffect

from PyQt5.QtGui import QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from AppDesigner import Ui_MainWindow
from pdtable import PdTable, WinDescr
from Lab_main import Lab_main
from Lab_test import Lab_test

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

# Подключить mpl +
# Подключить таблицу +
# Связать кнопку с действием +
# Сделать рабочим spin +
# Заполнить label'ы +

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)

		self.setWindowTitle("Вторая лабораторная") 

		self.initUi()
		self.widget_adjust()

	def initUi(self):
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.font.setPointSize(13)
		self.font.setBold(False)
		self.font.setWeight(50)

		self.font2 = QtGui.QFont()
		self.font2.setFamily("Arial")
		self.font2.setPointSize(11)
		self.font2.setBold(False)
		self.font2.setWeight(50)


	def initLab(self, lab, font, text):
		lab.setMaximumHeight(30)
		lab.setMinimumHeight(30)
		lab.setFont(font)
		lab.setText(text)

	def initSpinBox(self, lab, font, text=''):
		self.spinBox_partition.setRange(1, 9999999)
		self.spinBox_partition.setMaximumHeight(30)
		self.spinBox_partition.setMinimumHeight(30)
		self.spinBox_partition.setFont(self.font)
		self.spinBox_partition.setMaximumWidth(75)


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
		lab.setMinimumWidth(200)
		lab.setFont(font)
		lab.setText(text)
		lab.setCursor(Qt.PointingHandCursor)
		lab.setStyleSheet(style)

	def myAddWidget(self, lab, lay):
		lay.addWidget(lab, alignment=QtCore.Qt.AlignCenter) 	

	def showDescr(self):
		self.win_descr = WinDescr()
		self.win_descr.show()

	def widget_adjust(self):
		# Настраиваем кнопки
		self.initBut(self.button_test_task, self.font2, self.layout_button_task, 'Решить тестовую задачу')
		self.initBut(self.button_main_task, self.font2, self.layout_button_task, 'Решить основную задачу')
		self.initBut(self.but_descr, self.font, self.lay_descr, 'Показать задачи')

		self.button_test_task.setCheckable(True)
		self.button_test_task.clicked[bool].connect(self.call_func)

		self.button_main_task.setCheckable(True)
		self.button_main_task.clicked[bool].connect(self.call_func)

		self.but_descr.clicked.connect(self.showDescr)

		# Настраиваем разбиение
		self.label_partition.setMaximumHeight(30)
		self.label_partition.setMinimumHeight(30)
		self.label_partition.setFont(self.font)
		self.label_partition.setText('Введите число разбиений:')

		# Настраиваем ползунок
		self.spinBox_partition.setRange(1, 9999999)
		self.spinBox_partition.setMaximumHeight(30)
		self.spinBox_partition.setMinimumHeight(30)
		self.spinBox_partition.setFont(self.font)
		self.spinBox_partition.setMaximumWidth(75)

		# Настраиваем три лейбла
		self.label_dif.setMaximumHeight(30)
		self.label_dif.setMinimumHeight(30)
		self.label_dif.setFont(self.font)

		self.label_n_partition.setMaximumHeight(30)
		self.label_n_partition.setMinimumHeight(30)
		self.label_n_partition.setFont(self.font)

		self.label_eps.setMaximumHeight(30)
		self.label_eps.setMinimumHeight(30)
		self.label_eps.setFont(self.font)

		self.label_eps.setText('Задача решена с точностью <strong>?</strong>')
		self.label_n_partition.setText('Для решения задачи на сетке было использовано <strong>?</strong> разбиений')
		self.label_dif.setText('Максимальное разность решения наблюдается в точке <strong>?</strong>')

		# Настраиваем таблицу с данными
		self.PdTable.setMinimumSize(400, 300)
		self.PdTable.setMaximumWidth(600)

		# Настраиваем графику
		self.MplWidget.setMinimumSize(400, 300)
		self.MplWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Настраиваем слои
		self.layout_three_labels.addWidget(self.label_eps, alignment=QtCore.Qt.AlignCenter)
		self.layout_three_labels.addWidget(self.label_dif, alignment=QtCore.Qt.AlignCenter)
		self.layout_three_labels.addWidget(self.label_n_partition, alignment=QtCore.Qt.AlignCenter)

		# Вызов функций построения
		self.plot_empty_graph()
		self.create_empty_table()

	# Вызов работы алгоритмов
	def call_func(self):
		source = self.sender()
		self.n = self.spinBox_partition.value()

		self.result = Lab_main(self.n) if source.text() == "Решить основную задачу" else Lab_test(self.n)
		self.note, self.ndata = self.result.Solution()

		self.label_eps.setText('Задача решена с точностью <strong>{0}</strong>'.format(str(self.note[1])))
		self.label_n_partition.setText('Для решения задачи на сетке было использовано <strong>{0}</strong> разбиений'.format(str(int(self.note[0]))))
		self.label_dif.setText('Максимальное разность решения наблюдается в точке <strong>{0}</strong>'.format(str(int(self.note[2]))))

		self.create_plot_main(self.ndata) if source.text() == "Решить основную задачу" else self.create_plot_test(self.ndata)
		# (!) доработать
		self.create_table(self.ndata)

	# Построение графика по ndata (Lab_test)
	def create_plot_test(self, ndata):
		self.MplWidget.canvas.axes1.clear()
		self.MplWidget.canvas.axes2.clear()

		self.MplWidget.canvas.axes1.plot(ndata['x'].values, ndata['v(x)'].values, label='численное решение v(x)')
		self.MplWidget.canvas.axes1.plot(ndata['x'].values, ndata['u(x)'].values, label='точное решение u(x)')
		self.MplWidget.canvas.axes2.plot(ndata['x'], ndata['|u(x) - v(x)|'], label='|u(x) - v(x)|')

		self.MplWidget.canvas.axes1.set_title('График аналитического и численного решений')
		self.MplWidget.canvas.axes1.set_ylabel('v(x), u(x)')
		self.MplWidget.canvas.axes1.legend(loc='best', fontsize=10)

		self.MplWidget.canvas.axes2.set_title('Разность аналитического и численного решения')
		self.MplWidget.canvas.axes2.set_ylabel('|u(x) - v(x)|')
		self.MplWidget.canvas.axes2.set_xlabel('x')
		self.MplWidget.canvas.axes2.legend(loc='best', fontsize=10)

		# self.MplWidget.canvas.figure.tight_layout()
		self.MplWidget.canvas.draw()

	# Построение графика по ndata (Lab_main)
	def create_plot_main(self, ndata):
		self.MplWidget.canvas.axes1.clear()
		self.MplWidget.canvas.axes2.clear()

		self.MplWidget.canvas.axes1.plot(ndata['x'].values, ndata['v(x)'].values, label='численное решение v(x)')
		self.MplWidget.canvas.axes1.plot(ndata['x'].values, ndata['v2(x2i)'].values, label='численное решение v2(x2i)')
		self.MplWidget.canvas.axes2.plot(ndata['x'], ndata['|v(x) - v2(x2i)|'], label='|v(x) - v2(x2i)|')

		self.MplWidget.canvas.axes1.set_title('График численных решений с целым и половинным шагом')
		self.MplWidget.canvas.axes1.set_ylabel('v(x), v2(x2i)')
		self.MplWidget.canvas.axes1.legend(loc='best', fontsize=10)

		self.MplWidget.canvas.axes2.set_title('Разность численных решений в общих узлах')
		self.MplWidget.canvas.axes2.set_ylabel('|v(x) - v2(x2i)|')
		self.MplWidget.canvas.axes2.set_xlabel('x')
		self.MplWidget.canvas.axes2.legend(loc='best', fontsize=10)

		# self.MplWidget.canvas.figure.tight_layout()
		self.MplWidget.canvas.draw()

	# Построение таблицы
	def create_table(self, ndata):
		self.table = PdTable(self, ndata)

	# Построение пустого графа
	def plot_empty_graph(self):
		self.MplWidget.canvas.axes1.clear()
		self.MplWidget.canvas.axes2.clear()

		self.MplWidget.canvas.axes1.set_title('График решений')
		self.MplWidget.canvas.axes1.set_ylabel('v(x), ?') 

		self.MplWidget.canvas.axes2.set_title('Разность решений')
		self.MplWidget.canvas.axes2.set_ylabel('? - ?') 
		self.MplWidget.canvas.axes2.set_xlabel('x')

		# self.MplWidget.canvas.figure.tight_layout()
		self.MplWidget.canvas.draw()

	# Построение пустой таблицы
	def create_empty_table(self):
		columns = ['???'] * 5
		ndata = pd.DataFrame(columns=columns)
		
		self.emptyTable = PdTable(self, ndata)



