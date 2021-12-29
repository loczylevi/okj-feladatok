"""Üdv a TTPSZ támogatásával létrejött a disznónyelv forditó
 ahol lehetőségünk van összetett disznó mondatokat
 lefordítani ami persze idő igényes hát de na erre volt keret"""


"""FIGYELMEZTETÉS!! A program következő szabályoktól müködik beirsz egy szót:
pl: "ui" az ui-után kell raknod egy ";" - jelet különben a program nem működik
pl: /; ui; /; uí; uui; uíí; uií; uui; --> ez így helyes
de ha csak ennyit írsz: / ui / uí uui uíí uií uui --> akkor a program nem müködik
használj minden szó végén ";"-jelet és spaceket!!!
ha kérdőjelet (?) ir a program akkor az a szó a szótárban nem szerepel!
"""
#_______________________________________________________________________
with open("fordito.txt","w",encoding="latin2") as f:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    f.write(bekeres)



#________________________________________________________________________

with open("fordito.txt", "r",encoding="latin2") as f2:
    lista = []
    for sor in f2:
        lista.append(sor.strip().split(";"))

megoldas = []
#________________________________________________________________________
for sor in lista:
    if " ui" in sor:
        megoldas.append("ui = igen")
        #print("igen")
    if " uí" in sor:
        #print("nem")
        megoldas.append("uí = nem")
    if " /" or " rőff" in sor:
        #print("szóelválasztás")
        megoldas.append(" /, röff = szóelválasztás")
    if " uui" in sor:
        #print("csörtet")
        megoldas.append("uui = csörtet")
    if " uií" in sor:
        megoldas.append("uií = pata")
    if " uíí" in sor:
        megoldas.append("uíí = makk (termés)")
    if " iú" in sor:
        megoldas.append("iú = buta (utalás arra, hogy az alany fordítva visít)")
    if " uuií" in sor:
        megoldas.append("uuií = (vad)kan")
    if " uúií" in sor:
        megoldas.append("uúií = (vad)koca")
    if " uííííí" in sor:
        megoldas.append("uííííí = menekülés")
    if " uuíí" in sor:
        megoldas.append("uuíí = legféltettebbgyémánt, kismalac")
    if " uúíí" in sor:
        megoldas.append("uúíí = 1.ólajtó (kapu az ólba),")
    if " uii uíi uuííii" in sor:
        megoldas.append("uii uíi uuííii = fény vele csinál ronda kép disznó ((fényképész) a visítások külön külön nem mindig jelentik magyar megfelelő szórészeit! Pl.: uii NEM egyenlő fény)")
    if " uuuií" in sor:
        megoldas.append("uuuií = kukorica")
    if " uúúíííí" in sor:
        megoldas.append("uúúíííí = táplálkozik, ")
    if " úúúíííí" in sor:
        megoldas.append("úúúíííí = ágy")
    if " uiiii" in sor:
        megoldas.append("uiiii = marad")
    if " úi" in sor:
        megoldas.append("úi = éhes")
    if " uííí" in sor:
        megoldas.append("uííí = és")
    if " úí" in sor:
        megoldas.append("úí = van (a disznónyelv egyetlen létigéje)")
    if " uuui" in sor:
        megoldas.append("uuui = én")
    if " uuuí" in sor:
        megoldas.append("uuuí = te")
    if " uuuíi" in sor:
        megoldas.append("uuuíi = ő")          
    if " uuui/uííí/uuuí" in sor:
        megoldas.append("uuui/uííí/uuuí = mi")
    if " uuuiííi" in sor:
        megoldas.append("uuuiííi = ki")        
    if " uuuíiií" in sor:
        megoldas.append("uuuíiií = mi")        
    if " uuuuí" in sor:
        megoldas.append("uuuuí = hol")        
    if " uuuui" in sor:
        megoldas.append("uuuui = mikor")
    else:
        megoldas.append("? = error")
        
print(megoldas)
            
        
#_______________________________________________________
"""
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
    if " " in sor:
        megoldas.append("")
"""
