# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lay_table = QtWidgets.QVBoxLayout()
        self.lay_table.setObjectName("lay_table")
        self.PdTable = QtWidgets.QTableWidget(self.centralwidget)
        self.PdTable.setObjectName("PdTable")
        self.PdTable.setColumnCount(0)
        self.PdTable.setRowCount(0)
        self.lay_table.addWidget(self.PdTable)
        self.lay_buts = QtWidgets.QHBoxLayout()
        self.lay_buts.setObjectName("lay_buts")
        self.but_call = QtWidgets.QPushButton(self.centralwidget)
        self.but_call.setObjectName("but_call")
        self.lay_buts.addWidget(self.but_call)
        self.but_descr = QtWidgets.QPushButton(self.centralwidget)
        self.but_descr.setObjectName("but_descr")
        self.lay_buts.addWidget(self.but_descr)
        self.lay_table.addLayout(self.lay_buts)
        self.horizontalLayout_2.addLayout(self.lay_table)
        self.lay_graph = QtWidgets.QVBoxLayout()
        self.lay_graph.setObjectName("lay_graph")
        self.MplGraph = MyGraph(self.centralwidget)
        self.MplGraph.setObjectName("MplGraph")
        self.lay_graph.addWidget(self.MplGraph)
        self.vlayout_left_right = QtWidgets.QHBoxLayout()
        self.vlayout_left_right.setObjectName("vlayout_left_right")
        self.vlayout_left = QtWidgets.QVBoxLayout()
        self.vlayout_left.setObjectName("vlayout_left")
        self.label_params_enter = QtWidgets.QLabel(self.centralwidget)
        self.label_params_enter.setObjectName("label_params_enter")
        self.vlayout_left.addWidget(self.label_params_enter)
        self.lay_top = QtWidgets.QVBoxLayout()
        self.lay_top.setObjectName("lay_top")
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setObjectName("label_top")
        self.lay_top.addWidget(self.label_top)
        self.lay_L = QtWidgets.QHBoxLayout()
        self.lay_L.setObjectName("lay_L")
        self.label_L = QtWidgets.QLabel(self.centralwidget)
        self.label_L.setObjectName("label_L")
        self.lay_L.addWidget(self.label_L)
        self.doubleSpinBox_L = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_L.setObjectName("doubleSpinBox_L")
        self.lay_L.addWidget(self.doubleSpinBox_L)
        self.lay_top.addLayout(self.lay_L)
        self.lay_R = QtWidgets.QHBoxLayout()
        self.lay_R.setObjectName("lay_R")
        self.label_R = QtWidgets.QLabel(self.centralwidget)
        self.label_R.setObjectName("label_R")
        self.lay_R.addWidget(self.label_R)
        self.doubleSpinBox_R = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_R.setObjectName("doubleSpinBox_R")
        self.lay_R.addWidget(self.doubleSpinBox_R)
        self.lay_top.addLayout(self.lay_R)
        self.lay_I0 = QtWidgets.QHBoxLayout()
        self.lay_I0.setObjectName("lay_I0")
        self.label_I0 = QtWidgets.QLabel(self.centralwidget)
        self.label_I0.setObjectName("label_I0")
        self.lay_I0.addWidget(self.label_I0)
        self.doubleSpinBox_I0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_I0.setObjectName("doubleSpinBox_I0")
        self.lay_I0.addWidget(self.doubleSpinBox_I0)
        self.lay_top.addLayout(self.lay_I0)
        self.vlayout_left.addLayout(self.lay_top)
        self.lay_center = QtWidgets.QVBoxLayout()
        self.lay_center.setObjectName("lay_center")
        self.label_center = QtWidgets.QLabel(self.centralwidget)
        self.label_center.setObjectName("label_center")
        self.lay_center.addWidget(self.label_center)
        self.lay_E0 = QtWidgets.QHBoxLayout()
        self.lay_E0.setObjectName("lay_E0")
        self.label_E0 = QtWidgets.QLabel(self.centralwidget)
        self.label_E0.setObjectName("label_E0")
        self.lay_E0.addWidget(self.label_E0)
        self.doubleSpinBox_E0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_E0.setObjectName("doubleSpinBox_E0")
        self.lay_E0.addWidget(self.doubleSpinBox_E0)
        self.lay_center.addLayout(self.lay_E0)
        self.lay_w = QtWidgets.QHBoxLayout()
        self.lay_w.setObjectName("lay_w")
        self.label_w = QtWidgets.QLabel(self.centralwidget)
        self.label_w.setObjectName("label_w")
        self.lay_w.addWidget(self.label_w)
        self.doubleSpinBox_w = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_w.setObjectName("doubleSpinBox_w")
        self.lay_w.addWidget(self.doubleSpinBox_w)
        self.lay_center.addLayout(self.lay_w)
        self.vlayout_left.addLayout(self.lay_center)
        self.lay_bottom = QtWidgets.QVBoxLayout()
        self.lay_bottom.setObjectName("lay_bottom")
        self.label_bottom = QtWidgets.QLabel(self.centralwidget)
        self.label_bottom.setObjectName("label_bottom")
        self.lay_bottom.addWidget(self.label_bottom)
        self.lay_V = QtWidgets.QHBoxLayout()
        self.lay_V.setObjectName("lay_V")
        self.label_V = QtWidgets.QLabel(self.centralwidget)
        self.label_V.setObjectName("label_V")
        self.lay_V.addWidget(self.label_V)
        self.doubleSpinBox_V = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_V.setObjectName("doubleSpinBox_V")
        self.lay_V.addWidget(self.doubleSpinBox_V)
        self.lay_bottom.addLayout(self.lay_V)
        self.vlayout_left.addLayout(self.lay_bottom)
        self.vlayout_left_right.addLayout(self.vlayout_left)
        self.vlayout_right = QtWidgets.QVBoxLayout()
        self.vlayout_right.setObjectName("vlayout_right")
        self.label_params_enter2 = QtWidgets.QLabel(self.centralwidget)
        self.label_params_enter2.setObjectName("label_params_enter2")
        self.vlayout_right.addWidget(self.label_params_enter2)
        self.lay_h0 = QtWidgets.QHBoxLayout()
        self.lay_h0.setObjectName("lay_h0")
        self.label_h0 = QtWidgets.QLabel(self.centralwidget)
        self.label_h0.setObjectName("label_h0")
        self.lay_h0.addWidget(self.label_h0)
        self.doubleSpinBox_h0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_h0.setObjectName("doubleSpinBox_h0")
        self.lay_h0.addWidget(self.doubleSpinBox_h0)
        self.vlayout_right.addLayout(self.lay_h0)
        self.lay_n = QtWidgets.QHBoxLayout()
        self.lay_n.setObjectName("lay_n")
        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setObjectName("label_n")
        self.lay_n.addWidget(self.label_n)
        self.spinBox_n = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_n.setObjectName("spinBox_n")
        self.lay_n.addWidget(self.spinBox_n)
        self.vlayout_right.addLayout(self.lay_n)
        self.lay_eps = QtWidgets.QHBoxLayout()
        self.lay_eps.setObjectName("lay_eps")
        self.label_eps = QtWidgets.QLabel(self.centralwidget)
        self.label_eps.setObjectName("label_eps")
        self.lay_eps.addWidget(self.label_eps)
        self.doubleSpinBox_eps = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_eps.setObjectName("doubleSpinBox_eps")
        self.lay_eps.addWidget(self.doubleSpinBox_eps)
        self.vlayout_right.addLayout(self.lay_eps)
        self.lay_xmax = QtWidgets.QHBoxLayout()
        self.lay_xmax.setObjectName("lay_xmax")
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setObjectName("label_xmax")
        self.lay_xmax.addWidget(self.label_xmax)
        self.doubleSpinBox_xmax = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_xmax.setObjectName("doubleSpinBox_xmax")
        self.lay_xmax.addWidget(self.doubleSpinBox_xmax)
        self.vlayout_right.addLayout(self.lay_xmax)
        self.lay_xeps = QtWidgets.QHBoxLayout()
        self.lay_xeps.setObjectName("lay_xeps")
        self.label_xeps = QtWidgets.QLabel(self.centralwidget)
        self.label_xeps.setObjectName("label_xeps")
        self.lay_xeps.addWidget(self.label_xeps)
        self.doubleSpinBox_xeps = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_xeps.setObjectName("doubleSpinBox_xeps")
        self.lay_xeps.addWidget(self.doubleSpinBox_xeps)
        self.vlayout_right.addLayout(self.lay_xeps)
        self.vlayout_left_right.addLayout(self.vlayout_right)
        self.lay_graph.addLayout(self.vlayout_left_right)
        self.horizontalLayout_2.addLayout(self.lay_graph)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_call.setText(_translate("MainWindow", "PushButton"))
        self.but_descr.setText(_translate("MainWindow", "PushButton"))
        self.label_params_enter.setText(_translate("MainWindow", "1"))
        self.label_top.setText(_translate("MainWindow", "TextLabel"))
        self.label_L.setText(_translate("MainWindow", "2"))
        self.label_R.setText(_translate("MainWindow", "3"))
        self.label_I0.setText(_translate("MainWindow", "6"))
        self.label_center.setText(_translate("MainWindow", "TextLabel"))
        self.label_E0.setText(_translate("MainWindow", "4"))
        self.label_w.setText(_translate("MainWindow", "5"))
        self.label_bottom.setText(_translate("MainWindow", "TextLabel"))
        self.label_V.setText(_translate("MainWindow", "14"))
        self.label_params_enter2.setText(_translate("MainWindow", "7"))
        self.label_h0.setText(_translate("MainWindow", "8"))
        self.label_n.setText(_translate("MainWindow", "9"))
        self.label_eps.setText(_translate("MainWindow", "10"))
        self.label_xmax.setText(_translate("MainWindow", "12"))
        self.label_xeps.setText(_translate("MainWindow", "13"))
from MyGraph import MyGraph


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
