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
                    ylemine_rohk REAL,
                    madalam_rohk REAL,
                    temperatuur REAL,
                    kaebus TEXT,
                    dieet TEXT,
                    diagnoos TEXT,
                    registreerimise_aeg TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    palati_nr INT,
                    arst_ID INTEGER,
                    staatus TEXT,
                    kommentaar TEXT,
                    FOREIGN KEY (arst_ID) REFERENCES kasutajad(ID))''')


# Добавляем данные для входа в систему для врача и медсестры
insert_values="""
INSERT INTO kasutajad (kasutajanimi, parool, amet, nimi) VALUES
("nurse1", "1234", "medõde", "Natalja Vassiljeva"),
("arst1", "1234", "arst", "Maria Smolina"),
("arst2", "1234", "arst", "Mart Tamm"),
("arst3", "1234", "arst", "Kadri Mets"),
("arst4", "1234", "arst", "Priit Saar"),
("arst5", "1234", "arst", "Helena Kütt");
"""

insert_parsiendi_andmed="""
INSERT INTO patsiendid (eesnimi, perekonnanimi, email, isikukood, kaal, pikkus, ylemine_rohk, madalam_rohk, temperatuur, kaebus, dieet, diagnoos, registreerimise_aeg, palati_nr, arst_ID, staatus, kommentaar) VALUES
("Jaan", "Tamm", "jaan.tamm@naidis.ee", "30303039914", 75.0, 180.0, 120.0, 80.0, 36.6, "Peavalu", "Diabeetiline", "Tundmatu", "2025-03-28 09:36:10", 4, 2, "Ootab arsti läbivaatust", NULL),
("Liis", "Jõgi", "liis.jogi@naidis.ee", "40404049996", 65.0, 165.0, 110.0, 70.0, 37.0, "Köha", "Laktoosivaba", "Kopsupõletik", "2025-03-20 08:37:42", 2, 2, "Arsti poolt läbivaadatud", "Raviplaan: Verekultuuride võtmine, antibiootikumravi, hapnikravi ning intravenoosne vedelikuravi."),
("Alice", "Johanson", "alice.johanson@naidis.ee", "40404049985", 58.0, 170.0, 115.0, 68.0, 36.9, "Väsimus", "Baasdieet", "Tundmatu", "2025-03-24 15:34:05", 2, 3, "Ootab arsti läbivaatust", NULL),
("Karin", "Kallavus", "karin.kallavus@naidis.ee", "40504040001", 85.0, 175.0, 125.0, 75.0, 36.7, "Rinnavalu", "Diabeetiline", "Äge südameinfarkt", "2025-03-27 13:28:29", 2, 4, "Arsti poolt läbivaadatud", "Raviplaan: EKG, südame markerite määramine, trombolüüsravi, hingamisaparaadi kasutamine ja intensiivravi."),
("Hanna", "Mets", "hanna.mets@naidis.ee", "61101012257", 90.0, 160.0, 130.0, 85.0, 37.2, "Hingamisraskused", "Laktoosivaba", "Tundmatu", "2025-03-31 08:35:34", 2, 2, "Ootab arsti läbivaatust", NULL),
("David", "Martinson", "david.martinson@naidis.ee", "30303039816", 70.0, 180.0, 120.0, 80.0, 36.8, "Seljavalu", "Baasdieet", "Lülisamba kompressioonmurd", "2025-03-22 10:11:22", 6, 6, "Arsti poolt läbivaadatud", "Raviplaan: Kompressioonimurru röntgen, stabiliseerimine, valuvaigistite manustamine ning operatiivne sekkumine kui vajalik."),
("Eve", "Lind", "eve.lind@naidis.ee", "49912318881", 55.0, 160.0, 100.0, 60.0, 37.1, "Palavik", "Baasdieet, Diabeetiline", "Tundmatu", "2025-04-01 18:36:43", 3, 4, "Ootab arsti läbivaatust", NULL),
("Frank", "Wilson", "frank.wilson@naidis.ee", "50001029996", 80.0, 170.0, 120.0, 75.0, 37.0, "Kurguvalu", "Laktoosivaba", "Mandlite mädapõletik", "2025-03-26 14:25:40", 4, 5, "Arsti poolt läbivaadatud", "Raviplaan: Kõrge palaviku alandamine, antibiootikumravi intravenoosselt, mandlite kirurgiline eemaldamine vajalik."),
("Ants", "Tamm", "grete.lopez@naidis.ee", "30303039903", 72.0, 165.0, 110.0, 72.0, 36.9, "Kõhuvalu", "Diabeetiline", "Tundmatu", "2025-03-29 12:32:15", 5, 3, "Ootab arsti läbivaatust", NULL),
("Robert", "Pruul", "robert.pruul@naidis.ee", "51501017721", 77.0, 175.0, 115.0, 80.0, 37.3, "Iiveldus", "Baasdieet", "Äge maksapuudulikkus", "2025-04-01 09:45:10", 5, 3, "Arsti poolt läbivaadatud", "Raviplaan: Maksafunktsiooni testid, intravenoosne toitmine, hemodialüüs ning vajadusel maksa siirdamine.");
"""

# cursor.execute(insert_values)
# cursor.execute(insert_parsiendi_andmed)

conn.commit()
conn.close()
