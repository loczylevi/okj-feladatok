'''Helyezes;Nev;Orszag;Nyeremeny'''


class Snooker:
    def __init__(self,sor):
        sor = sor.strip().replace(".",",").split(";")
        self.Helyezes = int(sor[0])
        self.nev = str(sor[1])
        self.orszag = str(sor[2])
        self.nyer = int(sor[3])

#1-2.feladat:_________________________________________________________________________________

with open("snooker.txt","r",encoding="latin2") as f:
    elsosor= f.readline()
    lista = [Snooker(sor) for sor in f]
    
        
#3.feladat:_________________________________________________________________________________

print(f"3.feladat: A világranglistán {len(lista)} versenyző szerepel")

#4.feladat:_________________________________________________________________________________

ossz = [ sor.nyer for sor in lista ]
atlag = sum(ossz)
atlag2 = atlag / len(ossz)

print(f"4.feladat: A versenyzok átlagosan {atlag2:.2f} fontot kerestek")

kinaiak = [(sor.nyer,sor )for sor in lista if sor.orszag == "Kína"]
kinaiak2, adatok = max(kinaiak)
forint = kinaiak2 * 380

print("5.feladat:lejobban kereső kinai játékos:")
print(f'''
            helyezés: {adatok.Helyezes}
            Név: {adatok.nev}
            Ország: {adatok.orszag}
            nyeremény: {adatok.nyer}
            Nyeremény összege: {forint} Ft''')

norveg = [sor for sor in lista if sor.orszag == "Norvégia"]

if len(norveg) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')

 
