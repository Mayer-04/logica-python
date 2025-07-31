"""
* Sets en Python: Conjuntos
----------------------------
- Un conjunto (set) es una colección desordenada y sin elementos repetidos.
- Los elementos de un set son únicos y mutables.
- Se definen utilizando llaves {} o la función set().
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

# Creando un conjunto utilizando el constructor `set()` - Conjunto vacío.
new_set = set()
print(new_set)  # Imprime: set()

# Inicialmente, las llaves vacías {} definen un diccionario, no un set
empty_dict = {}
print(empty_dict)  # Imprime: {}
print(type(empty_dict))  # Imprime: <class 'dict'>

# Creación de un set con elementos
sample_set = {1, 2, 3, 4, 5}
print(sample_set)  # Imprime: {1, 2, 3, 4, 5}
print(type(sample_set))  # Imprime: <class 'set'>

# Añadir un único elemento a un set
new_set.add("Andres")
print(new_set)  # Imprime: {'Andres'}

# Intentar agregar un elemento duplicado no cambia el set
new_set.add("Andres")
print(new_set)  # Imprime: {'Andres'}

# Añadir múltiples elementos a un set
new_set.update([1, 2, 3])
print(new_set)  # Imprime: {'Andres', 1, 2, 3}

# Crear una copia superficial de un set
copy_set = new_set.copy()
print(copy_set)  # Imprime: {'Andres', 1, 2, 3}

# Eliminar un elemento existente de un set
new_set.remove("Andres")
print(new_set)  # Imprime: {1, 2, 3}

# Intentar eliminar un elemento no existente sin generar un error
new_set.discard("Andres")
print(new_set)  # Imprime: {1, 2, 3}

# Comprobar si un elemento existe en un set
print("Andres" in new_set)  # Imprime: False
print(1 in new_set)  # Imprime: True

# Recorrer todos los elementos de un set
for element in new_set:
    print(element)  # Imprime cada elemento del set en una línea diferente

# Limpiar todos los elementos de un set
new_set.clear()
print(new_set)  # Imprime: set()

# Realizar la unión de dos sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Imprime: {1, 2, 3, 4, 5}

# Unión de sets utilizando el operador |
union_operator_set = set1 | set2
print("union_operator_set:", union_operator_set)  # Imprime: {1, 2, 3, 4, 5}

# Intersección de sets utilizando el operador &
intersection_operator_set = set1 & set2
print("intersection_operator_set:", intersection_operator_set)  # Imprime: {3}

# Realizar la intersección de dos sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Imprime: {3}

# Verificar si un set es subconjunto de otro
subset_set = {1, 2}
print(subset_set.issubset(set1))  # Imprime: True

# Verificar si un set es superconjunto de otro
print(set1.issuperset(subset_set))  # Imprime: True

# Diferencia entre dos sets (elementos presentes en set1 pero no en set2)
difference_set = set1.difference(set2)
print(difference_set)  # Imprime: {1, 2}

# Diferencia simétrica entre dos sets (elementos presentes en set1 o en set2 pero no en ambos)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Imprime: {1, 2, 4, 5}

# Uso de frozenset para crear conjuntos inmutables
# Un frozenset es un set que no se puede modificar una vez creado
immutable_set = frozenset([1, 2, 3, 4])
print("Frozenset:", immutable_set)  # Imprime: frozenset({1, 2, 3, 4})
