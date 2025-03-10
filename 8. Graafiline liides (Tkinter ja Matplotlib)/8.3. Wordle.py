from tkinter import *
from tkinter import messagebox, ttk, font, simpledialog
from PIL import Image, ImageTk
import random


def reeglid():
    messagebox.showinfo("Wordle Reeglid", 
    "1. Eesmärk – ära arvata 5-täheline sõna 6 katsega.\n2. Tähtede värvid näitavad vihjeid:\n    Roheline – õige täht õiges kohas.\n    Kollane – õige täht, aga vales kohas.\n    Hall – tähte pole sõnas.\n3. Ainult kehtivad sõnad on lubatud.\n4. 6 katse järel näidatakse õiget vastust.")

def loe_sonad_failist(failinimi:str):
    """
    Loeb sõnad .txt failist ja teeb nendest järjend
    """
    sonad=[]
    with open(failinimi, 'r', encoding="utf-8-sig") as file:
        for line in file:
            sonad.append(line.strip())  # Убираем лишние пробелы и символы новой строки
    return sonad

def salvesta_tulemus(nimi, katsed):
    """Salvestab mängija tulemusi faili"""
    tulemused={}
    with open(r'8. Graafiline liides (Tkinter ja Matplotlib)\tulemused.txt', "r", encoding="utf-8") as f:
        for line in f:
            key,value=line.strip().split(" - ")
            tulemused[key]=value
    
    # Добавляем новый результат и сортируем
    tulemused[str(katsed)]=nimi  # ключ может быть только строкой, а katsed это число
    tulemused=dict(sorted(tulemused.items()))
    
    # Записываем обновленные результаты в файл
    with open(r'8. Graafiline liides (Tkinter ja Matplotlib)\tulemused.txt', "w", encoding="utf-8") as f:
        for key, value in tulemused.items():
            f.write(f"{key} - {value}\n")

def rating():
    tulemused_str=""  # строка для всех результатов
    with open(r'8. Graafiline liides (Tkinter ja Matplotlib)\tulemused.txt', "r", encoding="utf-8") as f:
        for line in f:
            key, value=line.strip().split(" - ")
            tulemused_str=tulemused_str+f"{key} - {value}\n"  # добавляем результат в строку
    
    # Отображаем все результаты в messagebox
    messagebox.showinfo("Parimad tulemused", tulemused_str)

def vali_sona():
    sonad=loe_sonad_failist(r'8. Graafiline liides (Tkinter ja Matplotlib)\sonad.txt') 
    return random.choice(sonad)  # Выбираем случайное слово из списка

def kontrolli_katset():
    """
    Kontrollib sisestatud sõna, värvib tähti ja juhib mängu kulgu
    """
    global katsed

    tulemused=[]
    sisestatud_sona=""
    vastus_label.config(text="")

    if katsed<=6:
        # Собираем введенное пользователем слово
        for column in range(5):
            sisestatud_sona=sisestatud_sona+tahed[katsed*5+column].get().lower()

        # Проверяем, что слово состоит ровно из 5 букв
        if len(sisestatud_sona)==5:
            if sisestatud_sona in sonad:
                tulemused=["hall"]*5  # По умолчанию все буквы серые
                oige_sona_koopia=list(oige_sona)  # Копия загаданного слова

                # Сначала проверяем буквы на правильных местах (зелёный цвет)
                for i in range(5):
                    if sisestatud_sona[i]==oige_sona_koopia[i]:
                        tulemused[i]="roheline"
                        oige_sona_koopia[i]=None

                # Затем проверяем буквы, которые есть в слове, но не на своих местах (жёлтый цвет)
                for i in range(5):
                    if tulemused[i]=="hall" and sisestatud_sona[i] in oige_sona_koopia:
                        for j in range(len(oige_sona_koopia)):
                            if oige_sona_koopia[j]==sisestatud_sona[i]:
                                tulemused[i]="kollane"
                                oige_sona_koopia[j]=None
                                break

                # Раскрашиваем буквы
                varvi_tahed(tulemused, tahed[katsed*5:katsed*5+5])  

                katsed=katsed+1

                # Проверяем условия завершения игры
                if sisestatud_sona==oige_sona or katsed==6:
                    lopeta_mang(sisestatud_sona)

            else:
                for column in range(5):
                    tahed[katsed*5+column].delete(0, END)
                    vastus_label.config(text="Seda sõna ei ole sõnastikus!", font=("Lilita One", 16), foreground="red")

        # Если длина слова не 5 букв, показываем сообщение об ошибке
        else:
            vastus_label.config(text="Viga! Sisesta täpselt 5 tähte!", font=("Lilita One", 16), foreground="orange")

    return tulemused

