# =====================================
# * Función incorporada sum()
# =====================================
# La función sum() devuelve la suma de todos los elementos
# numéricos de un iterable (lista, tupla, conjunto, etc.).
#
# Forma general:
# sum(iterable, inicio=0)
#
# Parámetros:
# - iterable: secuencia de números a sumar.
# - inicio (opcional): valor inicial que se suma al total.
#   Por defecto es 0.
#
# `sum()` solo funciona con números. Si se usa con cadenas, dará error

# Ejemplo 1: Sumar una lista de números
print(sum([1, 2, 3, 4, 5]))
# Salida: 15 → 1+2+3+4+5

# Ejemplo 2: Sumar una tupla
print(sum((10, 20, 30)))
# Salida: 60

# Ejemplo 3: Sumar un conjunto
print(sum({1, 2, 3}))
# Salida: 6

# Ejemplo 4: Usar el parámetro inicio
print(sum([1, 2, 3], 10))
# Salida: 16 → suma los elementos y luego añade 10 al resultado
