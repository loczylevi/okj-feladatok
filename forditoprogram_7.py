folytkov = True
thisdict = {
  "I": "én",
  "you": "te",
  "he": "Ő",
  "apple":"alma",
  "watermelon:" :"dinnye"
}

while folytkov:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    bekeres = bekeres.split(" ")
    for szo in bekeres:
        print(thisdict.get(szo,"ismeretlen"),end=" ")
    print("")
    if bekeres == "vége":
        folytkov = False
        print(">>> Program vége <<<")



