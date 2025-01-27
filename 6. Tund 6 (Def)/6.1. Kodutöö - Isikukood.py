# Kodutöö "Isikukood" https://moodle.edu.ee/mod/assign/view.php?id=1713190

from Isikukood_Modul import * 

ikoodid=[]  # Список верно введенных личных кодов
arvud=[]   # Список неверно введенных личных кодов

# Бесконечно запрашиваем личные коды

while True:
    try:
        ikood=input("\nSisestage isikukood (või sisestage 'X' lõpetamiseks): ")

        if ikood.lower()=="x":  # Проверка команды выхода
            break

        # Проверка на количество символов
        if not kontroll_pikkus(ikood):
            print("Isikukood peab sisaldama 11 numbrit!")
            arvud.append(ikood)
            continue

        # Проверка первого символа и даты рождения (не родился ли человек в будующем)
        aasta,kuu,paev=leia_synniaeg(ikood)
        if not kontroll_synniaeg(aasta,kuu,paev):
            print("Vale sünniaeg isikukoodis!")
            arvud.append(ikood)
            continue

        sunniaeg=f"{paev}.{kuu}.{aasta}"

        # Проверка контрольного числа
        kontroll_num=int(ikood[10])
        jaak=leia_kontroll_nr(ikood)
        if jaak!=kontroll_num:  # проверка, если остаток не равен контрольному номеру
            print("Vale kontroll number!")
            arvud.append(ikood)
            continue
        
        # Определение места рождения
        sunnikoht_num=int(ikood[7:10])
        sunnikoht=leia_sunnikoht(sunnikoht_num)
        if sunnikoht=="Tundmatu sünnikoht":
            print("Vale sünnikoht!")
            arvud.append(ikood)
            continue

        # Определение пола
        sugu=leia_sugu(ikood)


        print(f"See on {sugu}, tema sünnipäev on {sunniaeg}.\nSünnikoht on {sunnikoht}.")
        ikoodid.append(ikood)

    except:
        print("Sisestage isikukood!")

# Сортировка списков
arvud.sort() # Упорядочила по-возростанию

# перебирает все элементы из списка ikoodid и создает список из женских исикукодов, которые начинаются на 2,4,6
ikoodid_naised=[ikood for ikood in ikoodid if int(ikood[0]) in {2,4,6}]
# перебирает все элементы из списка ikoodid и создает список из мужских исикукодов, которые начинаются на 1,3,5
ikoodid_mehed=[ikood for ikood in ikoodid if int(ikood[0]) in {1,3,5}]
# соединила списки, в начало поставила искикукоды женщин, потом мужчин
ikoodid=ikoodid_naised+ikoodid_mehed

# Вывод на экран обоих списков
print(f"\nÕiged isikukoodid: {ikoodid}")
print(f"\nVigased isikukoodid: {arvud}")
print()


