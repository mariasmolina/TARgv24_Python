from datetime import *
from math import *

# #Ülesanne 1 - Juku
# print("-- Ülesanne 1 --")
# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi=="JUKU":
#         print("Lähme kinno")
#         try:
#             vanus=int(input(f"Kui vana sa oled {nimi}? "))
#             if vanus<0:
#                 print("Viga!")
#             elif vanus<=6:
#                 print("Tasuta")
#             elif vanus<15:
#                 print("Lastepilet")
#             elif vanus<65:
#                 print("Täispilet")
#             elif vanus<100:
#                 print("Sooduspilet")
#             else:
#                 print("Nii palju!!!")
#         except:
#             print("Vale andmetüüp!")
#     else:
#         print("Oootan Juku")
# else:
#     print("Segatud sõne")
# print()


# #Ülesanne 2 - Pinginaabrid
# print()
# print("-- Ülesanne 2 --")
# nimi1=input("Mis on esimese inimese nimi? ")
# nimi2=input("Mis on teise inimese nimi? ")
# print()
# #1 вариант
# nimed=["Jevgeni","Milana"]   #список имен
# if nimi1.isalpha() and nimi2.isalpha():
#     if (nimi1 in nimed) and (nimi2 in nimed):
#         print("Need inimesed on pinginaabrid")
#     else:
#         print("Need inimesed ei ole pinginaabrid!")
# else:
#     print("Viga!")
# print()
# #2 вариант
# if (nimi1=="Jevgeni" and nimi2=="Milana") or (nimi1=="Milana" and nimi2=="Jevgeni"):
#         print("Need inimesed on pinginaabrid")
# else:
#     print("Need inimesed ei ole pinginaabrid!")
# print()


# #Ülesanne 3 - Remont
# print()
# print("-- Ülesanne 3 --")
# try: 
#    a=float(input("Mis on toa pikkus? "))
#    b=float(input("Mis on toa laius? "))
#    S=a*b
#    print(f"Põranda pindala on {S} m**2")
#    print()
#    vastus=input("Kas te soovite remondi teha?(Jah-1/Ei-0) ") #.upper() - можно и после вопроса, тогда в if не надо
#    if vastus.upper()=="JAH" or vastus=="1":
#        print("Teeme remondi!")
#        print()
#        hind=float(input("Ühe meetri hind: "))
#        summa=hind*S
#        print(f"Põranda vahetamise hind on {summa} eurot")
#    elif vastus.upper()=="EI" or vastus=="0":
#        print("-")
#    else:
#         print("Ei saa aru")
# except:
#     print("Vale andmetüüp!")
# print()



#Ülesanne 4 - Allahindus
print()
print("-- Ülesanne 4 --")
try:
    alghind=float(input("Sisesta hind: "))
    soodus=round((alghind*0.7),2)
    if alghind>700:
        print(f"Soodustusega 30% hind on {soodus} eurot")
    else:
        print("Hind peab olema suurem kui 700")
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 5 - Temperatuur
print()
print("-- Ülesanne 5 --")
try:
    temp=float(input("Sisestage temperatuur (Celsius): "))
    if temp>18:
        print(f"Temperatuur on {temp} kraadi. Sobiv toasoojus talvel!")
    else:
        print(f"Temperatuur on {temp} kraadi. Ei sobi, talvel võib olla külm!")
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 6 - Pikkus
print()
print("-- Ülesanne 6 --")
try:
    pikkus=float(input("Mis on sinu pikkus? "))
    if 160<=pikkus<=175:
       print("Sa oled keskmine")
    elif pikkus<160:
        print("Sa oled lühike")
    else:
        print("Sa oled pikk")
except:
    print("Viga andmetüüp!")
print()



