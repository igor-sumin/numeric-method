import sys

from MyApp import MainWindow
from PyQt5.QtWidgets import QApplication

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
	app = QApplication(sys.argv)
	main = MainWindow()

	main.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main_application()