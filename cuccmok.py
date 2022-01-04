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
    for sor in thisdict:
        if bekeres in thisdict.keys():
            print(thisdict[bekeres])
            break
            folytkov = True
        
    if bekeres == "vége":
        folytkov = False
        print(">>> Program vége <<<")


