import tkinter as tk
import sqlite3, requests, random, json, string, smtplib, ssl
from tkinter import filedialog, messagebox, ttk, font
from Isikukood_Modul import *
from db_funktsioonid import *
from PIL import Image, ImageTk
from email.message import EmailMessage



# Глобальные переменные для хранения данных
patsiendid=[]
kasutajad=[]

def db_data():
    global patsiendid, kasutajad

    # Подключение к базе данных
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()

    # Получаем все данные из таблиц
    cursor.execute("SELECT * FROM patsiendid")
    patsiendid=cursor.fetchall()

    cursor.execute("SELECT * FROM kasutajad")
    kasutajad=cursor.fetchall()

    conn.close()


# Выводит данные таблиц из базы данных в терминале (для себя)
def print_patsiendid():
    # Печатаем все строки таблицы patsiendid в консоль
    if not patsiendid:
        print("\nТаблица 'patsiendid' пуста")
    else:
        print("\nAndmed tabelist patsiendid:")
        for patient in patsiendid:
            print(patient)  # Выводим каждую строку (пациента) в консоль

    # Печатаем все строки таблицы kasutajad в консоль
    if not kasutajad:
        print("\nТаблица 'kasutajad' пуста")
    else:
        print("\n\nAndmed tabelist kasutajad:")
        for kasutaja in kasutajad:
            print(kasutaja)  # Выводим каждую строку (пользователя) в консоль


# Форма для входа для медсестер и врачей
def sisselogimine_aken():
    global sisend_kasutajanimi, sisend_parool, aken_login
    aken_login=tk.Tk()
    aken_login.title("Autoriseerimine")
    aken_login.geometry("300x200")
    print_patsiendid() 

    tk.Label(aken_login, text="Kasutajanimi", font="Nunito").pack()
    sisend_kasutajanimi=tk.Entry(aken_login)
    sisend_kasutajanimi.pack()

    tk.Label(aken_login, text="Parool", font="Nunito").pack()
    sisend_parool=tk.Entry(aken_login, show="*")
    sisend_parool.pack()

    tk.Button(aken_login, text="Logi sisse", command=sisselogimine_kasutaja).pack()

    aken_login.mainloop()


# Функция с авторизацией медсестер и врачей
def sisselogimine_kasutaja():
    global amet, nimi
    kasutajanimi=sisend_kasutajanimi.get()
    parool=sisend_parool.get()

    # Поиск пользователя среди загруженных данных
    kasutaja=None
    for kasutaja in kasutajad:
        if kasutaja[1]==kasutajanimi and kasutaja[2]==parool: # 1 - kasutajanimi", 2 - parool
            kasutaja=kasutaja
            break

    if kasutaja:
        nimi, amet = kasutaja[4], kasutaja[3]   # 4 - nimi, 3 - amet
        messagebox.showinfo("Tere tulemast!", f"Tere tulemast, {nimi}! \n\nSisse logitud kui {amet}")

        aken_login.destroy()  # Закрываем окно входа
        patsiendide_andmed(nimi, amet)  # Открываем главное окно
    else:
        messagebox.showerror("Viga", "Vale kasutajanimi või parool!")


