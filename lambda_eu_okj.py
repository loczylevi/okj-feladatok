#Ausztria;1995.01.01
class Eu:
  def __init__(self,sor):
    sor = sor.strip().split(";")
    self.orszag = sor[0]
    self.ev = int(sor[1][:4])
    self.honap = sor[1][5:7]
    self.nap = int(sor[1][8:10])
    self.datum = sor[1]

with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
  lista = [Eu(sor) for sor in f]

#3
  
print(f"3.feladat: Eu tagállamainak száma: {len(lista)} db")

#4

csatlakozas = [sor.orszag for sor in lista if sor.ev == 2007]

print(f"4.feladat: 2007-ben {len(csatlakozas)} ország csatlakozott")

#5

magyar = [sor.datum for sor in lista if sor.orszag == "Magyarország"]

print(f"5.feladat: Magyarország csatlakozás dátuma: {magyar[0]}")

#6
kereso_majus = [sor.honap for sor in lista if sor.honap == "05"]

if len(kereso_majus) > 0:
  print("6.feladat: Májusban volt csatlakozás!")
else:
  print("6.feladat: Májusban nem volt csatlakozás!")

#7
"""
datumok = [sor.ev for sor in lista]
legutcso = datumok[0]

for sor in lista:
  if sor.ev > legutcso:
    legutcso = sor.ev
    orszag = sor.orszag
"""


def macska(x):
  return x.datum

utolso_orszag1 = max(lista, key = lambda x:x.datum).orszag
utolso_orszag2 = max(lista, key = macska).orszag

#print(utolso_orszag1)
#print(utolso_orszag2)

print(f"7.feladat: Legutoljára csatlakozott ország: {utolso_orszag2}")

#8

stat = dict()

for sor in lista:
  ev = sor.ev
  stat[ev] = stat.get(ev, 0) + 1
print("8:feladat: Statisztika")
for ev,darab in stat.items():
    print(f"     {ev} - {darab} ország")

