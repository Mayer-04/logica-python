"""
* Listas en Python: Secuencia
------------------------------
Una lista en Python es una colección ordenada y mutable de elementos.

Características de las listas:
-------------------------------
- Se definen usando corchetes: `[]`.
- Son equivalentes a los arrays o vectores en otros lenguajes de programación.
- Pueden contener elementos de `diferentes tipos`: números, cadenas, booleanos, otras listas, objetos, etc.
- Son mutables, lo que significa que sus elementos pueden modificarse después de la creación.
- Soportan listas anidadas (listas dentro de listas), permitiendo la creación de estructuras complejas como matrices.
- Son iterables, es decir, se pueden recorrer usando bucles como `for`.
- Se pueden concatenar con el operador `+` y repetir con el operador `*`.
- Internamente, las listas son objetos de la clase `list`, que utiliza arreglos dinámicos para gestionar su tamaño.
- Puedes crear una lista vacía o convertir otros iterables en lista usando la función `list()`.
- Es posible convertir listas en otros tipos de datos, como:
  - `tuple` (tupla)
  - `set` (conjunto)
  - `dict` (diccionario, si los elementos son pares clave-valor)
  - `str` (cadena, si todos los elementos son cadenas)


⚠️ Importante:
Asignar una lista a otra variable `no crea una copia`, sino que ambas variables `apuntan a la misma lista`.
Para copiar una lista correctamente, usa `copy()` o slicing (`lista[:]`).

Rendimiento y buenas prácticas:
-------------------------------
- Para agregar `múltiples elementos` a una lista, usa `extend()` o `+=` en lugar de `+`,
  ya que son más eficientes.
- Si solo necesitas agregar un único elemento, `append()` es la opción más directa y rápida.
- El acceso por `slicing` (`lista[1:4]`) es seguro y no genera errores si los índices
  están fuera del rango permitido (aunque puede retornar una lista vacía).
- El operador `+=` es más eficiente que `+` cuando se trabaja con listas o cadenas,
  ya que modifica la lista existente en lugar de crear una nueva.

Métodos comunes de las listas:
-------------------------------
- `append(x)`: Agrega `x` al final de la lista.
- `extend(iterable)`: Agrega todos los elementos de un iterable (como otra lista) al final de la lista.
- `insert(i, x)`: Inserta `x` en la posición `i`.
- `remove(x)`: Elimina la primera aparición de `x`.
- `pop([i])`: Elimina y retorna el elemento en la posición `i`. Si no se especifica, elimina el último.
- `clear()`: Elimina todos los elementos de la lista.
- `index(x[, start[, end]])`: Retorna el índice de la primera aparición de `x`. 
  Puede limitarse a un rango con `start` y `end`.
- `count(x)`: Cuenta cuántas veces aparece `x` en la lista.
- `sort(key=None, reverse=False)`: Ordena la lista en su lugar. 
  Se puede personalizar con una función `key` o invertir con `reverse=True`.
- `reverse()`: Invierte el orden de los elementos.
- `copy()`: Devuelve una `copia superficial` de la lista (los elementos no se duplican, solo la estructura).
"""

# Crear una lista vacía utilizando la función list()
new_list = list()
print("Lista vacía usando list():", new_list)  # Salida: []

# Crear una lista vacía utilizando corchetes []
empty_list = []
print("Lista vacía usando corchetes []:", empty_list)  # Salida: []

# Crear una lista con elementos enteros
numbers = [1, 2, 3, 4, 5]
print("Lista de enteros:", numbers)  # Salida: [1, 2, 3, 4, 5]

# Crear una lista con elementos de diferentes tipos de datos
# Nota: No se recomienda hacer este tipo de listas en Python
mixed_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(
    "Lista con diferentes tipos:", mixed_list
)  # Salida: [1, "Hello", 3.14, True, [1, 2, 3]]

# Acceder a los elementos de una lista usando índices
print("Primer elemento:", mixed_list[0])  # Salida: 1
print("Segundo elemento:", mixed_list[1])  # Salida: "Hello"
print("Último elemento:", mixed_list[-1])  # Salida: [1, 2, 3]
print("Primer elemento de la lista anidada:", mixed_list[-1][0])  # Salida: 1

# Obtener la longitud de una lista usando len()
print("Longitud de la lista numbers:", len(numbers))  # Salida: 5

# Modificar un elemento de una lista usando su índice
numbers[0] = 10
print("Lista modificada:", numbers)  # Salida: [10, 2, 3, 4, 5]

# Concatenar dos listas utilizando el operador +
numbers = numbers + [6, 7, 8]
print("Listas concatenadas:", numbers)  # Salida: [10, 2, 3, 4, 5, 6, 7, 8]

# Crear una lista con tamaño predefinido
# Crea una lista de 2 elementos (inicialmente con valores 'None')
list_pre = [None] * 2
list_pre[0] = 2
list_pre[1] = 4
print("Lista con tamaño predefinido:", list_pre)

# Desempaquetar una lista en variables individuales
a, b, c, d, e = mixed_list
print(
    "Elementos desempaquetados:", a, b, c, d, e
)  # Salida: 1 Hello 3.14 True [1, 2, 3]

# Copiar una lista usando el método copy()
new_copy = numbers.copy()
print("Copia de la lista numbers:", new_copy)  # Salida: [10, 2, 3, 4, 5, 6, 7, 8]

# Añadir un elemento al final de una lista usando append()
empty_list.append("Hello")
print("Lista después de append():", empty_list)  # Salida: ["Hello"]

