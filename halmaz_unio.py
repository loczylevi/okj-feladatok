print("2.feladat:")
def beker():
  a = 0
  hiba = False
  lista = []
  while hiba == False:
    a = a + 1
    bekeres = input(f"\'A\' halmaz {a}. eleme: ")
    if bekeres == "":
      hiba = True
    else:
      szam = 0
      while ((szam < len (lista)) and (hiba == False)):
        if lista [szam] == int(bekeres):
          print(f"HIBA! a(z) {bekeres} már benne van a(z) \'A\' halmazban!")
          hiba = True
        szam = szam + 1 

      if (hiba == False):
        lista.append(int(bekeres))
  return lista

l = []
l = beker()
print ("A lista: ", l)

def beker2():
  b = 0
  hiba2 = False
  lista2 = []
  while hiba2 == False:
    b = b + 1
    bekeres2 = input(f"\'B\' halmaz {b}. eleme: ")
    if bekeres2 == "":
      hiba2 = True
    else:
      szam2 = 0
      while ((szam2 < len (lista2)) and (hiba2 == False)):
        if lista2 [szam2] == int(bekeres2):
          print(f"HIBA! a(z) {bekeres2} már benne van a(z) \'B\' halmazban!")
          hiba2 = True
        szam2 = szam2 + 1 

      if (hiba2 == False):
        lista2.append(int(bekeres2))
  return lista2

k = []
k = beker2()
print ("B lista: ", k)
unio = []
for szam1 in l:
  for szam2 in k:
    if szam1 == szam2:
      unio.append(szam2)


print(f"'A', 'b' uniója: {unio}")

