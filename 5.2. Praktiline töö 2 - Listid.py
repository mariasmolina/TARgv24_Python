# Praktiline töö 2: "Listid" (https://moodle.edu.ee/mod/assign/view.php?id=1449749)

# Ülesanded:

# Ülesanne 1. Sõna/Lause
# Sisestage sõna või lause klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on.
# Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.

import string
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtpsdfghklzxcvbnm"
markid=string.punctuation # %&'()*+,-./:;<=>?@[\]^_`{|}~     #string.punctuation - содержит все символы пунктуации

while True:
    v=k=m=t=0    #v - vokaal, k - konsolant, m - markid, t - tühikud
    tekst=input("Sisesta mingi tekst: ").lower()
    if tekst.isdigit():    # если ввел только цифры, программа завершается
        break
    else:
        tekst_list=list(tekst)
        print(tekst_list) # "p", "r"
        for taht in tekst_list:
            if taht in vokaali:
                v+=1
            elif taht in konsonanti:
                k+=1
            elif taht in markid or taht=="ˇ":
                m+=1
            elif taht ==" ":
                t+=1
    print("Vokaali: ", v)
    print("Konsonanti: ", k)
    print("Markid: ", m)
    print("Tühikud: ", t)



# Ülesanne 2. Loetelu
# 2.1 Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
# Lisa võimalist loendis olevaid nimesid muuta.
# 2.2 Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed. opilased = [‘Juhan’,’Kati’,’Mario’,’Mario’,’Mati’,’Mati’]
# Loo kood, mis ei väljasta kordusi.
# 2.3 Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine.

vanused=[]
for i in range(7):
    vanus=int(input(f"{i+1}. Vanus: "))
    vanused.append(vanus)
print(f"Sisestatud vanused: {vanused}")
print(max(vanused)) #maksimaalne arv
print(min(vanused)) #minimaalne arv
print(sum(vanused)/len(vanused)) # keskmine arv vanusest


nimed=[]
for i in range(5):
    nimi=input(f"{i+1}.Nimi: ")
    nimed.append(nimi)
print("Enne sorteerimist:")
print(nimed)

nimed.sort()
print("Sorteerimise pärast:")
print(nimed)
print(f"Viimasena lisatud nimi on: {nimi}") #{nimed[4]}, {nimed[-1]}
v=input("Kas muudame nimeid?: ").lower()
if v=="jah":
    v=input("Nimi või positsioon: N/P").upper()
    if v=="P":
        print("Sisesta nime asukoht")
        v=int(input())
        uus_nimi=input("Uus nimi: ")
        nimed[v-1]=uus_nimi
    else:
        print("Sisesta nimi")
        vana_nimi=input("Vana nimi: ")
        v=nimed.index(vana_nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[v]=uus_nimi
print("Nimed muutmise pärast: ")
print(nimed)
# dublikatid 1
dublta=list(set(nimed))
print("Mitte korduv loetelu 1.variant")
print(dublta)
# dublikatid 2
dublta=[]
for nimi in nimed:
    if nimi not in dublta:
        dublta.append(nimi)
print("Mitte korduv loetelu 2.variant")
print(dublta)



# Ülesanne 3. Tärnid
# Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.

Värtused=[]
read=int(input("Reade kogus: "))
for i in range(read):
    arv=int(input("Arv"))
    Värtused.append(arv)
print(Värtused)
s=input("Sümbol: ")
for vartus in Värtused:
    print(vartus*s)

print()



# Ülesanne 4. Postiindex
# Kirjuta programm, mis kontrollib sisestatud indeksit (tähemärkide arv, vastav andmetüüp jne) ja näitab, millisesse maakonda see kuulub.

indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]
while 1:
    try:
        postiindex=int(input("Postiindeks: ")) #42345
        if len(str(postiindex))==5:
            break
        else:
            print("On vaja 5 sümboleid!")
    except:
        print("!!!")
print("Postiindeksi analüüs:")
index_list=list(str(postiindex)) #"4","2","3"...
s1=int(index_list[0]) # 4
print(f" Postiindeks {postiindex} on {indexid[s1-1]} piirkond") #12345 Tallinn