def nagy(lista):
    legnagyobb = 0
    for szam in lista:
        if legnagyobb < szam:
            legnagyobb = szam
    return legnagyobb


def kicsi(lista):
    legkisebb = lista[0]
    for szam in lista:
        if legkisebb > szam:
            legkisebb = szam
    return legkisebb

def ossz(lista):
    x = 0
    for szam in lista:
        x += szam
        
    return x

        
