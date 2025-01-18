# Kodutöö "Isikukood" https://moodle.edu.ee/mod/assign/view.php?id=1713190


from datetime import *

ikoodid=[]  # Список правильных личных кодов
arvud=[]   # Список неправильных личных кодов

# Бесконечно запрашиваем личные коды
while True:
    try:
        ikood=input("Sisestage isikukood: ")

        # Проверка на количество символов
        if len(ikood)!=11:   
            arvud.append(ikood)
            print("Isikukood peab sisaldama 11 numbrit!")
            continue

        # Проверка первого символа   
        esimene_arv=int(ikood[0])
        if esimene_arv not in {1,2,3,4,5,6}:
            arvud.append(ikood)
            print("Isikukoodi esimene number peab olema 1 kuni 6!")
            continue

        # Извлекаем год, месяц, день рождения, место рождения и контрольный номер из исикукода
        # Точный год рождения находим зная первую цифру исикукода (1,2 - 1800; 3,4 - 1900; 5,6 - 2000)
        aasta=int(ikood[1:3])+(1800 if esimene_arv in {1,2} else 1900 if esimene_arv in {3,4} else 2000)
        kuu=int(ikood[3:5])
        paev=int(ikood[5:7])
        sunnikoht_num=int(ikood[7:10])
        kontroll_num=int(ikood[10])
        sunniaeg=f"{paev}.{kuu}.{aasta}"

        # Проверка даты рождения с помощью функции datetime
        try:
            datetime(aasta,kuu,paev)
        except:
            print("Viga! Vale sünniaeg isikukoodis!")
            arvud.append(ikood)
            continue

        # Проверка - не родился ли человек в будующем (с помощью функции datetime.now)
            if datetime(aasta,kuu,paev)>datetime.now():
                print("Viga! Vale sünniaeg isikukoodis")
                arvud.append(ikood)
                continue

        # Вычисление контрольного числа и проверка
        astme_kaal_1=[1,2,3,4,5,6,7,8,9,1]   # I astme kaal
        astme_kaal_2=[3,4,5,6,7,8,9,1,2,3]   # II astme kaal

        # сумма = первое число ikood * первое число astme_kaal + --> и далее по циклу
        astme_summa_1=sum(int(ikood[i])*astme_kaal_1[i] for i in range (10))
        jaak=astme_summa_1%11  # остаток = сумма делится на 11 --> остаток = контрольный номер

        if jaak==10:  # в случае если остаток равен 10, то -->
            astme_summa_2=sum(int(ikood[i])*astme_kaal_2[i] for i in range (10)) # такой же цикл, как и с astme_summa_1
            jaak=astme_summa_2%11    
            if jaak==10: 
                jaak=0    # по условию, если остаток равен 10, то контрольный номер будет 0
        
        if jaak!=kontroll_num:  # проверка, если остаток не равен контрольному номеру
            print("Vale kontroll number!")
            arvud.append(ikood)
            continue

        # Определение места рождения (делаем список вложенный в список)
        haiglad=[
            [1,10,"Kuressaare Haigla"],
            [11,19,"Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"],
            [21,220,"Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"],
            [221,270,"Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"],
            [271,370,"Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"],
            [371,420,"Narva Haigla"],
            [421,470,"Pärnu Haigla"],
            [471,490,"Pelgulinna Sünнitusmaja (Tallinn), Haapsalu haigla"],
            [491,520,"Järvamaa Haigla (Paide)"],
            [521,570,"Rakvere, Tapa haigla"],
            [571,600,"Valga Haigla"],
            [601,650,"Viljandi Haigla"],
            [651,700,"Lõuna-Eesti Haigla (Võru), Põlva Haigla"]
            ]

        for alg,lopp,koht in haiglad:    # задаю цикл, перебирающий все элементы в haiglad
            if alg<=sunnikoht_num<=lopp:  # условие, есть ли номер места рождения между первым и вторым элементом
                sunnikoht=koht           
                break
        else:
            print("Vale sünnikoht!")
            arvud.append(ikood)
            continue

        # Определение пола (1,3,5 -муж, 2,4,6-жен)
        if esimene_arv in {1,3,5}:
            sugu="mees"
        else:
            sugu="naine"

        # Вывод на экран результата
        print(f"See on {sugu}, tema sünnipäev on {sunniaeg} ja sünnikoht on {sunnikoht}.")
        ikoodid.append(ikood)


        # Сортировка списков
        arvud.sort() # Упорядочила по-возростанию

        # разделила списки по полу 

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

    except:
        print("Sisestage isikukood!")
    
