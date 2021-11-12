"""taxi_id indulas	idotartam	tavolsag	viteldij	borravalo	fizetes_modja"""
class Fuvar:
    def __init__(self, sor):
        s = sor.strip().replace(",",".").split(";")
        self.taxi_id = int(s[0])
        self.indulas = str(s[1])
        self.idotartam = int(s[2])
        self.tavolsag = float(s[3])
        self.viteldij = float(s[4])
        self.borravalo = float(s[5])
        self.fizetes_modja = str(s[6])
        
#1.-2.feladat_________________________________________________    
with open("fuvar.csv", "r", encoding="UTF-8") as f:
    elsosor = f.readline()
    lista = [ Fuvar(sor) for sor in f ]

#3.feladat____________________________________________________

print(f"3.feladat: {len(lista)} fuvar")
#4.feladat____________________________________________________

negyedik = [sor.viteldij + sor.borravalo for sor in lista if sor.taxi_id=="6185"]
print(sum(negyedik))      
