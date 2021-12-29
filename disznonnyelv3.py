"""Üdv a TTPSZ támogatásával létrejött a disznónyelv forditó
 ahol lehetőségünk van összetett disznó mondatokat
 lefordítani ami persze idő igényes hát de na erre volt keret"""


"""FIGYELMEZTETÉS!! A program következő szabályoktól müködik beirsz egy szót:
pl: "ui" az ui-után kell raknod egy "," - jelet különben a program nem működik
pl: /, ui, /, uí, uui, uíí, uií, uui, --> ez így helyes
de ha csak ennyit írsz: / ui / uí uui uíí uií uui --> akkor a program nem müködik
használj minden szó végén ","-jelet és NE használj spaceket!!!
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
        lista.append(sor.strip().split(","))

megoldas = []
#________________________________________________________________________
for sor in lista:
    if "ui" in sor:
        megoldas.append("igen")
        #print("igen")
    if "uí" in sor:
        #print("nem")
        megoldas.append("nem")
    if "/" or "rőff" in sor:
        #print("szóelválasztás")
        megoldas.append("szóelválasztás")
    if "uui" in sor:
        #print("csörtet")
        megoldas.append("csörtet")
    if "uií" in sor:
        megoldas.append("pata")
    if "uíí" in sor:
        megoldas.append("makk (termés)")
    if "iú" in sor:
        megoldas.append("buta (utalás arra, hogy az alany fordítva visít)")
    if "uuií" in sor:
        megoldas.append("(vad)kan")
    if "uúií" in sor:
        megoldas.append("(vad)koca")
    if "uííííí" in sor:
        megoldas.append("menekülés")
    if "uuíí" in sor:
        megoldas.append("legféltettebbgyémánt, kismalac")
    if "uúíí" in sor:
        megoldas.append("1.ólajtó (kapu az ólba),")
    if "uii uíi uuííii" in sor:
        megoldas.append("fény vele csinál ronda kép disznó ((fényképész) a visítások külön külön nem mindig jelentik magyar megfelelő szórészeit! Pl.: uii NEM egyenlő fény)")
    if "uuuií" in sor:
        megoldas.append("kukorica")
    if "uúúíííí" in sor:
        megoldas.append("1. táplálkozik, ")
    if "úúúíííí" in sor:
        megoldas.append("ágy")
    if "uiiii" in sor:
        megoldas.append("marad")
    if "úi" in sor:
        megoldas.append("éhes")
    if "uííí" in sor:
        megoldas.append("és")
    if "úí" in sor:
        megoldas.append("van (a disznónyelv egyetlen létigéje)")
    if "uuui" in sor:
        megoldas.append("én")
    if "uuuí" in sor:
        megoldas.append("te")
    if "uuuíi" in sor:
        megoldas.append("ő")          
    if "uuui/uííí/uuuí" in sor:
        megoldas.append("mi")
    if "uuuiííi" in sor:
        megoldas.append("ki")        
    if "uuuíiií" in sor:
        megoldas.append("mi")        
    if "uuuuí" in sor:
        megoldas.append("hol")        
    if "uuuui" in sor:
        megoldas.append("mikor")
    else:
        megoldas.append("?")
        
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
