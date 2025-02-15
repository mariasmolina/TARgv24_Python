from random import *
from math import *
from os import system
from gtts import *

riik_pealinn={}  #sõnastik {"Riik":"Pealinn"}
pealinn_riik={}  # sõnastik {"Pealinn": "Riik"}

def failist_to_dict(f: str):
    """Loeb tekstifailist riikide ja pealinnade paare ning tagastab kaks sõnastikku: {"Riik":"Pealinn"} ja {"Pealinn": "Riik"}
    :param f: Sõnastiku .txt fail
    :rtype: str  Kaks sõnastikku (riik_pealinn, pealinn_riik)
    """
    riik_pealinn = {}  # sõnastik {"Riik": "Pealinn"}
    pealinn_riik = {}  # sõnastik {"Pealinn": "Riik"}
    riigid = []  # järjend, kus talletakse riigide nimetused
   
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')  # k-võti, v-väärtus
        riik_pealinn[k] = v  # täidame riik_pealinn
        pealinn_riik[v] = k  # täidame pealinn_riik
        riigid.append(k)
    file.close()
   
    return riik_pealinn, pealinn_riik, riigid

# Добавляем в фаил и обновляем словарь
def fail_dict_uuendamine(k:any, v:any, fail: str, sõnastik: dict)->dict:
    """Lisab uue riigi ja pealinna sõnastikku ja salvestab faili
    :param any riik: Riik
    :param any pealinn: Pealinn
    :param str fail: Sõnastiku .txt fail
    :param dict sõnastik: Sõnastik
    :rtype: dict Uuendatud sõnastik
    """    
    sõnastik.update({k: v})   # Обновляем словарь  (k-võti, v-väärtus)
    sõnastik=dict(sorted(sõnastik.items()))    # Сортируем словарь

    with open(fail, 'w', encoding="utf-8-sig") as f:
        for k, v in sõnastik.items():  
            f.write(f"{k}-{v}\n")

    return sõnastik

# def leia_linn_pealinn(sõnastik:dict, vastupidine_sõnastik:dict, otsitav_sõna:str, fail:str):
#     """Kuvab riigi pealinna, kui kasutaja sisestab riigi nime. Kui riiki ei leita, küsib pealinna ja lisab sõnastikku
#     :param dict sõnastik: Peamine sõnastik (nt riik_pealinn)
#     :param dict vastupidine_sõnastik: Vastupidine sõnastik (nt pealinn_riik)
#     :param str otsitav_sõna: "riik" (küsib riiki, kuvab pealinna) või "pealinn" (küsib pealinna, kuvab riiki)
#     :param str fail: Sõnastiku .txt fail
#     """
#     while True:
#         if otsitav_sõna=="pealinn":
#             vastus=input("Sisestage riik: ")
#             for k in sõnastik:   # k-võti, v-väärtus
#                 if k.lower()==vastus.lower():   # в случае, если вводит с маленькой буквы
#                     print("Pealinn:", {sõnastik[k]})
#                     # räägimine(f"Riik on {k}, Pealinn on {v}", "et")   # text to speech/проговаривание страны и столицы
#                     return sõnastik, vastupidine_sõnastik

#             print("Otsingu sõna puudub sõnastikus. Lisame seda!")   # Если не нашли в словаре, спрашиваем и добавляем
#             uus_sõna=input(f"Sisestage {vastus} vastav {otsitav_sõna}: ")
#             sõnastik=fail_dict_uuendamine(vastus, uus_sõna, fail, sõnastik)
#             vastupidine_sõnastik.update({uus_sõna:vastus})
#             print(f"'{vastus}-{uus_sõna}' on lisatud sõnastikusse")

#             return sõnastik, vastupidine_sõnastik
           

#         elif otsitav_sõna=="riik":
#             vastus=input("Sisestage pealinn: ")
#             for k, v in vastupidine_sõnastik.items():
#                 if k.lower()==vastus.lower():
#                     print("Riik: ", v)
#                     # räägimine(f" Riik on {v}, Pealinn on {k}", "et")
#                     return sõnastik, vastupidine_sõnastik

#             print("Otsingu sõna puudub sõnastikus. Lisame seda!")   # Если не нашли в словаре, спрашиваем и добавляем
#             uus_sõna=input(f"Sisestage {vastus} vastav {otsitav_sõna}: ")
#             sõnastik=fail_dict_uuendamine(uus_sõna, vastus, fail, sõnastik)
#             vastupidine_sõnastik.update({vastus:uus_sõna})
#             print(f"'{vastus}-{uus_sõna}' on lisatud sõnastikusse")
#             return sõnastik, vastupidine_sõnastik

#         if vastus.lower()=="x":
#             break



# Исправление ошибок в словаре
def viga_parandus(sõnastik:dict, fail: str)->dict:
    """Parandab vale riigi ja pealinna paari sõnastikus ja salvestab muudatused faili
    :param dict sõnastik: 
    :param str fail: Sõnastiku .txt fail
    :rtype: dict Uuendatud sõnastik
    """
    while True:
        riik=input("Sisestage riik, mille andmed soovite parandada: ")
        if riik in sõnastik:
            uus_riik=input("Sisestage parandatud riik: ")
            uus_pealinn=input("Sisestage parandatud pealinn: ")

            # Обновляем словарь
            sõnastik[uus_riik]=sõnastik.pop(riik)  # Меняем ключ
            sõnastik[uus_riik]=uus_pealinn  # Меняем значение

            # Сортируем словарь
            sõnastik=dict(sorted(sõnastik.items()))

            # Перезаписываем словарь в файл
            with open(fail, 'w', encoding="utf-8-sig") as f:
                for riik, pealinn in sõnastik.items():  
                    f.write(f"{riik}-{pealinn}\n")

            print(f"Viga on parandatud! Parandatud andmed: {uus_riik} - {uus_pealinn}")

            return sõnastik

        elif riik=="x":
            return False
        else:
            print(f"Riik {riik} ei ole sõnastikus.")

def räägimine(tekst:str,keel:str):
    """Teeb kõne tekstist ja keelest, seejärel mängib heli
    :param str tekst: Tekst, mis teisendatakse kõneks
    :param str keel: Keel, milles kõne tehakse
    """
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

def viktoriin(sõnastik:dict):
    """Käivitab viktoriini, kus küsitakse riikide ja pealinnade kohta
    :param dict sõnastik: Sõnastik
    """
    print("\n--- Tere tulemast viktoriini! ---\nTeile esitatakse juhuslikke küsimusi, kas riigi või pealinna kohta\n")
    õiged_vastused=0
    for i in range(5):
        riik,pealinn=choice(list(sõnastik.items()))   # Выбираем случайную пару "страна - столица"  (choice не работает с .items() --> переделала в list)
        valik=choice(["riik","pealinn"])  # Случайным образом решаем, что спрашивать у пользователя - страну или столицу
        if valik=="riik":
            vastus=input(f"Mis riigi pealinn on {pealinn}? ")
            if vastus.lower()==riik.lower():
                print("Õige!")
                õiged_vastused+=1
            else:
                print(f"Vale! Õige vastus: {riik}")
        else:
            vastus=input(f"Mis on {riik} pealinn? ")
            if vastus.lower()==pealinn.lower():
                print("Õige!")
                õiged_vastused+=1
            else:
                print(f"Vale! Õige vastus: {pealinn}")

    tulemus=round((õiged_vastused/5)*100)
    print(f"\nTeie tulemus: {tulemus}% õigetest vastustest!")
