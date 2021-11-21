'''Hegycsúcs neve;Hegység;Magasság
Ágasvár;Mátra;789                    '''

p2v = lambda x:x.replace('.',',')
class Hegyek:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.hegycsucs_neve = sor[0]
        self.hegyseg = sor[1]
        self.magassag = int(sor[2])

#1-2.feadat____________________________________________________

with open("hegyekMO.txt","r",encoding="utf-8") as f:
    elso_sor = f.readline()
    lista = [Hegyek(sor) for sor in f]
    
#3.feadat____________________________________________________

print(f"3.feladat: Hegycsúcsok száma: {len(lista)} db")

#4.feadat____________________________________________________
 
hegy_atlag_magassag = [sor.magassag for sor in lista ]

ossz = sum(hegy_atlag_magassag)
atlag = ossz / len(lista)
atlag = str(atlag)

print(f"4.feladat: Hegycsúcsok átlagos magassága: {p2v(atlag)} m")

#5.feadat____________________________________________________

legmagasabb = 0
for sor in lista:
    if sor.magassag > legmagasabb:
        legmagasabb = sor.magassag
        nev = sor.hegycsucs_neve
        hegyseg = sor.hegyseg
        mennyiremagas = sor.magassag
        
print(f"""5.feladat: A legmagasabb hegycsúcs adatai:
            Név : {nev}
            Hegység: {hegyseg}
            Magasság: {mennyiremagas} m
            """)

#6.feadat____________________________________________________

               


