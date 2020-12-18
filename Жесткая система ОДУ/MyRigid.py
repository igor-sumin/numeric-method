import pandas as pd
import numpy as np

class RigidSystem:
	def __init__(self, n_, h_, eps_, f_):
		"""
		Определение параметров для решения жесткой системы ОДУ
		"""

		self.n = n_
		self.f = f_

		# Количество узлов
		self.node = self.n + 1

		# без ОЛП
		if self.f:
			self.h = np.full(self.node, h_)

		# с ОЛП
		else:
			self.h = np.empty(self.node, dtype=np.double)
			self.S = np.empty([self.node, 2], dtype=np.double)

			self.S[0] = 0.
			self.h[0] = h_
			self.eps = eps_

		self.lambda1 = -1000
		self.lambda2 = -0.01

		# Матрица коэф-тов
		self.A = np.array([
			[-500.005, 499.995],
			[499.995, -500.005]
		], dtype=np.double)

		# Порядок метода Эйлера
		self.P = 2

		# Точное решение 
		self.u = np.empty([self.node, 2], dtype=np.dtype)
		# Численное решение
		self.v = np.empty([self.node, 2], dtype=np.dtype)
		# Глобальная погрешность
		self.E = np.empty([self.node, 2], dtype=np.dtype)
		# Значения exp^lambda12*x
		self.lambdas = np.empty([self.node, 2], dtype=np.double) 

		self.x = np.empty(self.node, dtype=np.double)

		# Начальные условия
		self.u0 = np.array([7, 13], dtype=np.double)

		self.u[0] = self.u0
		self.v[0] = self.u0
		self.E[0] = np.zeros(2)
		self.x[0] = 0
		self.lambdas[0] = np.ones(2)

		self.olp = np.full([self.node, 2], 0)
		self.c1 = np.zeros(self.node, dtype=np.int)
		self.c2 = np.zeros(self.node, dtype=np.int)

	def exactlySolution(self, x):
		"""
		Точное решение жесткой системы ОДУ
		"""

		w1 = np.array([1, -1])
		w2 = np.array([1, 1])
		
		return np.array([
			np.exp(self.lambda1 * x), np.exp(self.lambda2 * x)]), np.array([
				-3 * w1[0] * np.exp(self.lambda1 * x) + 10 * w2[0] * np.exp(self.lambda2 * x),
				-3 * w1[1] * np.exp(self.lambda1 * x) + 10 * w2[1] * np.exp(self.lambda2 * x)
			], dtype=np.double
		)

	def RK_II(self, x, v, h):
		"""
		Численное решение жесткой системы ОДУ методом РК-2 
		"""

		return x + h, v + h * self.A.dot(v + h / 2 * self.A.dot(v))

	def ControlLocErr(self, x, v, h, idx):
		""" Контроль локальной погрешности (ЛП) """

		x_next, v_next = self.RK_II(x, v, h)
		x_half, v_half = self.RK_II(x, v, h / 2)
		x_new, v_new  = self.RK_II(x_half, v_half, h / 2)
		
		self.S[idx] = (v_new - v_next) / (2 ** self.P - 1)
		
		return self.ControlCompare(x, v, h, idx)

	def ControlCompare(self, x, v, h, idx):
		""" Контроль локальной погрешности (ЛП) (продолжение) """

		self.S[idx] = np.absolute(self.S[idx])
		self.c1[idx] = self.c1[idx - 1]
		self.c2[idx] = self.c2[idx - 1]

		zn = 2 ** (self.P + 1)
		
		if ((self.eps / zn) <= self.S[idx, 0] <= self.eps) and ((self.eps / zn) <= self.S[idx, 1] <= self.eps):
			self.h[idx] = h

			return True

		elif (self.S[idx, 0] < (self.eps / zn)) and (self.S[idx, 1] < (self.eps / zn)):
			if h >= 1e10:
				self.h[idx] = h
			else:
				self.h[idx] = h * 2
				self.c1[idx] += 1

			return True

		else:
			self.h[idx] = h / 2
			self.c2[idx] += 1

			return False

		assert False

	def algoSolution(self):
		"""
		Численное и точное решение жесткой системы ОДУ 
		"""

		for i in range(1, self.node):
			self.x[i], self.v[i] = self.RK_II(self.x[i - 1], self.v[i - 1], self.h[i - 1])
			self.lambdas[i], self.u[i] = self.exactlySolution(self.x[i])

	def algoSolution_olp(self):
		""" Численное и точное решение жесткой системы ОДУ """

		for i in range(1, self.node):
			self.x[i], self.v[i] = self.RK_II(self.x[i - 1], self.v[i - 1], self.h[i - 1])
			self.lambdas[i], self.u[i] = self.exactlySolution(self.x[i])

			if not self.ControlLocErr(self.x[i - 1], self.v[i - 1], self.h[i - 1], i):
				self.ControlLocErr(self.x[i - 1], self.v[i - 1], self.h[i - 1], i)

			if np.isnan(self.v[i, 0]) or np.isnan(self.v[i, 1]) \
				or np.isinf(self.v[i, 0]) or np.isinf(self.v[i, 1]) \
				or np.isneginf(self.v[i, 0]) or np.isneginf(self.v[i, 1]
			):
				print('last x = ', self.x[i - 1])

				# Очистка списков от мусора
				self.x = np.delete(self.x, np.s_[i:], axis=0)
				self.v = np.delete(self.v, np.s_[i:], axis=0)
				self.u = np.delete(self.u, np.s_[i:], axis=0)
				self.h = np.delete(self.h, np.s_[i:], axis=0)
				self.c1 = np.delete(self.c1, np.s_[i:], axis=0)
				self.c2 = np.delete(self.c2, np.s_[i:], axis=0)
				self.olp = np.delete(self.olp, np.s_[i:], axis=0)
				self.lambdas = np.delete(self.lambdas, np.s_[i:], axis=0)

				break

	def output(self):
		"""
		Формирование результата
		"""

		if self.f:
			self.algoSolution()
		else:
			self.algoSolution_olp()
			self.olp = (2 ** self.P) * self.S

		# смещение шага интегрирования
		self.h2 = np.concatenate(([0], self.h[:-1]))
		self.E = np.subtract(self.u, self.v)

		ndata = pd.DataFrame({
			'n': np.arange(self.node), 'x': np.round(self.x, len(str(self.eps))) if not self.f else np.around(self.x, 16), 'h': self.h2,  \
			'u(1)': self.u[:, 0], 'u(2)': self.u[:, 1], \
			'v(1)': self.v[:, 0], 'v(2)': self.v[:, 1], \
			'exp(-1000*x)': self.lambdas[:, 0], 'exp(-0.01*x)': self.lambdas[:, 1], \
			'|ОЛП|(1)': self.olp[:, 0], '|ОЛП|(2)': self.olp[:, 1], \
			'c1': self.c1, 'c2': self.c2, \
			'E(1)': self.E[:, 0], 'E(2)': self.E[:, 1]
		})

		return ndata