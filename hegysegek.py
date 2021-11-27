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

bekeres = int(input("6.feladat: Kérek egy magassági értéket:\t"))


kereso1 = [sor.magassag for sor in lista if bekeres > legmagasabb]
if len(kereso1) > 0:
    print(f"6.feladat: Nincs {bekeres}m-nél magasabb hegycsúcs Börzsönyben!")
else:
    print(f"6.feladat: {bekeres} m-nél van magasabb hegység börzsönyben")

#7.feladat___________________________________________________________

haromezer = [sor.hegyseg for sor in lista if sor.magassag * 3.280839895 > 3000]
hany_db_3000 = len(haromezer)

print(f"7.feladat: 3000 lábnál magasabb hegycsúcsok száma: {hany_db_3000}")

#8.feladat___________________________________________________________


stat = dict()
for sor in lista:
    hegyseg = sor.hegyseg
    stat[hegyseg] = stat.get(hegyseg, 0) + 1
print("8:feladat: Hegység statisztika")
for hegyseg,darab in stat.items():
    print(f"     {hegyseg} - {darab} db")

