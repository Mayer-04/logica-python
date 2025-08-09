# =====================================
# * Función incorporada type()
# =====================================
# La función type() devuelve el tipo de dato o clase de un objeto.
#
# Forma general:
# type(objeto)
#
# Útil para:
# - Saber qué tipo de dato tiene una variable.
# - Verificar clases al trabajar con programación orientada a objetos.

# Ejemplo 1: Tipo de una cadena
print(type("Hola, mundo"))  # Salida: <class 'str'>

# Ejemplo 2: Tipos de números
print(type(42))  # <class 'int'>   → número entero
print(type(3.14))  # <class 'float'> → número decimal
print(type(True))  # <class 'bool'>  → valor booleano

# Ejemplo 3: Tipos de estructuras de datos
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({"a": 1, "b": 2}))  # <class 'dict'>
print(type({1, 2, 3}))  # <class 'set'>


# Ejemplo 4: Comparación con isinstance()
# type() comprueba el `tipo` exacto.
# isinstance() también devuelve `True` para subclases.
class Animal:
    pass


class Perro(Animal):
    pass


scooby_doo = Perro()
print(type(scooby_doo) is Perro)  # True → es exactamente de la clase Perro
print(isinstance(scooby_doo, Animal))  # True → es un Perro, pero también un Animal
