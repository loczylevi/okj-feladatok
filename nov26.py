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



def hossz(lista):
    szamlalo = 0
    for szam in lista:
        if type(szam) == int:
            szamlalo += 1

    return szamlalo

találat = False

lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
def hany_db_3(lista1):
    szamlalo = 0
    for szam in lista1:
        if szam % 3 == 0:
            szamlalo += 1
            találat = True
            
            
    return szamlalo

hany_db_3(lista1)

if találat:
    print("Van a listában hárommal osztható szám.")
else:
    print('Nincs a listában hárommal osztható szám.')



lista3 = [1,2,312,34141,124,412,13,412,1,3,3,1]
stat = dict()
for i in lista3:
    stat[i] = stat.get(i,0) + 1
    #ennyi HE 
    
