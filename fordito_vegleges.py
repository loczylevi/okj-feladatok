"""Üdv a TTPSZ támogatásával létrejött a disznónyelv forditó
 ahol lehetőségünk van összetett disznó mondatokat
 lefordítani ami persze idő igényes hát de na erre volt keret"""

"""FIGYELMEZTETÉS!! A program következő szabályoktól müködik beirsz egy szót:
pl: "ui" az ui-után kell raknod egy " " - (space) jelet különben a program nem működik
Pl igy:  ui uí uui uíí uií uui --> akkor a program müködik!
használj minden szó végén " "- spaceket!!!
ha "Nincs ilyen szó a szótárban!"-ír a program akkor az a szó a szótárban nem szerepel!
"""
# "Sok szerencsét a disznólkodáshoz!" by Zefi
#_______________________________________________________________________________________
folytkov = True
# szótár:
thisdict = {
  "ui" : "igen",
  "uí" : "nem",
  "uui" : "csörtet",
  "uií" : "pata",
  "uíí" : "makk",
  "iú" : "buta (utalás arra, hogy az alany forditva visit)",
  "uuií" : "(vad)kan",
  "uúií" : "(vad)koca",
  "uííííí" : "menekülés",
  "uuíí" : "legfeltettebbgyemant, kismalac",
  "uúíí" : "olajto",
  "uii uíi uuííii" : "fény vele csinál ronda kép / disznó fényképész",
  "uuuií" : "kukorica",
  "uúúíííí" : "táplálkozik",
  "úúúíííí" : "ágy",
  "uiiii" : "marad",
  "úi" : "éhes",
  "uííí" : "és",
  "úí" : "van(a disznónyelv egyetlen létigéje)",
  "uuui" : "én",
  "uuuí" : "te",
  "uuuíi" : "ő",
  "uuui/uííí/uuuí" : "mi",
  "uuuiííi" : "ki",
  "uuuíiií" : "mi",
  "uuuuí" : "hol",
  "uuuui" : "mikor",
  "röff" : "élelmet keres"
}
# maga a program (ne piszkálj bele) _________________________________

while folytkov:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    if bekeres == "Grrr":
        folytkov = False
        print(">>> Program vége <<<")
        break
    bekeres = bekeres.split(" ")
    for szo in bekeres:
        print(thisdict.get(szo,"Nincs ilyen szó a szótárban!"),end=" ")
    print("")
    
        
