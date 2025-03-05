from tkinter import *
from tkinter import filedialog, messagebox, ttk, font
from PIL import Image, ImageTk
import random

def loe_sonad_failist(f:str):
    sonad=[]
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        sonad.append(f)
    file.close()
    
    return sonad

def vali_sona():
    """
    """

def kontrolli_katset():
    """
    """

def varvi_tahed():
    """
    """

def lopeta_mang():
    """
    """

def uus_mang():
    """
    """

def sisestatud_taht():
     if len(sisesta_taht)>1:
        messagebox.showerror("Viga!", "Peab olema üks täht")
        return False
     else:
        return sisesta_taht.upper()



aken=Tk()
aken.geometry("550x800")
aken.resizable(False, False) # Отключает изменение размера окна (Ширина - False, Высота - False)
aken.title("Wordle")

bg=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\tume_bg.jpg")
bg_resized=bg.resize((550, 800)) 
bg_image=ImageTk.PhotoImage(bg_resized)

label_bg=Label(aken, image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)


# # Стили 
style=ttk.Style()
style.configure("TButton", font=("Poppins", 14, "bold"), foreground="black", pady=10, height=40)
style.configure("TLabel", font=("Lilita One", 40, "bold"), foreground="#21006c", background="red", pady=20, width=20, anchor="center", borderwidth=10, relief="groove")
# style.configure("TEntry", font=("Poppins", 40, "bold"), foreground="white", background="darkblue",  width=5, height=5)

pealkiri=ttk.Label(aken,text="WORDLE MÄNG")
pealkiri.pack()

kirjeldus=Label(aken,text="Puuviljad, marjad ja loomad",font=("Lilita One", 18), fg="red", bg="black", justify="center", pady=5)
kirjeldus.pack()

# Поля ввода для букв
sisend=Frame(aken)
sisend.pack()

tahed=[]

for row in range(6):  # 6 рядов
    for column in range(6):   # 5 колонок
        sisesta_taht=Entry(sisend, font=("Poppins", 34, "bold"), fg="white", bg="#21006c",  width=2, justify="center")
        sisesta_taht.grid(row=row, column=column, pady=2, padx=2)  # Размещение в сетке
        tahed.append(sisesta_taht)

# Пустой ряд, чтобы сделать отстпу
tyhi_rida=Frame(aken)

tyhi_rida.pack(pady=10)

nupude_rida=Frame(aken)
nupude_rida.pack()

bg=Image.open(r"8. Graafiline liides (Tkinter ja Matplotlib)\tume_bg.jpg")
bg_resized=bg.resize((545, 80)) 
bg_image_2=ImageTk.PhotoImage(bg_resized)
label_bg2=Label(nupude_rida, image=bg_image_2)
label_bg2.grid(row=0, column=0, columnspan=4)

kontrolli_nupp=ttk.Button(nupude_rida, command=sisestatud_taht, text="Kontrolli", width=10)
kontrolli_nupp.grid(row=0, column=1, pady=5)

uus_nupp=ttk.Button(nupude_rida, text="Uus mäng", width=10)
uus_nupp.grid(row=0, column=2, pady=5)



aken.mainloop()