import pandas as pd
import numpy as np

class NonStat:
	def __init__(self, T_, n_, m_):
		"""Нестационарное уравнение теплопроводности. Неявная схема. Задача 10"""

		# участки по x, t
		self.n = n_
		self.node = self.n + 1
		self.m = m_
		self.mode = self.m + 1

		# конечная температура
		self.T = T_
		self.a, self.b = 0, 1

		self.kappa = np.array([0, 0])

		# h - шаг по x
		self.h = (self.b - self.a) / self.n
		# x - узлы сетки по x
		self.x = [self.a + i * self.h for i in range(self.node)]

		# print('h = ', self.h)

		# tau - шаг по t
		self.tau = self.T / self.m
		# t - узлы сетки по времени
		self.t = [j * self.tau for j in range(self.mode)]

		# print('t = ', self.tau)

		# gamma - коэф-т
		self.gamma = 2
		# g(x, t) - функция
		self.g = lambda x, t: np.exp(-t) * np.sin(7 * np.pi * x) + 1
		# ui0 - начальное условие, i = 0,node
		self.phi = lambda x: 1 - x ** 2

		# u0j - ГУ 1 рода (левый уонец стержня), j = 1,mode
		self.mu1 = lambda t: np.cos(t)
		# unodej - ГУ 1 рода (правый уонец стержня), j = 1,mode
		self.mu2 = lambda t: np.sin(4 * t)

		# решетка на прямоугольнике [n, m] - матрица с узлами сетки с координатами (xi, tj), i=1,node-1; j=1,mode
		self.u = np.empty([self.node, self.mode], dtype=np.double)
		# print('u = ', self.u)
		# print('shape = ', self.u.shape)
		# print()
		# print('x = ', self.x)
		# print('t = ', self.t)
		# print()

		# коэф-ты для системы (13)
		self.A = self.gamma ** 2 * self.tau / (self.h ** 2)
		self.B = self.A
		self.C = 1 + 2 * self.A

		self.PH = lambda i, j: self.u[i, j - 1] + self.g(self.x[i], self.t[j]) * self.tau

	def numerical(self, jdx):
		"""Построение СЛАУ трехдиагональной матрицы"""

		# нижняя, главная, верхняя диагонали
		bottom = np.diag(self.calcdiag(-1), k=-1)
		middle = np.diag(self.calcdiag(0), k=0)
		high = np.diag(self.calcdiag(1), k=1)

		# Построим разностную схему в матричном виде: (AAvj = b)
		AA = bottom + middle + high

		# ищем b
		b = np.concatenate((
			[self.mu1(self.t[jdx])], [-self.PH(i, jdx) for i in range(1, self.n)], [self.mu2(self.t[jdx])]
		))

		return self.run_through(jdx)

	def calcdiag(self, k):
		if k == 0:
			# главная диаг = 1 a1 ... an-1 1
			return np.concatenate((
				[1], np.full(self.n - 1, self.C), [1]
			))

		elif k == -1:
			# нижняя диаг = a1 ... an-1 -kappa2
			return np.concatenate((
				np.full(self.n - 1, self.A), [-self.kappa[1]]
			))
		else:
			# верхняя диаг = -kappa1 a2 ... an
			return np.concatenate((
				[-self.kappa[0]], np.full(self.n - 1, self.B)
			))

		assert False

	def direct(self, jdx):
		"""Прямой ход прогонки"""

		# находим параметры
		alpha = np.empty(self.node, np.double)
		beta = np.empty(self.node, np.double)

		# начальное условие
		alpha[0] = self.kappa[0]
		beta[0] = self.mu1(self.t[jdx])

		for i in range(self.node - 1):
			alpha[i + 1] = self.B / (self.C - self.A * alpha[i])
			beta[i + 1] = (self.PH(i, jdx) + self.A * beta[i]) / (self.C - self.A * alpha[i])

		return alpha, beta

	def reverse(self, alpha, beta, jdx):
		"""Обратный ход прогонки"""

		# находим численное решение
		vj = np.empty(self.node, np.double)

		# начальное и конечное условия
		vj[0] = self.mu1(self.t[jdx])
		vj[-1] = (-self.kappa[1] * beta[-1] - self.mu2(self.t[jdx])) / (self.kappa[1] * alpha[-1] - 1)

		for i in range(self.node - 2, 0, -1):
			vj[i] = alpha[i + 1] * vj[i + 1] + beta[i + 1]

		return vj

	def run_through(self, jdx):
		"""Метод прогонки"""
		
		alpha, beta = self.direct(jdx)
		# print()
		# print('alpha = ', alpha)
		# print('beta = ', beta)
		# print()
		vj = self.reverse(alpha, beta, jdx)

		return vj

	def Solution(self):
		"""Применяем систему (14) (смотри фото)"""

		# находим нач условия
		for i in range(self.node):
			# ui0
			self.u[i, self.a] = self.phi(self.x[i])

		for j in range(1, self.mode):
			# u0j
			self.u[-1, j] = self.mu1(self.t[j])
			# unj
			self.u[self.a, j] = self.mu2(self.t[j])

		# print('self = ', self.u)

		for j in range(1, self.mode):
			self.u[:, j] = self.numerical(j)

		self.u = self.u.T

	def output(self):
		"""Сбор результатов"""

		self.Solution()

		x, t = np.meshgrid(self.x, self.t)

		a = sorted(list(np.arange(self.mode)) * self.node)
		b = sorted(list(self.t) * self.node)
		iterables = np.array([a, b])
		index = list(pd.MultiIndex.from_arrays(iterables, names=['j', 'tj']))
		arra = np.asarray(index)

		# таблица
		df = pd.DataFrame({
			'tj': np.around(arra[:, 1], 7), \
			'i': list(np.arange(self.node, dtype=np.int)) * self.mode, \
			'xi': np.around(list(self.x) * self.mode, 7), \
			'vij': np.around(self.u.ravel(), 14)
		})

		# pd.set_option('display.max_rows', df.shape[0] + 1)
		# print(df.head(50))

		return np.array([x, t, self.u]), df