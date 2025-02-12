from random import *

def failist_to_dict(f: str):
    riik_pealinn = {}  # sõnastik {"Riik": "Pealinn"}
    pealinn_riik = {}  # sõnastik {"Pealinn": "Riik"}
    riigid = []  # järjend, kus talletakse riigide nimetused
   
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')  # k-võti, v-väärtus
        riik_pealinn[k] = v  # täidame riik_pealinn
        pealinn_riik[v] = k  # täidame pealinn_riik
        riigid.append(k)
    file.close()
   
    return riik_pealinn, pealinn_riik, riigid


def failisse_lisamine(riik,pealinn):
    f=open(f,'w',encoding="utf-8-sig")
    for element in riik,pealinn:
        f.write(f"{riik}-{pealinn}")
    f.close()

    