def varvi_tahed(tulemused, tahed):
    """
    Värvib tähed vastavalt tulemusele
    """
    for i in range(len(tulemused)):
        if tulemused[i]=="roheline":
            tahed[i].config(bg="#099813")
        elif tulemused[i]=="kollane":
            tahed[i].config(bg="#cb910e")
        else:
            tahed[i].config(bg="#4b4a5d")

def lopeta_mang(sisestatud_sona):
    """
    Kuvab õige sõna ja lõpetab mängu
    """
    global oige_sona

    if sisestatud_sona==oige_sona:
        vastus_label.config(text=f"Hurraa, sa arvasid sõna ära, aitäh mängu eest!", fg="#00FF00")
        salvesta_tulemus(nimi, katsed)
    elif katsed==6 or not timer_running:
        vastus_label.config(text=f"Kahjuks, mäng on läbi! Õige sõna on -  {oige_sona}", fg="white")

    for entry in tahed:
    # Передаём текущее значение bg, чтобы фон не изменялся
        entry.config(state="disabled", disabledbackground=entry.cget("bg"), disabledforeground="white")

def uus_mang():
    """
    Puhastab väljad ja alustab uut mängu
    """
    global nimi, katsed, oige_sona, timer_running

    if timer_running:
        timer_running=False
    nimi=simpledialog.askstring("Alusta!", "Sisesta oma nimi:")
    if not nimi:
        nimi="Mängija"
    katsed=0  # Сбросим счетчик попыток

    # Очистим поля ввода
    for taht in tahed:
        taht.config(state="normal")
        taht.delete(0, END)  
        taht.config(bg="#0f0f26") 

    # Генерируем новое слово и обновляем переменную oige_sona
    oige_sona=vali_sona()  
    vastus_label.config(text="") 

    return oige_sona

def vajuta_klaviatuuri_nupp(taht):
    """
    """
    global katsed
    if katsed<6:
        for column in range(5):
            if tahed[katsed*5+column].get()=="":   
                tahed[katsed*5+column].insert(0, taht)
                break

# Функция для отсчета времени
def start_timer():
    global timer_running, timer_seconds
    if not timer_running:  # Если таймер еще не запущен
        timer_running=True
        timer_seconds=60  # Время в секундах
        update_timer()

def update_timer():
    global timer_seconds, timer_running
    if timer_seconds<=10:
        vastus_label.config(fg="red")

    if timer_seconds>0 and timer_running:
        timer_seconds=timer_seconds-1
        vastus_label.config(text=f"Aeg: {timer_seconds} sekundit")
        aken.after(1000, update_timer)  # обновляем каждую секунду
    else:
        timer_running=False
        lopeta_mang(sisestatud_sona)  # Время вышло, заканчиваем игру



# Счетчик попыток
katsed=0  
sonad=loe_sonad_failist(r'8. Graafiline liides (Tkinter ja Matplotlib)\sonad.txt')  # Читаем слова из файла
oige_sona=vali_sona()  # Выбираем слово для игры
timer_running=False  # Таймер еще не запущен
timer_seconds=0  # Начальное время (в секундах)
sisestatud_sona=""

