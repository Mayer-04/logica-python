# =====================================
# * Función incorporada filter()
# =====================================
# La función filter() selecciona elementos de un iterable
# (lista, tupla, conjunto, etc.) que cumplen con una condición.
# Devuelve un objeto de tipo filter, que es un iterable con los elementos que pasaron el filtro.
#
# Forma general:
# filter(funcion_condicion, iterable)
#
# - funcion_condicion: debe devolver True para los elementos que quieras conservar
# - iterable: la secuencia de datos a filtrar

# Ejemplo 1: Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Salida: [2, 4, 6]

# Ejemplo 2: Filtrar palabras con más de 4 letras
palabras = ["sol", "montaña", "mar", "cielo"]
largas = filter(lambda p: len(p) > 4, palabras)
print(list(largas))  # Salida: ['montaña', 'cielo']

# Ejemplo 3: Filtrar valores "verdaderos"
valores = [0, 1, "", "hola", [], [1, 2], None, True]
verdaderos = filter(None, valores)  # None hace que filter descarte los valores falsos
print(list(verdaderos))  # Salida: [1, 'hola', [1, 2], True]

# Ejemplo 4: Alternativa con listas por comprensión
pares_comp = [x for x in numeros if x % 2 == 0]
print(pares_comp)  # Salida: [2, 4, 6]
# A veces es más fácil de leer que usar filter() con lambda.
