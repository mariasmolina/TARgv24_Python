from tkinter import *
from Tund_9_Matplotlib_def import *

def figuur():
    valik=var.get()
    if valik==1:
        Vaal()
    elif valik==2:
        Liblikas()
    else:
        Prillid()
        print("Joonestan hiljem")

aken=Tk()
aken.geometry("800x400")  # Задаем размер
aken.title("Graafikud")
pealkiri=Label(aken,text="Erinevad piltid Matplotlib abil",font="Poppins 24",fg="purple",bg="cyan", pady=20, width=200)

var=IntVar()
r1=Radiobutton(aken,text="Vaal",font="Poppins 18",variable=var,value=1,command=figuur)
r2=Radiobutton(aken,text="Liblikas",font="Poppins 18",variable=var,value=2,command=figuur)
r3=Radiobutton(aken,text="Prillid",font="Poppins 18",variable=var,value=3,command=figuur)

pealkiri.pack()
r1.pack()
r2.pack()
r3.pack()

aken.mainloop()

