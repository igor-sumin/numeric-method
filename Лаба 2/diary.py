import pandas as pd
import numpy as np
# import sys

class Lab_test:
    def __init__(self, num_part):
        """
        Определение параметров и компонент стационарного уравнения теплоемкости
        """

        # if num_part == 0:
        #     sys.exit()

        self.n = num_part
        self.node = self.n + 1
        
        self.start, self.end = 0, 2
        # шаг интегрирования
        self.h = (self.end - self.start) / self.n
        
        # целый шаг
        self.x = [self.start + i * self.h for i in range(self.node)]
        # половинный шаг
        self.x2 = [self.start + (i + 0.5) * self.h for i in range(self.node - 1)]
        
        self.mu = np.array([13, 19])
        self.kappa = np.array([0, 0])
        # точка разрыва
        self.ksi = 0.4
        
        # для a
        self.k1 = lambda x: 3
        self.k2 = lambda x: 7

        # для d
        self.q1 = lambda x: 0
        self.q2 = lambda x: 5

        # для phi
        self.f1 = lambda x: 10
        self.f2 = lambda x: -15
    
    def analytic(self):
        """
        Построение точного решения 
        """ 
        def first(x):
            return -5/3 * x ** 2 - 5.3049817 * x + 13

        def second(x):
            return 3.653153288 * np.exp(np.sqrt(35) * x / 7) + np.exp((-1) * np.sqrt(35) * x / 7) * \
            ((-1) * (3.653153288 * np.exp(2 * np.sqrt(35) / 7)) / (np.exp(-np.sqrt(35) * 2 / 7)) + (22 / (np.exp(-np.sqrt(35) * 2 / 7)))) - 3

        return np.array([first(self.x[i]) if self.x[i] < self.ksi else second(self.x[i]) for i in range(self.node)])
    
    def numerical(self):
        """
        Построение численного решения 
        """
        
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
                self.phi[i] = (self.f1(self.x[i]) + self.f2(self.x[i])) / 2
                self.d[i] = (self.q1(self.x[i]) + self.q2(self.x[i])) / 2
        
        # подсчет a
        j = 1
        for i in range(self.n):
            if self.ksi >= self.x[j]:
                self.a[i] = self.k1(self.x2[i])

            elif self.ksi <= self.x[j - 1]:
                self.a[i] = self.k2(self.x2[i])

            elif self.x[j - 1] < self.ksi < self.x[j]:
                self.a[i] = 1 / (1 / (2 * self.k1(self.x[i])) + 1 / (2 * self.k2(self.x[i])))

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
        self.C = (-1) * np.diag(self.AA)[1:-1]
        self.b = np.concatenate(([self.mu[0]], -self.phi, [self.mu[1]]))

        print("C: ", self.C)
        print("B: ", self.B)
        print("A: ", self.A)
        print("AA: \n", self.AA)
        print("b: \n", self.b)

        # найдем v
        return self.run_through()
        
    def calcdiag(self, k):
        if k == 0:
            # главная диаг = 1 a1 ... an-1 1
            return np.concatenate(
                ([1], (-1) * np.array([self.a[i] / (self.h ** 2) + self.a[i + 1] / (self.h ** 2) + self.d[i] for i in range(self.n - 1)]), [1])
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

        # i = 1, n - 1
        for i in range(self.n - 1):
            alpha[i + 1] = self.B[i] / (self.C[i] - self.A[i] * alpha[i])
            beta[i + 1] = (self.phi[i] + self.A[i] * beta[i])/ (self.C[i] - self.A[i] * alpha[i])

        return alpha, beta

    def difference(self):
        """
        Разница численного и точного решений
        """
        # print("u = ", self.u, "\nv = ", self.v)
        return np.absolute(self.u - self.v)

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

        self.u = self.analytic()
        self.v = np.concatenate(([self.mu[0]], self.numerical()))
        self.dif = self.difference()

        # таблица
        ndata = pd.DataFrame({
            'n': np.arange(self.node), 'x': np.round(self.x, 3), 'u(x)': np.round(self.u, 14), 'v(x)': np.round(self.v, 14), \
            '|u(x) - v(x)|': np.round(self.dif, 14)
        })

        # записи
        note = np.array([self.n, self.dif[self.node // 2 if self.node % 2 == 1 else int(self.node / 2 - 1)], np.argmax(self.dif)])

        return note, ndata