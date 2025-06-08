import numpy as np
import matplotlib.pyplot as plt

# 테일러 다항식 근사 (홀수 차수만 포함)
p1 = lambda a : a
p3 = lambda a : a - a**3/6
p5 = lambda a : a - a**3/6 + a**5/120
p7 = lambda a : a - a**3/6 + a**5/120 - a**7/5040
p9 = lambda a : a - a**3/6 + a**5/120 - a**7/5040 + a**9/362880

x = np.arange(-np.pi, np.pi, 0.01)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, p1(x), 'g', label='p1')
ax.plot(x, p3(x), 'm', label='p3')
ax.plot(x, p5(x), 'k', label='p5')
ax.plot(x, p7(x), 'r', label='p7')
ax.plot(x, p9(x), 'c', label='p9')

legend = ax.legend(loc='best')
# ax.set(xlim=(-np.pi, np.pi), ylim=(-1.2, 1.2))
plt.show()