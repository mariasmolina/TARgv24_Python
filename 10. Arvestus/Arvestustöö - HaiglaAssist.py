import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk

# имя, исикукоод, рост и вес, давление, температура, пульс, диета (базовая, диабетическая, безлактозы) - лактоза, емаил arst: kodune ravi ja soovitused, 2.50 vooditasu

conn = sqlite3.connect("10. Arvestus/AppData/haigla.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS kasutajad (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    kasutajanimi TEXT UNIQUE,
                    parool TEXT,
                    amet TEXT,
                    nimi TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS patsiendid (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Eesnimi TEXT,
                    Perekonnanimi TEXT,
                    Vanus INTEGER,
                    Kaal REAL,
                    kaebus TEXT,
                    diagnoos TEXT,
                    ravitoitumine TEXT,
                    staatus TEXT DEFAULT 'ожидание',
                    arstiSoovitused TEXT,
                    registreerimise_aeg TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    email TEXT,
                    arst_ID INTEGER,
                    FOREIGN KEY (arst_ID) REFERENCES kasutajad(ID))''')

# # Добавляем данные для входа в систему для медсестры
# cursor.execute("INSERT INTO kasutajad (kasutajanimi, parool, amet, nimi) VALUES (?, ?, ?, ?)", 
#                ("nurse1", "1234", "medõde", "Natalja Vassiljeva"))

# # Добавляем данные для входа в систему для врача
# cursor.execute("INSERT INTO kasutajad (kasutajanimi, parool, amet, nimi) VALUES (?, ?, ?, ?)", 
#                ("arst1", "1234", "arst", "Maria Smolina"))


conn.commit()
conn.close()

# --- Функции ---

# Функция с авторизацией медсестер и врачей
def sisselogimine():
    kasutajanimi=sisend_kasutajanimi.get()
    parool=sisend_parool.get()

    conn=sqlite3.connect("10. Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    cursor.execute("SELECT nimi, amet FROM kasutajad WHERE kasutajanimi=? AND parool=?", (kasutajanimi, parool))
    kasutaja=cursor.fetchone()
    conn.close()

    if kasutaja:
        nimi, amet=kasutaja
        messagebox.showinfo("Tere tulemast!", f"Tere tulemast, {nimi}! \n\nSisse logitud kui {amet}")

        aken_login.destroy()  # Закрываем окно входа
        peamine_aken(nimi, amet)  # Открываем главное окно
    else:
        messagebox.showerror("Viga", "Vale kasutajanimi või parool!")


# Функция для открытия главного окна после успешного входа
def peamine_aken(nimi, amet):
    global main_aken

    main_aken = tk.Tk()
    main_aken.title("Haigla Assist")
    main_aken.geometry("400x300")

    tk.Label(main_aken, text=f"Tere, {nimi}!", font=("Arial", 16)).pack(pady=20)

    # Кнопки
    tk.Button(main_aken, text="Kuva patsiendid", command=patsiendide_andmed).pack(pady=10)
    tk.Button(main_aken, text="Kuva oskond", command=osakond_aken).pack(pady=10)

    main_aken.mainloop()


# Функция для отображения таблицы пациентов
def patsiendide_andmed():

    global main_aken # Делаем переменную глобальной

    if main_aken:   # Перед destroy() мы проверяем, существует ли окно.
        main_aken.destroy()  # Закрываем главное окно

    patsient_aken = tk.Tk()  # Открываем новое окно пациентов
    patsient_aken.title("Patsiendid")
    patsient_aken.geometry("900x500")

    frame = tk.Frame(patsient_aken)
    frame.pack(pady=20, fill=tk.BOTH, expand=True)

    buttons_frame = tk.Frame(frame)
    buttons_frame.pack(side=tk.RIGHT, anchor="e")

    open_button = tk.Button(buttons_frame, text="Lisa andmeid", command=lisa_patsient)
    open_button.pack(side=tk.LEFT, padx=5)

    # Таблица с прокруткой
    scrollbar=tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree=ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("Eesnimi", "Perekonnanimi", "Vanus", "Kaal", "Kaebus", "Diagnoos", "Ravitoitumine", "Staatus", "Email"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    # Связываем прокрутку с таблицей
    scrollbar.config(command=tree.yview)

    # Заголовки столбцов
    tree.heading("Eesnimi", text="Eesnimi")
    tree.heading("Perekonnanimi", text="Perekonnanimi")
    tree.heading("Vanus", text="Vanus")
    tree.heading("Kaal", text="Kaal")
    tree.heading("Kaebus", text="Kaebus")
    tree.heading("Diagnoos", text="Diagnoos")
    tree.heading("Ravitoitumine", text="Ravitoitumine")
    tree.heading("Staatus", text="Staatus")
    tree.heading("Email", text="Email")

    # Ширина столбцов
    tree.column("Eesnimi", width=100)
    tree.column("Perekonnanimi", width=150)
    tree.column("Vanus", width=60)
    tree.column("Kaal", width=80)
    tree.column("Kaebus", width=200)
    tree.column("Diagnoos", width=100)
    tree.column("Ravitoitumine", width=150)
    tree.column("Staatus", width=100)
    tree.column("Email", width=150)

    # Загружаем данные из базы данных
    load_data_from_db(tree)

    patsient_aken.mainloop()



def lisa_patsient():
    global sisend_eesnimi, sisend_perekonnanimi, sisend_vanus, sisend_kaal, sisend_kaebused, valitud_diagnoos, sisend_email

    lisa_patsient_aken = tk.Toplevel()
    lisa_patsient_aken.title("Lisa andmed")
    lisa_patsient_aken.geometry("800x600")

    # Поля для ввода данных пациента
    tk.Label(lisa_patsient_aken, text="Eesnimi").pack()
    sisend_eesnimi = tk.Entry(lisa_patsient_aken)
    sisend_eesnimi.pack()

    tk.Label(lisa_patsient_aken, text="Perekonnanimi").pack()
    sisend_perekonnanimi = tk.Entry(lisa_patsient_aken)
    sisend_perekonnanimi.pack()

    tk.Label(lisa_patsient_aken, text="Vanus").pack()
    sisend_vanus = tk.Entry(lisa_patsient_aken)
    sisend_vanus.pack()

    tk.Label(lisa_patsient_aken, text="Kaal (kg)").pack()
    sisend_kaal = tk.Entry(lisa_patsient_aken)
    sisend_kaal.pack()

    tk.Label(lisa_patsient_aken, text="Kaebused").pack()
    sisend_kaebused = tk.Text(lisa_patsient_aken, height=3, width=30)
    sisend_kaebused.pack()

    # Выбор диагноза (Combobox)
    tk.Label(lisa_patsient_aken, text="Diagnoos").pack()
    valitud_diagnoos = ttk.Combobox(lisa_patsient_aken, values=["Diabeet", "Hüpertensioon", "Gastriit"])
    valitud_diagnoos.pack()

    tk.Label(lisa_patsient_aken, text="Email").pack()
    sisend_email = tk.Entry(lisa_patsient_aken)
    sisend_email.pack()

    tk.Button(lisa_patsient_aken, text="Salvesta", command=salvesta_patsient).pack(pady=10)

    lisa_patsient_aken.mainloop()

# Функция для загрузки данных пациентов в таблицу
def load_data_from_db(tree):
    conn=sqlite3.connect("10. Arvestus/AppData/haigla.db")
    cursor=conn.cursor()
    cursor.execute('''SELECT Eesnimi, Perekonnanimi, Vanus, Kaal, kaebus, diagnoos, ravitoitumine, staatus, email 
                      FROM patsiendid''')
    patients=cursor.fetchall()
    conn.close()

    for patient in patients:
        tree.insert("", tk.END, values=patient)


# Функция для открытия окна с картой этажа
def osakond_aken():
    osakond_aken= tk.Toplevel(main_aken)
    osakond_aken.title("Oskonna kaart")
    osakond_aken.geometry("600x600")

    for i in range(9):
        row = i // 3
        col = i % 3
        color = "green" if i % 3 == 0 else "red" if i % 3 == 1 else "yellow"
        room = tk.Label(osakond_aken, text=f"Palat {i+1}", bg=color, width=10, height=4)
        room.grid(row=row, column=col, padx=10, pady=10)

# Функция для сохранения данных пациента
def salvesta_patsient():
    eesnimi = sisend_eesnimi.get()
    perekonnanimi = sisend_perekonnanimi.get()
    vanus = sisend_vanus.get()
    kaal = sisend_kaal.get()
    kaebus = sisend_kaebused.get("1.0", tk.END).strip()
    diagnoos = valitud_diagnoos.get()
    email = sisend_email.get()

    # Автоматическое назначение диеты
    dieet={
        "Diabeet": "Madal suhkur, rohkem köögivilju",
        "Hüpertensioon": "Vähem soola, rohkem kala",
        "Gastriit": "Pehme toit, vältida vürtsikaid toite"
    }

    ravitoitumine=dieet.get(diagnoos, "Tavaline toitumine")

    # Запись в базу данных
    conn=sqlite3.connect("10. Arvestus/AppData/haigla.db")
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO patsiendid (Eesnimi, Perekonnanimi, Vanus, Kaal, Kaebus, Diagnoos, Ravitoitumine, Staatus, Email)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (eesnimi, perekonnanimi, vanus, kaal, kaebus, diagnoos, ravitoitumine, "Uus", email))
    conn.commit()
    conn.close()

    messagebox.showinfo("Edu", "Patsient lisatud!")









    
# ----- Peaaken -----
aken_login=tk.Tk()
aken_login.title("Autoriseerimine")
aken_login.geometry("300x200")

# Sisselogimise vorm
tk.Label(aken_login, text="Kasutajanimi").pack()
sisend_kasutajanimi=tk.Entry(aken_login)
sisend_kasutajanimi.pack()

tk.Label(aken_login, text="Parool").pack()
sisend_parool=tk.Entry(aken_login, show="*")
sisend_parool.pack()

tk.Button(aken_login, text="Logi sisse", command=sisselogimine).pack()

aken_login.mainloop()


