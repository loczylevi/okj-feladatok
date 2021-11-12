'''Ausztria;1995.01.01'''
#1-2. feladat_________________________________________________

with open("eucsatlakozas.txt","r",encoding="UTF-8") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3. feladat_________________________________________________

print(f"3.feladat: EU tagállamainak száma: {len(lista)} db")

#4. feladat2007-ben _________________________________________________

eu2007 = [ sor for sor in lista if sor[1][0:4] == "2007"]
szamlalo = len(eu2007)

print(f"4.feladat: 2007-ben {szamlalo} ország csatlakozott")

#5. feladat_________________________________________________

magyarorszag = [sor[1][0:10] for sor in lista if sor[0]=="Magyarország"]
#magyar = ()
#magyar = (magyarorszag)


print(f"5.feladat: Magyarország csatlakozási dátuma: {magyarorszag[0]}")

#6. feladat_________________________________________________

majusban = [sor for sor in lista if sor[1][5:7] == "05"]
if majusban:
    print("6.feladat: Májusban Volt csatlakozás")
else:
    print("6.feladat: Májusban Nem volt csatlakozás")
    
#7. feladat_________________________________________________
#utoljára csatlakozott ország
    
utoljara = max([(sor[1],sor[0]) for sor in lista])

print(f"7.feladat: Legutoljára csatlakozott ország: {utoljara[1]}")

stat = dict()
for sor in lista:
    ev = sor[1][0:4]
    stat[ev] = stat.get(ev, 0) + 1
print("8:feladat: statisztika")
for ev,darab in stat.items():
    print(f"     {ev} - {darab} ország")
    


