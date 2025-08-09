# =====================================
# * Función incorporada range()
# =====================================
# La función range() genera una secuencia de números enteros.
# Es muy usada en bucles `for` y para crear listas de números.
#
# Forma general:
# range(inicio, fin, paso)
#
# Parámetros:
# - inicio (opcional): número inicial de la secuencia (por defecto 0).
# - fin: número hasta el cual se genera la secuencia (excluido).
# - paso (opcional): valor que se suma en cada iteración (por defecto 1).
#
# Nota:
# El objeto que devuelve range() es un iterable, no una lista.
# Para verlo como lista, se usa list(range(...)).

# Ejemplo 1: Secuencia del 1 al 5
print(list(range(1, 6)))  # Salida: [1, 2, 3, 4, 5]

# Ejemplo 2: Usar solo fin (inicio = 0 por defecto)
print(list(range(5)))  # Salida: [0, 1, 2, 3, 4]

# Ejemplo 3: Usar un paso distinto de 1
print(list(range(0, 10, 2)))  # Salida: [0, 2, 4, 6, 8]

# Ejemplo 4: Secuencia decreciente (paso negativo)
print(list(range(10, 0, -2)))  # Salida: [10, 8, 6, 4, 2]
