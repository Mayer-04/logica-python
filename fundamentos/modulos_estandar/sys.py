import sys

"""
* sys
------
Módulo de Python que proporciona métodos y atributos para interactuar con el sistema operativo.

- Función `getsizeof()` se utiliza para obtener el tamaño de un objeto en bytes.
- Función `intern()` se utiliza para reutilizar objetos inmutables (internado).
"""

# Tamaño de una cadena
cadena = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print("Tamaño de la cadena:", sys.getsizeof(cadena), "Bytes")  # Salida: 70 Bytes

# Tamaño de una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Tamaño de la lista:", sys.getsizeof(lista), "Bytes")  # Salida: 136 Bytes

# Tamaño de una tupla
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tamaño de la tupla:", sys.getsizeof(tupla), "Bytes")  # Salida: 120 Bytes

# Tamaño de un conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Tamaño del conjunto:", sys.getsizeof(conjunto), "Bytes")  # Salida: 728 Bytes

# Tamaño de un diccionario
diccionario = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
}
print(
    "Tamaño del diccionario:", sys.getsizeof(diccionario), "Bytes"
)  # Salida: 272 Bytes

# Tamaño de un rango
rango = range(1, 11)
print("Tamaño del rango:", sys.getsizeof(rango), "Bytes")  # Salida: 48 Bytes

# Internado de una cadena
texto1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
texto2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit."

texto1 = sys.intern(texto1)
texto2 = sys.intern(texto2)
# Comparar si los objetos internados son iguales
print(texto1 is texto2)  # True
