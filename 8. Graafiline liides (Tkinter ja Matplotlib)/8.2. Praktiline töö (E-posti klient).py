from msilib.schema import File
from tkinter import *
from tkinter import filedialog, messagebox, ttk, font
import smtplib, ssl, imghdr
from PIL import Image, ImageTk
from email.message import EmailMessage

#--------------------------------------------------------------------------------------
# E-posti klient Minu Oma Outlook  https://moodle.edu.ee/mod/assign/view.php?id=2568944


def vali_pilt():
    global files
    files=filedialog.askopenfilenames()   # Выбор нескольких файлов
    l_lisatud.configure(text=files)

    return files

def saada_kiri():
    kellele=email_box.get().split(",")  # Разделение почты запятой, from Entry 
    kiri=kiri_box.get("1.0",END) # from Text
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="mariia.smolina@gmail.com"
    password="utnh zlza okne zbps" # Teie rakenduse võti
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri) 
    msg['Subject']=tema_box.get()
    msg['From']="Marina Smolina"
    msg['To']=", ".join(kellele)   # Соединяем почты через запятую
    for file in files:
        with open(file,'rb') as fpilt:
            pilt=fpilt.read()
        msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None,pilt))
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon","Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga!",e)
    finally:
        server.quit()

def bold_text():
    valitud_font=font_combobox.get()    # Получаем выбранный шрифт из списка
    valitud_suurus=font_suurus_combobox.get()
    kiri_box.tag_configure("bold", font=(valitud_suurus, valitud_suurus, "bold"))
    kiri_box.tag_add("bold", "sel.first", "sel.last")  # Применяем стиль текста к выделенному тексту
    # sel.first, sel.last - указывает на начало и конец выделенного текста

def italic_text():
    selected_font=font_combobox.get()
    valitud_suurus=font_suurus_combobox.get()
    kiri_box.tag_configure("italic", font=(selected_font, valitud_suurus, "italic"))
    kiri_box.tag_add("italic", "sel.first", "sel.last")

def normal_text():
    valitud_suurus=font_suurus_combobox.get()
    kiri_box.tag_remove("bold", "1.0", "end")  # Убираем все теги bold
    kiri_box.tag_remove("italic", "1.0", "end")  # Убираем все теги italic
    kiri_box.config(font=(font_combobox.get(), valitud_suurus))  # Устанавливаем шрифт в обычный

def muuta_font_suurus(event=None):
    valitud_font=font_combobox.get()
    valitud_suurus=font_suurus_combobox.get()  # Получаем выбранный размер
    kiri_box.config(font=(valitud_font, valitud_suurus))  # Устанавливаем новый размер шрифта

def muuta_font(event=None):
    valitud_font=font_combobox.get()
    valitud_suurus=font_suurus_combobox.get()
    kiri_box.config(font=(valitud_font, valitud_suurus))  # Изменяем шрифт на выбранный

def puhasta_vorm():
    email_box.delete(0, END)  # 0, END - от начала до конца
    tema_box.delete(0, END)
    kiri_box.delete("1.0", END)  # 1.0, END - с первой строки до конца
    l_lisatud.configure(text="...")  # Сбрасывает поле с путём картинки до '...'



aken=Tk()
aken.geometry("500x550")
aken.resizable(False, False) # Отключает изменение размера окна (Ширина - False, Высота - False)
aken.title("Minu Outlook")
aken.columnconfigure(1, weight=0, minsize=360)  # Колонка 1 не растягивается, минимальный размер 360px
aken.rowconfigure(4, weight=0, minsize=250)  # Cтрока 4 не растягивается, минимальный размер 250px


# Стили ttk 
style = ttk.Style()
style.configure("TButton", font=("Poppins", 14, "bold"), foreground="white")
style.configure("LisaPilt.TButton", font=("Poppins", 14), foreground="#10226d", padding=(1, 1))
style.configure("TEntry", font=("Poppins", 12), padding=5)
style.configure("Bold.TButton", font=("Poppins", 10, "bold"), foreground="#10226d", padding=1)
style.configure("Italic.TButton", font=("Poppins", 10, "italic"), foreground="#10226d", padding=1)
style.configure("Normal.TButton", font=("Poppins", 10, "normal"), foreground="#10226d", padding=1)
style.configure("TCombobox", font=("Poppins", 12), foreground="#10226d", padding=6)


