folytkov = True
while folytkov:
    with open("fordito.txt", "r",encoding="utf-8") as f2:
        elso_sor = f2.readline()
        lista = []
        for sor in f2:
            lista.append(sor.strip().split("="))
    
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    for sor in lista:
        if bekeres == sor[0]:
            print(f"Forditás eredménye: {sor[1]}")
            print("")
            folytkov = True
        
    if bekeres == "Grrr":
        folytkov = False
        print(">>> Program vége <<<")
        
    

