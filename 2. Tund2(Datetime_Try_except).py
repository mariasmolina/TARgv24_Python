from datetime import *
from calendar import *
from math import *
from random import *


# #Ülesanne 1
# täna=date.today()

# print(f"Tere! Täna on {täna}\n")

# tänaf=date.today().strftime("%B %d, %Y")  #nimetus() - funktsioon
# print(f"Tere! Täna on {täna}")

# d=täna.day  #nimetus - omadus
# m=täna.month
# y=täna.year
# print(d)
# print(m)
# print(y)
# try:
#     lõpp_päev=int(input("\nKui palju päeva on selles kuus? "))
#     päeva_jäänud=lõpp_päev-d
#     print(f"Kuu lõppuni on jaanud {päeva_jäänud}")
# except:
#     print("On vaja täisnumbrei sisestada!")

# paevadekogus=monthrange(2024,11)[1]
# print(paevadekogus)

# detsP=monthrange(2024,12)[1] #31

# novP=monthrange(2024,11)[1] #30
# jaak=detsP+novP-d
# jaak2=novP-d
# print(f"Aasta lõppuni on {jaak} päeva")
# print(f"Kuu lõppuni on {jaak2} päeva")

# #Ülesanne 2
# vastus1=3+8/(4-2)*4
# print(f"\n3+8/(4-2)*4={vastus1}")
# vastus2=3+8/4-2*4
# print(f"Kui sulgud mitte kasutada, siis: 3+8/4-2*4={vastus2}")
# vastus3=3+(8/4-2*4)
# print(f"Teise kombinatsiooni vastus: 3+(8/4-2*4)={vastus3}")


# #Ülesanne 3
# #r=радиус круга
# #1 variant
# try:
#     r=float(input("Sisestage ringi raadius: "))
#     S_ruut=round((r*2)**2,2)
#     P_ruut=round((r*2)*4,2)
#     S_ring=round(pi*r**2,2)
#     C=round(pi*r*2,2)  #C-длина окружности
#     print(f"Ringi pindala on {S_ring}\nRingi ümbermõõt on {C}\nRuudu pindala on {S_ruut}\nRuudu ümbermõõt on {P_ruut}")

# except:
#     print("Sisestage arv!")


# #2 variant
# r=trunc(random()*100)  #0.0...1.0
# S_ruut=round((r*2)**2,2)
# P_ruut=round((r*2)*4,2)
# S_ring=round(pi*r**2,2)
# C=round(pi*r*2,2)
# print(f"\nr={r}")
# print(f"Ringi pindala on {S_ring}\nRingi ümbermõõt on {C}\nRuudu pindala on {S_ruut}\nRuudu ümbermõõt on {P_ruut}")

# #Ülesanne 4
# maa=6378
# maa*=100000  #радиус Земли в сантиметрах
# d=2.575  #диаметр 2-евро монеты в сантиментрах
# Lmaa=pi*maa*2
# kogus=int(Lmaa/d)
# #'{:,.3f}'.format(kogus)
# print(f"{kogus:,d} 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa.\nMeil on vaja {(kogus*2):,d} eur.")

#Ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
c=a*2+b 
print(c*2,a*4)
print()

#Ülesanne 6 - 1 variant
laul="Rong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?\n\nRong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill.".upper()   
print(laul)
print()
print()
#Ülesanne 6 - 2 variant
laul="""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""
print(laul.upper())
print()

#Ülesanne 7
try:
    print("Leiame ristküliku ümbermõõdu ja pindala!")
    pikkus=float(input("Sisetage ristküliku pikkus: "))
    laius=float(input("Sisestage ristküliku laius: "))
    P=round(2*(pikkus+laius),2) #P-периметр
    S=round(pikkus*laius,2)  #S-площадь
    print(f"Ristküliku ümbermõõt on {P}\nRistküliku pindala on: {S}")

except:
    print("Sisestage arv!")
print()

#Ülesanne 8
try:
    print("Kütusekulu arvutamine!")
    l=float(input("Sisestage, kui palju kütuse liitreid oli tangitud: "))  #l-количество литров топлива было заправлено
    s=float(input("Sisestage läbitud kilomeetrid: "))  #s-количество пройденных километров
    kütusekulu=round((l/s)*100,2)
    print(f"Kütusekulu 100km kohta on keskmiselt {kütusekulu} liitrid")

except:
    print("Sisestage arv!")
print()

#Ülesanne 9
try: 
    print("Rulluisutajad\nRulluisutaja keskmine kiirus on 29,9 km/t")
    minut=float(input("Sisestage minutid: "))
    S=round((29.9*(minut/60)),2)  #minut перевела в часы и нашла расстояние
    print(f"Rulluisutaja jõuab {S} km {round(minut,2)} minutiga")

except:
    print("Sisestage arv!")
print()

#Ülesanne 10
try:
    print("Ajateisendus")
    aeg=float(input("Sisestage aja minutites: "))
    tunnid=int(aeg/60)   #целые часы
    minutid=int(aeg-tunnid*60)  #остаток минут
    print(f"Vastus: {tunnid}:{minutid:02d}")  #:02d-формат, если число(минуты) состоит из меньшего количества цифр, чем указаны в формате(2), то перед числом будет 0

except:
    print("Sisestage arv!")