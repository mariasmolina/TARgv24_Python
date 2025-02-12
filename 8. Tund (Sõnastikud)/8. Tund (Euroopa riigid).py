# Работа со словарями "Euroopa riigid"      https://moodle.edu.ee/mod/assign/view.php?id=1966729

from Euroopa_Liigid_Module import *

riik_pealinn, pealinn_riik, riigid = failist_to_dict('8. Tund (Sõnastikud)/riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())

print("Euroopa riigid - sõnastik")
print("\n1-Pealinna kuvamine\n2-Riigi nimi\n3-Viga parandamine\n4- Viktoriin\n")
vastus=int(input("Sisestage arv: "))

# отображение столицы, если вводиться название государства
while True:
    if vastus==1:
        riik=input("Sisetage riik: ")
        if riik=="X": 
            break
       
        if riik not in riigid:
            print("Otsingu sõna puudub sõnastikus. Lisame seda!")
            pealinn=input("Sisestage seda riigi pealinn: ")
            riik_pealinn.update({'riik'-'pealinn'})
            failisse_lisamine()
        else:
            print("Pealinn: ",riik_pealinn[riik])
        

# отображение государства, если вводиться столица
while True:
    if vastus==2:
        pealinn=input("Sisetage pealinn: ")
        if pealinn=="X": 
            break
        print("Riik: ",pealinn_riik[pealinn])

for key, value in riik_pealinn.items():
    print(key+"-"+value+"\n")
