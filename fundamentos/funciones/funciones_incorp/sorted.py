# =====================================
# * Función incorporada sorted()
# =====================================
# La función sorted() ordena los elementos de un iterable
# (lista, tupla, cadena, etc.) y devuelve una `nueva lista` ordenada,
# sin modificar el iterable original.
#
# Forma general:
# sorted(iterable, key=None, reverse=False)
#
# Parámetros:
# - iterable: la secuencia que quieres ordenar.
# - key: función para definir el criterio de ordenación (opcional).
# - reverse: si es True, ordena en orden descendente.

# Ejemplo 1: Ordenar números de menor a mayor
numeros = [3, 2, 1]
ordenados = sorted(numeros)
print(ordenados)  # Salida: [1, 2, 3]
print(numeros)  # Salida: [3, 2, 1] → la lista original no cambia

# Ejemplo 2: Ordenar números de mayor a menor
ordenados_desc = sorted(numeros, reverse=True)
print(ordenados_desc)  # Salida: [3, 2, 1]

# Ejemplo 3: Ordenar cadenas alfabéticamente
palabras = ["manzana", "pera", "banana"]
print(sorted(palabras))  # Salida: ['banana', 'manzana', 'pera']

# Ejemplo 4: Ordenar ignorando mayúsculas/minúsculas
nombres = ["Juan", "ana", "Pedro", "luis"]
print(sorted(nombres, key=str.lower))  # Salida: ['ana', 'Juan', 'luis', 'Pedro']

# Ejemplo 5: Ordenar por la longitud de las palabras
print(sorted(palabras, key=len))  # Salida: ['pera', 'banana', 'manzana']
