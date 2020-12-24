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

		# точка разрыва
		self.ksi = 0.5
		self.mu = np.array([1, 1])
		self.kappa = np.array([0, 0])

		# для a
		self.k1 = lambda x: np.exp(-x) * np.sqrt(np.exp(1))
		self.k2 = lambda x: 1

		# для d
		self.q1 = lambda x: 2
		self.q2 = lambda x: np.sin(np.pi * x)

		# для phi
		self.f1 = lambda x: np.cos(np.pi * x)
		self.f2 = lambda x: np.exp(x) / np.sqrt(np.exp(1))

	def numerical(self, k):
		"""
		Построение численного решения v(xi)
		"""

		# введем новые переменные
		self.phi = np.empty(k * self.n - 1, np.double)
		self.d = np.empty(k * self.n - 1, np.double)
		self.a = np.empty(k * self.n, np.double)

		# подсчет phi, d
		j = 1
		for i in range(k * self.n - 1):
			if self.ksi >= self.x2[i + 1]:
				self.phi[i] = self.f1(self.x[j])
				# self.phi[i] = 1 / (self.h * np.pi) * (np.sin(np.pi * self.x2[i + 1]) - np.sin(np.pi * self.x2[i]))
				
				self.d[i] = self.q1(self.x[j])
				# self.d[i] = 2 / self.h * (self.x2[i + 1] - self.x2[i])

			elif self.ksi <= self.x2[i]:
				self.phi[i] = self.f2(self.x[j])
				# self.phi[i] = 1 / (self.h * np.sqrt(np.exp(1))) * (np.exp(self.x2[i + 1]) - np.exp(self.x2[i]))

				self.d[i] = self.q2(self.x[j])
				# self.d[i] = 1 / (self.h * np.pi) * (-np.cos(np.pi * self.x2[i + 1]) + np.cos(np.pi * self.x2[i]))

			elif self.x2[i] < self.ksi < self.x2[i + 1]:
				self.phi[i] = (1 / self.h) * (
					self.f1((self.x2[i] + self.ksi) / 2) * (self.ksi - self.x2[i]) + \
					self.f2((self.ksi + self.x2[i + 1]) / 2) * (self.x2[i + 1] - self.ksi)
				)
				# self.phi[i] = 1 / self.h * (
				# 	(1 / np.pi) * (np.sin(np.pi * self.ksi) - np.sin(np.pi * self.x2[i])) \
				# 	+ (1 / np.sqrt(np.exp(1))) * (np.exp(self.x2[i + 1]) - np.exp(self.ksi))
				# )

				self.d[i] = (1 / self.h) * (
					self.q1((self.x2[i] + self.ksi) / 2) * (self.ksi - self.x2[i]) + \
					self.q2((self.ksi + self.x2[i + 1]) / 2) * (self.x2[i + 1] - self.ksi)
				)
				# self.d[i] = 1 / self.h * (2 * (self.ksi - self.x2[i]) + 1 / np.pi * (-np.cos(self.x2[i + 1] * np.pi) + np.cos(np.pi * self.ksi)))

			j += 1

		# подсчет a
		j = 1
		for i in range(k * self.n):
			if self.ksi >= self.x[j]:
				self.a[i] = self.k1(self.x2[i])
				# self.a[i] = (self.h * np.sqrt(np.exp(1))) / (np.exp(self.x[j]) - np.exp(self.x[j - 1]))

			elif self.ksi <= self.x[j - 1]:
				self.a[i] = self.k2(self.x2[i])
				# self.a[i] = self.h / (self.x[j] - self.x[j - 1])


			elif self.x[j - 1] < self.ksi < self.x[j]:
				self.a[i] = 1 / ((1 / self.h) * (
					((self.ksi - self.x[i]) / (self.k1((self.x[i] + self.ksi) / 2))) + \
					((self.x[i + 1] - self.ksi) / (self.k2((self.ksi + self.x[i + 1]) / 2))) 
				))
				# self.a[i] = (self.h * np.sqrt(np.exp(1))) / (np.exp(self.ksi) - np.exp(self.x[j - 1]) + self.x[j] - self.ksi)

			j += 1

		# print()
		# print("phi: ", self.phi)
		# print("d: ", self.d)
		# print("a: ", self.a)
		# print()

		# # нижняя, главная, верхняя диагонали
		# bottom = np.diag(self.calcdiag(-1, k), k=-1)
		# middle = np.diag(self.calcdiag(0, k), k=0)
		# high = np.diag(self.calcdiag(1, k), k=1)

		# # Построим разностную схему в матричном виде: (AAv = b)
		# self.AA = bottom + middle + high

		# self.A = np.diag(self.AA, k=-1)[:-1]
		# self.B = np.diag(self.AA, k=1)[1:]
		# self.C = (-1) * np.diag(self.AA)[1:-1]
		# self.b = np.concatenate(([self.mu[0]], -self.phi, [self.mu[1]]))

		# нижняя диаг
		self.A = np.array([self.a[i] / (self.h ** 2) for i in range(k * self.n - 1)])
		# верхняя диаг
		self.B = np.array([self.a[i] / (self.h ** 2) for i in range(1, k * self.n)])
		# главная диаг
		self.C = np.array([self.a[i] / (self.h ** 2) + self.a[i + 1] / (self.h ** 2) + self.d[i] for i in range(k * self.n - 1)])

		# print("AA: \n", self.AA)
		# print("A: ", self.A)
		# print("B: ", self.B)
		# print("C: ", self.C)
		# print("b: \n", self.b)
		# print()

		# найдем v
		return self.run_through(k)

	def calcdiag(self, k, k1):
		if k == 0:
			# главная диаг = 1 a1 ... an-1 1
			return np.concatenate(
				([1], (-1) * np.array([self.a[i] / (self.h ** 2) + self.a[i + 1] / (self.h ** 2) + self.d[i] for i in range(k1 * self.n - 1)]), [1])
			)

		elif k == -1:
			# нижняя диаг = a1 ... an-1 -kappa2
			return np.concatenate(
				(np.array([self.a[i] / (self.h ** 2) for i in range(k1 * self.n - 1)]), [-self.kappa[1]])
			)
		else:
			# верхняя диаг = -kappa1 a2 ... an
			return np.concatenate(
				([-self.kappa[0]], np.array([self.a[i] / (self.h ** 2) for i in range(1, k1 * self.n)]))
			)

	def direct(self, k):
		"""
		Прямой ход прогонки
		"""

		# находим параметры
		alpha = np.empty(k * self.n, np.double)
		beta = np.empty(k * self.n, np.double)

		# нач условие (3) 
		alpha[0] = self.kappa[0]
		beta[0] = self.mu[0]

		# i = 1, n
		for i in range(k * self.n - 1):
			alpha[i + 1] = self.B[i] / (self.C[i] - self.A[i] * alpha[i])
			beta[i + 1] = (self.phi[i] + self.A[i] * beta[i]) / (self.C[i] - self.A[i] * alpha[i])

		return alpha, beta

	def reverse(self, k):
		"""
		Обратный ход прогонки
		"""

		# находим численное решение
		y = np.empty(k * self.n, np.double)

		# нач условие (6)
		y[-1] = (-self.kappa[1] * self.beta[-1] - self.mu[1]) / (self.kappa[1] * self.alpha[-1] - 1)

		# i = 0, n - 1
		for i in range(k * self.n - 2, -1, -1):
		    y[i] = self.alpha[i + 1] * y[i + 1] + self.beta[i + 1]

		return y

	def run_through(self, k):
		"""
		Метод прогонки
		"""

		self.alpha, self.beta = self.direct(k)
		# print('alpha = ', self.alpha)
		# print('beta = ', self.beta)

		return self.reverse(k)

	def Solution(self):
		"""
		Составление таблицы
		"""

		# численные решения
		k = 1

		self.h = (self.end - self.start) / self.n
		self.x = [self.start + i * self.h for i in range(self.node)]
		self.x2 = [self.start + (i + 0.5) * self.h for i in range(self.node - 1)]
		self.v = np.concatenate(([self.mu[0]], self.numerical(k)))

		# print('x = ', self.x)
		# print('x2 = ', self.x2)
		# print('v = ', self.v)

		# численное решение с половинным шагом
		k = 2
		self.h /= 2
		self.x = [self.start + i * self.h for i in range(self.node * k)]
		self.x2 = [self.start + (i + 0.5) * self.h for i in range(self.node * k - 1)]
		self.v2 = np.concatenate(([self.mu[0]], self.numerical(k)))[::2]

		# print('new x = ', self.x)
		# print('new x2 = ', self.x2)
		# print('v2 = ', self.v2)

		# разница численных решений
		self.dif = np.absolute(self.v - self.v2)
		self.x = self.x[::2]

		# таблица
		ndata = pd.DataFrame({
			'№ узла': np.arange(self.node), 'x': np.round(self.x, len(str(self.h))), 'v(x)': np.round(self.v, 14), \
			'v2(x2i)': np.round(self.v2, 14), '|v(x) - v2(x2i)|': np.round(self.dif, 14)
		})

		# записи
		note = np.array([self.n, self.dif[self.node // 2 if self.node % 2 == 1 else int(self.node / 2 - 1)], np.argmax(self.dif)])

		# pd.set_option('display.max_rows', ndata.shape[0] + 1)
		# print(ndata)

		return note, ndata