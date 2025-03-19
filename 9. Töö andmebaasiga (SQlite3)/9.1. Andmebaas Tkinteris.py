import sqlite3
from os import *
import tkinter as tk
from tkinter import messagebox

create_table="""
CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  director TEXT,
  release_year INTEGER,
  genre TEXT,
  duration INTEGER,
  rating REAL,
  language TEXT,
  country TEXT,
  description TEXT
);
"""

insert_values="""
INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'The A The On The In. By To A At On The. From The In With At In To A.'),
('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'With By In The A On. The With To A At The From. On A From With At By The.'),
('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'English', 'Germany', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
('From The By With.', 'Christopher Nolan', 1960, 'Drama', 134, 8.5, 'English', 'UK', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
('The By On A.', 'Francis Ford Coppola', 1999, 'Thriller', 112, 7.8, 'English', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
('On A The From.', 'Quentin Tarantino', 2015, 'Comedy', 126, 7.9, 'English', 'Italy', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'English', 'France', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
('From With The By.', 'Martin Scorsese', 1980, 'Crime', 163, 9.1, 'English', 'Germany', 'On The A By In The From. With By On A The In From. To The In At By With On A.');
"""

# # Ühenduse loomine 
# try:
#     filename=path.abspath(__file__)
#     dbdir=filename.rstrip('9.1. Andmebaas Tkinteris.py')
#     dbpath=path.join(dbdir,'movies.db')

#     conn = sqlite3.connect(dbpath)  
#     # Loo ühendus andmebaasiga (NB! kui 'movies.db' ei eksisteeri, siis see luuakse)
#     cursor = conn.cursor()  # cursor on oluline päringute tegemisel
#     print("Ühendus loodud")
#     cursor.execute(create_table)
#     cursor.execute(insert_values)
#     conn.commit()

# except sqlite3.Error as error:
#     print("Tekkis viga andmebaasiga ühendamisel:", error)
# finally:
#     if conn:
#         conn.close()  # Ühenduse sulgemine


# # Andmete lugemine
# try:
#     # filename=path.abspath(__file__)
#     # dbdir=filename.rstrip('9.1. Andmebaas Tkinteris (Ühendamine ja lugemine).py')
#     # dbpath=path.join(dbdir,'movies.db')
#     # conn = sqlite3.connect(dbpath)  

#     conn = sqlite3.connect('9. Töö andmebaasiga (SQlite3)/movies.db')
#     cursor = conn.cursor()
#     print("Ühendus loodud")

#     # Teostame päringu, et lugeda kõik andmed tabelist 'movies'
#     cursor.execute("SELECT * FROM movies")
#     rows = cursor.fetchall()

#     # Väljastame kõik loetud read
#     for row in rows:
#         print(row)

# except sqlite3.Error as error:
#     print("Tekkis viga andmebaasiga ühendamisel või päringu teostamisel:", error)
# finally:
#     if conn:
#         conn.close()
#         print("Ühendus suleti")


#puhastab kõik sisestusväljad
def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

# validate_data funktsioon, mis kontrollib kas sisestatud andmed on korrektsed
def validate_data():
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    return True


# valideerib andmed ja lisab need andmebaasi
def insert_data():
    if validate_data():
        connection = sqlite3.connect("9. Töö andmebaasiga (SQlite3)/movies.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entries["Pealkiri"].get(),
            entries["Režissöör"].get(),
            entries["Aasta"].get(),
            entries["Žanr"].get(),
            entries["Kestus"].get(),
            entries["Reiting"].get(),
            entries["Keel"].get(),
            entries["Riik"].get(),
            entries["Kirjeldus"].get()
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
        clear_entries()

# Loo Tkinteri aken
root = tk.Tk()
root.title("Filmi andmete sisestamine")

# Loo sildid ja sisestusväljad
labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
entries = {}

for i, label in enumerate(labels):   
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# Näita Tkinteri akent
root.mainloop()

