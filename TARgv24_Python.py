from math import pi
from random import * #*-kõik funktisoonid, randint as rd funktisoonide ümbernimetus
#import random -> random.randint()
from math import *

#Ülesanne 1
# print("Hello world!")
# nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa, upper()-AAA, capitalize()-Aaa
# print("Tere tulemast! Tervitan sind ", nimi)
# print("Tere tulemst! Tervitan sind "+ nimi)
# vanus=int(input("Kui vana sa oled? "))
# print("Tere, maailm! Tervitan sind "+nimi+"! Sa oled ",vanus," aastat vana.")
# print(f"\tTere, maailm! \nTervitan sind {nimi}! Sa oled {vanus} aastat vana.")


#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus),(eesnimi),(pikkus),(kas_käib_koolis))


#Ülesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")


#Ülesanne 4
print("Lääbimõõdu leidmine!")
#C-ümbermõõt
C=float(input("Ümbermööt: "))
läbimõõt=C/pi
print(f"Läbimõõt on {round(läbimõõt,2)}")