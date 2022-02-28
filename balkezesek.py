#n�v;els�;utols�;s�ly;magass�g
#Jim Abbott;1989-04-08;1999-07-21;200;75

class Balkezesek:
  def __init__(self,sor):
    sor = sor.strip().split(";")
    self.nev = sor[0]
    self.elso = sor[1]
    self.utolso = sor[2]
    self.suly = int(sor[3])
    self.magassag = int(sor[4])

with open("balkezesek.csv","r",encoding="latin2") as f:
  fejlec = f.readline()
  lista = [Balkezesek(sor) for sor in f]

#3
print(f"3.feladat: {len(lista)}")

#4
print("4.feladat:")
kereso = [sor for sor in lista if sor.utolso[:7] == '1999-10']
[print(f"     {sor.nev} {sor.magassag*2.54:.2f} cm") for sor in kereso]

#5
print("5.feladat:")
while True:
    bekeres = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
    if 1990 <= bekeres <= 1999:
        break
    else:
        print("Hibás adat, kérek egy 1990 és 1999 közötti évszámot!")     
#6

suly = [sor.suly for sor in lista if int(sor.elso[:4]) <= bekeres <= int(sor.utolso[:4])]
ossz = sum(suly)
atlag = ossz / len(suly)
        
print(f"6.feladat: {atlag:.2f} font")   
