"""
* List Comprehension (Comprensión de Listas)
---------------------------------------------
- Permite crear listas de forma rápida y eficiente.
- Se basa en una sintaxis compacta para generar listas a partir de iterables.
- Facilita la creación de listas a partir de listas ya existentes, o incluso de rangos de números, cadenas, etc.
- Se pueden incluir condiciones para filtrar elementos.
- Pueden ser usado también para tuplas, conjuntos, diccionarios y cadenas de texto.
- Es una característica tomada de la `programación funcional` específicamente del lenguaje 'Haskell'.

Sintaxis:
----------
[expresión `for` variable `in` iterable `if` condición]

- Expresión: Es lo que se va a almacenar o devolver en cada iteración. 
Puede ser la misma variable o algún valor modificado de ella.
- Variable: Es la variable que se usará en cada iteración para referirse a cada elemento del `iterable`.
- Iterable: Es el objeto que se va a iterar. Puede ser una lista, un conjunto, un diccionario, una cadena de texto, etc.
- Condición: Es una expresión que se evaluará para decidir si incluir o no el valor de esa iteración. Es opcional.

Características principales:
----------------------------
- Sintaxis compacta y legible.
- Puede incluir expresiones y condiciones.
- Mejor rendimiento en comparación con bucles tradicionales.
"""

# Crear una lista a partir de otra
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nueva_lista = [i for i in lista]
print("Lista nueva:", nueva_lista)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear una lista por comprensión de números del 0 al 9
# En la lista numeros `x` va ser cada uno de los elementos de `range(10)`
numeros = [x for x in range(10)]
print("Lista de números del 0 al 9:", numeros)  # Imprime [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Aplicar una expresión para transformar elementos
# En la lista cuadrados `x` va ser cada uno de los elementos de `range(10)` elevados al cuadrado
cuadrados = [x**2 for x in range(10)]
print(
    "Cuadrados de números del 0 al 9:", cuadrados
)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# * Condición de comprensión
# Usar condiciones para filtrar elementos y ponerlos en una nueva lista
# Aquí se genera una lista con números pares del 0 al 9.
# La forma de leer este código es: Tomamos la variable `x` para cada uno de los elementos del rango entre 0 y 9,
# si el resto de la división entre `x` y `2` es `0` entonces `x` es par, almacenarlo en la variable `pares`.
pares = [x for x in range(10) if x % 2 == 0]


# * Comprensión de Tuplas
# Crear una tupla con los números del 0 al 4, cada uno elevado al cuadrado
cuadrados_tupla = (x**2 for x in range(5))
print(
    "Tupla de cuadrados:", cuadrados_tupla
)  # Imprime <generator object <genexpr> at 0x000001B964AD3780>

# Para obtener una tupla, necesitas convertir el generador a una tupla
cuadrados_tupla = tuple(x**2 for x in range(5))
print("Tupla de cuadrados:", cuadrados_tupla)  # Imprime (0, 1, 4, 9, 16)

# * Comprensión de Diccionarios
# Crear un diccionario donde las claves son números del 0 al 4 y los valores son sus cuadrados
cuadrados_dict = {x: x**2 for x in range(5)}
print(
    "Diccionario de cuadrados:", cuadrados_dict
)  # Imprime {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Crear un diccionario con números pares y su cuadrado
pares_cuadrados_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(
    "Diccionario de números pares y sus cuadrados:", pares_cuadrados_dict
)  # Imprime {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# * Compresión de Conjuntos (Sets)
# Crear un set con los números del 0 al 4, cada uno elevado al cuadrado
cuadrados_set = {x**2 for x in range(5)}
print("Set de cuadrados:", cuadrados_set)  # Imprime {0, 1, 4, 9, 16}

# Crear un set con números pares del 0 al 9
pares_set = {x for x in range(10) if x % 2 == 0}
print("Set de números pares:", pares_set)  # Imprime {0, 2, 4, 6, 8}


# * Compresión de Cadenas (Strings)
# Se utiliza la función `join` para unir los elementos de una lista en una cadena
# Crear una cadena con los números del 0 al 4, cada uno elevado al cuadrado
cuadrados_str = "".join([str(x**2) for x in range(5)])
print("Cadena de cuadrados:", cuadrados_str)  # Imprime "01234"


# Crear una cadena con los caracteres de la cadena original duplicados
cadena = "abc"
duplicados = "".join([c * 2 for c in cadena])
print("Caracteres duplicados:", duplicados)  # Imprime "aabbcc"
