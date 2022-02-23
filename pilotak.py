#név;születési_dátum;nemzetiség;rajtszám

class Pilotak():
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.nev = sor[0]
        self.szuletesi_datum = sor[1]
        self.nemzetiseg = sor[2]
        self.rajtszam = sor[3]
        self.ev = int(sor[1][0:4])
        
with open("pilotak.csv","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Pilotak(sor) for sor in f]
#3.feladat
print(f"3.feladat: {len(lista)}")

#4.feladat
pilotak = [sor.nev for sor in lista]
print(f"3.feladat: {pilotak[-1]}")
#5.feladat

kereso = [sor for sor in lista if sor.ev < 1901]
print("5.feladat")
[print(f"       {sor.nev} ({sor.szuletesi_datum})")for sor in kereso]

#6.feladat
rajtszam = [int(sor.rajtszam) for sor in lista if sor.rajtszam != ""]
nemzetiseg = ""
kicsi = rajtszam[0]
for sor in lista:
    if sor.rajtszam != "":
        if int(sor.rajtszam) < kicsi:
            kicsi = int(sor.rajtszam)
            nemzetiseg = sor.nemzetiseg

print(f"6.feladat: {nemzetiseg}")
    
#7.feladat
rajtszam2 = [int(sor.rajtszam) for sor in lista if sor.rajtszam != ""]

statisztika = dict()
print("7.feladat:")
for sor in rajtszam2:
    rajtszam = sor
    statisztika[rajtszam] = statisztika.get(rajtszam, 0) + 1
y = [ print(f' {rajtszam},',end="") for rajtszam, db in statisztika.items() if db > 1]
