Exemple d'arquitectura en 3 capes
=======================

![Pokemon logo](https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg)

Aplicació que permet desar i recuperar noms de pokémon a un fitxer.

![Diagrama de l'arquitectura en 3 capes](https://upload.wikimedia.org/wikipedia/commons/5/51/Overview_of_a_three-tier_application_vectorVersion.svg)



* Versió monolítica ([wikipedia](https://en.wikipedia.org/wiki/Monolithic_application)):
  - [Aplicació monolítica](pokemon_monolitic.py)
* Versió amb 3 capes ([wikipedia](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture)):
  - [Capa de presentació, TUI](pokemon_capa_presentacio.py)
  - [Capa de lògica](pokemon_capa_logica.py)
  - [Capa de dades, CSV](pokemon_capa_dades.py)

Per demostrar les bondats d'aquesta arquitectura, es poden intercanviar algunes capes.
* Capes intercanviables:
  - [Capa de presentació, GUI](pokemon_capa_presentacio_gui.py)
  - [Capa de dades, JSON](pokemon_capa_dades_json.py)




---

Autor: Joan Rodríguez Bellido

Col·laborador: [ChatGPT](https://chat.openai.com/)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Llicència de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Aquesta obra està subjecta a una llicència de <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Reconeixement 4.0 Internacional de Creative Commons</a>

---

[#FpInfor](https://profesinformatica.github.io/FpInfor/) #Dam #Daw