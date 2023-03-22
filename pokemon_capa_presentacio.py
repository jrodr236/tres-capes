class PokemonCapaPresentacio:
    def __init__(self, capa_logica):
        self._capa_logica = capa_logica

    def iniciar(self):
        while True:
            print("1. Introduïr pokemons")
            print("2. Mostrar pokemons")
            print("3. Sortir")

            opcio = input("Selecciona una opció: ")

            if opcio == "1":
                self.introduir_pokemons()
            elif opcio == "2":
                self.mostrar_pokemons()
            elif opcio == "3":
                break
            else:
                print("Opció no vàlida")

    def introduir_pokemons(self):
        while True:
            pokemon = input("Introdueix un pokemon (o deixa en blanc per sortir): ")
            if not pokemon:
                break
            self._capa_logica.afegir_pokemon(pokemon)

        self._capa_logica.desar_pokemons()

    def mostrar_pokemons(self):
        self._capa_logica.llegir_pokemons()
        pokemons = self._capa_logica.obtenir_pokemons()
        if not pokemons:
            print("No hi ha pokemons")
        else:
            for pokemon in pokemons:
                print(pokemon)
