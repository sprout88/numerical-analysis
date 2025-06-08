import numpy as np
import matplotlib.pyplot as plt

def Euler(f,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    h = (tf-t0)/N
    y = np.zeros(N)
    y[0] = y0
    for i in range(N-1):
        y[i+1] = y[i] + h*f(t[i],y[i])
    return y,t

def IEuler(f,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    h = (tf-t0)/N
    y = np.zeros(N)
    y[0] = y0
    for i in range(N-1):
        fty = f(t[i],y[i])
        y[i+1] = y[i] + h/2*( fty + f(t[i+1],y[i]+h*fty) )
    return y,t

def RK(f,t0,tf,y0,N):
    t = np.linspace(t0,tf,N)
    h=(tf-t0)/N
    y = np.zeros(N)
    y[0] = y0
    for i in range(N-1):
        y1 = f(t[i],y[i])
        y2 = f(t[i]+h/2, y[i]+h/2*y1)
        y3 = f(t[i]+h/2, y[i]+h/2*y2)
        y4 = f(t[i]+h, y[i]+h*y3)
        y[i+1] = y[i] + h/6*( y1 + 2*y2 + 2*y3 + y4)
    return y,t

# y' = ty, t\in(1,3), y(1)=1 : ytrue(t)=exp((t^2-1)/2)

def trf(t):
    return np.exp(t*t/2-1/2)

def f(t,y):
    return t*y

t0=1
tf=3
y0=1
N=10

yE,t = Euler(f,t0,tf,y0,N)
yI,dummy = IEuler(f,t0,tf,y0,N)
yR,dummy = RK(f,t0,tf,y0,N)
ttrue = np.linspace(t0,tf,101)
yT = trf(ttrue)
yTT = trf(t)

plt.plot(ttrue, yT, 'r-',t,yE,'b*-',t,yI,'cv-',t,yR,'kp-')
plt.grid()
plt.show()