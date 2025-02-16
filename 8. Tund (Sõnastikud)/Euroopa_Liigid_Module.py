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

# Ищем страну или столицу в словаре и добавляем новую пару, если искомое слово отсутствует
def leia_linn_pealinn(sõnastik:dict, otsitav_sõna:str, fail:str)->dict:
    """Otsib riigi või pealinna sõnastikust ning lisab uue andmepaari, kui otsitav sõna puudub
    :param dict sõnastik: Sõnastik
    :param str otsitav_sõna:  Otsitav sõna, kas "riik" või "pealinn", et valida funktsioon
    :param str fail: Sõnastiku .txt fail
    :rtype: dict Uuendatud sõnastik
    """ 
    if otsitav_sõna=="pealinn":
        while True:
            riik=input("Sisetage riik: ")
            if riik=="x": 
                break
            for k in sõnastik:   # k-võti
                if k.lower()==riik.lower():    # в случае, если вводит с маленькой буквы
                    print("Pealinn: ",sõnastik[k])
                    räägimine(f" Riik on {k}, Pealinn on {sõnastik[k]}", "et")    # text to speech/проговаривание страны и столицы

                    return sõnastik
            else:
                print("Otsingu sõna puudub sõnastikus. Lisame seda!")
                pealinn=input("Sisestage seda riigi pealinn: ")
                sõnastik=fail_dict_uuendamine(riik, pealinn, fail, sõnastik)   # Добавляе в фаил (словарь обновляется)
                print(f"Teave riigi {riik} ja pealinna {pealinn} kohta on lisatud sõnastikusse")

                return sõnastik   # Возвращаем обновленный словарь

    elif otsitav_sõna=="riik":
        while True:
            pealinn=input("Sisetage pealinn: ")
            if pealinn=="x": 
                break
            for k, v in sõnastik.items():  # k-võti, v-väärtus
                if v.lower()==pealinn.lower():   # в случае, если вводит с маленькой буквы
                    print("Riik: ",sõnastik[k])
                    räägimine(f" Riik on {sõnastik[k]}, Pealinn on {k}", "et")

                    return sõnastik # Возвращаем словарь (он не изменился)
            else:
                print("Otsingu sõna puudub sõnastikus. Lisame seda!")
                riik=input("Sisestage seda pealinna riik: ")
                sõnastik=fail_dict_uuendamine(riik, pealinn, fail, sõnastik)   # Добавляе в фаил (словарь обновляется)
                print(f"Teave riigi {riik} ja pealinna {pealinn} kohta on lisatud sõnastikusse")

                return sõnastik 

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

# text to speech/проговаривание страны и столицы
def räägimine(tekst:str,keel:str):
    """Teeb kõne tekstist ja keelest, seejärel mängib heli
    :param str tekst: Tekst, mis teisendatakse kõneks
    :param str keel: Keel, milles kõne tehakse
    """
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

# Викторина на знание словаря
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
