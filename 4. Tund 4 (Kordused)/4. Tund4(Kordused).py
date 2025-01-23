from random import *


# #Ülesanne 2
# #Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
# print("--Ülesanne 2--")
# while True:
#     try:
#         A=int(input("Sisesta A: "))
#         break                 #чтобы остановить цикл while True
#     except:
#         print("On vaja naturaalne arv!")
# summa=0
# if A>0:
#     for i in range(1,A+1,1):  #если не просят шаг, то можно не ставить
#         summa+=i              #summa=summa+i
#         print(f"{i}. samm summa={summa}")
# print(f"Vastus {summa}")



# #Ülesanne 3
# #Вводят 8 чисел. Найти их произведение (только положительных).
# print()
# print("--Ülesanne 3--")
# p=1
# for i in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1} arv: "))
#             break
#         except:
#             print("On vaja arv!")
#     if arv>0:
#         p*=arv
#     else:
#         print("Korrutame arvud rohkem kui 0")
#     print(f"{i+1}. samm korrutis = {p}")
# print(f"Lõpptulemus on {p}")'
# print()



# #Ülesanne 4
# #Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
# print()
# print("--Ülesanne 4--")
# for i in range(10,21,1):
#     print(i**2, end=";")
# print()



# #Ülesanne 16
# #Напишите программу, печатающую столбик строк такого вида:
# print()
# print("--Ülesanne 16--")
# for j in range(1,10):
#     for i in range (1,10):
#         if i==j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()
# print()



# #Ülesanne 15
# #Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
# print()
# print("--Ülesanne 15--")
# for j in range(10):          #j - read, i - rida
#     for i in range(10):
#         print(i, end=" ")
#     print()
# print()



# #Ülesanne 17
# #Напишите программу, печатающую столбик таблицу умножения такого вида:
# print()
# print("--Ülesanne 17--")
# for i in range(1,9):
#     a=2*i
#     print(f"2*{i}={a}")
# print()



# #Ülesanne 18
# #Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.
# print()
# print("--Ülesanne 18--")
# for i in range(20,51):
#     if i%3==0 and i%5!=0:
#         print(i, end=", ")
# print()



# #Ülesanne 26
# # Два двузначных числа, записанных одно за другим, образуют четырехзначное число, которое делится на их произведение. Найти эти числа.
# print()
# print("--Ülesanne 26--")
# for i in range(10,100):             # Первое число
#     for j in range(10,100):         # Второе число
#         number=int(f"{i}{j}")       # Склеиваем два числа и получаем четырехзначное
#         korrutis=i*j
#         if korrutis!=0 and number%korrutis==0:       # Проверка: делится ли четырехзначное число на произведение 2ух чисел
#             print(f"Arvud: {i} ja {j}, neljakohaline number: {number}, korrutis: {korrutis}")
#             break    # Выход из внутреннего цикла
#     else:     
#         continue     # Если внешний цикл не был прерван, продолжаем его
#     break            # Прерывает внешний цикл, если внутренний цикл был прерван
# print()



# #Ülesannne 28
# # Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.
# print()
# print("--Ülesanne 28--")
# print()
# print("Tere tulemast mini-lotosse!")
# print("Ma mõtlesin numbri vahemikus 1 kuni 100. Proovige seda ära arvata!")
# print()
# minu_arv=randint(1,100)   # Загадываем число
# katse_arv=0        # Счётчик попыток
# while True:
#     try:
#         arv=int(input("Mis numbri ma mõtlesin? "))
#         katse_arv+=1        # Увеличиваем количество попыток
#         if arv<minu_arv:
#             print("Liiga väike! Proovige veel kord")
#         elif arv>minu_arv:
#             print("Liiga suur! Proovige veel kord")
#         else:
#             print(f"Õnnitlen, te arvasite ära õige number! Arvasite numbri {minu_arv} --> {katse_arv} katses.")
#             break      # Прерываем цикл, если угадано число
#     except:
#      print("Sisetage ainult täisarv!")
# print()



#Ülesanne 31
# Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.
# Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.
print()
print("--Ülesanne 31--")

