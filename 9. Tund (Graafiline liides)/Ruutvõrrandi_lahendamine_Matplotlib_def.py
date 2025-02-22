import math   # Импортируем стандартную, "внутреннюю" библиотеку math
import matplotlib.pyplot as plt    # Импортируем один из пакетов "внешней" библиотеки Matplotlib
from matplotlib import mlab   # Импортируем еще один пакет со вспомогательными функциями

# Рисуем график функции ax^2+bx+c=0
def funktsiooon(x):
    """
    ax^2+bx+c=0
    """
    if x==0:
        return 1.0
    return math.sin(x)/x

