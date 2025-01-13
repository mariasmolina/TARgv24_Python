#Praktiline töö 1: Sõne ja järjesti funktsioonid

nimed = ["Jaan", "Mari", "Peeter", "Kadri", "Liisa"]
perenimed = ["Tamm", "Kask", "Saare", "Pärn", "Kuusk"]
print(f"Изначальный список имён: {', '.join(nimed)}")   # Преобразует список в строку S.join(список) (Функции и методы строк)
while True:
    print()
    print("1 - Добавить новое имя в конец списка")   #list.append
    print("2 - Склеить список имён с списком фамилий")  #list.extend
    print("3 - Добавить имя на определённую позицию в списке")   #list.insert
    print("4 - Удалить имя из списка")  #list.remove
    print("5 - Найти позицию имени в списке")  #list.index
    print("6 - Посчитать количество имён в списке")   #list.count
    print("7 - Сортировать список")  #list.sort
    print("8 - Развернуть список")   #list.reverse
    print("9 - Копировать список")   #list.copy
    print("10 - Очистить список")    #list.clear
    print("11 - Посмотреть список имен")
    print("12 - Посмотреть список фамилий")
    print("0 - Выйти")
    while True:
        try:
            valik = int(input("\nВыберите действие: "))
            break
        except:
            print("Ошибка! Введите число из списка действий!")

    if valik==0:
        print("Выход из программы")
        break

    elif valik==1:
        a=input("Введите имя: ").lower().capitalize()   # Чтобы все имена имели нижний регистр и первую заглавную букву
        nimed.append(a)  # Добавляет элемент в конец списка
        print(f"Добавили {a}. \nНовый список: {', '.join(nimed)}")

    elif valik==2:
        nimed.extend(perenimed)  # Расширяет список, добавляя элементы другого списка
        print(f"Фамилии добавлены в список. \nНовый список: {', '.join(nimed)}")

    elif valik==3:
        a=input("Введите имя, которое хотите добавить: ").lower().capitalize()
        while True:
            try:
                i=int(input("Введите позицию (начиная с 1): "))
                break
            except:
                print("Ошибка! Введите число!")
        nimed.insert(i-1,a)  # Вставляет элемент на указанную позицию
        print(f"Добавили {a} на позицию {i}. \nНовый список: {', '.join(nimed)}")

    elif valik==4:
        a=input("Введите имя для удаления: ").lower().capitalize()
        if a in nimed:
            nimed.remove(a)  # Удаляет введеный элемент
            print(f"Удалили {a}. \nНовый список: {', '.join(nimed)}")
        else:
            print(f"Имя {a} не найдено в списке.")

    elif valik==5:
        a=input("Введите имя для поиска: ").lower().capitalize()   # В случае, если имя введет не так как в списке
        try:
            index=nimed.index(a)  # Находит индекс(позицию) первого элемента
            print(f"Имя {a} находится на позиции - {index + 1}")
        except:
            print(f"Имя {a} отсутствует в списке.")

    elif valik==6:
        a=input("Введите имя для подсчёта: ").lower().capitalize()
        count=nimed.count(a)  # Подсчитывает количество введонного имени в списке
        print(f"Количество имени {a} в списке - {count}")

    elif valik==7:
        nimed.sort()  # Сортирует список в алфавитном порядке
        print(f"Список после сортировки: {', '.join(nimed)}")

    elif valik==8:
        nimed.reverse()  # Разворачивает список
        print(f"Новый список: {', '.join(nimed)}")

    elif valik==9:
        print("Доступные списки для копирования:")
        print(f"1 - имена: {', '.join(nimed)}")
        print(f"2 - фамилии: {', '.join(perenimed)}")
        while True:
            try:
                valik2=int(input("Выберите номер списка для копирования: "))
                break
            except:
                print("Ошибка! Введите число 1 или 2!")
        if valik2==1:
            copy_nimed_list=nimed.copy()  # Создаёт копию списка
            print("Список имен скопирован.")
        elif valik2==2:
            copy_perenimed_list=perenimed.copy() 
            print("Список фамилий скопирован.")
        else:
            print("Неверный выбор.")

    elif valik==10:
        print("Доступные списки для очистки:")
        print(f"1 - имена: {', '.join(nimed)}")
        print(f"2 - фамилии: {', '.join(perenimed)}")
        while True:
            try:
                valik3=int(input("Выберите номер списка для очистки: "))
                break
            except:
                print("Ошибка! Введите число 1 или 2!")
        if valik3==1:
            nimed.clear()   # Очищает список
            print("Список имен очищен.")
        elif valik3==2:
            perenimed.clear()
            print("Список фамилий очищен.")
        else:
            print("Неверный выбор.")

    if valik==11:
        print(f"Список имён: {', '.join(nimed)}")

    if valik==12:
        print(f"Список фамилий: {', '.join(perenimed)}")





