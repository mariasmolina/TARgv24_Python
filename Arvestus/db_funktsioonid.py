import sqlite3

conn = sqlite3.connect("Arvestus/AppData/haigla.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS kasutajad (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    kasutajanimi TEXT,
                    parool TEXT,
                    amet TEXT,
                    nimi TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS patsiendid (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    eesnimi TEXT,
                    perekonnanimi TEXT,
                    email TEXT,
                    isikukood TEXT,  
                    kaal REAL,
                    pikkus REAL,
                    ylemineRohk REAL,
                    madalamRohk REAL,
                    temperatuur REAL,
                    kaebus TEXT,
                    dieet TEXT,
                    diagnoos TEXT,
                    registreerimiseAeg TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    palati_nr INT,
                    arst_ID INTEGER,
                    staatus TEXT,
                    kommentaar TEXT,
                    FOREIGN KEY (arst_ID) REFERENCES kasutajad(ID))''')


# # Добавляем данные для входа в систему для врача и медсестры
insert_values="""
INSERT INTO kasutajad (kasutajanimi, parool, amet, nimi) VALUES
("1", "1", "medõde", "Natalja Vassiljeva"),
("arst1", "1234", "arst", "Maria Smolina"),
("arst2", "1234", "arst", "Mart Tamm"),
("arst3", "1234", "arst", "Kadri Mets"),
("arst4", "1234", "arst", "Priit Saar"),
("arst5", "1234", "arst", "Helena Kütt");
"""
# cursor.execute(insert_values)

conn.commit()
conn.close()
