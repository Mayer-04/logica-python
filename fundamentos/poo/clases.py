"""
* Clases en Python
-------------------
- Una clase es una plantilla o molde que define los atributos (datos) y métodos (comportamientos)
  que tendrán sus objetos.
- Una `instancia` es un objeto concreto creado a partir de una clase.
- Un `objeto` es, por tanto, una instancia de una clase.
- Por convención, los nombres de las clases se escriben en formato `PascalCase`.
- El parámetro `self` representa a la instancia actual de la clase (el propio objeto en uso).
- Cada instancia de una clase almacena sus datos en un `diccionario de atributos`.
- Las clases también tienen un diccionario interno que guarda sus atributos y métodos, accesible mediante `__dict__`.
- En Python, todas las clases heredan implícitamente de la clase base `object`, incluso si no se especifica.
"""


# ---------------------------
# * Definición de una clase
# ---------------------------
class Persona:
    # _init_(self): Define los valores iniciales de nuestra clase.
    def __init__(self, nombre: str, edad: int) -> None:
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear una instancia de la clase Persona.

        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

    def presentar(self) -> None:
        """
        Imprime un saludo con el nombre y la edad de la persona.

        Ejemplo:
            persona = Persona("Mayer", 25)
            persona.presentar()
            # Salida: Hola, mi nombre es Mayer y tengo 25 años
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")


# Crear una instancia de la clase `Persona`
mayer = Persona("Mayer", 25)

print(
    mayer
)  # Imprime la referencia de la instancia: <__main__.Persona object at 0x0000016C44596510>

# Llamar al método `presentar()` de la instancia
mayer.presentar()


# --------------------------
# * Argumentos con nombre
# --------------------------
class Car:
    """
    Clase que representa un automóvil con un modelo y un color.
    Solo acepta `argumentos con nombre` al crear una instancia.
    """

    def __init__(self, *, model: str, color: str) -> None:
        """
        Constructor de la clase.

        Args:
            model (str): Modelo del automóvil.
            color (str): Color del automóvil.
        """
        self.model = model
        self.color = color


# Crear un automóvil usando argumentos con nombre
toyota = Car(model="Corolla Cross", color="Azul")
print("modelo:", toyota.model)  # Salida: modelo: Corolla Cross
print("color:", toyota.color)  # Salida: color: Azul

# Atributo __dict__ en instancias
chevrolet = Car(model="Celta", color="Rojo")
# __dict__ devuelve un diccionario con los atributos de la instancia y sus valores.
print(chevrolet.__dict__)  # Salida: {'model': 'Celta', 'color': 'Rojo'}


# -------------------------
# * Métodos en Python
# -------------------------
# - Métodos de instancia: reciben 'self', acceden y modifican atributos del objeto.
# - Métodos de clase: reciben 'cls', acceden/modifican atributos compartidos de la clase.
# - Métodos estáticos: no reciben ni 'self' ni 'cls', son funciones auxiliares dentro de la clase.


class Banco:
    cuentas_creadas = 0  # Atributo de clase (global para todas las cuentas)

    def __init__(self, titular, saldo=0):
        self.titular = titular  # Atributo de instancia
        self.saldo = saldo
        Banco.cuentas_creadas += 1

    # --------------------------
    # Método de instancia
    # --------------------------
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"{self.titular} ha depositado {cantidad}. Nuevo saldo: {self.saldo}"

    # --------------------------
    # Método de clase
    # --------------------------
    @classmethod
    def total_cuentas(cls):
        return f"Se han creado {cls.cuentas_creadas} cuentas en el banco."

    # --------------------------
    # Método estático
    # --------------------------
    @staticmethod
    def convertir_moneda(monto, tasa):
        """Convierte monto según una tasa (ej: de USD a COP)."""
        return monto * tasa
