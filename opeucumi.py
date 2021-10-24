'''Ausztria;1995.01.01'''
class EUtagallamok:
    def __init__(self, sor):
        s = sor.strip().split(";")
        self.orszag = s[0]
        self.ev = s[1][0:4]
        self.honap = s[1][5:7]
        self.nap = s[8:10]
        self.full_datum = s[1][0:10]
       

#1-2. feladat _______________________________________________________________

with open("EUcsatlakozas.txt","r") as f:
    #fejléc = f.readline().strip().split(';')
    lista = [ EUtagallamok(sor) for sor in f ]
    
#3. feladat _______________________________________________________________
        
versenyzok_szama = len(lista)
print(f"3. feladat: EU agállamainak száma {versenyzok_szama} db.")

#4. feladat _______________________________________________________________

szamlalo = 0
for sor in lista:
    if sor.ev == "2007":
        szamlalo += 1

print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott")

#5. feladat _______________________________________________________________
tarolt = ""
for sor in lista:
    if sor.orszag == "Magyarország":
        tarolt = sor.full_datum
        
print(f"5.feladat: Magyarország csatlakozási dátuma: {tarolt}")

#6. feladat _______________________________________________________________
majus = False
for sor in lista:
    if sor.honap == "05":
        szamlalo = True
        
if majus:
    print(f"6.feladat: Májusban volt csatlakozás!")


#7. feladat _______________________________________________________________


utoljara = ""
for sor in lista:
    if sor.ev > utoljara:
        utoljara = sor.ev
        orszag1 = sor.orszag
     
print(f"7.feladat A legutoljára csatlakozott ország: {orszag1}")


    