# Функция для отображения таблицы пациентов
def patsiendide_andmed(nimi, amet):
    global tree, search_entry, peamine_aken

    peamine_aken=tk.Tk() 
    peamine_aken.title("Haigla Assist")
    peamine_aken.geometry("1200x500")

    tk.Label(peamine_aken, text=f"Tere, {nimi}!", font=("Nunito", 16)).pack(pady=20)

    # Панель с поиском
    search_frame=tk.Frame(peamine_aken)
    search_frame.pack(pady=10)

    search_label=tk.Label(search_frame, text="Otsi patsient isikukoodi järgi:")
    search_label.pack(side=tk.LEFT)

    search_entry=tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button=tk.Button(search_frame, text="Otsi", command=on_search)
    search_button.pack(side=tk.LEFT)

    frame=tk.Frame(peamine_aken)
    frame.pack(pady=20, fill=tk.BOTH, expand=True)

    # Панель с кнопками с правой стороны таблицы
    nupude_frame=tk.Frame(frame)
    nupude_frame.pack(side=tk.RIGHT, anchor="e", padx=10)

    lisa_nupp=tk.Button(nupude_frame, text="Lisa andmeid", command=lisa_patsient)
    lisa_nupp.pack(padx=10, pady=10)

    osakond_nupp=tk.Button(nupude_frame, text="Kuva oskond", command=osakond_aken)
    osakond_nupp.pack(pady=10)

    if amet=="arst":  # Если пользователь - врач, добавляем кнопку фильтрации по его пациентам
        filter_nupp=tk.Button(nupude_frame, text="Minu patsiendid", command=lambda: load_data_from_db(tree, arst_nimi=nimi))
        filter_nupp.pack(pady=10)

    logi_valja_nupp=tk.Button(nupude_frame, text="Logi välja", command=lambda: (peamine_aken.destroy(), sisselogimine_aken()))
    logi_valja_nupp.pack(side="bottom", anchor="s", pady=80)

    # Таблица с прокруткой
    scrollbar=tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree=ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("Eesnimi", "Perekonnanimi", "Isikukood", "Registreerimis aeg", "Palati nr", "Arst", "Diagnoos", "Staatus"), show="headings")
    tree.bind("<Double-1>", lambda event: valitud_patsient(tree))
    tree.pack(fill=tk.BOTH, expand=True)

    # Связываем прокрутку с таблицей
    scrollbar.config(command=tree.yview)

    # Заголовки столбцов
    tree.heading("Eesnimi", text="Eesnimi")
    tree.heading("Perekonnanimi", text="Perekonnanimi")
    tree.heading("Isikukood", text="Isikukood")
    tree.heading("Registreerimis aeg", text="Registreerimis aeg")
    tree.heading("Palati nr", text="Palati nr")
    tree.heading("Arst", text="Arst")
    tree.heading("Diagnoos", text="Diagnoos")
    tree.heading("Staatus", text="Staatus")

    # Ширина столбцов
    tree.column("Eesnimi", width=100)
    tree.column("Perekonnanimi", width=150)
    tree.column("Isikukood", width=80)
    tree.column("Registreerimis aeg", width=110)
    tree.column("Palati nr", width=50)
    tree.column("Arst", width=100)
    tree.column("Diagnoos", width=150)
    tree.column("Staatus", width=100)

    # Загружаем данные из базы данных
    load_data_from_db(tree)

    peamine_aken.mainloop()


