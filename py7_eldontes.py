'''
2.3 Feladat
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!

A felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
'''
jo = []
rossz = []
jotipp = 0
rossztipp = 0
szo = "almafa"
while True:
  bekeres = input("Kérek egy betüt!\t")
  if bekeres == "":
    break
  else:
    kereso = [szavak for szavak in szo if bekeres == szavak]
    if len(kereso) >0:
     print(f"A felhasználó által begépelt betü: {bekeres}\n  a változoban szerepelt szó: {szo},\n A szóban szerepel ez a betű: {kereso[0]}")
     jotipp = jotipp + 1
     jo.append(bekeres)
    else:
     print(f"Nincs ilyen betü: {bekeres} a szóban")
     rossztipp = rossztipp + 1
     rossz.append(bekeres)





print(f"Jó tippek száma: {jotipp} A jó szavak: {jo}\n Rossz tippek száma: {rossztipp} Nem eltalált szavak: {rossz}")


