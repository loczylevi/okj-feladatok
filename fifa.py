'''Csapat;Helyezes;Valtozas;Pontszam'''

#1-2.feladat______________________________________________________

class Fifa:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.csapat = (sor[0])
        self.helyezes = int(sor[1])
        self.valtozas = int(sor[2])
        self.pontszam = int(sor[3])
        
#1-2.feladat:____________________________________________
        
with open("fifa.txt","r",encoding="latin2") as f:
    fejléc = f.readline().strip().split(';')
    lista = [Fifa(sor) for sor in f]
    

#3.feladat:________________________________________________

print(f"3.feladat: A világranglistán {len(lista)} csapat szerepel")

#4.feladat:________________________________________________

pontszam = [sor.pontszam for sor in lista]
osszpont = sum(pontszam)
atlag = osszpont / len(lista)

print(f"4.feladat: A csapatok átlagos pontszáma: {atlag:.2f} pont")

#5.feladat:________________________________________________

#valtozas = [ sor.valtozas for sor in lista ]
#legtobb = max(valtozas)
legkisebb = 0
for sor in lista:
    if sor.valtozas > legkisebb:
        legkisebb = sor.valtozas
        helyezes = sor.helyezes
        csapat = sor.csapat
        pontszam = sor.pontszam
        
print(f'''
5. feladat: A legtöbbet javító csapat:
        Helyezés: {helyezes}
        Csapat: {csapat}
        Pontszám : {pontszam}
''')

#6.feladat:________________________________________________

magyarorszag = [sor for sor in lista if sor.csapat =="Magyarország"]

if magyarorszag:
    print("6.feladat: A csapatok között van Magyarország")
else:
    print("6.feladat: A csapatok között nincs Magyarország")
    
#7.feladat:________________________________________________

