# Insertar un elemento en una posición específica de la lista usando insert()
numbers.insert(0, 0)
print("Lista después de insert(0, 0):", numbers)  # Salida: [0, 10, 2, 3, 4, 5, 6, 7, 8]

# Añadir varios elementos a una lista usando extend()
# Nota: extend() espera un iterable
empty_list.extend("Python")
print(
    "Lista después de extend():", empty_list
)  # Salida: ["Hello", "P", "y", "t", "h", "o", "n"]

# Remover el primer elemento que coincide con el valor especificado usando remove()
numbers.remove(10)
print("Lista después de remove(10):", numbers)  # Salida: [0, 2, 3, 4, 5, 6, 7, 8]

# Remover y retornar el último elemento de una lista usando pop()
last_element = numbers.pop()
print("Elemento eliminado con pop():", last_element)  # Salida: 8
print("Lista después de pop():", numbers)  # Salida: [0, 2, 3, 4, 5, 6, 7]

# Eliminar un elemento de una lista por su índice usando del
del numbers[0]
print("Lista después de del numbers[0]:", numbers)  # Salida: [2, 3, 4, 5, 6, 7]

"""
Slicing (subdivisión de secuencias) en Python
---------------------------------------------
Sintaxis: sequence[start:stop:step]
Parámetros:
- start: Índice donde comienza el slicing (opcional, por defecto 0).
- stop: Índice donde se detiene el slicing (exclusivo, por defecto final de la secuencia).
- step: Paso o intervalo entre los elementos seleccionados (opcional, por defecto 1).
Notas:
- Si no se especifica `start`, se toma el inicio de la secuencia (o el final si step es negativo).
- Si no se especifica `stop`, se toma el final de la secuencia (o el inicio si step es negativo).
- Si `step` es negativo, la secuencia se recorre en orden inverso.
"""

slicing_example = [2, 3, 4, 5, 6, 7]

# Obtener los primeros 3 elementos de la lista
print("Primeros 3 elementos:", slicing_example[:3])  # Salida: [2, 3, 4]

# Obtener los últimos 3 elementos de la lista
print("Últimos 3 elementos:", slicing_example[-3:])  # Salida: [5, 6, 7]

# Slicing con saltos: selecciona elementos desde el índice 1 hasta el 5 (exclusive), con un salto de 2
print("Elementos con salto de 2:", slicing_example[1:5:2])  # Salida: [3, 5]

# Ejemplo de slicing extendido
extended_slicing = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Selecciona elementos a partir del índice 1 hasta el final, con un salto de 3
result = extended_slicing[1::3]
print("Slicing extendido:", result)  # Salida: [20, 50, 80]

# Selecciona elementos de la lista en orden inverso con un salto de 2
reversed_slicing = extended_slicing[::-2]
print(
    "Slicing extendido en orden inverso:", reversed_slicing
)  # Salida: [90, 70, 50, 30, 10]

# Operaciones adicionales con listas
# ----------------------------------

# clear() elimina todos los elementos de una lista
numbers.clear()
print("Lista después de clear():", numbers)  # Salida: []

# Uso del método index() para encontrar la posición o índice de un elemento
fruits = ["apple", "banana", "cherry"]
print("Índice de 'cherry' en fruits:", fruits.index("cherry"))  # Salida: 2

# Contar las apariciones de un elemento en la lista usando count()
print("Número de apariciones de 'apple':", fruits.count("apple"))  # Salida: 1

# sort() ordena los elementos de una lista de menor a mayor in-place
fruits.sort()
print("Lista fruits ordenada:", fruits)  # Salida: ['apple', 'banana', 'cherry']

# Para ordenar de mayor a menor con sort() usamos reverse=True
fruits.sort(reverse=True)
print(
    "Lista fruits ordenada de mayor a menor:", fruits
)  # Salida: ['cherry', 'banana', 'apple']

# Invertir el orden de los elementos de una lista usando reverse()
fruits.reverse()
print("Lista fruits invertida:", fruits)  # Salida: ['apple', 'banana', 'cherry']

# Iterar a través de los elementos de una lista usando un bucle for
for fruit in fruits:
    print(fruit)

# Crear una lista por comprensión de números del 0 al 9
numbers = [x for x in range(10)]
print("Lista de números del 0 al 9:", numbers)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Crear una lista de listas - Matrices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3:", matrix)  # Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acceder a elementos en una lista de listas
element = matrix[1][2]
print("Elemento en la posición [1][2] de la matriz:", element)  # Salida: 6

# Asignar una lista a una variable (paso por referencia)
numbers = [1, 2, 3, 4, 5]
new_numbers = numbers  # Asignar la lista `numbers` a la nueva variable `new_numbers`
new_numbers.append(6)
print(
    "numbers después de modificar new_numbers:", numbers
)  # Salida: [1, 2, 3, 4, 5, 6]

# Desempaquetar elementos dentro de una lista con el operador *
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print("Lista combinada:", combined_list)  # Salida: [1, 2, 3, 4, 5, 6]

# Agregar múltiples valores a una lista con el operador +=
list1 += [7, 8, 9]
print("Lista extendida:", list1)  # Salida: [1, 2, 3, 7, 8, 9]

# Iterar dos listas a la vez con la función zip()
# Nota: zip() se detendrá cuando la lista más corta se agote
for item1, item2 in zip(list1, list2):
    print(f"{item1} - {item2}")