# --- Подробная информация о пациенте (при двойном клике на пациента) -------------------------------
def valitud_patsient(tree):
    global patsiendi_info

    valik=tree.selection()
    if not valik:
        return

    # Получаем данные из выбранной строки
    values=tree.item(valik, "values")
    isikukood=values[2]  # индекс 2 - это столбец "Isikukood"

    # Ищем пациента в глобальном списке пациентов
    for patsient in patsiendid:
        if patsient[4] == isikukood:
            break  # если пациент найден, прерываем цикл
    else:
        messagebox.showerror("Viga", "Patsiendi andmeid ei leitud!")
        return

    # Открываем новое окно с информацией о пациенте
    patsiendi_info_aken=tk.Toplevel()
    patsiendi_info_aken.title("Patsiendi andmed")
    patsiendi_info_aken.geometry("400x600")

    labels=["Eesnimi", "Perekonnanimi", "E-mail", "Isikukood", "Sünniaeg", "Sugu", "Kaal (kg)", 
              "Pikkus (cm)", "Ülemine rõhk", "Alumine rõhk", "Temperatuur", 
              "Kaebus", "Dieet", "Diagnoos", "Registeerimise aeg", "Palati nr", "Arst", "Staatus"]
    
    # Извлекаем имя врача по ID
    arst_id=patsient[16]
    arst_nimi="Määramata"  # если не нашли, ставим значение по умолчанию
    for k in kasutajad:
        if k[0]==arst_id:  # проверяем, совпадает ли ID врача
            arst_nimi=k[4]  
            break

    # Вычисляем дату рождения и возраст с помощью импортированного модуля проверки исикукода
    synniaeg=leia_synniaeg(isikukood)
    sugu=leia_sugu(isikukood)

    patsient=list(patsient)  # Конвертируем данные пациента в список для изменения
    patsient.insert(5, synniaeg.strftime("%d.%m.%Y"))  # Вставляем дату рождения
    patsient.insert(6, sugu)  # Вставляем пол
    patsient[12]=arst_nimi # Заменяем ID врача на его имя

    # Вывод данных в новом окне
    for i, label in enumerate(labels):
        tk.Label(patsiendi_info_aken, text=label + ":", font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        tk.Label(patsiendi_info_aken, text=str(patsient[i+1]), font=("Arial", 10)).grid(row=i, column=1, sticky="w", padx=10, pady=5)


    # Если роль врача и статус "В ожидании осмотра врача" --> появляется кнопка для добавления эпикриза
    epikriis_nupp=tk.Button(patsiendi_info_aken, text="Lisa epikriis", command=lambda: lisa_epikriis(isikukood))
    if amet=="arst":
        epikriis_nupp.grid(row=len(labels)+ 1, column=0, columnspan=1, padx=5, pady=10)

    # Если роль врача и статус "Осмотрен врачом" --> появляется кнопка для выписки пациента из больницы
    valja_kirjutada_nupp=tk.Button(patsiendi_info_aken, text="Välja kirjutada", command=on_update)
    staatus=patsient[15] 
    if amet=="arst" and  staatus=="Arsti poolt läbivaadatud":
        valja_kirjutada_nupp.grid(row=len(labels)+ 1, column=1, columnspan=1, padx=5, pady=10)


# --- Врач составляет эпикриз ---------------------------------------
def lisa_epikriis(isikukood):
    if patsiendi_info:   
        patsiendi_info.destroy() 
    epikriis_aken=tk.Tk()
    epikriis_aken.title("Epikriis")
    epikriis_aken.geometry("400x300")

    tk.Label(epikriis_aken, text="Diagnoos:").pack(pady=10)
    diagnoos_entry = tk.Entry(epikriis_aken, width=40)
    diagnoos_entry.pack(pady=10)

    tk.Label(epikriis_aken, text="Kommentaar:").pack(pady=10)
    kommentaar_text = tk.Text(epikriis_aken, height=6, width=40)
    kommentaar_text.pack(pady=10)

    # Кнопка для сохранения эпикриза и изменения статуса
    def save_epikriz():
        diagnoos=diagnoos_entry.get()
        kommentaar=kommentaar_text.get("1.0", tk.END).strip()

        if diagnoos=="" or kommentaar=="":
            messagebox.showerror("Viga", "Diagnoos ja kommentaar on kohustuslikud!")
            return

        # Обновляем статус пациента и добавляем эпикриз
        conn = sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE patsiendid 
            SET diagnoos = ?, staatus = ? 
            WHERE isikukood = ?
        """, (diagnoos, "Arsti poolt läbivaadatud", isikukood))
        conn.commit()
        conn.close()

        messagebox.showinfo("Edu", "Epikriis on salvestatud ja staatus muudetud!")
        epikriis_aken.destroy()

    save_button = tk.Button(epikriis_aken, text="Salvesta epikriis", command=save_epikriz)
    save_button.pack(pady=20)


# --- Выписка пациента ----------------------------------------------
def on_update():
    selected_item=tree.selection()  # выбранный ряд
    if selected_item:
        isikukood=selected_item[0]  # id (ID)
        patsiendi_valja_kirjutamine(isikukood)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

def patsiendi_valja_kirjutamine(isikukood):
    global advice_text, paevad_haiglas
    
    valja_kirjutamine_aken=tk.Toplevel()
    valja_kirjutamine_aken.title("Koduravi ja arve patsiendile")


    tk.Label(valja_kirjutamine_aken, text="Sisestage patsiendi nõuanded koduse raviks:").pack(padx=10, pady=10)
    advice_text=tk.Text(valja_kirjutamine_aken, height=10, width=40)
    advice_text.pack(padx=10, pady=10)

    tk.Label(valja_kirjutamine_aken, text="Päevade arv haiglas:").pack(padx=10, pady=5)
    paevad_haiglas=tk.Spinbox(valja_kirjutamine_aken, from_=0, to=100, increment=1, width=5)
    paevad_haiglas.pack(padx=10, pady=10)

    # Кнопка для отправки советов
    tk.Button(valja_kirjutamine_aken, text="Välj kitjutada ja saada", command=lambda: saada_kiri(isikukood)).pack(pady=10)


# --- Оплата за кол-во дней в больнице (ссылка прикрепляется к тексту письма)
def generate_nonce(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_payment():
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


# Отправка письма (с советами и назначением лечения от врача + ссылка на оплату количества проведенных дней в больнице)
def saada_kiri(isikukood):
    selected_item = tree.selection()  # Võta valitud rida
    if selected_item:
        email = patsiendid[3]
        isikukood = patsiendid[4]

        payment_link = create_payment()
        kiri=advice_text.get("1.0","end")+f"\nДля оплаты услуг перейдите по ссылке: {payment_link}"

        smtp_server="smtp.gmail.com"
        port=587
        sender_email="mariia.smolina@gmail.com"
        password="utnh zlza okne zbps" # Teie rakenduse võti
        context=ssl.create_default_context()
        msg=EmailMessage()
        msg.set_content(kiri) 
        msg['Subject']="Koduravi ja arve"
        msg['From']=f"LuumHaigla - Arst {nimi}"
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

# Функция проверяет, правильны ли введенные данные
def validate_data():

    eesnimi=entries["Eesnimi"].get()
    perekonnanimi=entries["Perekonnanimi"].get()
    email=entries["E-mail"].get()
    isikukood=entries["Isikukood"].get()
    kaal=entries["Kaal (kg)"].get()
    pikkus=entries["Pikkus (cm)"].get()
    rohk_yl=entries["Rõhk_ül"].get()
    rohk_al=entries["Rõhk_al"].get()
    temperatuur=entries["Temperatuur"].get()
    kaebus=entries["Kaebus"].get("1.0", tk.END).strip()

    # Получаем значения чекбоксов для диеты
    dieet_baas=entries["Dieet_baas"].get()
    dieet_diabeet=entries["Dieet_diabeet"].get()
    dieet_laktoos=entries["Dieet_laktoos"].get()

    if not eesnimi or not perekonnanimi:
        tk.messagebox.showerror("Viga", "Ees- ja Perekonnanimi on kohustuslik!")
        return False
    if not kaal.isdigit() or not pikkus.isdigit() or not temperatuur.isdigit() or not rohk_yl.isdigit() or not rohk_al.isdigit() :
        tk.messagebox.showerror("Viga", "Sisend peab olema arv!")
        return False
    if not kaebus:
        tk.messagebox.showerror("Viga", "Kaebus on kohustuslik!")
        return False
    if "@" not in email or "." not in email:
        tk.messagebox.showerror("Viga", "E-mail peab olema korrektne!")
        return False
    # Проверка искикода
    teade=kontrolli_ikood(isikukood)
    if teade is not True:
        tk.messagebox.showerror("Viga", teade)
        return False

    return True


# Очищает все поля ввода
def clear_entries():
    for entry in entries.items():
        if isinstance(entry, tk.Entry) or isinstance(entry, ttk.Combobox):
            entry.delete(0, tk.END)
        elif isinstance(entry, tk.Text):
            entry.delete("1.0", tk.END)
        elif isinstance(entry, tk.BooleanVar):  # Сброс чекбоксов
            entry.set(False)

# Добавление пациента
def lisa_patsient():
    global entries

    lisa_patsient_aken=tk.Toplevel()
    lisa_patsient_aken.title("Patsiendi andmete sisetamine")
    lisa_patsient_aken.geometry("460x550")

    # Поля для ввода данных пациента
    labels=["Eesnimi", "Perekonnanimi", "E-mail", "Isikukood", "Kaal (kg)", "Pikkus (cm)", "Vererõhk", "Temperatuur", "Kaebus", "Dieet", "Arst", "Palati number"]
    entries={}

    for i, label in enumerate(labels):
        tk.Label(lisa_patsient_aken, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        if label=="Dieet":
            # Создаем Frame для чекбоксов
            dieet_frame=tk.Frame(lisa_patsient_aken)
            dieet_frame.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            # Создаем переменные для чекбоксов (BooleanVar - напрямую управляет состоянием чекбокса как True (выбран) или False (не выбран)) 
            dieet_baas_var=tk.BooleanVar()  
            dieet_diabeet_var=tk.BooleanVar()
            dieet_laktoos_var=tk.BooleanVar()

            # Создаем чекбоксы
            dieet_baas=tk.Checkbutton(dieet_frame, text="Baasdieet", variable=dieet_baas_var)
            dieet_baas.grid(row=0, column=0, padx=5, sticky="w")
        
            dieet_diabeet=tk.Checkbutton(dieet_frame, text="Diabeetiline", variable=dieet_diabeet_var)
            dieet_diabeet.grid(row=0, column=1, padx=5, sticky="w")
        
            dieet_laktoos=tk.Checkbutton(dieet_frame, text="Laktoosivaba", variable=dieet_laktoos_var)
            dieet_laktoos.grid(row=0, column=2, padx=5, sticky="w")

            # Сохраняем чекбоксы в entries
            entries["Dieet_baas"]=dieet_baas_var
            entries["Dieet_diabeet"]=dieet_diabeet_var
            entries["Dieet_laktoos"]=dieet_laktoos_var

        elif label=="Kaebus":
            entry=tk.Text(lisa_patsient_aken, height=6, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        elif label=="Arst":
            # Извлекаем список врачей с их ID и именами
            conn=sqlite3.connect("Arvestus/AppData/haigla.db")  # Открываем соединение с базой данных
            cursor=conn.cursor()
            cursor.execute("SELECT id, nimi FROM kasutajad WHERE amet='arst'")
            arstid=cursor.fetchall()

            # Составляем список имен врачей для отображения в Combobox
            arstide_nimed=[arst[1] for arst in arstid] 
            entry=ttk.Combobox(lisa_patsient_aken, values=arstide_nimed)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            cursor.close()  
            conn.close()

        elif label=="Vererõhk":
           # Создаем Frame для давления
            rohk_frame=tk.Frame(lisa_patsient_aken)
            rohk_frame.grid(row=i, column=1, columnspan=2, padx=5, pady=5, sticky="w")

            # Верхнее (систолическое) давление
            tk.Label(rohk_frame, text="Ülemine").grid(row=0, column=0, padx=(0,5))
            entries["Rõhk_ül"]=tk.Spinbox(rohk_frame, from_=90, to=200, increment=10, width=5)
            entries["Rõhk_ül"].grid(row=0, column=1, padx=5)

            # Нижнее (диастолическое) давление
            tk.Label(rohk_frame, text="Alumine").grid(row=0, column=2, padx=(10,5))
            entries["Rõhk_al"]=tk.Spinbox(rohk_frame, from_=50, to=130, increment=10, width=5)
            entries["Rõhk_al"].grid(row=0, column=3, padx=5)
            continue

        elif label=="Palati number":
            entry=ttk.Combobox(lisa_patsient_aken, values=["1", "2", "3", "4", "5", "6"])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        else:
            entry=tk.Entry(lisa_patsient_aken, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[label]=entry

         # Дата регистрации (сегодняшняя дата)
        today_date=datetime.today().strftime("%Y-%m-%d")
        entries["RegistreerimiseAeg"] = today_date  # Устанавливаем сегодняшнюю дату

    # Кнопки сохранения и очистки
    button_frame=tk.Frame(lisa_patsient_aken)
    button_frame.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

    lisa_nupp=tk.Button(button_frame, text="Registreeri patsient", command=insert_data)
    lisa_nupp.pack(side="left", padx=10)

    kustuta_nupp=tk.Button(button_frame, text="Puhasta väljad", command=clear_entries)
    kustuta_nupp.pack(side="left", padx=10)

    lisa_patsient_aken.mainloop()

def valitud_dieet():
    dieet_baas=entries["Dieet_baas"].get()
    dieet_diabeet=entries["Dieet_diabeet"].get()
    dieet_laktoos=entries["Dieet_laktoos"].get()

    selected_dieet=[]

    if dieet_baas:
        selected_dieet.append("Baasdieet")
    if dieet_diabeet:
        selected_dieet.append("Diabeetiline")
    if dieet_laktoos:
        selected_dieet.append("Laktoosivaba")

    return ", ".join(selected_dieet)


def saada_arsti_id():
    # Получаем имя врача, выбранного в комбобоксе
    valitud_arst=entries["Arst"].get()

    # Ищем врача в списке kasutajad
    for arst in kasutajad:
        if arst[4]==valitud_arst:  
            return arst[0] # Возвращаем ID врача

    return None

# Проверяет данные и добавляет их в базу данных
def insert_data():
    if validate_data():
        connection=sqlite3.connect("Arvestus/AppData/haigla.db")
        cursor=connection.cursor()

        cursor.execute("""
            INSERT INTO patsiendid (eesnimi, perekonnanimi, email, isikukood, kaal, pikkus, ylemineRohk, madalamRohk, temperatuur, kaebus, dieet, arst_ID, palati_nr, diagnoos, staatus)
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
            valitud_dieet(),
            entries["Palati number"].get(),
            saada_arsti_id(),
            "Tundmatu",
            "Ootel arstilt"))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Patsient on registreeritud süsteemi!")


