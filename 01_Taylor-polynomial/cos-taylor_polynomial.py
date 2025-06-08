import numpy as np
import matplotlib.pyplot as plt

p0 = lambda a : 1 + 0*a
p2 = lambda a : 1 - a**2/2
p4 = lambda a : 1 - a**2/2 + a**4/24
p6 = lambda a : 1 - a**2/2 + a**4/24 - a**6/720
p8 = lambda a : 1 - a**2/2 + a**4/24 - a**6/720 + a**8/40320

x = np.arange(-np.pi, np.pi, 0.01)

fig, ax = plt.subplots()

ax.plot(x, np.cos(x), label='cos(x)')
ax.plot(x, p0(x), 'g', label='p0')
ax.plot(x, p2(x), 'm', label='p2')
ax.plot(x, p4(x), 'k', label='p2')
ax.plot(x, p6(x), 'r', label='p4')
ax.plot(x, p8(x), 'c', label='p6')


legend = ax.legend(loc='best')
ax.set(xlim=(-np.pi, np.pi), ylim=(-1.2, 1.1))
plt.show()

