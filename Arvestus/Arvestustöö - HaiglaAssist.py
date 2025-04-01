import tkinter as tk
import sqlite3, requests, random, json, string, smtplib, ssl
from tkinter import messagebox, ttk
from customtkinter import *   # расширение стандартного модуля Tkinter, которое использует библиотеку CTk
from CTkSpinbox import *
from ttkthemes import ThemedTk
from PIL import Image
from email.message import EmailMessage
from Isikukood_Modul import *
from DB_funktsioonid import *


def print_patsiendid():
    """ Выводит данные таблиц из базы данных в терминале (для себя) """
    # Подключение к базе данных
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    # Проверка успешного соединения
    print("\nÜhenduse loomine andmebaasiga õnnestus")

    # Получаем все данные из таблицы patsiendid
    cursor.execute("""SELECT * FROM patsiendid""")
    patsiendid=cursor.fetchall()

    cursor.execute("""SELECT * FROM kasutajad""")
    kasutajad=cursor.fetchall()

    if not patsiendid:
        print("\nTabel 'patsiendid' on tühi")
    else:
        print("\nAndmed tabelist patsiendid:")
        for patient in patsiendid:
            print(patient)

    if not kasutajad:
        print("\nTabel 'kasutajad' on tühi")
    else:
        print("\n\nAndmed tabelist kasutajad:")
        for kasutaja in kasutajad:
            print(kasutaja) 

    conn.close()


