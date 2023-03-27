import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100 * np.pi, 100)


def f(x):
    return np.sin(7 * x) + np.cos(4 * x)


f_values = np.vectorize(f)(x)

plt.plot(x, f_values, label='sen(7x) + cos(4x)')
# plt.plot(x, g_values, label='cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.xlim([0, 300])
plt.show()
