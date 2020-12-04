import pandas as pd
import numpy as np

class RigidSystem:
	def __init__(self, n_, h_, xmin_):
		"""
		Определение параметров для решения жесткой системы ОДУ
		"""

		self.n = n_
		self.h = h_
		self.xmin = xmin_

		self.lambda1 = -1000
		self.lambda2 = -0.01

		# Матрица коэф-тов
		self.A = np.array([
			[-500.005, 499.995],
			[499.995, -500.005]
		], dtype=np.double)

		# Порядок метода Эйлера
		self.P = 2

		# Количество узлов
		self.node = self.n + 1

		# Точное решение 
		self.u = np.empty([self.node, 2], dtype=np.dtype)
		# Численное решение
		self.v = np.empty([self.node, 2], dtype=np.dtype)
		# Глобальная погрешность
		self.E = np.empty([self.node, 2], dtype=np.dtype)
		# Значения exp^lambda12*x-xmin
		self.lambdas = np.empty([self.node, 2], dtype=np.double) 

		self.x = np.empty(self.node, dtype=np.double)

		# Начальные условия
		self.u0 = np.array([7, 13], dtype=np.double)

		self.u[0] = self.u0
		self.v[0] = self.u0
		self.E[0] = np.zeros(2)
		self.x[0] = self.xmin
		self.lambdas[0] = np.ones(2)


	def exactlySolution(self, x):
		"""
		Точное решение жесткой системы ОДУ
		"""

		w1 = np.array([1, -1])
		w2 = np.array([1, 1])
		
		return np.array([
			np.exp(self.lambda1 * (x - self.xmin)), np.exp(self.lambda2 * (x - self.xmin))]), np.array([
				-3 * w1[0] * np.exp(self.lambda1 * (x - self.xmin)) + 10 * w2[0] * np.exp(self.lambda2 * (x - self.xmin)),
				-3 * w1[1] * np.exp(self.lambda1 * (x - self.xmin)) + 10 * w2[1] * np.exp(self.lambda2 * (x - self.xmin))
			], dtype=np.double
		)

	def RK_II(self, v):
		"""
		Численное решение жесткой системы ОДУ методом РК-2 
		"""

		return v + self.h * self.A.dot(v + self.h / 2 * self.A.dot(v))

	def algoSolution(self):
		"""
		Численное и точное решение жесткой системы ОДУ 
		"""

		for i in range(1, self.node):
			self.v[i] = self.RK_II(self.v[i - 1])
			self.x[i] = self.x[i - 1] + self.h

			self.lambdas[i], self.u[i] = self.exactlySolution(self.x[i])

		# self.v = ([self.RK_II(self.v[i - 1]) for i in range(1, self.n)])
		# self.x = ([self.x[i - 1] + self.h for i in range(1, self.n)])
		# self.lambdas, self.u = self.exactlySolution(self.x)

		self.E = np.subtract(self.u, self.v)

	def output(self):
		"""
		Формирование результата
		"""

		self.algoSolution()

		ndata = pd.DataFrame({
			'n': np.arange(self.node), 'x': np.around(self.x, 6), 'u(1)': self.u[:, 0], 'u(2)': self.u[:, 1], 
			'v(1)': self.v[:, 0], 'v(2)': self.v[:, 1], 
			'exp(-1000*x)': self.lambdas[:, 0], 'exp(-0.01*x)': self.lambdas[:, 1], 
			'E(1)': self.E[:, 0], 'E(2)': self.E[:, 1]}
		)

		return ndata