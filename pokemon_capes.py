from pokemon_capa_dades_json import PokemonCapaDadesJson as CapaDades
from pokemon_capa_logica import PokemonCapaLogica as CapaLogica
from pokemon_capa_presentacio_gui import PokemonCapaPresentacioGui as CapaPresentacio

capa_dades = CapaDades()
capa_logica = CapaLogica(capa_dades)
capa_presentacio = CapaPresentacio(capa_logica)

capa_presentacio.iniciar()