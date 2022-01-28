'''Csapat;Helyezes;Valtozas;Pontszam'''

#1-2.feladat______________________________________________________

class Fifa:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.csapat = str(sor[0])
        self.helyezes = int(sor[1])
        self.valtozas = int(sor[2])
        self.pontszam = int(sor[3])
        
#1-2.feladat:____________________________________________
        
with open("fifa.txt","r",encoding="latin2") as f:
    f.readline()
    lista = [Fifa(sor) for sor in f]
    

#3.feladat:________________________________________________

print(f"3.feladat: A világranglistán {len(lista)} csapat szerepel")

#4.feladat:________________________________________________

pontszam = [sor.pontszam for sor in lista]
osszpont = sum(pontszam)
atlag = osszpont / len(lista)

print(f"4.feladat: A csapatok átlagos pontszáma: {atlag:.2f} pont")