def sisselogimine_aken():
    """ Форма для входа для медсестер и врачей """
    global sisend_kasutajanimi, sisend_parool, aken_login
    
    pilt_login_src=Image.open("Arvestus/pildid/login_pilt.png")
    smart_id_src=Image.open("Arvestus/pildid/smart_id.png")
    pilt_login=CTkImage(light_image=pilt_login_src, size=(300, 480))  # CustomTkinter требует хотя бы один параметр (light_image или dark_image)
    smart_id=CTkImage(light_image=smart_id_src, size=(120, 45))

    aken_login=CTk()
    aken_login.title("HaiglaAssist - Autoriseerimine")
    aken_login.geometry("600x480")
    aken_login.resizable(0,0)  # нельзя поменять размер окна
    print_patsiendid()

    CTkLabel(aken_login, text="", image=pilt_login).pack(expand=True, side="left")  # expand=True - занимает доступное пространство в контейнере

    frame=CTkFrame(aken_login, width=300, height=480, fg_color="white")
    frame.pack_propagate(0)   # зафиксировать размер Frame (по умолчанию Frame изменяет свои размеры
    frame.pack(expand=True, side="right")

    CTkLabel(frame, text="Hailga Assist", text_color="#55b3d9", anchor="w", justify="left", font=("Nunito", 24, "bold")).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(frame, text="Logige oma kontole sisse", text_color="#7E7E7E", anchor="w", justify="left", font=("Nunito", 14)).pack(anchor="w", padx=(25, 0))

    CTkLabel(frame, text="👤 Kasutajanimi", text_color="#008ba9", anchor="w", justify="left", font=("Nunito", 16), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    sisend_kasutajanimi=CTkEntry(frame, width=225, fg_color="#EEEEEE", border_color="#55b3d9", border_width=1, text_color="black")
    sisend_kasutajanimi.pack(anchor="w", padx=(25, 0))

    CTkLabel(frame, text="🔒 Parool", text_color="#008ba9", anchor="w", justify="left", font=("Nunito", 16), compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    sisend_parool=CTkEntry(frame, width=225, fg_color="#EEEEEE", border_color="#55b3d9", border_width=1, text_color="black", show="*")
    sisend_parool.pack(anchor="w", padx=(25, 0))

    logi_sisse_nupp=CTkButton(frame, text="Logi sisse", fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white", width=225, command=sisselogimine_kasutaja)
    logi_sisse_nupp.pack(anchor="w", pady=(30, 0), padx=(25, 0))

    smart_id_nupp=CTkButton(frame, text="", fg_color="white", hover_color="white", image=smart_id, command=message)
    smart_id_nupp.pack(anchor="w", pady=(30, 0), padx=(65, 0))

    aken_login.mainloop()


def message():
    """ Сообщение, для частей проекта, которые в разработке """
    messagebox.showwarning("Vabandage!", "Ajutiselt väljatöötamisel!")


def sisselogimine_kasutaja():
    """ Функция с авторизацией медсестер и врачей """
    global amet, nimi
    kasutajanimi=sisend_kasutajanimi.get()
    parool=sisend_parool.get()

    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    cursor.execute("""
    SELECT nimi, amet 
    FROM kasutajad 
    WHERE kasutajanimi=? AND parool=? 
    """, (kasutajanimi, parool))
    kasutaja=cursor.fetchone()
    conn.close()

    if kasutaja:
        nimi, amet=kasutaja
        messagebox.showinfo("Tere tulemast!", f"Tere tulemast, {nimi}! \n\nSisse logitud kui {amet}")
        
        aken_login.destroy()   # Закрываем старое
        patsiendide_andmed(nimi, amet)  # Открываем главное окно
    else:
        messagebox.showerror("Viga", "Vale kasutajanimi või parool!")


def patsiendide_andmed(nimi, amet):
    """ Функция для отображения таблицы пациентов """
    global tree, search_entry, peamine_aken

    peamine_aken=ThemedTk(theme="adapta") # Использовала модуль с темой
    peamine_aken.title("Haigla Assist")
    peamine_aken.geometry("1250x500")
    peamine_aken.configure(background="#55b3d9")
    peamine_aken.resizable(0,0)

    # Панель кнопок
    nupude_frame = CTkFrame(peamine_aken, width=200, fg_color="#55b3d9")
    nupude_frame.pack_propagate(0)
    nupude_frame.pack(side="right", fill="y")

    logo_src=Image.open("Arvestus/pildid/hospital.png")
    logo_pilt=CTkImage(light_image=logo_src, size=(130, 130))
    CTkLabel(nupude_frame, text="", image=logo_pilt).pack(pady=(30, 40), padx=10)

    lisa_nupp=CTkButton(nupude_frame, text="➕ Lisa andmeid", command=lisa_patsient, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    lisa_nupp.pack(padx=10, pady=10, ipady=5)
    
    osakond_nupp=CTkButton(nupude_frame, text="📋 Kuva osakond", command=osakond_aken, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    osakond_nupp.pack(pady=10, ipady=5)
    
    if amet=="arst":
        filter_nupp=CTkButton(nupude_frame, text="👥 Minu patsiendid", command=lambda: load_data_from_db(tree, arst_nimi=nimi), fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
        filter_nupp.pack(pady=(10,0), ipady=5)
    
    logi_valja_nupp=CTkButton(nupude_frame, text="➜ Logi välja", command=lambda: (peamine_aken.destroy(), sisselogimine_aken()), fg_color="white", hover_color="#01608b", font=("Nunito", 16, "bold"), text_color="#55b3d9")
    logi_valja_nupp.pack(side="bottom", pady=50, ipady=5)
    
    # Основной фрейм
    frame=CTkFrame(peamine_aken, fg_color="white")
    frame.pack(pady=20, side="left", expand=True, fill="both")

    # Верхняя информационная панель
    info_frame=CTkFrame(frame, fg_color="white", height=50)
    info_frame.pack(fill="x")
    
    tanane_kuupaev=datetime.today().strftime('%d.%m.%Y')
    
    vasak_frame=CTkFrame(info_frame, fg_color="white")
    vasak_frame.pack(side="left", padx=20, pady=5)
    
    CTkLabel(vasak_frame, text="Amet:", font=("Nunito", 16, "bold"), anchor="w", text_color="#01608b").pack(anchor="w")
    CTkLabel(vasak_frame, text="Nimi:", font=("Nunito", 16, "bold"), anchor="w", text_color="#01608b").pack(anchor="w")
    CTkLabel(vasak_frame, text="Kuupäev:", font=("Nunito", 16, "bold"), anchor="w", text_color="#01608b").pack(anchor="w")
    
    parem_frame=CTkFrame(info_frame, fg_color="white")
    parem_frame.pack(side="left", padx=10, pady=5)
    
    CTkLabel(parem_frame, text=f"{amet}", font=("Nunito", 16), anchor="w", text_color="#01608b").pack(anchor="w")
    CTkLabel(parem_frame, text=f"{nimi}", font=("Nunito", 16), anchor="w", text_color="#01608b").pack(anchor="w")
    CTkLabel(parem_frame, text=f"{tanane_kuupaev}", font=("Nunito", 16), anchor="w", text_color="#01608b").pack(anchor="w")
    
    CTkLabel(info_frame, text="HailgaAssist", font=("Comfortaa", 50, "bold"), text_color="#55b3d9").pack(side="right", padx=(20,100))
    
    # Поисковая панель
    search_frame=CTkFrame(frame, fg_color="#EEEEEE")
    search_frame.pack(side="top", fill="x", padx=10, pady=10, ipady=15)
    
    search_label=CTkLabel(search_frame, text="Otsi patsient isikukoodi järgi:", font=("Nunito", 14))
    search_label.pack(side=tk.LEFT, padx=5)

    search_entry=CTkEntry(search_frame, border_color="#55b3d9", border_width=2,)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button=CTkButton(search_frame, text="Otsi", command=on_search, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    search_button.pack(side=tk.LEFT, padx=10)

    refresh_button=CTkButton(search_frame, text="Värskenda tabel", command=lambda:load_data_from_db(tree), fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    refresh_button.pack(side=tk.LEFT, padx=10)
    
    # Таблица
    table_frame=CTkFrame(frame)
    table_frame.pack(fill="both", expand=True)
    
    scrollbar=CTkScrollbar(table_frame, fg_color="white")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    tree=ttk.Treeview(table_frame, yscrollcommand=scrollbar.set, columns=("Eesnimi", "Perekonnanimi", "Isikukood", "Registreerimise aeg", "Palati nr", "Arst", "Diagnoos", "Staatus"), show="headings")
    tree.bind("<Double-1>", lambda event: valitud_patsient(tree))
    tree.pack(side="top", fill="both", expand=True)

    # Связываем прокрутку с таблицей
    scrollbar.configure(command=tree.yview)

    # Заголовки столбцов
    tree.heading("Eesnimi", text="Eesnimi")
    tree.heading("Perekonnanimi", text="Perekonnanimi")
    tree.heading("Isikukood", text="Isikukood")
    tree.heading("Registreerimise aeg", text="Registreerimise aeg")
    tree.heading("Palati nr", text="Palati nr")
    tree.heading("Arst", text="Arst")
    tree.heading("Diagnoos", text="Diagnoos")
    tree.heading("Staatus", text="Staatus")


    # Ширина столбцов
    tree.column("Eesnimi", width=100)
    tree.column("Perekonnanimi", width=150)
    tree.column("Isikukood", width=70)
    tree.column("Registreerimise aeg", width=110)
    tree.column("Palati nr", width=50)
    tree.column("Arst", width=100)
    tree.column("Diagnoos", width=200)
    tree.column("Staatus", width=130)

    # Загружаем данные из базы данных
    load_data_from_db(tree)

    peamine_aken.mainloop()


# --- Выбранный пациент из таблицы -------------------------------
def valitud_patsient(tree):
    """ Подробная информация о пациенте (при двойном клике на пациента) """
    global patsiendi_info, patient_data

    valik=tree.selection()
    if not valik:
        return

    # Получаем данные из выбранной строки
    values=tree.item(valik, "values")
    isikukood=values[2]  # Индекс 2 - это столбец "Isikukood"

    # Подключаемся к базе данных и получаем данные пациента
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    cursor.execute("""
        SELECT eesnimi, perekonnanimi, email, isikukood, kaal, pikkus, 
        ylemine_rohk, madalam_rohk, temperatuur, dieet, palati_nr, arst_ID, staatus, diagnoos 
        FROM patsiendid WHERE isikukood = ? 
        """, (isikukood,))
    patient_data=cursor.fetchone()
    
    conn.close()

    if not patient_data:
        messagebox.showerror("Viga", "Patsiendi andmeid ei leitud!")
        return

    # Открываем новое окно с информацией о пациенте
    patsiendi_info=CTkToplevel(peamine_aken)
    patsiendi_info.title("Patsiendi andmed")
    patsiendi_info.geometry("400x600")
    patsiendi_info.resizable(0,0)

    # Cоздаём вкладочный интерфейс (notebook)
    notebook=ttk.Notebook(patsiendi_info, style="TNotebook")
    notebook.pack(fill="both", expand=True)
    style=ttk.Style()
    style.configure("TNotebook", background="#EEEEEE") 

    # Вкладка - Patsiendi andmed
    info_frame=ttk.Frame(notebook)
    notebook.add(info_frame, text="Andmed")

    labels=["Eesnimi", "Perekonnanimi", "E-mail", "Isikukood", "Sünniaeg", "Sugu", "Kaal (kg)", "Pikkus (cm)", "Ülemine rõhk", "Alumine rõhk", "Temperatuur", "Dieet", "Palati nr", "Arst", "Staatus"]
    
    # Извлекаем имя врача по ID
    arst_id=patient_data[11]
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT nimi 
    FROM kasutajad 
    WHERE ID = ? 
    """, (arst_id,))
    arst_nimi=cursor.fetchone()
    conn.close()

    if arst_nimi:
        arst_nimi=arst_nimi[0]
    else:
        arst_nimi="Määramata"

    # Вычисляем дату рождения и возраст с помощью импортированного модуля проверки исикукода
    synniaeg=leia_synniaeg(isikukood)
    sugu=leia_sugu(isikukood)

    patient_data=list(patient_data)
    patient_data[11]=arst_nimi  # Заменяем ID врача на имя
    patient_data.insert(4, synniaeg.strftime("%d.%m.%Y"))  # Дата рождения
    patient_data.insert(5, sugu)  # Возраст

    # Вывод данных в новом окне
    for i, label in enumerate(labels):    # enumerate - создаёт пары (индекс, значение)
        ttk.Label(info_frame, text=label + ":", font=("Nunito", 11, "bold"), foreground="#008ba9", background="#fafbfc").grid(row=i, column=0, sticky="w", padx=10, pady=5)
        ttk.Label(info_frame, text=str(patient_data[i]), font=("Nunito", 11), background="#fafbfc").grid(row=i, column=1, sticky="w", padx=10, pady=5)

    # Если роль врача и статус "В ожидании осмотра врача" --> показываем кнопку для добавления эпикриза
    epikriis_nupp=CTkButton(info_frame, text="📌 Lisa epikriis", command=lambda: lisa_epikriis(isikukood), fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    if amet=="arst":
        epikriis_nupp.grid(row=len(labels)+ 1, column=0, rowspan=1, padx=10, pady=30)

    # Если роль врача и статус "Осмотрен врачем" --> показываем кнопку для возможности выписки пациента
    valja_kirjutada_nupp=CTkButton(info_frame, text="📧 Välja kirjutada", command=on_update, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    staatus=patient_data[14]
    if amet=="arst" and  staatus=="Arsti poolt läbivaadatud":
        valja_kirjutada_nupp.grid(row=len(labels)+ 1, column=1, rowspan=1, padx=10, pady=30)


    # Вкладка - Päevik
    diary_frame=ttk.Frame(notebook)
    notebook.add(diary_frame, text="Päevik")

    # Контейнер для комментариев
    paevik=tk.Label(diary_frame, width=60, height=20)
    paevik.pack(padx=10, pady=10)
    
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT p.kommentaar, p.kaebus, k.nimi AS arst_nimi 
    FROM patsiendid p 
    LEFT JOIN kasutajad k ON p.arst_ID=k.id 
    WHERE p.isikukood = ? AND k.nimi = ? 
    """, (isikukood, arst_nimi))
    diary_entries=cursor.fetchall()
    conn.close()


    for entry in diary_entries:
        # Создаем один раз CTkTextbox
        diary_text=CTkTextbox(paevik, width=600, height=470, font=("Nunito", 14), text_color="#333333", wrap="word")
        diary_text.pack(padx=10, pady=10, fill='both', expand=True)
    
        if entry[0]:  # Если комментарий не пустой
            lisa_text=f"Kaebus: {entry[1]}\n\n{entry[2]}:\n{entry[0]}\n"
        else:  # Если комментарий пустой
            lisa_text=f"Kaebus: {entry[1]}"
    
        diary_text.insert("1.0", lisa_text)
        diary_text.configure(state="disabled")
    
    kommentaar_nupp=CTkButton(diary_frame, text="Lisa kommentaar", command=message, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    kommentaar_nupp.pack(pady=10)


def lisa_epikriis(isikukood):
    """ Добавление эпикриза врачом """
    global kommentaar

    if patsiendi_info:   
        patsiendi_info.destroy() 
    epikriz_aken=CTkToplevel()
    epikriz_aken.title("Epikriis")
    epikriz_aken.geometry("400x450")
    epikriz_aken.resizable(0,0)

    CTkLabel(epikriz_aken, text="Diagnoos:", font=("Nunito", 16, "bold"), text_color="#008ba9").pack(pady=10)
    diagnoos_entry=CTkEntry(epikriz_aken, width=300, border_color="#55b3d9")
    diagnoos_entry.pack(pady=10)

    CTkLabel(epikriz_aken, text="Kommentaar:", font=("Nunito", 16, "bold"), text_color="#008ba9").pack(pady=10)
    kommentaar_text=CTkTextbox(epikriz_aken, height=200, width=300)
    kommentaar_text.pack(pady=10)


    def salvesta_epikriis():
        """ Кнопка для сохранения эпикриза и изменения статуса """
        diagnoos=diagnoos_entry.get()
        kommentaar = kommentaar_text.get("1.0", tk.END).strip()

        if diagnoos=="" or kommentaar=="":
            messagebox.showerror("Viga", "Diagnoos ja kommentaar on kohustuslikud!")
            return

        # Обновляем статус пациента и добавляем эпикриз
        conn=sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE patsiendid 
            SET diagnoos = ?, kommentaar = ?, staatus = ? 
            WHERE isikukood = ? 
            """, (diagnoos, kommentaar, "Arsti poolt läbivaadatud", isikukood))
        conn.commit()
        conn.close()

        messagebox.showinfo("Edu", "Epikriis on salvestatud ja staatus muudetud!")
        epikriz_aken.destroy()


    save_button=CTkButton(epikriz_aken, text="Salvesta epikriis", command=salvesta_epikriis, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    save_button.pack(pady=20)


# --- Выписка пациента ---
def on_update():
    """ Проверяет, выбрана ли строка в Treeview """
    selected_item=tree.selection()  # выбранный ряд
    if selected_item:
        isikukood=selected_item[0]  # id (ID)
        patsiendi_valja_kirjutamine(isikukood)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

def patsiendi_valja_kirjutamine(isikukood):
    """ Выписка пациента из больницы """
    global koduravi_text, paevad_haiglas

    if patsiendi_info:   
        patsiendi_info.destroy() 
    
    valja_kirjutamine_aken=ThemedTk(theme="arc")
    valja_kirjutamine_aken.title("Koduravi ja arve patsiendile")
    valja_kirjutamine_aken.geometry("400x450")
    valja_kirjutamine_aken.resizable(0,0)

    CTkLabel(valja_kirjutamine_aken, text="Sisestage patsiendi nõuanded koduse raviks:", font=("Nunito", 16, "bold"), text_color="#008ba9").pack(padx=10, pady=10)
    koduravi_text=CTkTextbox(valja_kirjutamine_aken, height=230, width=300)
    koduravi_text.pack(padx=10, pady=10)

    CTkLabel(valja_kirjutamine_aken, text="Päevade arv haiglas:", font=("Nunito", 16, "bold"), text_color="#008ba9").pack(padx=10, pady=5)
    paevad_haiglas=ttk.Spinbox(valja_kirjutamine_aken, from_=0, to=100, increment=1, width=5)
    paevad_haiglas.pack(padx=10, pady=10)

    # Кнопка для отправки советов
    CTkButton(valja_kirjutamine_aken, text="Saada kiri", command=lambda: saada_kiri(isikukood), fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white").pack(pady=10)


def generate_nonce(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_payment():
    """ Оплата за кол-во дней в больнице (ссылка прикрепляется к тексту письма) """
    global payment_reference, paevad_hailglas
    # EveryPay данные
    API_URL = "https://igw-demo.every-pay.com/api/v4/payments/oneoff"
    API_AUTH = "ZTM2ZWI0MGY1ZWM4N2ZhMjo3YjkxYTNiOWUxYjc0NTI0YzJlOWZjMjgyZjhhYzhjZA=="
    API_USERNAME = "e36eb40f5ec87fa2"
    ACCOUNT_NAME = "EUR3D1"
    CUSTOMER_URL = "https://maksmine.web.app/makse"

    payment_reference = ""  # Глобально для хранения ID платежа

    amount = float(paevad_haiglas.get()) * 2.50

    data = {
        "api_username": API_USERNAME,
        "account_name": ACCOUNT_NAME,
        "amount": amount,
        "order_reference": str(random.randint(100000, 999999)),
        "nonce": generate_nonce(),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "customer_url": CUSTOMER_URL
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {API_AUTH}"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        payment_info = response.json()
        return payment_info["payment_link"]
    else:
        messagebox.showerror("Ошибка", f"Не удалось создать платёж: {response.status_code}\n{response.text}")
        return None


def saada_kiri(isikukood):
    """ Отправка письма (с советами и назначением лечения от врача + ссылка на оплату количества проведенных дней в больнице) """
    selected_item = tree.selection() 
    if selected_item:
        email = patient_data[2]
        isikukood = patient_data[3]

        payment_link = create_payment()
        kiri="Koduravi: "+koduravi_text.get("1.0","end")+f"\nVoodipäevatasu tasumiseks haiglas järgige linki: {payment_link}"  # домашнее лечение + ссылка на оплату

        smtp_server="smtp.gmail.com"
        port=587
        sender_email="mariia.smolina@gmail.com"
        password="utnh zlza okne zbps" # Teie rakenduse võti
        context=ssl.create_default_context()
        msg=EmailMessage()
        msg.set_content(kiri) 
        msg['Subject']="Koduravi ja arve"
        msg['From']=f"Tallinna Haigla - Arst {nimi}"
        msg['To']=email  
        try:
            server=smtplib.SMTP(smtp_server,port)
            server.starttls(context=context)
            server.login(sender_email,password)
            server.send_message(msg)
            messagebox.showinfo("Informatsioon","Kiri oli saadetud")

            tree.delete(selected_item)  # Удалить пациента из таблицы, после отправки письма
            conn = sqlite3.connect("Arvestus/AppData/haigla.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM patsiendid WHERE isikukood=?", (isikukood,))
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Tekkis viga!",e)
        finally:
            server.quit()


#--- Добавление нового пациента и сохранение в базу данных и таблицу --------------------------------------------------------------
def validate_data():
    """ Функция проверяет, правильны ли введенные данные """

    eesnimi=entries["Eesnimi"].get()
    perekonnanimi=entries["Perekonnanimi"].get()
    email=entries["E-mail"].get()
    isikukood=entries["Isikukood"].get()
    kaal=entries["Kaal (kg)"].get()
    pikkus=entries["Pikkus (cm)"].get()
    temperatuur=entries["Temperatuur"].get()
    kaebus=entries["Kaebus"].get("1.0", tk.END).strip()
    palat=int(entries["Palati number"].get().strip())

    # Получаем значения чекбоксов для диеты
    dieet_baas=entries["Dieet_baas"].get()
    dieet_diabeet=entries["Dieet_diabeet"].get()
    dieet_laktoos=entries["Dieet_laktoos"].get()

    if not eesnimi or not perekonnanimi:
        tk.messagebox.showerror("Viga", "Ees- ja Perekonnanimi on kohustuslik!")
        return False
    if not kaebus:
        tk.messagebox.showerror("Viga", "Kaebus on kohustuslik!")
        return False
    if "@" not in email or "." not in email:
        tk.messagebox.showerror("Viga", "E-mail peab olema korrektne!")
        return False

    # Проверка, что данные вес, рост, температура - числа
    try:
        float(kaal)
        float(pikkus)
        float(temperatuur)
    except:
        tk.messagebox.showerror("Viga", "Sisend peab olema arv!")
        return False

    # Проверка, что хотя бы одна диета выбрана
    if not (dieet_baas or dieet_diabeet or dieet_laktoos):
        tk.messagebox.showerror("Viga", "Valige vähemalt üks dieet!")
        return False

    # Проверка искикода
    teade=kontrolli_ikood(isikukood)
    if teade is not True:
        tk.messagebox.showerror("Viga", teade)
        return False

    conn=sqlite3.connect("Arvestus/AppData/haigla.db") 
    cursor=conn.cursor()
    cursor.execute("""
    SELECT 
        (SELECT COUNT(*) FROM patsiendid WHERE isikukood = ?) AS isikukood_count,
        (SELECT COUNT(*) FROM patsiendid WHERE palati_nr = ?) AS palati_count 
        """, (isikukood, palat))

    isikukood_arv, patsientide_arv=cursor.fetchone()

    # Проверяем количество пациентов в палате
    if patsientide_arv>=4:
        tk.messagebox.showerror("Viga", f"Palatis {palat} on juba täis!")
        return False

    # Если исикукод уже зарегистрирован, выводим ошибку
    if isikukood_arv>0:
        tk.messagebox.showerror("Viga", "Isikukood on juba registreeritud!")
        conn.close()
        return False

    conn.close()
    return True


def clear_entries():
    """ Очищает все поля ввода """
    for key, entry in entries.items():
        if isinstance(entry, CTkEntry):
            entry.delete(0, tk.END)
        elif isinstance(entry, CTkComboBox):
            entry.set("")  # Очистка комбобокса
        elif isinstance(entry, CTkTextbox):
            entry.delete("1.0", tk.END)
        elif isinstance(entry, CTkSpinbox):  
            entry.set(0)   # Сброс значения спинбокса на 0
        elif isinstance(entry, IntVar):  # Сброс чекбоксов
            entry.set(0)

             
def lisa_patsient():
    """ Добавление пациента """
    global entries

    lisa_patsient_aken=tk.Toplevel()
    lisa_patsient_aken.title("Patsiendi andmete sisetamine")
    lisa_patsient_aken.geometry("480x600")
    lisa_patsient_aken.configure(bg="#f5f6f7") 
    lisa_patsient_aken.resizable(0,0) 

    # Поля для ввода данных пациента
    labels=["Eesnimi", "Perekonnanimi", "E-mail", "Isikukood", "Kaal (kg)", "Pikkus (cm)", "Vererõhk", "Temperatuur", "Kaebus", "Dieet", "Arst", "Palati number"]
    entries={}

    for i, label in enumerate(labels):
        ttk.Label(lisa_patsient_aken, text=label, font=("Nunito", 11, "bold"), background="#f5f6f7").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        if label=="Dieet":
            # Создаем Frame для чекбоксов
            dieet_frame=tk.Frame(lisa_patsient_aken)
            dieet_frame.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            dieet_frame.configure(bg="#f5f6f7")

            # Создаём переменные для чекбоксов
            dieet_baas_var=IntVar()   # IntVar - специальная переменная в Tkinter, которая связывает чекбокс с его состоянием (выбран/не выбран)
            dieet_diabeet_var=IntVar()
            dieet_laktoos_var=IntVar()

            # Создаём кастомные чекбоксы
            dieet_baas=CTkCheckBox(dieet_frame, text="Baasdieet", font=("Nunito", 13), variable=dieet_baas_var, fg_color="#55b3d9", hover_color="#008ba9")
            dieet_baas.grid(row=0, column=0, padx=5, sticky="w")

            dieet_diabeet=CTkCheckBox(dieet_frame, text="Diabeetiline", font=("Nunito", 13), variable=dieet_diabeet_var, fg_color="#55b3d9", hover_color="#008ba9")
            dieet_diabeet.grid(row=0, column=1, padx=5, sticky="w")

            dieet_laktoos=CTkCheckBox(dieet_frame, text="Laktoosivaba", font=("Nunito", 13), variable=dieet_laktoos_var, fg_color="#55b3d9", hover_color="#008ba9")
            dieet_laktoos.grid(row=0, column=2, padx=5, sticky="w")

            # Сохраняем чекбоксы в entries
            entries["Dieet_baas"]=dieet_baas_var
            entries["Dieet_diabeet"]=dieet_diabeet_var
            entries["Dieet_laktoos"]=dieet_laktoos_var

        elif label=="Kaebus":
            entry=CTkTextbox(lisa_patsient_aken, height=100, width=250, fg_color="white")
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        elif label=="Arst":
            # Извлекаем список врачей с их ID и именами
            conn=sqlite3.connect("Arvestus/AppData/haigla.db")  # Открываем соединение с базой данных
            cursor=conn.cursor()
            cursor.execute("SELECT id, nimi FROM kasutajad WHERE amet='arst'")
            arstid=cursor.fetchall()

            # Составляем список имен врачей для отображения в Combobox
            arstide_nimed=[arst[1] for arst in arstid] 
            entry=CTkComboBox(lisa_patsient_aken, values=arstide_nimed)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            cursor.close()  
            conn.close()

        elif label=="Vererõhk":
           # Создаем Frame для давления
            rohk_frame=CTkFrame(lisa_patsient_aken)
            rohk_frame.grid(row=i, column=1, columnspan=2, padx=5, pady=5, sticky="w")
            rohk_frame.configure(fg_color="#f5f6f7")
            
            # Верхнее (систолическое) давление
            tk.Label(rohk_frame, text="Ülemine", bg="#f5f6f7", font=("Nunito", 10)).grid(row=0, column=0, padx=(0,5))
            entries["Rõhk_ül"]=CTkSpinbox(rohk_frame, start_value=120, min_value = 90, max_value = 200, scroll_value=1, step_value=10, border_color="#f5f6f7", fg_color="#EEEEEE", font=("Nunito", 16, "bold"))
            entries["Rõhk_ül"].grid(row=0, column=1)

            # Нижнее (диастолическое) давление
            tk.Label(rohk_frame, text="Alumine", bg="#f5f6f7", font=("Nunito", 10)).grid(row=0, column=2, padx=(10,5))
            entries["Rõhk_al"]=CTkSpinbox(rohk_frame, start_value=80, min_value=50, max_value=130, scroll_value=1, step_value=10, border_color="#f5f6f7", font=("Nunito", 16, "bold"), fg_color="#EEEEEE")
            entries["Rõhk_al"].grid(row=0, column=3)
            continue

        elif label=="Palati number":
            entry=CTkComboBox(lisa_patsient_aken, values=["1", "2", "3", "4", "5", "6"])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        else:
            entry=CTkEntry(lisa_patsient_aken, width=250, border_color="#55b3d9")
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[label]=entry

         # Дата регистрации (сегодняшняя дата)
        today_date=datetime.today().strftime("%Y-%m-%d")
        entries["registreerimise_aeg"]=today_date  # Устанавливаем сегодняшнюю дату

        # Функция для проверки палаты в зависимости от "Isikukood"
        def check_palati():
            isikukood=entries["Isikukood"].get()
            if isikukood and isikukood[0] in ["1","3","5"]:
                # Показываем только палаты 4, 5, 6
                entries["Palati number"].configure(values=["4","5","6"])
            else:
                # Показываем только палаты 1, 2, 3
                entries["Palati number"].configure(values=["1","2","3"])

    # Привязываем проверку к изменению значения в поле "Isikukood"
    entries["Isikukood"].bind("<KeyRelease>", lambda event: check_palati())   # "<KeyRelease>" - когда клавиша на клавиатуре отпускается

    # Кнопки сохранения и очистки
    nuppude_frame=tk.Frame(lisa_patsient_aken)
    nuppude_frame.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)
    nuppude_frame.configure(bg="#f5f6f7")

    lisa_nupp=CTkButton(nuppude_frame, text="Registreeri patsient", command=insert_data, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    lisa_nupp.pack(side="left", padx=10, pady=(0, 10))

    kustuta_nupp=CTkButton(nuppude_frame, text="Puhasta väljad", command=clear_entries, fg_color="#55b3d9", hover_color="#008ba9", font=("Nunito", 16, "bold"), text_color="white")
    kustuta_nupp.pack(side="left", padx=10, pady=(0, 10))

    lisa_patsient_aken.mainloop()


def vali_dieet():
    """ Определение выбранной диеты """
    dieet_baas=entries["Dieet_baas"].get()
    dieet_diabeet=entries["Dieet_diabeet"].get()
    dieet_laktoos=entries["Dieet_laktoos"].get()

    valitud_dieet=[]

    if dieet_baas:
        valitud_dieet.append("Baasdieet")
    if dieet_diabeet:
        valitud_dieet.append("Diabeetiline")
    if dieet_laktoos:
        valitud_dieet.append("Laktoosivaba")

    return ", ".join(valitud_dieet)



def saada_arsti_id():
    """ Получаем имя врача, выбранного в комбобоксе """
    valitud_arst=entries["Arst"].get()
    connection=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=connection.cursor()

    cursor.execute("SELECT id FROM kasutajad WHERE nimi=?", (valitud_arst,))
    arst_id=cursor.fetchone()

    connection.close()

    if arst_id:
        return arst_id[0] # Возвращаем ID врача
    else:
        return None


def insert_data():
    """ Проверяет данные и добавляет их в базу данных """
    if validate_data():
        connection=sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor=connection.cursor()

        cursor.execute("""
            INSERT INTO patsiendid (eesnimi, perekonnanimi, email, isikukood, kaal, pikkus, ylemine_rohk, madalam_rohk, temperatuur, kaebus, dieet, palati_nr, arst_ID, diagnoos, staatus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entries["Eesnimi"].get(),
            entries["Perekonnanimi"].get(),
            entries["E-mail"].get(),
            entries["Isikukood"].get(),
            entries["Kaal (kg)"].get(),
            entries["Pikkus (cm)"].get(),
            entries["Rõhk_ül"].get(),
            entries["Rõhk_al"].get(),
            entries["Temperatuur"].get(),
            entries["Kaebus"].get("1.0", tk.END).strip(),
            vali_dieet(),
            entries["Palati number"].get(),
            saada_arsti_id(),
            "Tundmatu",
            "Ootab arsti läbivaatust"))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Patsient on registreeritud süsteemi!")


# --- Поиск и обновить -------------------------------------------------------------------

def on_search():
    search_query=search_entry.get()
    load_data_from_db(tree, search_query)

def load_data_from_db(tree, search_query="", arst_nimi=None):
    """ Функция, которая загружает данные из базы данных SQLite и вставляет их в таблицу """
    # Очистить таблицу Treeview перед добавлением новых данных
    for item in tree.get_children():
        tree.delete(item)

    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    if arst_nimi:  # Фильтрация пациентов по имени врача
        cursor.execute(""" 
        SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimise_aeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus 
        FROM patsiendid p 
        LEFT JOIN kasutajad k ON p.arst_ID = k.id 
        WHERE k.nimi = ? """,(arst_nimi,))
    elif search_query:
        cursor.execute(""" 
        SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimise_aeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus 
        FROM patsiendid p 
        INNER JOIN kasutajad k ON p.arst_ID=k.id 
        WHERE p.isikukood LIKE ? """, ('%' + search_query + '%',))
    else:
        cursor.execute(""" 
        SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimise_aeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus 
        FROM patsiendid p 
        INNER JOIN kasutajad k ON p.arst_ID=k.id """)

    rows=cursor.fetchall()

    # Добавляет данные в таблицу (tree)
    for row in rows:
        tree.insert("", "end", values=row)

    conn.close()


#----------------------------------------------------------------------------------------------
def osakond_aken():
    """ Функция для открытия окна с картой палат отделения """

    osakond_aken=tk.Toplevel(peamine_aken) 
    osakond_aken.title("Oskonna kaart")
    osakond_aken.geometry("400x500")

    # Отображения информации о выбранной палате
    info_label=CTkLabel(osakond_aken, text="Valige palat, et kuvada patsiendid\nNaiste palatid nr: 1 - 3\nMeeste palatid nr: 4 - 6", anchor="w", justify="left", font=("Nunito", 16, "bold"))
    info_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def naita_patsiendi_info(palati_nr):
        # Получаем список пациентов в выбранной палате
        conn=sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor=conn.cursor()
        cursor.execute("""SELECT eesnimi, perekonnanimi, isikukood 
                          FROM patsiendid 
                          WHERE palati_nr = ? """, (palati_nr,))
        patsiendid=cursor.fetchall()

        # Формируем строку для отображения информации о пациентах
        if len(patsiendid)>0:
            patsiendi_info_palatis="" 
        # Проходим по каждому пациенту
            for p in patsiendid:
                patsiendi_info_palatis+="\n"+p[0]+" "+p[1]+" - "+p[2]+"\n" # имя, фамилия, исикукод
        else:
             patsiendi_info_palatis="\nEi ole patsiente selles palatis"

        # Обновляем метку с информацией о пациентах
        info_label.configure(text=f"Palat nr {palati_nr}:\n{patsiendi_info_palatis}", font=("Nunito", 14))

    rows=[0,0,0,1,1,1]  # строки для каждой палаты
    cols=[0,1,2,0,1,2]  # колонки для каждой палаты

    for i in range(6):  # 6 палат
        row=rows[i]  
        col=cols[i] 

        # Получаем список пациентов в палате
        conn=sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor=conn.cursor()
        cursor.execute("""SELECT eesnimi, perekonnanimi, isikukood 
                            FROM patsiendid 
                            WHERE palati_nr = ? """, (i + 1,))
        patsiendid=cursor.fetchall()

        # В зависимости от количества пациентов меняем цвет
        if len(patsiendid)==4:
            varv="#FF3131"  # Палата полностью занята
        elif len(patsiendid)>=2:
            varv="#FFFF8F"  # 2 или 3 пациента
        else:
            varv="#50C878"  # 1 или 0 пациента

        room=CTkLabel(osakond_aken, text=f"PALAT NR {i+1}", font=("Nunito", 16, "bold"), fg_color=varv, corner_radius=10, width=112, height=112)
        room.grid(row=row, column=col, padx=10, pady=10)

        # Привязываем обработчик событий на клик по метке
        room.bind("<Button-1>", lambda event, palati_nr=i+1: naita_patsiendi_info(palati_nr))

    conn.close()


sisselogimine_aken()