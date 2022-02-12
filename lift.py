"""
with open("lift.txt","r",encoding="latin2") as f:
  lista = []
  for sor in f:
    lista.append(sor.strip().split(" "))

#3.feladat

print(f"3.feladat: Összes lift használat: {len(lista)}")

#4. feladat

print(f"4.feladat: Időszak: {lista[0][0]} - {lista[-1][0]}") 

#5. feladat

celszint = [int(sor[3]) for sor in lista]
legnagy = max(celszint)
print(f"5. feladat: Célszint max: {legnagy}")


#6. feladat
print("6.feladat:")
try:
  bekeres = input("     Kártya szám: ")
  bekeres2 = input("       Célszint szám: ")
  bekeres = int(bekeres)
  bekeres2 = int(bekeres2)
except ValueError:
      bekeres = 5
      bekeres2 = 5

#7. feladat
kereso = [sor for sor in lista if bekeres == sor[1] and bekeres2 == sor[3]]
if len(kereso) > 0:
  print(f"A(z) {bekeres}. kártyával utaztak a(z) {bekeres2}. emeletre")
else:
  print(f"A(z) {bekeres}. kártyával nem utaztak a(z) {bekeres2}. emeletre")


"""

#Használat ido, kartya sorszam,indulo es a celsorcelszam,


class Lift:
  def __init__(self,sor):
    sor = sor.strip().split(" ")
    self.ido = sor[0]
    self.kartyaszam = int(sor[1])
    self.indulo = int(sor[2])
    self.cel = int(sor[3])



with open("lift.txt","r",encoding="latin2") as f:
  lista = [Lift(sor) for sor in f]  

#3.feladat

print(f"3.feladat: Összes lift használat: {len(lista)}")

#4. feladat
datumok = [sor.ido for sor in lista]

print(f"4.feladat: Időszak: {datumok[0]} - {datumok[-1]}") 

#5. feladat

celszint = [sor.cel for sor in lista]
legnagy = max(celszint)
print(f"5. feladat: Célszint max: {legnagy}")

#6. feladat
print("6.feladat:")
try:
  bekeres = input("     Kártya szám: ")
  bekeres2 = input("       Célszint szám: ")
  bekeres = int(bekeres)
  bekeres2 = int(bekeres2)
except ValueError:
      bekeres = 5
      bekeres2 = 5

#7. feladat
kereso = [sor for sor in lista if bekeres == sor.kartyaszam and bekeres2 == sor.cel]
if len(kereso) > 0:
  print(f"A(z) {bekeres}. kártyával utaztak a(z) {bekeres2}. emeletre")
else:
  print(f"A(z) {bekeres}. kártyával nem utaztak a(z) {bekeres2}. emeletre")

#8. feladat

stat = dict()
for sor in lista:
    ido = sor.ido
    stat[ido] = stat.get(ido, 0) + 1
print("8:feladat: Statisztika")
for ido,darab in stat.items():
    print(f"     {ido} - {darab}x")







