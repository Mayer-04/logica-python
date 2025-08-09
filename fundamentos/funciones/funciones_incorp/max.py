# =====================================
# * Función incorporada max()
# =====================================
# La función max() devuelve el elemento más grande de un iterable
# (lista, tupla, conjunto, cadena, etc.).
#
# Forma general:
# max(iterable, *[, key, default])
# O bien:
# max(valor1, valor2, valor3, ...)
#
# Parámetros más usados:
# - iterable: secuencia de elementos comparables.
# - key (opcional): función que define el criterio de comparación.
# - default (opcional): valor a devolver si el iterable está vacío.

# Ejemplo 1: Máximo en una lista
print(max([1, 2, 3, 4, 5]))  # Salida: 5

# Ejemplo 2: Máximo entre varios valores sueltos
print(max(10, 25, 17))  # Salida: 25

# Ejemplo 3: Máximo en una cadena (alfabéticamente)
print(max("Python"))  # Salida: y → porque 'y' es la letra con mayor valor Unicode

# Ejemplo 4: Usar key para cambiar el criterio
palabras = ["sol", "montaña", "mar", "cielo"]
print(max(palabras, key=len))  # Salida: montaña → es la palabra más larga

# Ejemplo 5: Usar default para evitar errores en listas vacías
vacia = []
print(max(vacia, default="Sin datos"))  # Salida: Sin datos
