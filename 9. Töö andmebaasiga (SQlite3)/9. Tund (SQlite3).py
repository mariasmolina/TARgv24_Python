from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

conn=create_connection("9. Töö andmebaasiga (SQlite3)/AppData/data.db")

def execute_query(connection, query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Viga '{e}' tabeli loomisega")

create_users_table="""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

execute_query(conn, create_users_table)


create_users="""
INSERT INTO
    users (name, age, gender, nationality)
VALUES
('Mati', 25, 'mees', 'USA'),
('Lidia', 32, 'naine', 'France'),
('Brigitte', 35, 'naine', 'England'),
('Mike', 40, 'mees', 'Denmark'),
('Elizabeth', 21, 'naine', 'Eesti');
"""

def execute_read_query(connection, query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")

execute_query(conn, create_users)

select_users="SELECT * from users"

users=execute_read_query(conn, select_users)
for user in users:
    print(user)

def add_users_query(connection,user_data):
    """Lisame userit, mis on eraldi sisestatud
    """
    query="INSERT INTO users(name,age,gender,nationality) VALUES(?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

insert_user=(input("Nimi: "),int(input("Vanus: ")),input("Sugu: "),input("Riik: "))
print(insert_user)
add_users_query(conn,insert_user)

def delete_data_from_tabel(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}' andemete kustutamisega")

print("Andemete kustutamine tabelist 'users'")
delete_data_from_users="DELETE FROM users WHERE age<30"
delete_data_from_tabel(conn,delete_data_from_users)
print("Tabelis 'users' on jäänud neid kes vanem kui 30:")
users=execute_read_query(conn,select_users)

for user in users:
    print(user)