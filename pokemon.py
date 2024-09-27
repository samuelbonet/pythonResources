class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def atacar(self):
        pass


class Charizard(Pokemon):
    def __init__(self):
        super().__init__(nombre="Charizard", tipo="Fuego")

    def atacar(self):
        print(f"{self.nombre} usa Ataque Fuego. ¡Es muy efectivo!")


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(nombre="Squirtle", tipo="Agua")

    def atacar(self):
        print(f"{self.nombre} usa Pistola Agua. ¡Es muy efectivo!")


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(nombre="Bulbasaur", tipo="Planta")

    def atacar(self):
        print(f"{self.nombre} usa Látigo Cepa. ¡Es muy efectivo!")


def elegir_pokemon():
    personajes = ["charizard", "squirtle", "bulbasaur"]
    start = input("Bienvenido al pueblo Paleta, elige un pokemon (charizard, squirtle, bulbasaur): ")

    if start == personajes[0]:
        pokemon = Charizard()  # Asigna la instancia de Charizard
    elif start == personajes[1]:
        pokemon = Squirtle()  # Asigna la instancia de Squirtle
    elif start == personajes[2]:
        pokemon = Bulbasaur()  # Asigna la instancia de Bulbasaur
    else:
        print("No hay ningún Pokémon con ese nombre.")
        return None  # Si no se elige un Pokémon válido, retorna None

    return pokemon  # Devuelve la instancia del Pokémon elegido


# Llamada a la función para elegir Pokémon
pokemon_elegido = elegir_pokemon()

if pokemon_elegido:
    print(f"¡Has elegido a {pokemon_elegido.nombre}!")
    pokemon_elegido.atacar()  # El Pokémon elegido usa su ataque