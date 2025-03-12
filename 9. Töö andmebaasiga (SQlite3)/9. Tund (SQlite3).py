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

def execute_read_query(connection, query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")

# create_users_table="""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     gender TEXT,
#     nationality TEXT
# );
# """

# -----------------------------------
create_gender_table="""
CREATE TABLE IF NOT EXISTS gender (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nimetus TEXT NOT NULL);
"""
insert_gender="""
INSERT INTO gender(Nimetus)
VALUES 
('mees'),
('naine')
"""
create_users_table2="""
CREATE TABLE IF NOT EXISTS users2 (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lname TEXT NOT NULL,
Age TEXT NOT NULL,
GenderId INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender (Id)
);
"""
insert_users2="""
INSERT INTO
users2(Name,Lname,Age,GenderId)
VALUES
('Andrei','Mets',24,1),
('Maria','Smolina',28,2),
('Mati','Tamm',50,1)
"""

select_users2="SELECT * from users2"
select_users2_gender="""
SELECT
users2.Name,
users2.Lname,
gender.Nimetus
from users2
INNER join gender ON users2.GenderId=gender.Id
"""

execute_query(conn, create_gender_table)
execute_query(conn, insert_gender)
execute_query(conn, create_users_table2)
execute_query(conn, insert_users2)
users2=execute_read_query(conn, select_users2)
print("\nKasutajate tabel 1:")
for user in users2:
    print(user)
gender=execute_read_query(conn, select_users2_gender)
print("\nKasutajate tabel 2:")
for gender in gender:
    print(gender)
#------------------------------------------------


# create_users="""
# INSERT INTO
#     users (name, age, gender, nationality)
# VALUES
# ('Mati', 25, 'mees', 'USA'),
# ('Lidia', 32, 'naine', 'France'),
# ('Brigitte', 35, 'naine', 'England'),
# ('Mike', 40, 'mees', 'Denmark'),
# ('Elizabeth', 21, 'naine', 'Eesti');
# """

# execute_query(conn, create_users_table)

# execute_query(conn, create_users)

# select_users="SELECT * from users"

# users=execute_read_query(conn, select_users)
# for user in users:
#     print(user)

def add_users_query(connection,user_data):
    """Lisame userit, mis on eraldi sisestatud
    """
    query="INSERT INTO users(name,age,gender,nationality) VALUES(?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

# insert_user=(input("Nimi: "),int(input("Vanus: ")),input("Sugu: "),input("Riik: "))
# print(insert_user)
# add_users_query(conn,insert_user)

def delete_data_from_tabel(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}' andemete kustutamisega")

# print("Andemete kustutamine tabelist 'users'")
# delete_data_from_users="DELETE FROM users WHERE age<30"
# delete_data_from_tabel(conn,delete_data_from_users)
# print("Tabelis 'users' on jäänud neid kes vanem kui 30:")
# users=execute_read_query(conn,select_users)

# for user in users:
#     print(user)

