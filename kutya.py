#id	fajta_id	név_id	életkor	utolsó orvosi ellenőrzés ---> kutyak.csv
#_______________________________________________________________________

class Kutyak:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.id = int(sor[0])
        self.fajta_id = int(sor[1])
        self.nev_id = int(sor[2])
        self.eletkor = int(sor[3])
        self.ut_orvosi = sor[4]
        

with open('Kutyak.csv', 'r', encoding='utf-8-sig') as f:
    elso = f.readline()
    kutya_lista = [Kutyak(sor) for sor in f]
    
#id	kutyanév ---> KutyaNevek.csv
#________________________________________________________________________
    
class Kutya_nevek:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.id = int(sor[0])
        self.kutyanev = str(sor[1])
        
with open('KutyaNevek.csv', 'r', encoding='utf-8-sig') as f:
    elso2 = f.readline()
    kutya_nevek = [Kutya_nevek(sor) for sor in f]
    
#id	név	eredeti_név ---> KutyaFajtak.csv 
#________________________________________________________________________

    
class Kutya_fajtak:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.id = int(sor[0])
        self.nev = (sor[1])
        self.eredeti_nev = sor[2]

with open('KutyaFajtak.csv', 'r', encoding='utf-8-sig') as f:
    elso3 = f.readline()
    kutya_fajtak = [Kutya_fajtak(sor) for sor in f]


print(f"3:feladat: kutyanevek száma: {len(kutya_nevek)} db")

eletkor = [ sor.eletkor for sor in kutya_lista ]
ossz = sum(eletkor)
atlag = ossz / len(kutya_lista)

print(f"6:feladat: kutyák átlag életkora: {atlag:.2f}")

legidosebb = [(sor.eletkor,sor.fajta_id,sor.nev_id) for sor in kutya_lista ]
legidosebb2, fajta, nev = max(legidosebb)


nev = [sor.kutyanev for sor in kutya_nevek if nev == sor.id]
fajta = [sor.nev for sor in kutya_fajtak if fajta == sor.id]

print(f"7.feladat: legidosebb kutya neve és fajtája: {nev[0]} { fajta[0]}")

 



