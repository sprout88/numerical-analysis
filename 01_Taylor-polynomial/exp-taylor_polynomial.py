
p0 = lambda a : 1 + 0*a
p1 = lambda a : 1 + a
p2 = lambda a : 1 + a + a**2/2
p3 = lambda a : 1 + a + a**2/2 + a**3/6
p4 = lambda a : 1 + a + a**2/2 + a**3/6 + a**4/24
p5 = lambda a : 1 + a + a**2/2 + a**3/6 + a**4/24 + a**5/120

import numpy as np

x = np.arange(-1, 3, 0.01)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, p1(x), 'g', label='p0')
ax.plot(x, p2(x), 'm', label='p0')
ax.plot(x, p3(x), 'k', label='p0')
ax.plot(x, p4(x), 'b', label='p0')
ax.plot(x, p5(x), 'y', label='p0')
ax.plot(x, p5(x), 'c', label='p0') # most accurate taylor-polynomial

ax.plot(x, np.exp(x), 'r', label='exp(x)') # actual function

legend = ax.legend(loc='best')
plt.show()