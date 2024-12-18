#V4 Ülesanne 3
#T sõpra tulid restorani. Sissepääsu juures on robotvalvur ja laseb sisse ainult neid, kes on üle 16 aasta vanad. Tuleb välja selgitada, mitu sõpra saab õhtusöögi.

T=0
vanus=int(input("Sisestage vanus: "))
for i in range(0,T-1,1):
    if vanus>16:
        T+=1
    else:


