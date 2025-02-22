# Praktiline töö "Tarkvaraarendaja vastuvõtt"  https://moodle.edu.ee/mod/assign/view.php?id=829247
# Programm, mis küsitleb inimesi, kes soovivad saada tarkvaraarendajaks. Ettevõttel on vaja 5 spetsialisti.


from vastuvott_Module import *

# "7. Tund (Töö failidega)/kusimused_vastused.txt" Указываю путь к файлу, тк место откуда запускается программа, находится в другой папке

kus_vas=laadi_kusimused_vastused('6. Töö failidega/kusimused_vastused.txt')

vastuvõetud=[]     # Принятые кадидаты (имя, баллы)
ebaõnnestunud=[]   # Отклоненные кандидаты (имя)


# Опрашиваем кандидатов
while len(vastuvõetud)<5:
    nimi = input("\nTere tulemast tarkvaraarendaja vastuvõttule!\nMe küsime teie käest 5 küsimusi\nSisestage teie nimi: ")
    punktid=küsi_kandidaat(nimi,kus_vas)

    if punktid>=6:  # Если 3 или более правильных ответов --> кандидат принят
        vastuvõetud.append((nimi,punktid))
    else:
        ebaõnnestunud.append(nimi)

# Добавляем данные кандидатов в файлы
andmete_faili_kirjutamine(vastuvõetud,ebaõnnestunud,'6. Töö failidega/vastuvõetud.txt','6. Töö failidega/eisoobi.txt')

# Выводим список принятых кандидатов
print("\nVastuvõetud kandidaadid:\n")
with open('6. Töö failidega/vastuvõetud.txt','r') as f:
    for line in f:
        print(line)

# Выводим список отклоненных кандидатов
print("\nEbaõnnestunud kandidaadid:\n")
with open('6. Töö failidega/eisoobi.txt','r') as f:
    for line in f:
        print(line)