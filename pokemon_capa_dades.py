import csv

NOM_FITXER = "pokemons.csv"


class PokemonCapaDades:
    def desar_a_fitxer(self, pokemons):
        with open(NOM_FITXER, "w", newline="") as fitxer_csv:
            writer = csv.writer(fitxer_csv)
            for pokemon in pokemons:
                writer.writerow([pokemon])

    def llegir_des_de_fitxer(self):
        with open(NOM_FITXER, "r") as fitxer_csv:
            reader = csv.reader(fitxer_csv)
            pokemons = [row[0] for row in reader]
        return pokemons
