from datetime import *



täna=date.today()

print(f"Tere! Täna on {täna}\n")

tänaf=date.today().strftime("%B %d, %Y")  #nimetus() - funktsioon
print(f"Tere! Täna on {täna}")

d=täna.day  #nimetus - omadus
m=täna.month
y=täna.year
print(d)
print(m)
print(y)