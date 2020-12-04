import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QProgressBar
from PyQt5.QtCore import Qt

from MyApp import MainWindow

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')
params = {
	'legend.fontsize': 'medium',
	'legend.handlelength': 2,
}
plt.rcParams.update(params)

def main_application():
	import sys, time
	
	app = QApplication(sys.argv)

	# ->
	pixmap = QPixmap("./download.jpg")
	splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
	splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
	splash.setEnabled(False)

	progressBar = QProgressBar(splash)
	progressBar.setMaximum(10)
	progressBar.setGeometry(0, pixmap.height() - 50, pixmap.width(), 20)

	splash.show()
	splash.showMessage(
		"<h1><font color='white'; font-weight: bold;>Девятая задача / Валерия Алексеева</font></h1>", Qt.AlignCenter | Qt.AlignCenter, Qt.black
	)

	for i in range(1, 11):
		progressBar.setValue(i)
		t = time.time()
		while time.time() < t + 0.25:
			app.processEvents()

	main = MainWindow()
	main.show()

	# --
	splash.finish(main)
	# <-

	sys.exit(app.exec_())

if __name__ == '__main__':
	main_application()