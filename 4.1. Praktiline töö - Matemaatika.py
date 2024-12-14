from random import *

# Программа для проверки знаний по математике
# Предложить пользователю выбрать сложность заданий
while True:
    print("Tere tulemast matemaatikatesti!")
    print()
    print("Valige ülesannete raskusaste:")
    print("-------------------------------------------------")
    print("1 - Lihtne (operatsioonid + ja -, arvud kuni 10)")
    print("2 - Keskmine (operatsioonid +, -, *, arvud kuni 25)")
    print("3 - Raske (operatsioonid +, -, *, /, arvud kuni 50)")
    print("-------------------------------------------------")
    while True:
        try:
            tase=int(input("Sisestage raskusaste (1, 2, 3): "))
            if tase!=1 and tase!=2 and tase !=3:
                print("Palun valige tase 1, 2 või 3!")
            else:
                break  # Если все верно, выйти из цикла
        except:
            print("Palun sisestage number!")
    print()
    print("Teil on vaja vastata 10 küsimusele\nAlustame!\n")

    õiged_vastused=0        # Счётчик правильных ответов
    max_küsimusi=10         # Максимальное количество вопросов

    # Генерация примеров с учетом уровня сложности
    for i in range(1,max_küsimusi+1):
        if tase==1:      # Легкие задания (только + и -)
            num1=randint(1,10)
            num2=randint(1,10)
            op=choice(["+","-"])
        elif tase==2:     # Средние задания (+, -, *)
            num1=randint(1,25)
            num2=randint(1,25)
            op=choice(["+","-","*"])
        elif tase==3:     # Сложные задания (+, -, *, /, **)
            num1=randint(1,50)
            num2=randint(1,50)
            op=choice(["+","-","*","/","**"])

    # Вычисляет правильный ответ
        if op=="+":
            õige_vastus=num1+num2
        elif op=="-":
            õige_vastus=num1-num2
        elif op=="*":
            õige_vastus=num1*num2
        elif op == "/":
            num2=randint(1,10)  # Генерирует делитель   
            num1=num2*randint(1,10)     # Генерирует число, кратное делителю
            õige_vastus=round(num1/num2,2)
        elif op=="**":
            num2=randint(2,3)
            õige_vastus=num1**num2

        # Тест
        print(f"{i}. Kuidas lahendada {num1} {op} {num2}?")
        while True:
            try:
                vastus=float(input("Teie vastus: "))

            # Проверка ответа
                if vastus==õige_vastus:
                    print("Õige!\n")
                    õiged_vastused+=1
                else:
                    print(f"Vale! Õige vastus on {õige_vastus}\n")
                break
            except:
                print("Sisestage arv!")

    # Оценка
    hinne=(õiged_vastused/max_küsimusi)*100
    print(f"\nTe vastasite õigesti {õiged_vastused} küsimusele {max_küsimusi}st.")

    if hinne<60:
        print("Teie hinne on: 2")
    elif hinne<75:
        print("Teie hinne on: 3")
    elif hinne<90:
        print("Teie hinne on: 4")
    else:
        print("Teie hinne on: 5")

# Спрашивает, хочет ли пользователь пройти тест ещё раз
    while True:     # Проверка, если вдруг напишут что то, кроме да и нет
        uuesti = input("\nKas soovite uuesti proovida? (jah/ei): ").lower()
        print()
        if uuesti == "jah" or uuesti == "ei":
            break
        print("Palun sisestage ainult 'jah' või 'ei'!")
    if uuesti == "ei":
        print("Täname matemaatikatesti kasutamise eest!")
        break
