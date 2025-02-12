from MinuOmaMoodul import *

salasõnad=loe_failist("7. Tund (Töö failidega)/Salasõnad.txt")
kasutajanimed=loe_failist("7. Tund (Töö failidega)/Kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("\n1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv: "))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
        kirjuta_failisse('7. Tund (Töö failidega)/Kasutajad.txt',kasutajanimed)
        kirjuta_failisse('7. Tund (Töö failidega)/Salasõnad.txt',salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            kasutajanime=ümber_kirjuta_fail('7. Tund (Töö failidega)/Kasutajad.txt')
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
            salasõnad=ümber_kirjuta_fail('7. Tund (Töö failidega)/Salasõnad.txt')
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            kasutajanime=ümber_kirjuta_fail('7. Tund (Töö failidega)/Kasutajad.txt')
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
            salasõnad=ümber_kirjuta_fail('7. Tund (Töö failidega)/Salasõnad.txt')
    elif vastus==4:
        print("Unustanud parooli taastamine")
        vana_login=input("Sisestage kasutajanimi: ")
        if vana_login not in kasutajanimed:
            print("Kasutajanimi ei leitud. Proovige uuesti!")
        else:
            index_parool=kasutajanimed.index(vana_login)
            uus_parool=genereeri_parool()
            salasõnad.pop(index_parool)  
            salasõnad.insert(index_parool,uus_parool)
            kirjuta_failisse('7. Tund (Töö failidega)/Kasutajad.txt',kasutajanimed)
            kirjuta_failisse('7. Tund (Töö failidega)/Salasõnad.txt',salasõnad)
            print(f"Teie uus parool: {uus_parool}")
            saada_uus_parool(uus_parool)   # отправляет новый пароль на почту

    elif vastus==5:
        print("Lõpetamine")

        break
    else:
        print("Tundmatu valik")