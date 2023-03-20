import math
def Fun(x,y,a,b,c,d,arg):// “универсальная” функция для вычисления значения функции, производной по x и y
    if arg==1:
        return a * x + b * y + math.exp(c * x * x + d * y * y)//возвращает значение функции f(x,y)
    elif arg==2:
        return a + 2 * c * x * math.exp(c * x * x + d * y * y)//возвращает значение производной по x
    elif arg==3:
        return b + 2 * d * y * math.exp(c * x * x + d * y * y)//возвращает значение производной по y
//вводим коэффициенты
a=float(input("Enter a="))
b=float(input("Enter b="))
c=float(input("Enter c="))
d=float(input("Enter d="))
eps=0.0001//eps=10^-4
alf=1.0
x=0.0
y=0.0
x1=0.0
y1=0.0
while math.fabs(Fun(x, y, a, b, c, d,2)) >= (eps / 2) and math.fabs(Fun(x, y, a, b, c, d,3)) >= (eps / 2): // проверка условия по формуле (5.3)
    x1 = x - alf * Fun(x, y, a, b, c, d,2)
    y1 = y - alf * Fun(x, y, a, b, c, d,3)
    if Fun(x,y,a,b,c,d,1)>Fun(x1,y1,a,b,c,d,1):
        x=x1
        y=y1
    else:
        alf=alf/2
    print("x=", x, "y=", y, "alf=", alf, "F(x,y)=", Fun(x, y, a, b, c, d,1),"dfdx=",Fun(x,y,a,b,c,d,2),"dfdy=",Fun(x,y,a,b,c,d,3))
print("Точка минимума:")
print("x=",x,"y=",y)
