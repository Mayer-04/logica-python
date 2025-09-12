# --------------------------
# * Herencia
# --------------------------


class Animal:
    """
    Clase que representa un animal con un nombre y una edad.
    """

    def __init__(self, nombre: str, edad: int) -> None:
        """
        Constructor de la clase.

        Args:
            nombre (str): Nombre del animal.
            edad (int): Edad del animal.
        """
        self.nombre = nombre
        self.edad = edad


class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        super().__init__(nombre, edad)
        self.raza = raza


perro = Perro("Zeus", 4, "Dalmata")
print(perro.nombre)  # Salida: "Zeus"
print(perro.edad)  # Salida: 4
