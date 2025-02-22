import math   # Импортируем стандартную, "внутреннюю" библиотеку math
import matplotlib.pyplot as plt    # Импортируем один из пакетов "внешней" библиотеки Matplotlib
from matplotlib import mlab   # Импортируем еще один пакет со вспомогательными функциями

# Рисуем график функции ax^2+bx+c=0
def funktsiooni_lahendamine(a,b,c,x):
    D=b**2-4*a*c
    if D < 0:
        return None
    elif D==0:
        x=-b/(2*a)
        return (x)
    else:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        return (x1,x2)

def funktsioon(a, b, c, x):
    return a*x**2 + b*x + c

a = 1  # Пример коэффициента для x^2
b = -3  # Пример коэффициента для x
c = 2  # Пример свободного члена

xmin=-7.5
xmax=12.5
dx=0.5
xlist=mlab.frange(xmin, xmax, dx)
ylist=[funktsioon(a,b,c,x) for x in xlist]

plt.plot(xlist, ylist, color='b', linestyle='-', marker='', label="$y = ax^2 + bx + c$")
plt.legend(title="Функция")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции y = ax^2 + bx + c")
plt.grid(True)
plt.show()
