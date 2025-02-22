from tkinter import *
from Ruutvõrrandi_lahendamine_Matplotlib_def import *

# Приложение "Решение квадратного уравнения" https://moodle.edu.ee/mod/assign/view.php?id=832513

def sisend_kontroll():
    """Проверка заполненности всех полей"""
    if sisesta_a.get()=="":
        sisesta_a.configure(bg="red")   # .configure - позволяет обновить атрибуты виджета, такие как текст, цвет, размер и т.д.
    else:
        sisesta_a.configure(bg="lightblue")
    if sisesta_b.get()=="":
        sisesta_b.configure(bg="red")
    else:
        sisesta_b.configure(bg="lightblue")
    if sisesta_c.get()=="":
        sisesta_c.configure(bg="red")
    else:
        sisesta_c.configure(bg="lightblue")

def lahenda():
    try:
        sisend_kontroll()

        a=float(sisesta_a.get())
        b=float(sisesta_b.get())
        c=float(sisesta_c.get())

        tulemus.configure(text=(funktsiooni_lahendamine(a,b,c))) 
    except:
        tulemus.configure(text="Введите число!")

def graafik():
    try:
        sisend_kontroll()

        a=float(sisesta_a.get())
        b=float(sisesta_b.get())
        c=float(sisesta_c.get())

        funktsiooni_graafik(a,b,c)
    except:
        tulemus.configure(text="Введите число!")

# Создание окна
aken=Tk()
aken.geometry("550x200")
aken.title("Квадратные уравнения")

# Заголовок
pealkiri=Label(aken,text="Решение квадратного уравнения",font="Calibri 24",fg="green",bg="lightblue")

# Frame - контейнер для других виджетов, позволяет группировать несколько виджетов вместе, а также управлять их расположением и организацией в окне.
teine_rida=Frame(aken)  

# Поля для ввода коэффициентов
sisesta_a=Entry(teine_rida,font="Calibri 20",fg="green",bg="lightblue",width=3)
sisesta_b=Entry(teine_rida,font="Calibri 20",fg="green",bg="lightblue",width=3)
sisesta_c=Entry(teine_rida,font="Calibri 20",fg="green",bg="lightblue",width=3)

# Текст между полями ввода коэффициентов
tekst1=Label(teine_rida, text="x**2+",font="Calibri 20",fg="green")
tekst2=Label(teine_rida,text="x+",font="Calibri 20",fg="green")
tekst3=Label(teine_rida, text="=0",font="Calibri 20",fg="green")

# Кнопки для решения квадратного уравнения и для рисования графика функции
lahenda_nupp=Button(teine_rida,text="Решить",command=lahenda,font="Calibri 20",bg="green",fg="black",width=7,pady=1)
graafik_nupp=Button(teine_rida,text="График",command=graafik,font="Calibri 20",bg="green",fg="black",width=7,pady=1)

# Поле для вывода результата
tulemus=Label(aken,font="Calibri 12",text="Решение",bg="yellow",width=50,height=5)

# Расположение
pealkiri.pack()
teine_rida.pack(pady=10)
sisesta_a.grid(row=0, column=0)   # grid(row=...,column=...) - сетка
tekst1.grid(row=0,column=1)
sisesta_b.grid(row=0,column=2)
tekst2.grid(row=0,column=3)
sisesta_c.grid(row=0, column=4)
tekst3.grid(row=0,column=5)
lahenda_nupp.grid(row=0,column=6)
graafik_nupp.grid(row=0,column=7)
tulemus.pack()

aken.mainloop()