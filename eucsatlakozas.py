'''Ausztria;1995.01.01'''
with open("EUcsatlakozas.txt", "r",encoding="latin2") as f:
    #elso_sor = f.readline()
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
        
#3 feladat
        
print(f"3.feladat: EU tagállamainak száma: {len(lista)} db.")
#4feladat
szamlalo = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo = szamlalo + 1


print(f"4.feladat: 2007-ben {szamlalo} ország csatlakozott")


# 5 feladat Magyarország csatlakozási dátuma:

for sor in lista:
    if sor[0] == "Magyarország":
        print(f"5.feladat Magyarország csatlakozási dátuma: {sor[1]}")
#6 feladat
volt_csatlakozas = False
for sor in lista:
    if sor[1][5:7] == "05":
        volt_csatlakozas = True

if volt_csatlakozas:
    print(f"6.feladat Májusban volt a csatlakozás!")
else:
    print(f"6.feladat Nem volt Májusbban csatlakozás!")
    
utoljara = ""
for sor in lista:
    if sor[1] > utoljara:
        utoljara = sor[1]
        orszag = sor[0]
        
print(f"7.feladat A legutoljára csatlakozott ország: {orszag} {utoljara}")
