import csv

NOM_FITXER = "pokemons.csv"
pokemons = []

while True:
    print("\nMenú:")
    print("1. Introduir pokemons")
    print("2. Mostrar pokemons")
    print("3. Sortir")
    opcio = input("Escull una opció: ")
    if opcio == "1":
        while True:
            pokemon = input("Introdueix un nom de pokemon o prem Enter per sortir: ")
            if not pokemon:
                break
            pokemons.append(pokemon)
        with open(NOM_FITXER, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for pokemon in pokemons:
                writer.writerow([pokemon])
        print(f"S'han desat els pokemons a {NOM_FITXER}")
    elif opcio == "2":
        with open(NOM_FITXER, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0])
    elif opcio == "3":
        break
    else:
        print("Opció no vàlida")