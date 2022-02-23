"""hazai;idegen;hazai_pont;idegen_pont;
helyszín;időpont"""
class Kosar:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.hazai = sor[0]
        self.idegen = sor[1]
        self.hazai_pont = int(sor[2])
        self.idegen_pont = int(sor[3])
        self.helyszin = sor[4]
        self.idopont = sor[5]
with open("eredmenyek.csv","r",encoding="latin2") as f:
    fejléc = f.readline()
    lista = [Kosar(sor) for sor in f]
    
#3.feladat
szamlalo_hazai = [sor.hazai_pont for sor in lista if sor.hazai == "Real Madrid" ]
szamlalo_idegen = [sor.idegen_pont for sor in lista if sor.idegen == "Real Madrid" ]
print(f"3.feladat: Real Madrid: Hazai: {len(szamlalo_hazai)}, Idegen: {len(szamlalo_idegen)}")

#4.feladat
dontetlen = [sor for sor in lista if sor.idegen_pont == sor.hazai_pont]
if len(dontetlen) > 0:
    print("4.feladat: Volt döntetlen igen")
else:
    print("4.feladat: Volt döntetlen nem")
    
#5.feladat
kereso = [sor.hazai for sor in lista if "Barcelona" in sor.hazai]
print(f'5. feladat: barcelonai csapat neve: {kereso[0]}')

#6.feladat
kereso2 = [sor for sor in lista if sor.idopont == "2004-11-21"]
print( f'6. feladat:')
[print(f'        {sor.hazai}-{sor.idegen} ({sor.hazai_pont}:{sor.idegen_pont})') for sor in kereso2]
    
