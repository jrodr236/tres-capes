import tkinter as tk
from tkinter import messagebox


class PokemonCapaPresentacioGui:
    def __init__(self, capa_logica):
        self._capa_logica = capa_logica

        self._root = tk.Tk()
        self._root.title("Gestor de Pokemons")

        self.lliurar_noms = tk.StringVar()

        tk.Label(self._root, text="Nom del Pokemon").grid(row=0, column=0)
        self.nom_pokemon = tk.Entry(self._root, textvariable=self.lliurar_noms)
        self.nom_pokemon.grid(row=0, column=1)

        self.boto_introduir = tk.Button(self._root, text="Introduir Pokemon", command=self.introduir_pokemon)
        self.boto_introduir.grid(row=2, column=0)

        self.boto_desar = tk.Button(self._root, text="Desar Pokemons", command=self.desar_pokemons)
        self.boto_desar.grid(row=3, column=0)

        self.boto_mostrar = tk.Button(self._root, text="Mostrar Pokemons", command=self.mostrar_pokemons)
        self.boto_mostrar.grid(row=3, column=1)

        self.boto_sortir = tk.Button(self._root, text="Sortir", command=self.sortir)
        self.boto_sortir.grid(row=4, column=0, columnspan=2)

    def introduir_pokemon(self):
        nom_pokemon = self.nom_pokemon.get()
        try:
            self._capa_logica.afegir_pokemon(nom_pokemon)
            messagebox.showinfo("Introducció correcta", "El Pokemon s'ha introduït correctament")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def desar_pokemons(self):
        try:
            self._capa_logica.desar_pokemons()
            messagebox.showinfo("Gravació correcta", "Els Pokemons s'han desat correctament")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_pokemons(self):
        pokemons = self._capa_logica.obtenir_pokemons()
        if not pokemons:
            messagebox.showinfo("Llista buida", "No hi ha Pokemons per mostrar")
        else:
            messagebox.showinfo("Llista de Pokemons", "\n".join(pokemons))

    def sortir(self):
        self._root.destroy()

    def iniciar(self):
        self._root.mainloop()

