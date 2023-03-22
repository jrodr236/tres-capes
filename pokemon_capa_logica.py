class PokemonCapaLogica:
    def __init__(self, capa_dades):
        self._pokemons = []
        self._capa_dades = capa_dades

    def obtenir_pokemons(self):
        return self._pokemons

    def afegir_pokemon(self, pokemon):
        self._pokemons.append(pokemon)

    def desar_pokemons(self):
        self._capa_dades.desar_a_fitxer(self._pokemons)

    def llegir_pokemons(self):
        return self._capa_dades.llegir_des_de_fitxer()
