class hianyzas:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.nev = str(sor[0])
        self.osztaly = sor[1]
        self.elso = int(sor[2])
        self.utolso = int(sor[3])
        self.mulasztas = int(sor[4])
      
with open("szeptember.txt",encoding="UTF 8") as f:
    lista = [hianyzas(sor) for sor in f]
#2.Feladat
tanulok =[sor.nev for sor in lista]

mulasztas = [sor.mulasztas for sor in lista]
print(f"""2. feladat
      Összes mulasztott órák száma:{sum(mulasztas)} óra.
  """)
#3.Feladat
nap = int(input("""3.Feladat 
      Adjon meg egy számot 1 és 30 között: """))
tanulo = input("""      Adjon egy tanúlo nevet: """)
#4.Feladat
print("4.Feladat")
if tanulo in tanulok:
    print("""       A tanuló hiányzott szeptemberben""")
else:
    print("""       A tanuló nem hiányzott szeptemberben""")
#5.Feladat
hianyzasok = []  
#kereso = [sor.nev for sor in lista if nap == sor.elso ]
lista2 = []
for sor in lista:
  if sor.elso == nap:
    lista2.append(sor.nev)

print(f"""5.feladat: Hiányzók 2017.09.{nap}-n:""")

lista3 = []
for sor in lista:
  if sor.elso == nap:
    lista3.append(sor.osztaly)

try:
  meddig = len(lista3) - 1
  meddig2 = len(lista2) - 1
  a = 0
  b = 0
  while True:
    if a < meddig or b < meddig2:
      for nev in lista2:
        for szam in lista3:
            print(f"{lista2[a]} ({lista3[b]})")
            a = a + 1
            b = b + 1
    else:
      break
except IndexError:
  None
      


#for i in range(len(lista3)):
