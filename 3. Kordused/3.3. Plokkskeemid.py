#V4 Ülesanne 3
#T sõpra tulid restorani. Sissepääsu juures on robotvalvur ja laseb sisse ainult neid, kes on üle 16 aasta vanad.
#Tuleb välja selgitada, mitu sõpra saab õhtusöögi.

T=0
while True:
    try:
        T=int(input("Sisestage sõprade arv: "))  # Ввод общего количества друзей
        if T>0:
            break
        else:
            print("Palun sisetage positiivne arv!")
    except:
        print("Palun sisetage täisarv!")

# Счётчик друзей старше 16 лет
count=0
for i in range(T):
    while True:
        try:
            vanus=int(input(f"Sisestage sõbra {i+1} vanus: "))
            break
        except:
            print("Palun sisetage täisarvu!")
    if vanus>16:
        count+=1   # Увеличиваем счётчик, если возраст больше 16
print(f"{count} sõpra saavad õhtusöögi")


