import sys

from MyApp import MainWindow
from PyQt5.QtWidgets import QApplication

def main_application():
	app = QApplication(sys.argv)
	main = MainWindow()

	main.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main_application()