# Labels
button_bg_2=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\bg_2.png")
button_bg_2_resized=button_bg_2.resize((100, 35))
button_bg_image_2=ImageTk.PhotoImage(button_bg_2_resized)

label_kellele=Label(aken, text="E-MAIL:", font=("Poppins", 14), fg="#10226d",  image=button_bg_image_2, compound="center")
label_kellele.grid(row=0, column=0, padx=10, pady=10)

label_teema=Label(aken, text="TEEMA:", font=("Poppins", 14), fg="#10226d", image=button_bg_image_2, compound="center")
label_teema.grid(row=1, column=0, padx=10, pady=10)

button_pilt=ttk.Button(aken, style="LisaPilt.TButton", text="LISA PILT:", command=vali_pilt,  width=5, image=button_bg_image_2, compound="center")
button_pilt.grid(row=2, column=0, padx=1, pady=1)

label_kiri=Label(aken, text="KIRI:", font=("Poppins", 14),  fg="#10226d", image=button_bg_image_2, compound="center")
label_kiri.grid(row=4, column=0, padx=10, pady=10)


# Отображение добавленного изображения
l_lisatud=Label(aken, text="...", font=("Poppins", 8), width=30, height=1, fg="#10226d", bg="#dae0ee")
l_lisatud.grid(row=2, column=1, padx=5, pady=5, sticky="ew") # ew - виджет растягивается только по горизонтали


# Поля ввода
email_box=ttk.Entry(aken, width=30)
email_box.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tema_box=ttk.Entry(aken, width=30)
tema_box.grid(row=1, column=1,  padx=5, pady=5, sticky="ew")

kiri_box=Text(aken, font=("Poppins", 12), width=10, height=3, bg="#dae0ee", fg="#10226d", wrap="word")
kiri_box.grid(row=4, column=1,  padx=5, pady=5, sticky="nsew") #nsew - виджет растягивается по всем сторонам ячейки


# Кнопки
button_bg=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\bg.png")
button_bg_resized=button_bg.resize((135, 40)) 
button_bg_image=ImageTk.PhotoImage(button_bg_resized)

rida = Frame(aken)
rida.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

button_saada=ttk.Button(rida, text="SAADA", command=saada_kiri, image=button_bg_image, compound="center")
button_saada.grid(row=5, column=1, padx=(70, 2), pady=5, sticky="ew")

button_puhasta=ttk.Button(rida, text="PUHASTA", command=puhasta_vorm, image=button_bg_image, compound="center")
button_puhasta.grid(row=5, column=2, padx=(5, 2), pady=5, sticky="ew")


# Кнопки редаткирования текста - "bold", "italic"
text_vormind=Frame(aken)
text_vormind.grid(row=3, column=0, columnspan=4)

bold_button=ttk.Button(text_vormind, style="Bold.TButton", text="Bold", command=bold_text, width=5)
bold_button.grid(row=3, column=1, padx=(130, 2), pady=5)

italic_button=ttk.Button(text_vormind, style="Italic.TButton", text="Italic", command=italic_text, width=5)
italic_button.grid(row=3, column=2, padx=(2, 2), pady=5)

reset_button=ttk.Button(text_vormind, style="Normal.TButton", text="Normal", command=normal_text, width=7)
reset_button.grid(row=3, column=3, padx=(2, 2), pady=5)


# Cписок размеров шрифта
font_sizes=[8,10,12,14,16,18,20,22,24,26,28,30]

# Выбор размера шрифта
font_suurus_combobox=ttk.Combobox(text_vormind, values=font_sizes, width=2)
font_suurus_combobox.set(12)  # Устанавливаем начальный размер
font_suurus_combobox.grid(row=3, column=4, padx=5, pady=5)

# Привязываем изменение значения к функции обновления шрифта
font_suurus_combobox.bind("<<ComboboxSelected>>", muuta_font_suurus)


# Список шрифтов 
font_list=list(font.families())   # Получаем список доступных шрифтов
font_combobox=ttk.Combobox(text_vormind, values=font_list, width=14, height=5)
font_combobox.set("Poppins")  # Шрифт по умолчанию
font_combobox.grid(row=3, column=5, padx=5, pady=5)
font_combobox.bind("<<ComboboxSelected>>", muuta_font)  # Привязываем выбор шрифта к функции change_font
# .bind - привязка событий


aken.mainloop()