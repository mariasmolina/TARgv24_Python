from msilib.schema import File
from tkinter import *
from tkinter import filedialog, messagebox
import smtplib, ssl, imghdr
from PIL import Image, ImageTk
from email.message import EmailMessage

#--------------------------------------------------------------------------------------
# E-posti klient Minu Oma Outlook  https://moodle.edu.ee/mod/assign/view.php?id=2568944


def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    l_lisatud.configure(text=file)

    return file

def saada_kiri():
    kellele=email_box.get() # from Entry
    kiri=kiri_box.get("1.0",END) # from Text
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="mariia.smolina@gmail.com"
    password="utnh zlza okne zbps" # Teie rakenduse võti
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="E-kiri saatmine"
    msg['From']="Marina Smolina"
    msg['To']=kellele
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



aken=Tk()
aken.geometry("500x500")
aken.resizable(False, False) # Отключает изменение размера окна (Ширина - False, Высота - False)
aken.title("Minu Oma Outlook")

aken.columnconfigure(1, weight=1)  # Делаем второй столбец растягиваемым
aken.columnconfigure(2, weight=1)  # Делаем третий столбец растягиваемым


# Labels
button_bg_2=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\bg_2.png")
button_bg_2_resized=button_bg_2.resize((100, 30))
button_bg_image_2=ImageTk.PhotoImage(button_bg_2_resized)

label_kellele=Label(aken, text="E-MAIL:", font=("Poppins", 14), fg="#10226d",  image=button_bg_image_2, compound="center")
label_kellele.grid(row=0, column=0, padx=10, pady=10)

label_teema=Label(aken, text="TEEMA:", font=("Poppins", 14), fg="#10226d", image=button_bg_image_2, compound="center")
label_teema.grid(row=1, column=0, padx=10, pady=10)

label_lisa=Label(aken, text="LISA:", font=("Poppins", 14), fg="#10226d", image=button_bg_image_2, compound="center")
label_lisa.grid(row=2, column=0, padx=10, pady=10)

label_kiri=Label(aken, text="KIRI:", font=("Poppins", 14),  fg="#10226d", image=button_bg_image_2, compound="center")
label_kiri.grid(row=3, column=0, padx=10, pady=10)


# Отображение добавленного изображения
l_lisatud=Label(aken, text="...", font=("Poppins", 8), width=30, height=1, fg="#10226d", bg="#dae0ee")
l_lisatud.grid(row=2, column=1, padx=5, pady=5, sticky="ew")


# Поля ввода
email_box=Entry(aken, font=("Poppins", 12), width=30, bg="#dae0ee", fg="#10226d")
email_box.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tema_box=Entry(aken, font=("Poppins", 12), width=30, bg="#dae0ee", fg="#10226d")
tema_box.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

kiri_box=Text(aken, font=("Poppins", 12), width=30, height=8, bg="#dae0ee", fg="#10226d")
kiri_box.grid(row=3, column=1, padx=5, pady=5, sticky="ew")


# Кнопки
button_bg=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\bg.png")
button_bg_resized = button_bg.resize((145, 50)) 
button_bg_image = ImageTk.PhotoImage(button_bg_resized)

rida=Frame(aken)
rida.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

button1=Button(rida, text = "LISA PILT", font=("Poppins", 14, "bold"), command=vali_pilt, image=button_bg_image, compound="center", fg="white")
button1.grid(row=4, column=1, padx=(100, 5), pady=5, sticky="ew")

button2=Button(rida, text = "SAADA", font=("Poppins", 14, "bold"), command=saada_kiri, image=button_bg_image, compound="center", fg="white")
button2.grid(row=4, column=2, padx=(20, 5), pady=5, sticky="ew")


aken.mainloop()