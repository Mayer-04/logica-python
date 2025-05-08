"""
* Tuplas en Python: Secuencia
------------------------------
- Una tupla es una colección ordenada e inmutable de elementos.
- Las tuplas se definen utilizando paréntesis ().
- No es posible borrar (ni añadir) un elemento en una tupla, lo que provocará una excepción.
- Pueden contener elementos de cualquier tipo de datos (enteros, cadenas, listas, etc.).
- Una vez creada, no se pueden modificar (no se pueden añadir, eliminar o cambiar elementos).
- Son útiles para almacenar datos que no deben cambiar a lo largo de la ejecución del programa.
- Son más eficientes en términos de memoria y tiempo de ejecución en comparación con las listas.
- Si necesitas una estructura inmutable con un tamaño fijo y sabes los valores desde el principio,
una tupla es apropiada.

Métodos y operaciones comunes en tuplas:
----------------------------------------
- in: Verifica si un elemento está en la tupla.
- Concatenación `+`: Une dos o más tuplas.
- Repetición `*`: Repite los elementos de una tupla un número específico de veces.
- Slicing: Permite obtener una sub-tupla.
- count(): Devuelve el número de veces que un valor especificado aparece en la tupla.
- index(): Devuelve el índice de la primera aparición de un valor especificado.
- len(): Devuelve la longitud de la tupla.
"""

# Creando una tupla utilizando el contructor `tuple()`
my_tuple = tuple()
print("Tupla vacía utilizando tuple():", my_tuple)  # Imprime ()

# Crear una tupla vacía utilizando paréntesis
empty_tuple = ()
print("Tupla vacía utilizando paréntesis:", empty_tuple)  # Imprime ()

# Crear una tupla con elementos
numbers = (1, 2, 3, 4)
print("Tupla con elementos:", numbers)  # Imprime (1, 2, 3, 4)

# Acceder a los elementos de una tupla usando índices (positivo y negativo)
print("Primer elemento:", numbers[0])  # Imprime 1
print("Último elemento:", numbers[-1])  # Imprime 4

# Desestructurar una tupla en variables individuales (Desempaquetado de tuplas)
a, b, c, d = numbers
print("Elementos desempaquetados:", a, b, c, d)  # Imprime 1 2 3 4

# Desempaquetado avanzado con * para capturar el resto de los elementos
tupla_grande = (1, 2, 3, 4, 5, 6)
x, y, *resto = tupla_grande
print(
    "Desempaquetado con resto:", "x:", x, "y:", y, "resto:", resto
)  # Imprime x: 1 y: 2 resto: [3, 4, 5, 6]

# Desempaquetado omitiendo el resto de los elementos
x, y, *_ = tupla_grande
print("Desempaquetado omitiendo resto:", "x:", x, "y:", y)  # Imprime x: 1 y: 2

# Contar las apariciones de un elemento en la tupla usando count()
print("Apariciones del 3:", numbers.count(3))  # Imprime 1

# Encontrar el índice de un elemento en la tupla usando index()
print("Índice del número 3:", numbers.index(3))  # Imprime 2

# Obtener la longitud de una tupla usando len()
print("Longitud de la tupla:", len(numbers))  # Imprime 4

# Concatenar dos tuplas utilizando el operador `+`
new_tuple = numbers + (5, 6, 7)
print("Tupla concatenada:", new_tuple)  # Imprime (1, 2, 3, 4, 5, 6, 7)

# Repetir los elementos de una tupla utilizando el operador *
new_copy = numbers * 3
print("Tupla repetida:", new_copy)  # Imprime (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# Obtener una sub-tupla usando slicing
print("Sub-tupla con slicing:", new_copy[:4])  # Imprime (1, 2, 3, 4)

# Sub-tupla 2
print("Sub-tupla 2:", new_copy[1:4])  # Imprime (2, 3, 4)

# Convertir una tupla a lista usando list() - Útil si necesitas modificar los datos
new_list = list(numbers)
print("Tupla convertida a lista:", new_list)  # Imprime [1, 2, 3, 4]

# Comprobar si un elemento existe en una tupla utilizando in
print("¿El 3 está en la tupla?", 3 in numbers)  # Imprime True
print("¿El 5 está en la tupla?", 5 in numbers)  # Imprime False

# Iterar a través de los elementos de una tupla usando un bucle for
print("Iterando a través de la tupla:")
for number in numbers:
    print(number)

# Usar tuplas como claves en diccionarios (ya que son inmutables)
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris",
}
print("Diccionario con tuplas como claves:", locations)

# Acceso a valores en un diccionario usando tuplas como claves
tokyo_location = (35.6895, 139.6917)
print("Ciudad para la clave", tokyo_location, ":", locations[tokyo_location])

# Anidar tuplas
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Anidamiento de tuplas:", nested_tuple)
