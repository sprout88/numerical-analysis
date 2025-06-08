import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, nmax):
    x = np.zeros(nmax) # 길이가 nmax 이고 0으로 채워진 배열 x
    x[0] = a # 초기 경계값 지정
    x[1] = b # 초기 경계값 지정

    for n in range(nmax-2):
        x[n+2] = (a+b)/2 # 중간값 계산해서 배열 x 에 저장

        if f(x[n+2])*f(a) < 0: # 부호가 바뀌는 곳에 근이 존재함
            b = x[n+2] # f<0 이면 [a,b] 에 근이 존재한다는 뜻
        else:
            a = x[n+2] # f>0 이면 [(a+b)/2,b] 에 근이 존재한다는 뜻
    return x

def newton(f, fp, x0, nmax): # f 의 도함수 fp / 초기추정값(initial guess) x0
    x = np.zeros(nmax) # 길이가 nmax 이고 0으로 채워진 배열 x
    x[0] = x0 # 초기추정값 저장
    x[1] = x0 # 초기추정값 저장

    for n in range(nmax-2):
        # 뉴턴-랩슨 공식(Newton-Raphson method)
        # https://www.youtube.com/shorts/LjtA3D3Gizg
        xold = x[n+1]
        x[n+2] = xold - f(xold) / fp(xold) # f'(x0) 가 x축과 만나는 점 x1 -> 반복
        # 반복하면 xn 은 점점 곡선과 x축이 만나는 점에 가까워진다.
    return x

# 할선법
# 뉴턴법보다 느리지만 도함수가 필요없음. 도함수를 모를때 사용
def secant(f, a, b, nmax):
    x = np.zeros(nmax)
    x[0] = a
    x[1] = b
    for n in range(nmax-2):
        xold = x[n]
        xnew = x[n+1]
        x[n+2] = xnew - f(xnew)*(xnew-xold) / (f(xnew)-f(xold))
    return x

"""
근 구하기 예시
"""

# log(x) - 1 = 0 의 해 → x = e
f1 = lambda x: np.log(x) - 1  
f1p = lambda x: 1/x # log(x) - 1 의 도함수

xb = bisection(f1, 1, 3, nmax=10)
xs = secant(f1, 1, 3, nmax=5)
xn = newton(f1, f1p, 3, nmax=5)

y = np.linspace(0,12,num=300000)
plt.plot(y, f1(y), 'b-', xb, f1(xb), 'r-*', xs,f1(xs),'g-v',xn,f1(xn),'c-o')
plt.grid()
plt.show()

# plt.semilogy : 로그 스케일로 그리기 -> 0에 가까운 값을 더 자세히 볼 수 있음
plt.semilogy(y,abs(f1(y)),'b-')
plt.show()

# 누가 더 빨리 답에 수렴할까?
plt.semilogy(y,abs(f1(y)),'b-',xb,abs(f1(xb)),'r-*',xs,abs(f1(xs)), 'g-v',xn,abs(f1(xn)),'c-o')
plt.show()