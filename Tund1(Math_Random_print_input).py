from random import * #*-kõik funktisoonid, randint as rd funktisoonide ümbernimetus
#import random -> random.randint()
from math import *  #from math import pi

# #Ülesanne 1
# print("Hello world!")
# nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa, upper()-AAA, capitalize()-Aaa
# print("Tere tulemast! Tervitan sind ", nimi)
# print("Tere tulemst! Tervitan sind "+ nimi)
# try:
#     vanus=int(input("Kui vana sa oled? "))
#     print("Tere, maailm! Tervitan sind "+nimi+"! Sa oled ",vanus," aastat vana.")
#     print(f"\tTere, maailm! \nTervitan sind {nimi}! Sa oled {vanus} aastat vana.")
# except:
#     print("On vaja numbreid sisestada!")


# #Ülesanne 2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print("vanus: ",type(vanus))
# print("eesnimi: ",type(eesnimi)) 
# print("pikkus: ",type(pikkus))  
# print("kas_käib_koolis: ",type(kas_käib_koolis))
# #Mis võimalus veel peale True oleks viimast muutujat väärtustada?
# kas_käib_koolis = False
# kas_käib_koolis = "Jah"
# kas_käib_koolis = "Ei"
# print("kas_käib_koolis: ",type(kas_käib_koolis))

# #Ülesanne 3
# kokku=randint(1,1000)
# print(f"Kokku on {kokku} kommi")
# kommi=int(input("Mitu kommi sa tahad? "))
# kokku=kokku-kommi
# print(f"Jääk on {kokku} kommi")


# #Ülesanne 4
# print("Lääbimõõdu leidmine!")
# #C-ümbermõõt
# C=float(input("Ümbermööt: "))
# läbimõõt=C/pi
# print(f"Läbimõõt on {round(läbimõõt,2)}")


#Ülesanne 5
print("Ristkülikukujulise maatüki diagonaali leidmine!")
#d-diagonaal
N=float(input("Sisestage N (m): "))
M=float(input("Sisestage M (m): "))
d=sqrt(pow(N,2)+pow(M,2)) #теорема Пифагора
print(f"Ristkülikukujulise maatüki diagonaal on {round(d,2)} m!")


#Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg  #v=s/t, поменяла местами скорость и расстояние

print("Sinu kiirus oli " + str(round(kiirus,2)) + " km/h") #округлила до сотых


#Ülesanne 7
print("Leiame aritmeetilise keskmise suvalisest 5 täis arvust")
arv1=trunc(float(input("Sisestage esimene arv: ")))
arv2=trunc(float(input("Sisetage teine arv: ")))
arv3=trunc(float(input("Sisestage kolmas arv: ")))
arv4=trunc(float(input("Sisestage neljas arv: ")))
arv5=trunc(float(input("Sisestage viies arv: ")))
arit_keskmine=(arv1+arv2+arv3+arv4+arv5)/5
print(f"Nende viie arvu aritmeetiline keskmine on: {arit_keskmine}")
# trunc(float(....))-в случае если вводишь всё таки не целые числа, то программа преобразует их в целые и найдет из них среднее арифметическое
# arv1=int(input("Sisestage esimene arv: "))) jne. Если вводить сразу целые числа.


#Ülesanne 8
print('\t  @..@\n\t (----)\n\t( \__/ )\n\t^^ "" ^^')


#Ülesanne 9 (1 variant)
print("\t  Leiame kolmnurga ümbermõõdu!\n\tOn vaja teada 3 kolmnurga külge!\n")
#a-esimene külg, b-teine külg, c-kolmas külg
a=float(input("Kui suur on esimene külg? "))
b=float(input("Kui suur on teine külg? "))
c=float(input("Kui suur on kolmas külg? "))
#P-kolmnurga ümbermõõt
P=a+b+c
print(f"Kolmnurga ümbermõõt on {P}")


#Ülesanne 10
print("\тTellisime koos sõbrannaga P suure pitsa.\nKokku summa on 12,90 eur ja 10% jootraha teenindajale.\nArvutame, kui palju peab igaüks maksma!\n")
jootraha=12.90*0.1
#summa-pitsa hind + 10% jootraha
summa=jootraha+12.90
#summa-kui palju peab igaüks maksma
summa=round(summa/2,2)
print(f"Mina maksan: {summa} eur \nMinu sõber P maksab: {summa} eur")