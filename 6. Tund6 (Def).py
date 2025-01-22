from Tund6_Modul import *   # обращаемся к модулю

# a=int(input("Sisesta arv1: "))
# b=int(input("Sisesta arv2: "))
# c=input("Sisesta arv3: ")

# vastus=summa3(a,b,int(c))
# print(f"Summa: {vastus}")



# Практическая работа "Создание пользовательских функций" https://moodle.edu.ee/mod/assign/view.php?id=1972709

# # Ülesanne 1
# # Простейшие арифметические операции
# # Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

# a=int(input("Sisesta arv1: "))
# b=int(input("Sisesta arv2: "))
# c=input("Sisesta operatsioon(+,-,*,/): ")

# vastus=arithmetic(a,b,c)
# print(vastus)



# # Ülesanne 2
# # Високосный год
# # Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

# aasta=int(input("Sisesta aasta: "))

# vastus=is_year_leap(aasta)
# print(vastus)



# # Ülesanne 3
# # Квадрат
# # Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.

# külg=float(input("Sisesta ruudu külg (cm): "))

# vastus=square(külg)
# print(vastus)



# # Ülesanne 4
# #Времена года
# #Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis).

# kuu=int(input("Sisesta kuu number (1-12): "))

# vastus=season(kuu)

# print(vastus)



# # Ülesanne 5
# # Банковский вклад
# # Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# # Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

# vklad=float(input("Vali sissemakse summa eurodes: "))
# aasta=int(input("Kui palju aastaks soovite teha pangadeposiit: "))

# vastus=bank(vklad, aasta)

# print(vastus)



# # Ülesanne 6
# # Простые числа
# # Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

# print(vastus)



# Ülesanne 7
# Правильная дата
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.

päev=int(input("Sisestage päev: "))
kuu=int(input("Sisestage kuu: "))
aasta=int(input("Sisestage aasta: "))

vastus=date(päev,kuu,aasta)
print(vastus)


