# =====================================
# * Función incorporada len()
# =====================================
# La función len() devuelve la cantidad de elementos en un iterable
# (lista, tupla, cadena, diccionario, conjunto, string, etc.).
#
# Forma general:
# len(objeto_iterable)
#
# - En cadenas: devuelve el número de caracteres.
# - En listas/tuplas/conjuntos: devuelve el número de elementos.
# - En diccionarios: devuelve el número de claves.
#
# len() solo funciona con objetos que tienen una "longitud".
# Si intentas usarlo con un número entero, dará error.

# Ejemplo 1: Longitud de una cadena
texto = "Hola, mundo"
print(len(texto))  # Salida: 11 → incluye letras, espacios y signos de puntuación

# Ejemplo 2: Longitud de una lista
numeros = [10, 20, 30, 40]
print(len(numeros))  # Salida: 4 → hay cuatro elementos en la lista

# Ejemplo 3: Longitud de una tupla
coordenadas = (4, 5, 6)
print(len(coordenadas))  # Salida: 3

# Ejemplo 4: Longitud de un diccionario
persona = {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"}
print(len(persona))  # Salida: 3 → cuenta las claves, no los valores

# Ejemplo 5: Longitud de un conjunto
colores = {"rojo", "verde", "azul"}
print(len(colores))  # Salida: 3
