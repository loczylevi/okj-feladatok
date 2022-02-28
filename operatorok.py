#500 mod 265

class Operatorok:
  def __init__(self,sor):
    sor = sor.strip().split(" ")
    self.elso_operator = int(sor[0])
    self.szoveg = sor[1]
    self.masodik_operator = int(sor[2])

with open("kifejezesek.txt","r",encoding="latin2") as f:
  lista = [Operatorok(sor) for sor in f]

#2

print(f"2.feladat: kifejezések száma: {len(lista)}")

#3

mod = [sor.szoveg for sor in lista if sor.szoveg == "mod"]

print(f"3.feladat: Kifejezések maradékos osztással: {len(mod)}")

#4 alternativ megoldás
"""

oszthato_10 = [sor for sor in lista if sor.elso_operator % 10 == 0 and sor.masodik_operator % 10 == 0]

if len(oszthato_10) > 0:
  print("Van ilyen kifejezés!")
else:
    print("Nincs ilyen kifejezés!")
"""
#4

volt_e = False

for sor in lista:
  if sor.elso_operator % 10 == 0 and sor.masodik_operator % 10 == 0:
    volt_e = True
    break

if volt_e:
  print("Van ilyen kifejezés!")
else:
  print("Nincs ilyen kifejezés!")

#5 

stat = dict()
for sor in lista:
  if sor.szoveg == "+" or sor.szoveg == "-" or sor.szoveg == "*" or sor.szoveg == "/" or sor.szoveg == "div" or sor.szoveg == "mod":
    szoveg = sor.szoveg
    stat[szoveg] = stat.get(szoveg, 0) + 1
print("5.feladat: statisztika")
for szoveg,darab in stat.items():
    print(f"     {szoveg} -> {darab} db")

#6
bekeres = input("7.feladat: Kérek egy kifejezést (Pl: 1 + 1): ")