# --- Поиск -------------------------------------------------------------------
def on_search():
    search_query=search_entry.get()
    load_data_from_db(tree, search_query)

#Функция, которая загружает данные из базы данных SQLite и вставляет их в таблицу
def load_data_from_db(tree, search_query="", arst_nimi=None):
    # Очищает таблицу Treeview перед добавлением новых данных
    for item in tree.get_children():
        tree.delete(item)
   
    conn=sqlite3.connect("Arvestus/AppData/haigla.db")
    cursor=conn.cursor()
    # Делает запрос к базе данных для получения данных
    if arst_nimi:  # Фильтрация пациентов по имени врача
        cursor.execute("SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimiseAeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus FROM patsiendid p LEFT JOIN kasutajad k ON p.arst_ID = k.id WHERE k.nimi = ?",(arst_nimi,))
    elif search_query:
        cursor.execute(
            "SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimiseAeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus FROM patsiendid p LEFT JOIN kasutajad k ON p.arst_ID=k.id WHERE p.isikukood LIKE ?", 
            ('%' + search_query + '%',))
    else:
        cursor.execute(
            "SELECT p.eesnimi, p.perekonnanimi, p.isikukood, p.registreerimiseAeg, p.palati_nr, k.nimi AS arst_nimi, p.diagnoos, p.staatus FROM patsiendid p LEFT JOIN kasutajad k ON p.arst_ID=k.id")

    rows=cursor.fetchall()

    # Добавляет данные в таблицу (tree)
    for row in rows:
        tree.insert("", "end", values=row)

    conn.close()