#Ülesanne 7 - Pikkus ja sugu
print()
print("-- Ülesanne 7 --")
try:
    pikkus=float(input("Mis on sinu pikkus? "))
    sugu=input("Mis on sinu sugu?(mees-1/naine-2) ").upper()
    if sugu=="MEES" or sugu=="1":
        if 165<=pikkus<=180:
            print("Sa oled meeste jaoks keskmine")
        elif pikkus<165:
            print("Sa oled meeste jaoks lühike")
        else:
            print("Sa oled meeste jaoks pikk")
    elif sugu=="NAINE" or sugu=="2":
       if 160<=pikkus<=170:
           print("Sa oled naiste jaoks keskmine")
       elif pikkus<160:
           print("Sa oled naiste jaoks lühike")
       else:
           print("Sa oled naiste jaoks pikk")
    else:
        print("Sugu on ebakorrektne!")        
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 8 - Poes
##Программа спрашивает, желает ли покупатель купить тот или иной товар, если да --> спрашивает кол-во и в конце печатает чек
print()
print("-- Ülesanne 8 --")
hind_piim=0
hind_sai=0
hind_leib=0
vastus1=input("Kas te soovite osta piim?(jah/ei) ").upper()
if vastus1=="JAH":
    try:
        kogus_piim=int(input("Kui palju tk soovite osta? "))
        hind_piim=round(1.5*kogus_piim,2)
    except:
        print("Palun sisestage ainult numbreid!")
elif vastus1=="EI":
    pass                      #Если вводишь 'ei', то pass, чтобы не спрашивало количество
else:
    print("Viga! Vastus peab olema 'jah' või 'ei'!")
    exit()  
#Если вводишь не 'jah' или 'ei', то с помощью функции exit() отменяется подсчет чека
print()
vastus2=input("Kas te soovite osta saia?(jah/ei) ").upper()
if vastus2=="JAH":
    try:
        kogus_sai=int(input("Kui palju tk soovite osta? "))
        hind_sai=round(0.8*kogus_sai,2)
    except:
        print("Palun sisestage ainult numbreid!")
elif vastus2=="EI":
    pass
else:
    print("Viga! Vastus peab olema 'jah' või 'ei'!")
    exit()
print()
vastus3=input("Kas te soovite osta leiba?(jah/ei) ").upper()
if vastus3=="JAH":
    try:
        kogus_leib=int(input("Kui palju tk soovite osta? "))
        hind_leib=round(1.20*kogus_leib,2)
    except:
        print("Palun sisestage ainult numbreid!")
elif vastus3=="EI":
    pass
else:
    print("Viga! Vastus peab olema 'jah' või 'ei'!")
    exit()
print()
summa=round((hind_piim)+(hind_sai)+(hind_leib),2)
if vastus1=="JAH" or vastus2=="JAH" or vastus3=="JAH":    #если какой либо ответ "да", то печатаем чек
    print("Ostutšekk")
    if vastus1=="JAH":
        print(f"Piim {kogus_piim} tk - {hind_piim} eur")
    if vastus2=="JAH":
        print(f"Sai - {kogus_sai} tk - {hind_sai} eur")
    if vastus3=="JAH":
        print(f"Leib - {kogus_leib} tk - {hind_leib} eur")
    print(f"Ostukorvi kokku summa: {summa} eur")
if vastus1=="EI" and vastus2=="EI" and vastus3=="EI":     #если ничего не купил - прощаемся
    print("Te ei ostnud midagi. Head aega!")
print()



#Ülesanne 9 - Ruut
print()
print("-- Ülesanne 9 --")
try:
    a=float(input("Sisetage kujundi pikkus? "))
    b=float(input("Sisetage kujundi laius? "))
    if a==b:
        print("Tegemist on ruuduga!")
    else:
        print("Tegemist ei ole ruuduga!")
except:
    print("Palun sisestage ainult numbreid!")
print()
#Plokkskeem repositooriumis!



