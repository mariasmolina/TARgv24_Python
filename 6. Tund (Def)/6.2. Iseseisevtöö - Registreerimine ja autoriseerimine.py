# Iseseisevtöö "Registreerimine ja autoriseerimine" https://moodle.edu.ee/mod/assign/view.php?id=1102881

# Programm, mis simuleerib kasutajate registreerimist ja autoriseerimist mingis süsteemis.


from MyModule import *   # funktsioonid eraldi moodulis MyModule.py
import random

sisselogimised = []   # Список логинов
paroolid = []         # Список паролей

while True:
    print("\n--- Tere tulemast meie süsteemi! ---\n\n Siin te saate valida tegevus:\n1. Registreerimine\n2. Automatiseerimine\n3. Nime või parooli muutmine\n4. Unustanud parooli taastamine\n5. Lõpetamine")
    valik=input("\nSisestage valik (number või tegevus): ").lower()

    # 1. Регистрация
    if valik=="registreerimine" or valik=="1":
        uus_nimi=input("Sisestage uus kasutajanimi: ")
        if uus_nimi in sisselogimised:  # Проверяем, зарегестрировано ли уже имя
            print("Selline kasutaja on juba olemas!")
        sisselogimised.append(uus_nimi) 
        print("\nParooli loomine! Teil on kaks võimalust:\n1. Automaatne parooli genereerimine\n2. Looge parool ise")

        while True:
            valik_parool=input("\nValige tegevus (number 1 või 2): ")
            if valik_parool=="1":
                # Первый вариант кода из задания в moodle (так как создает более надежный пароль)
                str0=".,:;!_*-+()/#¤%&"
                str1 = '0123456789'
                str2 = 'qwertyuiopasdfghjklzxcvbnm'
                str3 = str2.upper()
                str4 = str0+str1+str2+str3
                ls = list(str4)
                random.shuffle(ls)
                # Извлекаем из списка 12 произвольных значений
                psword = ''.join([random.choice(ls) for x in range(12)])
                # Пароль готов
                print(f"Teie uus parool on: {psword}")
                paroolid.append(psword)

            elif valik_parool=="2":
                while True:
                    psword=input("Sisestage uus parool: ")
                    if not parool_kontroll(psword):
                        print("Sisestage turvalisem parool!")
                    else:
                        print(f"Teie uus parool on: {psword}")
                        break
                        paroolid.append(psword)
                break
            else:
                print("Valige tegevuse number 1 või 2!")

    # 2. 
    elif valik=="autoriseerimine" or valik=="2":
        print("")


    # 3. Смена логина или пароля
    elif valik=="nime või parooli muutmine" or valik=="3":
        print("")


    # 4. Восстановление забытого пароля
    elif valik=="unustanud parooli taastamine" or valik=="4":
        print("")


    # 5. Выход из программы
    elif valik=="lõpetamine" or valik=="5":
        print("\n--- Head aega! ---\nProgrammi lõpetamine...")
        break
    else:
        print("Valige tegevus või tegevuse number!")