#----------------------------------------------------------------------------------------------
# Функция для открытия окна с картой палат отделения
def osakond_aken():

    osakond_aken=tk.Toplevel(peamine_aken)
    osakond_aken.title("Oskonna kaart")
    osakond_aken.geometry("400x400")

    # Отображения информации о выбранной палате
    info_label=tk.Label(osakond_aken, text="Valige palat, et kuvada patsiendid", anchor="w", justify="left")
    info_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def naita_patsiendi_info(palati_nr):
        patsiendid_palatis=[
        (patsient[1], patsient[2], patsient[4])  # имя, фамилия, isikukood
        for patsient in patsiendid
        if patsient[14]==palati_nr  # Предположим, что палата указана в 15-м столбце
        ]

        # Формируем строку для отображения информации о пациентах
        if len(patsiendid_palatis)>0:
            patsiendi_info="" 
        # Проходим по каждому пациенту
            for p in patsiendid_palatis:
                patsiendi_info+="\n"+p[0]+" "+p[1]+" - "+p[2]+"\n" # имя, фамилия, исикукод
        else:
             patsiendi_info="\nEi ole patsiente selles palatis"

        # Обновляем метку с информацией о пациентах
        info_label.config(text=f"Palat nr {palati_nr}:\n{patsiendi_info}")

    rows=[0,0,0,1,1,1]  # строки для каждой палаты
    cols=[0,1,2,0,1,2]  # колонки для каждой палаты

    for i in range(6):  # 6 палат
        row=rows[i]  
        col=cols[i] 

        patsiendid_palatis=[
        (patsient[1], patsient[2], patsient[4]) 
        for patsient in patsiendid
        if patsient[14]==i + 1 
        ]

        # В зависимости от количества пациентов меняем цвет
        if len(patsiendid_palatis)==4:
            varv="red"  # Палата полностью занята
        elif len(patsiendid_palatis)>=2:
            varv="yellow"  # 2 или 3 пациента
        else:
            varv="green"  # 1 или 0 пациента

        room=tk.Label(osakond_aken, text=f"PALAT NR {i+1}", bg=varv, width=15, height=6)
        room.grid(row=row, column=col, padx=10, pady=10)

        # Привязываем обработчик событий на клик по метке
        room.bind("<Button-1>", lambda event, palati_nr=i+1: naita_patsiendi_info(palati_nr))

    conn.close()



db_data()
sisselogimine_aken()