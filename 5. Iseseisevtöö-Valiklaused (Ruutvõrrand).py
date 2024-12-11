from math import *


#Ülesanne 1
#Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное),
#если число положительное, то проверяет его на четность и нечетность.
print()
print("-- Ülesanne 1 --")
try:
    arv=float(input("Sisestage arv: "))
    if arv>=0:
        if arv%2==0:  #Проверка, делится ли число на 2 без остатка
            print("Arv on positiivne ja paaris")
        else:
            print("Arv on positiivne ja paaritu")
    else:
        print("Arv on negatiivne")
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 2
#Спросить у пользователя 3 числа, если они окажуться положительными,то проверить могут ли они быть углами одного треугольника(сумма углов 180)
# и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).
print()
print("-- Ülesanne 2 --")
try:
    arv1=float(input("Sisestage esimene arv: "))
    arv2=float(input("Sisestage teine arv: "))
    arv3=float(input("Sisestage kolmas arv: "))
    if arv1>0 and arv2>0 and arv3>0:
        if arv1+arv2+arv3==180:
            if arv1==arv2==arv3:
                print("Kolmnurk on - võrdkülgne")
            elif arv1==arv2 or arv2==arv3 or arv1==arv3:
                print("Kolmnurk on - võrdhaarne")
            else:
                print("Kolmnurk on - erikülgne")
        else:
            print("See ei ole kolmnurk! Summa peab olema 180 kraadi!")
    else:
        print("Arved peavad olema positiivsed! See ei ole kolmnurk!")
except:
    print("Vale andmetüüp! Sisestage arv!")
print()



#Ülesanne 3
#Выяснить у пользователя желание расшифровать порядковый номер дня недели в название.
# Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами),
#  спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.
print()
print("-- Ülesanne 3 --")
vastus=input("Kas te soovite nädala päeva järjestusnumbri nimeks dešifreerida?(jah/ei) ").upper()
if vastus=="JAH":
    try:
        arv=int(input("Sisestage täisarv (1-7): "))
        if 1<=arv<=7:
            päevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]  #Список дней недели
            #Выводим название дня недели
            print(f"Nädalapäev: {päevad[arv-1]}")  #Так как в списке отсчёт начинается с 0, то от выбранного числа отнимаем 1
    except:
        print("Sisestage ainult täisarv!")
elif vastus=="EI":
    print("Olgu, head aega!")
else:
    print("Sisestage vastus, kas 'jah' või 'ei'!")
print()



#Ülesanne 4
#Определить по дню и месяцу рождения пользователя кто он по гороскопу. 
#Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!
print()
print("-- Ülesanne 4 --")
try:
    päev=int(input("Sisestage teie sünnipäeva kuupäev (1-31): "))
    kuu=int(input("Sisestage teie sünnipäeva kuu (1-12): "))
    if (kuu==3 and 21<=päev<=31) or (kuu==4 and 1<=päev<=19):
        print("Teie sodiaak: Jäär (Овен)")
    elif (kuu==4 and 20<=päev<=30) or (kuu==5 and 1<=päev<=20):
        print("Teie sodiaak: Sõnn (Телец)")
    elif (kuu==5 and 21<=päev<=31) or (kuu==6 and 1<=päev<=21):
        print("Teie sodiaak: Kaksikud (Близнецы)")
    elif (kuu==6 and 22<=päev<=30) or (kuu==7 and 1<=päev<=22):
        print("Teie sodiaak: Vähk (Рак)")
    elif (kuu==7 and 23<=päev<=31) or (kuu==8 and 1<=päev<=22):
        print("Teie sodiaak: Lõvi (Лев)")
    elif (kuu==8 and 23<=päev<=31) or (kuu==9 and 1<=päev<=22):
        print("Teie sodiaak: Neitsi (Дева)")
    elif (kuu==9 and 23<=päev<=30) or (kuu==10 and 1<=päev<=22):
        print("Teie sodiaak: Kaalud (Весы)")
    elif (kuu==10 and 23<=päev<=31) or (kuu==11 and 1<=päev<=21):
        print("Teie sodiaak: Skorpion (Скорпион)")
    elif (kuu==11 and 22<=päev<=30) or (kuu==12 and 1<=päev<=21):
        print("Teie sodiaak: Ambur (Стрелец)")
    elif (kuu==12 and 22<=päev<=31) or (kuu==1 and 1<=päev<=19):
        print("Teie sodiaak: Kaljukits (Козерог)")
    elif (kuu==1 and 20<=päev<=31) or (kuu==2 and 1<=päev<=18):
        print("Teie sodiaak: Veevalaja (Водолей)")
    elif (kuu==2 and 19<=päev<=29) or (kuu==3 and 1<=päev<=20):
        print("Teie sodiaak: Kalad (Рыбы)")
    else:
        print("Valesti sisetatud sünnipäev!")
except:
    print("Sisetage ainult täisarvu!")
print()



#Ülesanne 5
#Проверить введенное пользователем число, отпределить его тип и если число целое, то найти от него 50%, если число дробное,
# то найти от него 70%, если это текст, то вывести его на экран. Для решения можно использовать: is_integer(), isalpha(), isdigit(), int(), float(), //, %.
print()
print("-- Ülesanne 5 --")
try:
    vastus=input("Sisestage arv: ")
    number=float(vastus)
    if number.is_integer():
        print(f"Arv on täisarv, 50% sellest arvust on - {round(number*0.5,2)}")
    else:
        print(f"Arv on murdarv, 70% sellest arvust on - {round(number*0.7,2)}")
except:
    if vastus.isalpha():
        print(f"{vastus}")
    else:
        print(f"Viga! Sisestage arv või tekst!")
print()



#Ülesanne 6
#Написать программу для решения квадратного уравнения a*x**2+b*x+c=0.
#Сначала спрашивается желание решить уравнение и только после утвердительного ответа спросить надо 3 значания: a, b, c.
#Если нет желания решать уравнение, то попрощаться с пользователем.
print()
print("-- Ülesanne 6 --")
vastus=input("Kas soovite lahendada ruutvõrrandi? (jah/ei): ").upper()
if vastus=="JAH":
    try:
        #Запрашиваем значения a, b, c
        a=float(input("Sisestage a: "))
        b=float(input("Sisestage b: "))
        c=float(input("Sisestage c: "))
        #Решаем уравнение a*x**2+b*x+c=0 через дискриминант(D)
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/(2*a)
            x2=(-b-sqrt(D))/(2*a)
            print(f"D>0 --> Ruutvõrrandil on kaks lahendust: x1 = {round(x1,2)}, x2 = {round(x2,2)}")
        elif D==0:
            x=-b/(2*a)
            print(f"D=0 --> Ruutvõrrandil on üks lahendus: x = {round(x,2)}")
        else:
            print("D<0 --> Ruutvõrrandil puuduvad lahendused")
    except:
        print("Viga! Sisestage arvud!")
elif vastus=="EI":
    print("Olgu, head aega!")
else:
    print("Viga! Sisestage 'jah' või 'ei'!")
print()