import json

NOM_FITXER = "pokemons.json"


class PokemonCapaDadesJson:
    def desar_a_fitxer(self, pokemons):
        with open(NOM_FITXER, "w") as fitxer_json:
            json.dump(pokemons, fitxer_json)

    def llegir_des_de_fitxer(self):
        try:
            with open(NOM_FITXER, "r") as fitxer_json:
                pokemons = json.load(fitxer_json)
        except FileNotFoundError:
            pokemons = []
        return pokemons
