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
# print(f"{kogus:, d} 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa.\nMeil on vaja {kogus*2} eur.")

#Ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
c=a + a + b 
print(f"{c*2} {a*4}")