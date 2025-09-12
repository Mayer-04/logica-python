"""
* Encapsulación

Por defecto en Python todos los atributos y métodos son publicos.


* atributo → público.
* _atributo → protegido (convención).
* __atributo → privado (name mangling).
* Getters/Setters modernos → con @property y @atributo.setter.
"""


class Persona:
    def __init__(self, nombre: str, edad: int):
        """
        Constructor de la clase Persona.

        Args:
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    @property
    def nombre(self):  # getter
        """Getter del nombre de la persona"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):  # setter
        """Setter del nombre de la persona"""
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    @property
    def edad(self):  # getter
        """Getter de la edad de la persona"""
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad: int):  # setter
        """Setter de la edad de la persona"""
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa")


# Uso de la clase
persona = Persona("Mayer", 25)
# Uso del getter
print(persona.nombre)  # Salida: Mayer
# Uso del setter
persona.edad = 30
print(persona.edad)  # Salida: 30