aken=Tk()
aken.geometry("600x940")
aken.resizable(False, False) # Отключает изменение размера окна (Ширина - False, Высота - False)
aken.title("🎲 Wordle")
aken_bg=Label(aken, bg="#0f0f26")
aken_bg.place(x=0, y=0, relwidth=1, relheight=1)
bg=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\tume_bg.jpg")


# Canvas
bg_resized=bg.resize((600, 100)) 
bg_image=ImageTk.PhotoImage(bg_resized)
canvas=Canvas(aken, width=600, height=100, highlightthickness=0)
canvas.create_image(0, 0, anchor="nw", image=bg_image)
canvas.pack()  

# Заголовок
canvas.create_text(300, 50, text="WORDLE MÄNG", font=("Lilita One", 40, "bold"), fill="white")

# Кнопка с правилами игры и рейтингом лучших
emoji_image=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\reeglid.png")
emoji_image_resized=emoji_image.resize((30, 30)) 
emoji_photo=ImageTk.PhotoImage(emoji_image_resized)
Button(aken, command=reeglid, image=emoji_photo, bg="#0f0f26", bd=0, highlightthickness=0).place(x=565, y=10)

emoji_image_2=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\rating.png")
emoji_image_resized_2=emoji_image_2.resize((30, 30)) 
emoji_photo_2=ImageTk.PhotoImage(emoji_image_resized_2)
Button(aken, command=rating, image=emoji_photo_2, bg="#df1710", bd=0, highlightthickness=0).place(x=565, y=60)


# Поля ввода для букв
taht_sisend=Frame(aken, bg="#0f0f26")
taht_sisend.pack(pady=20)

tahed=[]
for row in range(6):  # 6 рядов
    for column in range(5):  # 5 колонок
        sisesta_taht=Entry(taht_sisend, font=("Poppins", 28, "bold"), fg="white", bg="#0f0f26", width=3, justify="center", bd=0, highlightthickness=2, highlightbackground="#4b4a5d", highlightcolor="#4b4a5d")
        sisesta_taht.grid(row=row, column=column, pady=4, padx=4, ipadx=3, ipady=3)  # Размещение в сетке
        tahed.append(sisesta_taht)

# Поле сообщений
bg_resized_2=bg.resize((596, 60)) 
bg_image_2=ImageTk.PhotoImage(bg_resized_2)
vastus_label=Label(aken, image=bg_image_2,  font=("Lilita One", 18), compound="center", fg="white")
vastus_label.place(x=0, y=650)

# Кнопка проверки
kontrolli_button=Button(text="Kontrolli", command=kontrolli_katset, font=("Lilita One", 18), fg="white",bg="#1e0056")
kontrolli_button.place(x=462, y=748)

# Кнопка очистки и новой игры
uus_mang_button=Button(text="Uus mäng", command=uus_mang, font=("Lilita One", 18), fg="white",bg="#e40139")
uus_mang_button.place(x=458, y=808)

# Кнопка начала игры с таймером
timer_button=Button(text="Taimer", command=start_timer, font=("Lilita One", 18), fg="white", bg="#fc5318")
timer_button.place(x=472, y=868)

# Клавиатура
klaviatuur=Frame(aken, bg="#0f0f26")
klaviatuur.place(x=20, y=735)  

eesti_tahestik="ABDEFGHIJKLMNOPRSŠZŽTUVÕÄÖÜ"
row=0  # ряд
col=0  # столбец

for taht in eesti_tahestik:
    nupp=Button(klaviatuur, text=taht, font=("Poppins", 15), width=3, bg="#1e0056", fg="white", bd=0, command=lambda t=taht: vajuta_klaviatuuri_nupp(t)) 
    nupp.grid(row=row, column=col, padx=2, pady=2) 
    col=col+1
    if col==9:  # Если столбец достигает 13, начинаем новый ряд
        col=0
        row=row+1


uus_mang()
aken.mainloop()


