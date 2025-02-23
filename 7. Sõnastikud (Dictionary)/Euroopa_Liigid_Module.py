from random import *
from math import *
from os import system
from gtts import *
import os
import time

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

# text to speech/проговаривание страны и столицы
def räägimine(tekst:str,keel:str):
    """Teeb kõne tekstist ja keelest, seejärel mängib heli
    :param str tekst: Tekst, mis teisendatakse kõneks
    :param str keel: Keel, milles kõne tehakse
    """
    while os.path.exists("heli.mp3"):  # Чтобы запускать фаил несколько раз
        try:
            os.remove("heli.mp3")
        except:
            time.sleep(1)  # Ждём, пока файл освободится и повторяем
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

# Ищем страну или столицу в словаре и добавляем новую пару, если искомое слово отсутствует
def leia_linn_pealinn(sõnastik:dict, otsitav_sõna:str, fail:str)->dict:
    """Otsib riigi või pealinna sõnastikust ning lisab uue andmepaari, kui otsitav sõna puudub
    :param dict sõnastik: Sõnastik
    :param str otsitav_sõna:  Otsitav sõna, kas "riik" või "pealinn", et valida funktsioon
    :param str fail: Sõnastiku .txt fail
    :rtype: dict Uuendatud sõnastik
    """ 
    while True:
        if otsitav_sõna=="pealinn":
            vastus=input("Sisetage riik: ")

        else:
            vastus=input("Sisetage pealinn: ")
        
        if vastus=="x":
            break
        
        for k, v in sõnastik.items():    # k-võti (ключ), v-väärtus (значение)
            if otsitav_sõna=="pealinn" and k.lower()==vastus.lower():   # Если вводится с маленькой буквы
                print(f"Pealinn: {v}")
                räägimine(f"Riik on {k}, Pealinn on {v}", "et")

                return sõnastik

            elif otsitav_sõna=="riik" and v.lower()==vastus.lower():
                print(f"Riik: {k}")
                räägimine(f"Riik on {k}, Pealinn on {v}", "et")

                return sõnastik
        
        else:
            print("Otsingu sõna puudub sõnastikus. Lisame seda!")

            if otsitav_sõna=="pealinn":
                uus_sõna=input("Sisestage seda riigi pealinn: ")
            else:
                uus_sõna=input("Sisestage seda pealinna riik: ")
        
            sõnastik=fail_dict_uuendamine(vastus, uus_sõna, fail, sõnastik)
            print(f"Teave riigi '{vastus}' ja pealinna '{uus_sõna}' kohta on lisatud sõnastikusse")

            return sõnastik   # Возвращается обновленный словарь

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
