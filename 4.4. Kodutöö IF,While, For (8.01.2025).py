from math import *
from random import *

# Задачи по теме IF,While, For и проверка вводимых данных  https://moodle.edu.ee/mod/assign/view.php?id=1694243



# Ülesanne 1
# Определить и вывести максимальное из N вводимых пользователем чисел.
print("--Ülesanne 1--")
print()
N=0
while True:
    try:
        N=int(input("Kui palju arvu soovite sisestada? "))
        if N>0:
            break
        else:
            print("Arv peab olema positiivne!")
    except:
        print("Vale andmetüüp!")

# Ввод первого числа для дальнейшего сравнения максимального значения
while True:
    try:
        max_num = float(input("Sisestage 1 number: ")) 
        break
    except:
        print("Vale andmetüüp!")

# Вводим оставшиеся числа и обновляем максимальное значение
for i in range(2,N+1):    # Начинаем со второго числа
    while True:
        try:
            number=float(input(f"Sisestage {i} number: "))
            if number > max_num:
                max_num = number   # Обновляем максимальное значение
            break
        except:
            print("Vale andmetüüp!")

print(f"Maksimaalne arv on: {round(max_num)}")
print()



# Ülesanne 2
# Написать программу, которая бы запрашивала целые числа и распечатывала любые значение, кроме 13. 
# Если заданное число равно 13, вместо него печатается число 77.
print()
print("--Ülesanne 2--")
print()
count=int(input("Kui palju arvu soovite sisetada? "))
for i in range (count):
  while True:
    try:
        number = int(input("Sisestage täisarv: "))
        if number==13: 
            print(77)
        else:
            print(number)
        break
    except:
        print("Sisestatud väärtus pole täisarv! Palun sisestage täisarv.")
print()



# Ülesanne 3
# Начав тренировки, спортсмен в первый день пробежал 10 км. 
# Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за 7 дней?
print()
print("--Ülesanne 3--")
print()
print("Selle programmi abil arvutame, kui palju kaugust jooksja läbib 7 päeva jooksul, kui ta alustab 10 km-lt ja suurendab iga päev oma normi 10% võrra")
print()
algus=10
päevad=7
kokku_km=0
for i in range(päevad):
    kokku_km+=algus*(1.1**i)
print(f"Kokku joostud kaugus {päevad} päeva jooksul: {round(kokku_km,2)} km")
print()



# Ülesanne 4
# Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. Все данные по использованию ткани заносятся в компьютер. 
# Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется и предложить выкупить остаток.
# Если пользователь согласен, то продается последний кусок и программа заканчивает работу, если нет, то переходим к следующиму покупателю.
print()
print("--Ülesanne 4--")
M=round(uniform(10,100),2)    # Генерация случайной длины ткани
print(f"Tere tulemast poodi!\nKanga algne pikkus: {M} m")

# Цикл работы с тканью, пока она не закончится
while M>0:
    while True:
        try:
            soovitud_pikkus=float(input("Sisestage soovitud kanga tüki pikkus (m): "))
            break
        except:
            print("Vale andmetüüp!")

    if soovitud_pikkus>M:
        print(f"\nMaterjalist ei piisa! Kanga jääk on {round(M,2)} m.")
        print()
        while True:
            otsus = input("Kas soovite jäägi välja osta? (jah/ei): ").upper()
            if otsus=="JAH":
                print(f"\nJääk {round(M,2)} m müüdud!")
                M=0     # Завершаем цикл
                break
            elif otsus=="EI":
                print(f"\nLiigume järgmise kliendi juurde!\n")
                print("-------------------------------")
                print(f"Tere tulemast poodi!\n\nKanga pikkus on {round(M,2)} m")
                break
            else:
                print(f"Viga! Sisestage jah või ei!")
    else:
        M-=soovitud_pikkus
        print(f"Tükk pikkusega {soovitud_pikkus} m on lõigatud. Alles {round(M,2)} m.\n")
print("Kangas on otsas. Aitäh ostude eest! Head aega!")
print()



# Ülesanne 5
# Составьте программу для вычисления площади трапеций до тех пор пока пользователь не откажется вычислать.
print()
print("--Ülesanne 5--")
print()
print("Programm trapetsi pindala arvutamiseks!")
while True:
    print("\nSisestage andmed trapetsi pindala arvutamiseks")
    try:
        a=float(input("Sisestage aluse a pikkus: "))
        b=float(input("Sisestage aluse b pikkus: "))
        h=float(input("Sisestage kõrguse h pikkus: "))

# Проверяем, чтобы все значения были положительными
        if a<=0 or b<=0 or h<=0:
            print("Kõik väärtused peavad olema positiivsed. Proovige uuesti!")
            continue

# Расчет площади трапеции
        S=((a+b)/2)*h
        print(f"Trapetsi pindala: {round(S,2)}")
    except:
        print("Viga! Palun sisestage ainult numbreid. Proovige uuesti!")
        continue
# Спрашиваем, хочет ли пользователь продолжить
    while True:
        vastus=input("\nKas soovite arvutada veel ühe trapetsi pindala? (jah/ei): ").lower()
        if vastus=="ei":
            print("\nProgramm lõpetatud")
            break
        elif vastus=="jah":
            break
        else:
            print("Viga! Palun vastake ainult 'jah' või 'ei'")
# Завершаем основной цикл
    if vastus=="ei":
        break
print()



# Ülesanne 6
# Составьте программу, проверяющую, верно ли утверждение, что введенное вами целое число делится без остатка на 3.
print()
print("--Ülesanne 6--")
print()
print("Tere! Selle programmi abil saate kontrollida, kas sisestatud täisarv jagub 3-ga\n")
while True:
    try:
        number = int(input("Sisesta täisarv: "))
        if number%3==0:
            print("Arv jagub 3-ga")
        else:
            print("Arv ei jagu 3-ga")
        while True:
            vastus=input("\nKas soovite arvutada veel arvu kontrollida? (jah/ei): ").lower()
            print()
            if vastus=="ei":
                print("Programm lõpetatud")
                break
            elif vastus=="jah":
                break
            else:
                print("Viga! Palun vastake ainult 'jah' või 'ei'")
# Завершаем основной цикл
        if vastus=="ei":
            break
    except:
        print("Viga! Sisestage täisarv!")