# # Наведение мыши
# import sys
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
# from PyQt5.QtCore import QSize    

# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

#         self.setMinimumSize(QSize(300, 100))    
#         self.setWindowTitle("PyQt tooltip example - pythonprogramminglanguage.com") 

#         pybutton = QPushButton('Pyqt', self)
#         pybutton.clicked.connect(self.clickMethod)
#         pybutton.resize(100,32)
#         pybutton.move(50, 20)        
#         pybutton.setToolTip('This is a tooltip message.')  

#     def clickMethod(self):
#         print('PyQt')

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit( app.exec_() )


# # Цвет
# from PyQt4 import QtGui

# from PyQt4 import QtCore


# if __name__ == '__main__':
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     w = QtGui.QLineEdit()
#     palette = QtGui.QPalette()
#     palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
#     w.setPalette(palette)
#     font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
#     w.setFont(font)
#     w.show()
#     sys.exit(app.exec_())



# def algoSolution(self):
#     """ Численное и точное решение жесткой системы ОДУ """

#     f = True
#     for i in range(1, self.node):
#         self.x[i], self.Ij[i] = self.RK_III(self.x[i - 1], self.Ij[i - 1], self.h[i - 1])
#         self.uj[i] = self.Exactly(self.x[i])

#         if not self.ControlLocErr(self.x[i], self.Ij[i], self.h[i - 1], i, True):
#             self.ControlLocErr(self.x[i], self.Ij[i], self.h[i - 1], i, True)

#         if ((self.xmax - self.x[i]) < 0):
#             f = False

#         if not f or ((self.xmax - self.x[i]) < 0) or np.isnan(self.Ij[i]) or np.isinf(self.Ij[i]) or np.isneginf(self.Ij[i]):
#             # Очистка списков от мусора
#             # self.x = np.delete(self.x, np.s_[i:])
#             # self.Ij = np.delete(self.Ij, np.s_[i:])
#             # self.I2j = np.delete(self.I2j, np.s_[i:])
#             # self.S = np.delete(self.S, np.s_[i:])
#             # self.h = np.delete(self.h, np.s_[i:])
#             # self.c1 = np.delete(self.c1, np.s_[i:])
#             # self.c2 = np.delete(self.c2, np.s_[i:])
#             # self.uj = np.delete(self.uj, np.s_[i:])

#             break

#     if not f:
#         # xn
#         self.h[i - 1] /= 2
#         self.c2[i - 1] += 1
#         i -= 1
#         # xn > xmax || xn < (xmax - xeps)
#         while self.x[i - 1] > self.xmax or (self.x[i - 1] < (self.xmax - self.xeps)):
#             # считаем для i+1
#             self.x[i], self.Ij[i] = self.RK_III(self.x[i - 1], self.Ij[i - 1], self.h[i - 1])
#             self.uj[i] = self.Exactly(self.x[i])

#             if not self.ControlLocErr(self.x[i], self.Ij[i], self.h[i - 1], i, False):
#                 self.ControlLocErr(self.x[i], self.Ij[i], self.h[i - 1], i, False)

#             # xn+1 > xmax
#             if self.x[i] > self.xmax:
#                 # xn
#                 self.h[i - 1] /= 2
#                 self.c2[i - 1] += 1
#                 i -= 1

#             i += 1

#     self.x = np.delete(self.x, np.s_[i:])
#     self.Ij = np.delete(self.Ij, np.s_[i:])
#     self.I2j = np.delete(self.I2j, np.s_[i:])
#     self.S = np.delete(self.S, np.s_[i:])
#     self.h = np.delete(self.h, np.s_[i:])
#     self.c1 = np.delete(self.c1, np.s_[i:])
#     self.c2 = np.delete(self.c2, np.s_[i:])
#     self.uj = np.delete(self.uj, np.s_[i:])

#     self.difIj_I2j = np.subtract(self.Ij, self.I2j)
#     self.difuj_Ij = np.absolute(self.uj - self.Ij)
#     self.olp = (2 ** self.P) * self.S


import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen 
from PyQt5.QtCore import QTimer

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.b1 = QPushButton('Display screensaver')
        self.b1.clicked.connect(self.flashSplash)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.b1)

    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('D:/_Qt/img/pyqt.jpg'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Dialog()
    main.show()
    sys.exit(app.exec_())