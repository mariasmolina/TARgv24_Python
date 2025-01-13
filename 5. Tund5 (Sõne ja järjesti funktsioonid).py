#Video tund: Sõne ja järjesti funktsioonid

spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=['Abc','B','C']

slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)

while True:
    print("1-добавить букву в список")
    print("2-склеить списки")
    print("3-добавить букву на i-позицию")
    print("4-удалить элемент")
    valik=int(input())
    if valik==1:
        a=input("Введи букву: ")
        slovo_list.append(a)   #list.append - добавляет элемент в конец списка 
        print(f"Добавили {a} новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)    #list.extend - соединить 2 списка
        print(slovo_list)
    elif valik==3:
        a=input("Введи элемент, который хочешь добавить: ")
        i=int(input("Введи номер позиции, куда хочешь добавить элемент: "))
        slovo_list.insert(i-1,a)    #list.insert(куда,что) - добавляет a значение на i поцицию  (позиция начинается с 0)
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить: ")
        n=slovo_list.count(a)     #list.count - количество значений
        if n>0:
            for i in range(n):
                slovo_list.remove(a)      #list.remove - удалить выбранный элемент
        else:
            print("Искомой буквы нет")
        print(slovo_list)




        

