import math   # Импортируем стандартную, "внутреннюю" библиотеку math
import matplotlib.pyplot as plt    # Импортируем один из пакетов "внешней" библиотеки Matplotlib
from matplotlib import mlab   # Импортируем еще один пакет со вспомогательными функциями
import numpy as np

def funktsiooni_lahendamine(a,b,c):
    """Решение функции ax^2+bx+c=0"""
    D=b**2-4*a*c
    if D<0:
        return (f"D={D}\nРешений нет")
    elif D==0:
        x=round(-b/(2*a),2)
        return (f"D={D}\nX={x}")
    else:
        x1=round((-b+math.sqrt(D))/(2*a),2)
        x2=round((-b-math.sqrt(D))/(2*a),2)
        return (f"D={D}\nX1={x1}\nX2={x2}")

def funktsiooni_graafik(a,b,c):
    """График функции ax^2+bx+c=0"""

    x0=-b/(2*a)    # x координата вершины параболы
    y0=a*x0**2+b*x0+c     # y координата вершины параболы
    xmin=-7.5
    xmax=12.5
    dx=0.5

    xlist=np.arange(xmin,xmax,dx)
    ylist=[(a*x**2+b*x+c) for x in xlist]

    # Перекрашивает точку вершины параболы (.scatter - позволяет работать с одной или несколькими точками)
    plt.scatter(x0,y0,color="g",zorder=3)   # zorder - помогает изменить, какой элемент будет на переднем плане, а какой — на заднем
    plt.plot(xlist,ylist,color='b',linestyle=':',marker='o',label="$y = ax^2 + bx + c$")
    plt.legend(title="Функция")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Квадратное уравнение")
    plt.grid(True)

    plt.show()
