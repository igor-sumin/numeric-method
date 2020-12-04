import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class NineLab:
	def __init__(self, params_phys, params_rk):
		"""
		Определение параметров для решения 9 задачи
		"""

		# Инициализация параметров
		self.L, self.R, self.E0, self.w, self.I0, self.V = params_phys
		self.h0, self.n, self.eps, self.xmin, self.xmax, self.xeps = params_rk
		print(params_rk)

		# Порядок метода РК-3
		self.P = 3
		# Количество узлов
		self.node = int(self.n) + 1

		self.Ij = np.empty(self.node, dtype=np.double)
		self.uj = np.empty(self.node, dtype=np.double)
		self.yj = np.empty(self.node, dtype=np.double)
		self.x = np.empty(self.node, dtype=np.double)
		self.I2j = np.empty(self.node, dtype=np.double)
		self.h = np.empty(self.node, dtype=np.double)
		self.S = np.empty(self.node, dtype=np.double)
		self.c1 = np.zeros(self.node, dtype=np.int)
		self.c2 = np.zeros(self.node, dtype=np.int)

		self.x[0] = self.xmin
		self.Ij[0] = self.I0
		self.uj[0] = self.I0
		self.yj[0] = self.I0
		self.I2j[0] = 0.
		self.h[0] = self.h0
		self.S[0] = 0.

	def didx(self, x, v):
		""" Заданная функция """
		return 1 / self.L * (self.E0 * np.sin(self.w * x) - self.R * v)

	def Exactly(self, x):
		""" Точное решение """

		par1 = self.I0 + (self.E0 * self.w * self.L / (self.w ** 2 * self.L ** 2 + self.R ** 2))

		return (self.E0 * (-np.cos(self.w * x) * self.w * self.L + np.sin(self.w * x) * self.R) + par1 * np.exp(-self.R * x / self.L) * \
			(self.w ** 2 * self.L ** 2 + self.R ** 2)) / (self.w ** 2 * self.L ** 2 + self.R ** 2)

	def Exactly2(self, x):
		""" Точное решение 2"""

		par1 = self.I0 - self.V / self.R
		return self.V / self.R + par1 * np.exp(-self.R * x / self.L)

	def RK_III(self, x, v, h):
		""" Численное решение задачи методом РК-3 """
		
		k1 = self.didx(x, v)
		k2 = self.didx(x + h / 2, v + h / 2 * k1)
		k3 = self.didx(x + h, v + h * (-k1 + 2 * k2))
		
		x_ = x + h
		v_ = v + h / 6 * (k1 + 4 * k2 + k3)

		return x_, v_

	def ControlLocErr(self, x, v, h, idx, f):
		""" Контроль локальной погрешности (ЛП) """

		x_next, v_next = self.RK_III(x, v, h)
		x_half, self.I2j[idx] = self.RK_III(x, v, h / 2)
		x_new, v_new  = self.RK_III(x_half, self.I2j[idx], h / 2)
		
		self.S[idx] = (v_new - v_next) / (2 ** self.P - 1)
		
		return self.ControlCompare(x, v, h, idx, f)

	def ControlCompare(self, x, v, h, idx, f):
		""" Контроль локальной погрешности (ЛП) (продолжение) """

		self.S[idx] = np.absolute(self.S[idx])
		self.c1[idx] = self.c1[idx - 1]
		self.c2[idx] = self.c2[idx - 1]

		zn = 2 ** (self.P + 1)
		
		if (self.eps / zn) <= self.S[idx] <= self.eps:
			self.h[idx] = h

			return True

		elif f and self.S[idx] < (self.eps / zn):
			self.h[idx] = h * 2
			self.c1[idx] += 1

			return True

		else:
			self.h[idx] = h / 2
			self.c2[idx] += 1

			return False

		raise Exception('MyNineLab.py / 98 строка')

	def algoSolution(self):
		""" Численное и точное решение жесткой системы ОДУ """

		f = True
		for i in range(1, self.node):
			self.x[i], self.Ij[i] = self.RK_III(self.x[i - 1], self.Ij[i - 1], self.h[i - 1])
			self.uj[i] = self.Exactly(self.x[i])
			self.yj[i] = self.Exactly2(self.x[i])

			if not self.ControlLocErr(self.x[i - 1], self.Ij[i - 1], self.h[i - 1], i, True):
				self.ControlLocErr(self.x[i - 1], self.Ij[i - 1], self.h[i - 1], i, True)

			if ((self.xmax - self.x[i]) < 0):
				# xn
				self.h[i - 1] /= 2
				self.c2[i - 1] += 1
				# i -= 1
				while self.x[i - 1] > self.xmax or (self.x[i - 1] < (self.xmax - self.xeps)):
					# считаем для i+1
					self.x[i], self.Ij[i] = self.RK_III(self.x[i - 1], self.Ij[i - 1], self.h[i - 1])
					self.uj[i] = self.Exactly(self.x[i])
					self.yj[i] = self.Exactly2(self.x[i])

					if not self.ControlLocErr(self.x[i - 1], self.Ij[i - 1], self.h[i - 1], i, False):
						self.ControlLocErr(self.x[i - 1], self.Ij[i - 1], self.h[i - 1], i, False)

					# xn+1 > xmax
					if self.x[i] > self.xmax:
						# xn
						self.h[i - 1] /= 2
						self.c2[i - 1] += 1
						# i -= 1
						continue

					i += 1

				f = False

			if not f or np.isnan(self.Ij[i]) or np.isinf(self.Ij[i]) or np.isneginf(self.Ij[i]):
				print('last x = ', self.x[i - 1])

				# Очистка списков от мусора
				self.x = np.delete(self.x, np.s_[i:])
				self.Ij = np.delete(self.Ij, np.s_[i:])
				self.I2j = np.delete(self.I2j, np.s_[i:])
				self.S = np.delete(self.S, np.s_[i:])
				self.h = np.delete(self.h, np.s_[i:])
				self.c1 = np.delete(self.c1, np.s_[i:])
				self.c2 = np.delete(self.c2, np.s_[i:])
				self.uj = np.delete(self.uj, np.s_[i:])
				self.yj = np.delete(self.yj, np.s_[i:])

				break

		self.difIj_I2j = np.subtract(self.Ij, self.I2j)
		self.difuj_Ij = np.absolute(self.uj - self.Ij)
		self.olp = (2 ** self.P) * self.S
		# self.olp = self.S

	def output(self):
		""" Формирование результата """

		self.algoSolution()

		# допили ОЛП
		cols = ['n', 'x', 'Ij', 'I2j', 'Ij - I2j', '|ОЛП|', 'hj', 'C1', 'C2', 'uj', '| uj - Ij |', 'yj']
		ndata = pd.DataFrame({
			cols[0]: np.arange(len(self.x)), cols[1]: np.round(self.x, len(str(self.xeps))), cols[2]: self.Ij, cols[3]: self.I2j, \
			cols[4]: self.difIj_I2j, cols[5]: self.olp, cols[6]: self.h, cols[7]: self.c1, cols[8]: self.c2, \
			cols[9]: self.uj, cols[10]: self.difuj_Ij, cols[11]: self.yj
		})

		# print('ndata = ', ndata)
		# pd.set_option('display.max_rows', ndata.shape[0] + 1)
		
		return ndata