# https://infojegyzet.hu/vizsgafeladatok/okj-programozas/rendszeruzemelteto-210511/

"""Név;Neme;Részleg;Belépés;Bér"""

class Berek2020:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.nev = sor[0]
        self.neme = sor[1]
        self.reszleg = sor[2]
        self.belepes = int(sor[3])
        self.ber = int(sor[4])
        
#  1-2.feladat________________________________________________________

with open("berek2020.txt", "r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Berek2020(sor) for sor in f]
    
#3.feladat____________________________________________________________
    
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")

#4.feladat____________________________________________________________

ossz = [sor.ber for sor in lista ]
atlag = sum(ossz)
atlag2 = atlag / len(lista)
eredmeny = atlag2 / 1000
ere = f"{eredmeny:.1f}".replace(".",",")
print(f"4.feladat: Bérek átlaga: {ere} eFt")

#5.feladat____________________________________________________________

bekeres = input("5.feladat: Kérem egy részleg nevét: ")

#6.feladat____________________________________________________________

try:
    
    fizetes = [(sor.ber, sor) for sor in lista if bekeres == sor.reszleg]
    nagyobb, adatok = max(fizetes)

    if len(fizetes) > 0:
        print(f'''
6.feladat: A legtöbbet kereső a megadott részlegen:
       Név: {adatok.nev}
       Neme: {adatok.neme}
       Belépés: {adatok.belepes}
       Bér: {nagyobb} Forint''')
    else:
        print("6.feladat: A megadott részleg nem létezik a cégnél!")
except:
    print("6.feladat: A megadott részleg nem létezik a cégnél")

#7.feladat____________________________________________________________
    

stat = dict()
for sor in lista:
    reszleg = sor.reszleg
    stat[reszleg] = stat.get(reszleg, 0) + 1
print("7:feladat: statisztika")
for reszleg,darab in stat.items():
    print(f"     {reszleg} - {darab} fő")

