import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from MyNineLab import NineLab

plt.style.use('ggplot')
params = {
    'legend.fontsize': 'small',
    'legend.handlelength': 2,
}
plt.rcParams.update(params)

# list(map(np.double, input('L = ').split()))
# list(map(np.double, input('R = ').split()))
# list(map(np.double, input('I0 = ').split()))
# list(map(np.double, input('E0 = ').split()))
# list(map(np.double, input('w = ').split()))
# list(map(np.double, input('V = ').split()))
# list(map(np.double, input('h0 = ').split()))
# list(map(np.double, input('nmax = ').split()))
# list(map(np.double, input('eps = ').split()))
# list(map(np.double, input('xmax = ').split()))
# list(map(np.double, input('epsx = ').split()))

k = int(input('how = '))
def func(text):
    res = k * [1.0, 1.0]
    while len(res) != k:
        res = list(map(np.double, input(text).split()))

    return res    

L = func('L = ')
R = func('R = ')
I0 = func('I0 = ')
E0 = func('E0 = ')
w = func('w = ')
V = func('V = ')

h0 = func('h0 = ')
nmax = func('nmax = ')
eps = func('eps = ')
xmax = func('xmax = ')
epsx = func('epsx = ')

plt.title('Зависимость переменных токов I, I1\n и тока с самоиндукцией I2 от времени x')
plt.ylabel('I, A')
plt.xlabel('x, c')

for i in range(k):
    ph = np.array([L[i], R[i], E0[i], w[i], I0[i], V[i]])
    rk = np.array([h0[i], nmax[i], eps[i], xmax[i], epsx[i]])

    print('ph = ', ph)
    print('rk = ', rk)

    result = NineLab(ph, rk)
    ndata = result.output()

    plt.plot(ndata['x'], ndata['I'], label='({0}) численное решение для переменного тока'.format(i + 1))
    plt.plot(ndata['x'], ndata['I1'], label='({0}) точное решение для переменного тока'.format(i + 1))
    plt.plot(ndata['x'], ndata['I2'], label='({0}) точное решение для тока с самоиндукцией'.format(i + 1))

plt.legend(loc='best')
plt.show()