# =====================================
# * Función incorporada min()
# =====================================
# La función min() devuelve el elemento más pequeño de un iterable
# (lista, tupla, conjunto, cadena, etc.).
#
# Forma general:
# min(iterable, *[, key, default])
# O bien:
# min(valor1, valor2, valor3, ...)
#
# Parámetros más usados:
# - iterable: secuencia de elementos comparables.
# - key (opcional): función que define el criterio de comparación.
# - default (opcional): valor a devolver si el iterable está vacío.

# Ejemplo 1: Mínimo en una lista
print(min([1, 2, 3, 4, 5]))  # Salida: 1

# Ejemplo 2: Mínimo entre varios valores sueltos
print(min(10, 25, 17))  # Salida: 10

# Ejemplo 3: Mínimo en una cadena (alfabéticamente)
print(min("Python"))  # Salida: P → es la letra con menor valor Unicode

# Ejemplo 4: Usar key para cambiar el criterio
palabras = ["sol", "montaña", "mar", "cielo"]
print(min(palabras, key=len))  # Salida: sol → es la palabra más corta

# Ejemplo 5: Usar default para evitar errores en listas vacías
vacia = []
print(min(vacia, default="Sin datos"))  # Salida: Sin datos
