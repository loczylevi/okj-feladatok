#Név;Ország;Technikai;Komponens;Levonás

#1.feladat________________________________________________

class Mukorcsolya:
  def __init__(self,sor):
    s = sor.strip().split(";")
    self.nev = s[0]
    self.orszag = s[1]
    self.technika = float(s[2])
    self.komponens = float(s[3])
    self.levonas = int(s[4])
    
with open("donto.csv","r",encoding="latin2") as donto:
  fejlec = donto.readline()
  donto_lista = [ Mukorcsolya(sor) for sor in donto]

with open("rovidprogram.csv","r",encoding="latin2") as rovid:
  fejlec = rovid.readline()
  rovid_lista = [ Mukorcsolya(sor) for sor in rovid]

#2.feladat________________________________________________

print(f"""2.feladat:
       A rövidprogramban {len(rovid_lista)} verenyző volt""")

#3.feladat________________________________________________

kereso = [sor for sor in rovid_lista if sor.orszag == "HUN"]

if len(kereso) == 0:
  print("""3.feladat:
       Magyar versenyző NEM jutott be a kűrbe""")
else:
  print("""3.feladat:
       Magyar versenyző bejutott a kűrbe""")

#4.feladat________________________________________________
#tudom hogy csunya istenem ez van 

def ÖsszPontszam(rovid_lista,donto_lista,bekeres):
  tarolo = 0
  for sor in rovid_lista:
    if sor.nev == bekeres:
      tarolo = sor.technika
  tarolo2 = 0
  for sor in rovid_lista:
    if sor.nev == bekeres:
      tarolo2 = sor.komponens
  levonas = 0
  for sor in rovid_lista:
    if sor.nev == bekeres:
      levonas = sor.levonas
  összead = tarolo + tarolo2
  eredmeny1= összead - levonas

  tarolo3 = 0
  for sor in donto_lista:
    if sor.nev == bekeres:
      tarolo3 = sor.technika
  tarolo4 = 0
  for sor in donto_lista:
    if sor.nev == bekeres:
      tarolo4 = sor.komponens
  levonas2 = 0
  for sor in donto_lista:
    if sor.nev == bekeres:
      levonas2 = sor.levonas
  összead2 = tarolo3 + tarolo4
  eredmeny2 = összead2 - levonas2
  vegso = eredmeny1 + eredmeny2
  return vegso

# listákat nem lehet összeadni egymással? kár
"""
def ÖsszPontszam(rovid_lista,donto_lista,bekeres):
  ossz_rovid1 = [sor.technika for sor in rovid_lista if bekeres == sor.nev]
  ossz_rovid2 = [sor.komponens for sor in rovid_lista if bekeres == sor.nev]
  levonas = [sor.levonas for sor in rovid_lista if bekeres == sor.nev]
  összead = ossz_rovid1 + ossz_rovid2
  eredmeny1= összead - levonas

  ossz_donto1 = [sor.technika for sor in donto_lista if bekeres == sor.nev]
  ossz_donto2 = [sor.komponens for sor in donto_lista if bekeres == sor.nev]
  levonas2 = [sor.levonas for sor in donto_lista if bekeres == sor.nev]
  osszead2 = ossz_donto1 + ossz_donto2
  eredmeny2= osszead2 - levonas2
  vegso = eredmeny1 + eredmeny2
  return vegso
"""

#5-6.feladat________________________________________________

bekeres = input("""5.feladat
       Kérem a versenyző nevét: """)
nev_keres = [sor for sor in rovid_lista or donto_lista if bekeres == sor.nev]
if len(nev_keres) > 0:
  print(f"""6.feladat:
       A versenyző összpontszáma: {ÖsszPontszam(rovid_lista,donto_lista,bekeres)}""")
else:
  print("       Ilyen nevű induló nem volt ")

#7.feladat________________________________________________
# pontatlan megoldás

stat = dict()
for sor in donto_lista:
    orszag = sor.orszag
    stat[orszag] = stat.get(orszag, 0) + 1
print("7:feladat:")
for orszag,darab in stat.items():
    print(f"     {orszag}: {darab} versenyző")

#8.feladat________________________________________________
