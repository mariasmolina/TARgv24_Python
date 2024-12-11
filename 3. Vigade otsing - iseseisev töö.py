from math import *   #синтаксис не верен, поменяла местами

#Vigade otsing - Iseseisev töö
try:
    print("Ruudu karakteristikud")
    a=float(input('Sisesta ruudu külje pikkus => '))    #добавила тип данных - float
    S=a**2
    print("Ruudu pindala", S)
    P=4*a
    print("Ruudu ümbermõõt", P)   #не верно добавлены кавычки
    di=a*sqrt(2)    #исправила формулу нахождения диагонали
    print("Ruudu diagonaal", round(di,2))
except:
    print("Sisestage arv!")
print()
try:
    print("Ristküliku karakteristikud")   #убрала одну лишнюю скобку в конце
    b=float(input("Sisesta ristküliku 1. külje pikkus => "))    #добавила тип данных - float
    c=float(input("Sisesta ristküliku 2. külje pikkus => "))    #добавила тип данных - float
    S=b*c
    print('Ristküliku pindala', S)   #добавила кавычку ' в начале
    P=2*(b+c)   #исправила формулу нахождения периметра, добавила знак умножить
    print("Ristküliku ümbermõõt", P)
    di=sqrt(b**2+c**2)    #исправила формулу нахождения диагонали
    print("Ristküliku diagonaal", round(di,2))   #добавила скобку в конце, добавила 2 в round после di
except:
    print("Sisestage arv!")
print()
try:
    print("Ringi karakteristikud")
    r=float(input('Sisesta ringi raadiusi pikkus => '))   #добавила тип данных - float, убрала лишние кавычки в начале и в конце
    d=2*r   #добавила знак умножить
    print("Ringi läbimõõt", round(d,2))   #добавила запятую перед d, добавила округление до сотых
    S=pi*r**2   #исправила формулу: убрала скобки у pi/ радиус нужно не умножить на 2, а возвести в квадрат
    print("Ringi pindala", round(S,2))   #добавила 2 в round после S
    C=2*pi*r   #изменила формулу, добавила знак умножить
    print("Ringjoone pikkus", round(C,2))   #добавила скобку в конце, добавила 2 в round после С
except:
    print("Sisestage arv!")