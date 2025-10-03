"""
* Sets en Python: Conjuntos
----------------------------
- Un conjunto (set) es una colección desordenada y sin elementos repetidos.
- Los elementos de un set son únicos y mutables.
- Se definen utilizando llaves {} o con la función set().
- Pueden contener elementos de cualquier tipo de datos (enteros, cadenas, etc.).
- No tienen un orden particular, lo que significa que no se puede acceder a los elementos por `índice`.
- Internamente, Python utiliza una estructura de datos similar a un hashmap para la búsqueda rápida de elementos.
- Al igual que en otras colecciones, los conjuntos soportan `x in set`, `len(set)` y `for x in set`.
- los conjuntos no soportan indexado, ni operaciones de segmentado, ni otras capacidades propias de las secuencias.
- No pueden ser usados como claves de diccionarios ni como elementos de otros conjuntos.

Operaciones comunes con sets:
-----------------------------
- Creación de sets.
- Añadir y eliminar elementos.
- Comprobar la existencia de elementos.
- Realizar operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.
"""

# Creando un conjunto vacío usando el constructor set()
new_set = set()
print(new_set)  # Salida: set()

# IMPORTANTE: Las llaves vacías {} crean un diccionario, no un set
empty_dict = {}
print(empty_dict)  # Salida: {}
print(type(empty_dict))  # Salida: <class 'dict'>

# Creación de un set con elementos
sample_set = {1, 2, 3, 4, 5}
print(sample_set)  # Salida: {1, 2, 3, 4, 5}
print(type(sample_set))  # Salida: <class 'set'>

# Creando un set con elementos repetidos
repeated_set = {1, 2, 2, 3, 3, 4, 5}
print(repeated_set)  # Salida: {1, 2, 3, 4, 5}

# Añadir un único elemento a un set
new_set.add("Andres")
print(new_set)  # Salida: {'Andres'}

# Agregar un elemento duplicado
# El elemento no se agrega al set
new_set.add("Andres")
print(new_set)  # Salida: {'Andres'}

# Añadir múltiples elementos a un set
new_set.update([1, 2, 3])
print(new_set)  # Salida: {'Andres', 1, 2, 3}

# Crear una copia superficial de un set
copy_set = new_set.copy()
print(copy_set)  # Salida: {'Andres', 1, 2, 3}

# Eliminar un elemento existente de un set
new_set.remove("Andres")
print(new_set)  # Salida: {1, 2, 3}

# Eliminar sin error si el elemento no existe con discard()
new_set.discard("Andres")  # No lanza excepción
print("new_set:", new_set)  # Salida: {1, 2, 3}

# Comprobar si un elemento existe en un set
print("Andres" in new_set)  # Salida: False
print(1 in new_set)  # Salida: True

# Recorrer todos los elementos de un set
for element in new_set:
    print(element)  # Salida cada elemento del set en una línea diferente

# Vaciar el conjunto
new_set.clear()
print(new_set)  # Salida: set()

# -------------------------------
# * Operaciones entre conjuntos
# -------------------------------

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

# ------------------
# * Unión
# ------------------

# Combina los elementos de ambos conjuntos, eliminando duplicados
union_set = set_1.union(set_2)
print(union_set)  # Salida: {1, 2, 3, 4, 5}

# Unión utilizando el operador "|"
union_operator_set = set_1 | set_2
print("union_operator_set:", union_operator_set)  # Salida: {1, 2, 3, 4, 5}

# -----------------
# * Intersección
# -----------------

# Obtiene solo los elementos que están en los dos conjuntos
intersection_set = set_1.intersection(set_2)
print(intersection_set)  # Salida: {3}

# Intersección utilizando el operador "&"
print(set_1 & set_2)  # Salida: {3}

# ------------------
# * Diferencia
# ------------------

# Elementos que están en set1 pero no en set2
difference_set = set_1.difference(set_2)
print(difference_set)  # Salida: {1, 2}

# Usando el operador "-"
print(set_1 - set_2)  # Salida: {1, 2}

# --------------------------
# * Diferencia simétrica
# --------------------------

# Elementos que están en set1 o en set2, pero no en ambos
symmetric_difference_set = set_1.symmetric_difference(set_2)
print(symmetric_difference_set)  # Salida: {1, 2, 4, 5}

# Diferencia simétrica utilizando el operador "^"
print(set_1 ^ set_2)  # Salida: {1, 2, 4, 5}

# Verificar si un conjunto es subconjunto de otro
# (Es decir, si todos sus elementos están dentro del otro conjunto)
subset_set = {1, 2}
print(subset_set.issubset(set_1))  # Salida: True

# Verificar si un conjunto es superconjunto de otro
# (Es decir, si contiene todos los elementos del otro conjunto)
print(set_1.issuperset(subset_set))  # Salida: True

# frozenset: conjunto inmutable (no se puede modificar)
immutable_set = frozenset([1, 2, 3, 4])
print("Frozenset:", immutable_set)  # Salida: frozenset({1, 2, 3, 4})