#Ülesanne 10 - Matemaatika
print()
print("-- Ülesanne 10 --")
try:
    arv1=round(float(input("Sisestage esimene arv: ")),2)
    arv2=round(float(input("Sisestage teine arv: ")),2)
    tehe=input("Mis tehet te soovite (+-*/)? ")
    if tehe=="+":
        tulemus=round(arv1+arv2,2)
        print(f"Liitmine: {arv1:g}+{arv2:g}={tulemus:g}")
    #Формат g убирает лишние нули, если при вводе числа например 5, то в конце не будет .0
    elif tehe=="-":
        tulemus=round(arv1-arv2,2)
        print(f"Lahutamine: {arv1:g}-{arv2:g}={tulemus:g}")
    elif tehe=="*":
        tulemus=round(arv1*arv2,2)
        print(f"Korrutamine: {arv1:g}*{arv2:g}={tulemus:g}")
    elif tehe=="/":
        tulemus=round(arv1/arv2,2)
        print(f"Jagamine: {arv1:g}/{arv2:g}={tulemus:g}")
    else:
        print("Viga!")
except:
    print("Palun sisestage ainult arvu!")
print()
#Plokkskeem repositooriumis!



#Ülesanne 11 - Juubel
print()
print("-- Ülesanne 11 --")
täna=datetime.today()
sünnipäev=input("Sisetage oma sünnipäev (pp.kk.aaaa): ")
#Преобразуем день рождение в datetime
sünnipäev=datetime.strptime(sünnipäev, "%d.%m.%Y")
vanus=täna.year-sünnipäev.year
if vanus%10==0 and vanus>0:
    print(f"Sa tähistad juubelit! Oled {vanus} aastat vana")
elif vanus<=0:
    print(f"Palun sisesta kehtiv sünniaasta!")
else:
    print(f"Teil ei ole juubelit! Oled {vanus} aastat vana")
print()



#Ülesanne 12 - Müük
print()
print("-- Ülesanne 12 --")
try:
    hind=float(input("Sisestage toode hinna: "))
    soodus1=hind*0.9
    soodus2=hind*0.8
    if hind<=10:
        print(f"Teile tuleb soodus 10%! Toote lõplik hind on {round(soodus1,2)} eur")
    else:
        print(f"Teile tuleb soodus 20%! Toote lõplik hind on {round(soodus2,2)} eur")
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 13 - Jalgpalli meeskond
print()
print("-- Ülesanne 13 --")
try:
    print("Jalgpalli meeskonda kandideerimine")
    sugu=input("Mis on sinu sugu?(mees/naine) ").upper()
    if sugu=="MEES":
        vanus=int(input("Mis on sinu vanus? "))
        if 16<=vanus<=18:
            print("Te sobite meie jalgpalli meeskonda!")
        else:
            print("Te ei sobi meie jalgpalli meeskonda!")
    elif sugu=="NAINE":
        print("Naised meie jalgpalli meeskonda ei sobi!")
    else:
        print("Sugu on ebakorrektne!")
except:
    print("Vale andmetüüp!")
print()



#Ülesanne 14 - Busside logistika
print()
print("-- Ülesanne 14 --")
try:
    inimesed=int(input("Kui palju inimesi sõidab bussiga? "))
    bussi_koht=int(input("Mitu kohta on bussis? "))
    bussi_vaja=inimesed//bussi_koht    #целое кол-во автобусов
    viimane_buss=inimesed%bussi_koht   #остаток, сколько людей в последнем автобусе
    if inimesed<=0 or bussi_koht<=0:   #в случае если вводится 0 или меньше 0
        print("Sisesta positiivsed arvud!")
    elif inimesed<=bussi_koht:   #если людей меньше, чем мест в одном автобусе
        print("On vaja 1 buss. Kõik inimesed mahuvad ühte bussi")
    elif viimane_buss==0:    #если нет остатка, то все автобусы полностью заняты
        print(f"On vaja {bussi_vaja} bussi, et kõik inimesed kohale saaksid")
        print(f"Viimases bussis on {bussi_koht} inimesi, kõik bussid on täis")
    else:
        bussi_vaja+=1    #если есть остаток, находим сколько автобусов нужно и сколько в последнем автобусе человек
        print(f"On vaja {bussi_vaja} bussi,et kõik inimesed kohale saaksid")
        print(f"Viimases bussis on {viimane_buss} inimesi")
except:
    print("Vale andmetüüp!")
print()
