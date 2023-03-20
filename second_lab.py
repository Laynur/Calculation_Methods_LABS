import math
def func(x): # функция
    return (float)(math.sin(x))
def func1(x): # первая производная
    return (float)(math.cos(x))
def func2(x): # вторая производная
    return (float)(-math.sin(x))
def progon(n):
    h=(b-a)/n
    A[0]=1
    B[0]=0
    D[0]=func2(a)
    C[n]=0
    C[0] = 0
    A[n]=1
    D[n]=func2(b)
    B[n]=0
    L[0]=-B[0]/A[0]
    Mu[0]=D[0]/A[0]
    for i in range(1,n,1):
        A[i]=2*h/3
        B[i]=h/6
        C[i]=h/6
        D[i]=((Y[i + 1] - Y[i]) / h) - ((Y[i] - Y[i - 1]) / h)
    for i in range(1,n+1,1):
        L[i] = -(B[i] / (A[i] + C[i] * L[i - 1]))
        Mu[i] = (D[i] - (C[i] * Mu[i - 1])) / (A[i] + (C[i] * L[i - 1]))
    M[n]=Mu[n]
    for i in range(n-1,-1,-1):
        M[i] = (L[i] * M[i + 1]) + Mu[i]
def spline(x,n):
    h=(b-a)/n
    i=(int)((x-a)/h+1)
    t=(float)(((pow((X[i] - x), 3) - pow(h, 2) * (X[i] - x)) / (6.0 * h)) * M[i - 1] + ((pow((x - X[i - 1]), 3) - pow(h, 2) * (x - X[i - 1])) / (6.0 * h)) * M[i] + (X[i] - x) * Y[i - 1] / h + (x - X[i - 1]) * Y[i] / h)
    return (float)(t)
def Razb(n):# записываем x и y
    h=(b-a)/n
    X[0]=a
    Y[0]=func(X[0])
    for i in range(1,n+1,1):
        X[i]=X[i-1]+h
        Y[i]=func(X[i])
def DeltaMax(n):# функция для вычисления дельта макс
    dmax = 0.0
    h = (b - a) / n
    Razb(n)
    progon(n)
    for i in range(0,n,1):# 2.5.2
        v = (float)(spline(X[i] + h / 2.0, n))
        delta = float(abs(func(X[i] + h / 2.0) - v))#вычисление максимальной погрешности
        if dmax < delta:
            dmax = delta
    return (float)(dmax)
def DeltaOc(n):# дельта остаточная 2.4.1
    return (float)(DM[(int)(n / 2.0)] / 16.0)
def KoefD(n):
    return (float)(DM[(int)(n / 2.0)] / DM[n])
a=0.0
b=math.pi
N=10250
A,B,C,D,X,Y,L,Mu,M,DM=[0 for i in range(N)]
dmax=0.0
h=0.0


n=5 #число отрезков на которое мы делим область интегрирования a,b


while n<=10240:
    DM[n]=DeltaMax(n)
    print("%5d" % n, "%.2e" % DM[n], "%.2e" % DeltaOc(n), "%.2f" % KoefD(n))
    n=n*2
