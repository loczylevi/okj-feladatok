#év;típus;keresztnév;vezetéknév

#2017;fizikai;Rainer;Weiss

#1-2

class Nobel_dijak:
  def __init__(self,sor):
    ev,tipus,kereszt,vezetek = sor.strip().split(";")
    self.ev = int(ev)
    self.tipus = tipus
    self.kereszt = kereszt
    self.vezetek = vezetek

with open("nobel.csv","r",encoding="utf8") as f:
  fejlec = f.readline()
  lista = [Nobel_dijak(sor) for sor in f]

#3

kereso = [sor.tipus for sor in lista if sor.vezetek == "McDonald"][0]

print(f"3.feladat: {kereso}")

#4

irodalmi = [sor.kereszt for sor in lista if sor.ev == 2017 and sor.tipus == "irodalmi"][0]

irodalmi2 = [sor.vezetek for sor in lista if sor.ev == 2017 and sor.tipus == "irodalmi"][0]

print(f"4.feladat: {irodalmi} {irodalmi2}")

#5

beke = [sor for sor in lista if sor.ev > 1990 and sor.tipus == "béke" and sor.vezetek == ""]
print("5.feladat:")
[print(f"       {sor.ev}: {sor.kereszt}") for sor in beke]

#6

curie = [sor for sor in lista if "Cuire" in sor.kereszt or "Curie" in sor.vezetek]
print("6.feladat:")
[print(f"         {sor.kereszt} {sor.vezetek}({sor.tipus})") for sor in curie]

stat = dict()
print("7.feladat: ")
for sor in lista:
  tipus = sor.tipus
  stat[tipus] = stat.get(tipus,0) + 1
for tipus,darab in stat.items():
  print(f"         {tipus} - {darab} db.")
