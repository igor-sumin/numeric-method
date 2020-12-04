import pandas as pd
import numpy as np

# special
from scipy.integrate import quad

class Lab_main:
	def __init__(self, num_part):
		"""
		Определение параметров и компонент стационарного уравнения теплоемкости
		"""

		self.n = num_part
		self.node = self.n + 1

		self.start, self.end = 0, 1
		# шаг интегрирования
		self.h = (self.end - self.start) / self.n

		# целый шаг
		self.x = [self.start + i * self.h for i in range(self.node)]
		# половинный шаг
		self.x2 = [self.start + (i + 0.5) * self.h for i in range(self.node - 1)]

		self.mu = np.array([1, 1])
		self.kappa = np.array([0, 0])
		# точка разрыва
		self.ksi = 0.5

		# n1 = len(list(filter(lambda x: x < self.ksi, self.x)))
		# n2 = self.node - n1

		# self.k = lambda x: 1 / (np.exp(-x) * np.sqrt(np.exp(1))) if (x < 0.5) else 1
		# self.q = lambda x: 2 if (x < 0.5) else np.sin(np.pi * x)
		# self.f = lambda x: np.cos(np.pi * x) if (x < 0.5) else np.exp(x) / np.sqrt(np.exp(1))

		# для a
		self.k1 = lambda x: np.exp(-x) * np.sqrt(np.exp(1))
		self.k2 = lambda x: 1

		# для d
		self.q1 = lambda x: 2
		# self.q2 = lambda x: np.sin(np.pi * x * np.pi / 180)
		self.q2 = lambda x: np.sin(np.pi * x)

		# для phi
		# self.f1 = lambda x: np.cos(np.pi * x * np.pi / 180)
		self.f1 = lambda x: np.cos(np.pi * x)
		self.f2 = lambda x: np.exp(x) / np.sqrt(np.exp(1))

	def numerical(self):
		"""
		Построение численного решения v(xi)
		"""

		# # введем новые переменные
		# self.phi = np.array([(1 / self.h) * quad(self.f, self.x2[i - 1], self.x2[i])[0] for i in range(1, self.n)])
		# self.d = np.array([(1 / self.h) * quad(self.q, self.x2[i - 1], self.x2[i])[0] for i in range(1, self.n)])
		# self.a = np.array([(1 / (1 / self.h) * quad(self.k, self.x[i - 1], self.x[i])[0]) for i in range(1, self.n + 1)])

		# введем новые переменные
		self.phi = np.empty(self.n - 1, np.double)
		self.d = np.empty(self.n - 1, np.double)
		self.a = np.empty(self.n, np.double)

		# подсчет phi, d
		for i in range(self.n - 1):
			if self.ksi >= self.x2[i + 1]:
				self.phi[i] = self.f1(self.x[i])
				self.d[i] = self.q1(self.x[i])

			elif self.ksi <= self.x2[i]:
				self.phi[i] = self.f2(self.x[i])
				self.d[i] = self.q2(self.x[i])

			elif self.x2[i] < self.ksi < self.x2[i + 1]:
				self.phi[i] = (1 / self.h) * (
					self.f1((self.x2[i] + self.ksi) / 2) * (self.ksi - self.x2[i]) + \
					self.f2((self.ksi + self.x2[i + 1]) / 2) * (self.x2[i + 1] - self.ksi)
				)

				self.d[i] = (1 / self.h) * (
					self.q1((self.x2[i] + self.ksi) / 2) * (self.ksi - self.x2[i]) + \
					self.q2((self.ksi + self.x2[i + 1]) / 2) * (self.x2[i + 1] - self.ksi)
				)

		# подсчет a
		j = 1
		for i in range(self.n):
			if self.ksi >= self.x[j]:
				self.a[i] = self.k1(self.x2[i])

			elif self.ksi <= self.x[j - 1]:
				self.a[i] = self.k2(self.x2[i])

			elif self.x[j - 1] < self.ksi < self.x[j]:
				self.a[i] = 1 / ((1 / self.h) * (
					((self.ksi - self.x[i]) / (self.k1((self.x[i] + self.ksi) / 2))) + \
					((self.x[i + 1] - self.ksi) / (self.k2((self.ksi + self.x[i + 1]) / 2))) 
				))

			j += 1

		print()
		print("phi: ", self.phi)
		print("d: ", self.d)
		print("a: ", self.a)
		print()

		# нижняя, главная, верхняя диагонали
		bottom = np.diag(self.calcdiag(-1), k=-1)
		middle = np.diag(self.calcdiag(0), k=0)
		high = np.diag(self.calcdiag(1), k=1)

		# Построим разностную схему в матричном виде: (AAv = b)
		self.AA = bottom + middle + high

		self.A = np.diag(self.AA, k=-1)[:-1]
		self.B = np.diag(self.AA, k=1)[1:]
		self.C = np.diag(self.AA)[1:-1]
		self.b = np.concatenate(([self.mu[0]], -self.phi, [self.mu[1]]))

		print("AA: \n", self.AA)
		print("A: ", self.A)
		print("B: ", self.B)
		print("C: ", self.C)
		print("b: \n", self.b)
		print()

		# найдем v
		return self.run_through()

	def calcdiag(self, k):
		if k == 0:
			# главная диаг = 1 a1 ... an-1 1
			return np.concatenate(
				([1], np.array([self.a[i] / (self.h ** 2) + self.a[i + 1] / (self.h ** 2) + self.d[i] for i in range(self.n - 1)]), [1])
			)

		elif k == -1:
			# нижняя диаг = a1 ... an-1 -kappa2
			return np.concatenate(
				(np.array([self.a[i] / (self.h ** 2) for i in range(self.n - 1)]), [-self.kappa[1]])
			)
		else:
			# верхняя диаг = -kappa1 a2 ... an
			return np.concatenate(
				([-self.kappa[0]], np.array([self.a[i] / (self.h ** 2) for i in range(1, self.n)]))
			)

	def direct(self):
		"""
		Прямой ход прогонки
		"""

		# находим параметры
		alpha = np.empty(self.n, np.double)
		beta = np.empty(self.n, np.double)

		# нач условие (3) 
		alpha[0] = self.kappa[0]
		beta[0] = self.mu[0]

		# i = 1, n
		for i in range(self.n - 1):
			alpha[i + 1] = self.B[i] / (self.C[i] - self.A[i] * alpha[i])
			beta[i + 1] = (self.phi[i] + self.A[i] * beta[i])/ (self.C[i] - self.A[i] * alpha[i])

		return alpha, beta

	def reverse(self):
		"""
		Обратный ход прогонки
		"""

		# находим численное решение
		y = np.empty(self.n, np.double)

		# нач условие (6)
		y[-1] = (-self.kappa[1] * self.beta[-1] - self.mu[1]) / (self.kappa[1] * self.alpha[-1] - 1)

		# i = 0, n - 1
		for i in range(self.n - 2, -1, -1):
		    y[i] = self.alpha[i + 1] * y[i + 1] + self.beta[i + 1]

		return y

	def run_through(self):
		"""
		Метод прогонки
		"""

		self.alpha, self.beta = self.direct()
		# print("alp = ", self.alpha, "\nbeta = ", self.beta)
		return self.reverse()

	def Solution(self):
		"""
		Составление таблицы
		"""

		self.v = np.concatenate(([self.mu[0]], self.numerical()))

		# таблица
		ndata = pd.DataFrame({'x': self.x, 'v(x)': self.v}, index=np.arange(self.node))
		ndata.index.name = "№ узла"

		pd.set_option('display.max_rows', ndata.shape[0] + 1)


		return ndata