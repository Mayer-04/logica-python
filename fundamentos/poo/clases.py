"""
* Clases en Python
-------------------
- Las clases son los moldes o plantillas que definen los atributos y métodos de un objeto.
- Las instancias son los objetos creados a partir de una clase.
- Los objetos son instancias de una clase.
- Las nombres de las clases por convención se escriben en `PascalCase`.
- El parámetro `self` se refiere a la instancia de la clase, es decir, el objeto que se esta creando (el objeto mismo).
- Cada instancia de la clase tiene un `diccionario de atributos`.
- Las clases en sí tienen un diccionario que almacena sus atributos y métodos. Con el atributo `__dict__`
podemos acceder a este diccionario.
- En Python, todas las clases por defecto (es decir, las que no heredan de ninguna otra clase explícitamente) heredan
de la clase base `object`.
"""


# Definiendo una clase en Python.
class Persona:
    # Contructor: Método que se ejecuta cuando se crea una instancia de la clase.
    # _init_(self): Define los valores iniciales de nuestra clase.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        """
        Imprime un saludo de presentación.

        Ejemplo:
            persona = Persona("Mayer", 24)
            persona.presentar()  # Imprime "Hola, mi nombre es Mayer y tengo 24 años"
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")


# Creando una instancia de la clase Persona
mayer = Persona("Mayer", 24)
print(
    "persona:", mayer
)  # Imprime la referencia de la instancia: <__main__.Persona object at 0x0000016C44596510>

# Llamando al método `presentar()` de la instancia
mayer.presentar()


# Definiendo una clase Car que acepta argumentos con nombre.
class Car:
    # Los argumentos que siguen al asterisco deben ser pasados como `argumentos con nombre` (keyword arguments).
    def __init__(self, *, model: str, color: str) -> None:
        self.model = model
        self.color = color


# Si intentas pasar los argumentos sin nombrarlos obtendrás un error de tipo `TypeError`.
toyota = Car(model="Corolla Cross", color="Azul")
print("modelo:", toyota.model)  # modelo: Corolla Cross
print("color:", toyota.color)  # color: Azul

# Atributo __dict__.
# __dict__ almacena los atributos de clase. Esto incluye métodos y variables de clase.
chevrolet = Car(model="Celta", color="Rojo")
print(chevrolet.__dict__)  # {'model': 'Celta', 'color': 'Rojo'}
