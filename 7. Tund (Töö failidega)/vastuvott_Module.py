import random


# -- Словарь вопросов и ответов -- 

def laadi_kusimused_vastused(failinimi:str)->list:
    kus_vas={}   # словарь
    with open(failinimi,'r',encoding="utf-8") as f:
        for rida in f:
            # Разделяет строку на две части по символу ":" и удаляет все пробелы
            kusimus,vastus=rida.strip().split(':')
            kus_vas[kusimus]=vastus  # Добавляем вопрос-ответ в словарь (вопрос=ключ/key)
    return kus_vas



# -- Cобеседование с одним кандидатом --

def küsi_kandidaat(nimi,kus_vas):
    punktid=0
    #  Выбирает случайные 5 вопросов из словаря kus_vas
    # kus_vas.keys - все ключи (вопросы) из словаря --> преобразуем в список
    # random.sample(...,5) - выбирает случайные 5 элементов из этого списка
    vastuvotu_kusimused=random.sample(list(kus_vas.keys()),5)

    for kusimus in vastuvotu_kusimused:
        print(f"\n{nimi}, {kusimus}")

        vastus=input("Sisestage vastus: ")

        if vastus.lower()==kus_vas[kusimus].lower():
            punktid+=2   # 2 пункта за правильный ответ

    print(f"\nKandidaat {nimi} sai {punktid} punkti.\n")

    return punktid



# -- Запись данных принятых и отклоненных кандидатов --

def andmete_faili_kirjutamine(vastuvõetud:list,ebaõnnestunud:list,vastuvõetud_fail:str,eisoobi_fail:str):
    vastuvõetud.sort(key=lambda x: x[1], reverse=True)  # Сортировка по баллам
    ebaõnnestunud.sort()   # Сортировка в алфавитном порядке относительно имени

    # Запись данных принятых кадидатов в файл "vastuvõetud.txt"
    with open(vastuvõetud_fail,'w',encoding="utf-8") as f:
        for nimi,punktid in vastuvõetud:
            f.write(f"{nimi}, {punktid} punkti\n")

    # Запись данных отклоненных кадидатов в файл "eisoobi.txt"
    with open(eisoobi_fail,'w',encoding="utf-8") as f:
        for nimi in ebaõnnestunud:
            f.write(f"{nimi}\n")

