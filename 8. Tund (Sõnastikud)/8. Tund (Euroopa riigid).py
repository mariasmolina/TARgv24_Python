# Работа со словарями "Euroopa riigid"      https://moodle.edu.ee/mod/assign/view.php?id=1966729

from Euroopa_Liigid_Module import *

riik_pealinn, pealinn_riik, riigid = failist_to_dict('8. Tund (Sõnastikud)/riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())

while True:
    print("\n--- Euroopa riigid - sõnastik ---")
    print("\n1 - Sõnastik\n2 - Pealinna kuvamine\n3 - Riigi nimi kuvamine\n4 - Viga parandamine sõnastikus\n5 - Kontrollida sõnavara teadmisi\n6 - Lõpetamine")
    vastus=int(input("\nSisestage valik: "))

    if vastus==1:
        for key, value in riik_pealinn.items():
            print(f"{key} - {value}\n")

 # Отображение столицы, если вводиться название государства (и добавление в словарь - если нет)
    elif vastus==2:
        while True:
            riik=input("Sisetage riik: ")
            if riik=="x": 
                break
            for k in riik_pealinn:   # k-võti
                if k.lower()==riik.lower():    # в случае, если вводит с маленькой буквы
                    print("Pealinn: ",riik_pealinn[k])
                    räägimine(f" Riik on {k}, Pealinn on {riik_pealinn[k]}", "et")    # text to speech/проговаривание страны и столицы
                    break
            else:
                print("Otsingu sõna puudub sõnastikus. Lisame seda!")
                pealinn=input("Sisestage seda riigi pealinn: ")
                riik_pealinn=fail_dict_uuendamine(riik, pealinn, '8. Tund (Sõnastikud)/riigid_pealinnad.txt', riik_pealinn)   # Добавляе в фаил (словарь обновляется)
                print(f"Teave riigi {riik} ja pealinna {pealinn} kohta on lisatud sõnastikusse")

            break

# Отображение государства, если вводиться столица (и добавление в словарь - если нет)
    elif vastus==3:
        while True:
            pealinn=input("Sisetage pealinn: ")
            if pealinn=="x": 
                break
            for k in pealinn_riik:  # k-võti
                if k.lower()==pealinn.lower():   # в случае, если вводит с маленькой буквы
                    print("Riik: ",pealinn_riik[k])
                    räägimine(f" Riik on {pealinn_riik[k]}, Pealinn on {k}", "et")
                    break
            else:
                print("Otsingu sõna puudub sõnastikus. Lisame seda!")
                riik=input("Sisestage seda pealinna riik: ")
                pealinn_riik=fail_dict_uuendamine(riik, pealinn, '8. Tund (Sõnastikud)/riigid_pealinnad.txt', riik_pealinn)   # Добавляе в фаил (словарь обновляется)
                print(f"Teave riigi {riik} ja pealinna {pealinn} kohta on lisatud sõnastikusse")

            break

# Вывод словаря. Если пользователь находит ошибку в словаре, то у него есть возможность ее исправить
    elif vastus==4:
        riik_pealinn=viga_parandus(riik_pealinn, '8. Tund (Sõnastikud)/riigid_pealinnad.txt')
    
    elif vastus==5:
        viktoriin(riik_pealinn)

# Выход из программы
    elif vastus == 6:
        print("\n--- Head aega! ---\nProgrammi lõpetamine...")
        break

    else:
        print("Viga! Valige tegevus!")


