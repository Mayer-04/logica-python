"""
* List Comprehension (Comprensión de Listas)
---------------------------------------------
- Permite crear listas de forma rápida y eficiente.
- Es una forma concisa y elegante de crear listas a partir de `iterables existentes`.
- Es una alternativa más legible y eficiente a los bucles tradicionales para generar listas.
- Se pueden incluir condiciones para filtrar elementos.
- Pueden ser usado también para `tuplas`, `conjuntos`, `diccionarios` y `cadenas de texto`.
- Es una característica tomada de la `programación funcional` específicamente del lenguaje 'Haskell'.

¿Cuándo usarlas?
----------------
- Para transformar elementos de un iterable (mapeo).
- Para filtrar elementos que cumplan ciertas condiciones.
- Para crear listas a partir de rangos, cadenas, otros iterables.
- Cuando el código resultante es más claro que un bucle tradicional.

Sintaxis Fundamental:
--------------------
[expresión for variable in iterable]                                # Básica
[expresión for variable in iterable if condición]                   # Con filtro
[expresión for variable in iterable if condición1 and condición2]   # Con varias condiciones

Componentes explicados:
-----------------------
- expresión: Es lo que se va a almacenar o devolver en la nueva lista
  (puede ser la variable original o una transformación).
- variable: Variable temporal que representa cada elemento durante la iteración.
- iterable: Secuencia u objeto que se puede recorrer (lista, tupla, rango, cadena, etc.).
- condición (opcional): Expresión booleana que filtra qué elementos incluir.

Orden de ejecución (se lee de izquierda a derecha):
------------------------------------------------------
1. `for variable in iterable` - Se itera sobre cada elemento
2. `if condición` - Se evalúa la condición (si existe)
3. `expresión` - Se evalúa y agrega a la lista resultante

Consideraciones:
----------------
- Legibilidad: Código más conciso y expresivo.
- Rendimiento: Generalmente más rápidas que bucles equivalentes.
- Memoria: Más eficientes en términos de memoria.
- Funcional: Estilo de programación más funcional y declarativo.

Buenas prácticas:
------------------
- Mantén las expresiones simples y legibles.
- Usa nombres de variables descriptivos.
- Para lógica compleja, considera usar `funciones auxiliares`.
- Si la línea es muy larga, considera un bucle tradicional (for).
"""

# Crear una lista a partir de otra
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nueva_lista = [i for i in lista]
print("Lista nueva:", nueva_lista)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear una lista por comprensión de números del 0 al 9
# En la lista numeros `x` va ser cada uno de los elementos de `range(10)`
numeros = [x for x in range(10)]
print("Lista de números del 0 al 9:", numeros)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Aplicar una expresión para transformar elementos
# En la lista cuadrados `x` va ser cada uno de los elementos de `range(10)` elevados al cuadrado
cuadrados = [x**2 for x in range(10)]
print(
    "Cuadrados de números del 0 al 9:", cuadrados
)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ----------------------------
# * Condición de comprensión
# ----------------------------
# Usar condiciones para filtrar elementos y ponerlos en una nueva lista,
# Aquí se genera una lista con números pares del 0 al 9.
# La forma de leer este código es: Tomamos la variable `x` para cada uno de los elementos del rango entre 0 y 9,
# si el resto de la división entre `x` y `2` es `0` entonces `x` es par, almacenarlo en la variable `pares`.
pares = [x for x in range(10) if x % 2 == 0]

# ---------------------------
# * Comprensión de Tuplas
# ---------------------------
# Crear una tupla con los números del 0 al 4, cada uno elevado al cuadrado
# Nos devuelve un generador
cuadrados_tupla = (x**2 for x in range(5))
print(
    "Tupla de cuadrados:", cuadrados_tupla
)  # Salida: <generator object <genexpr> at 0x7738bebeab50>

# Para obtener la tupla, necesitas convertir el generador a una tupla
cuadrados_tupla = tuple(x**2 for x in range(5))
print("Tupla de cuadrados:", cuadrados_tupla)  # Salida: (0, 1, 4, 9, 16)

# --------------------------------------
# * Comprensión de Diccionarios
# --------------------------------------
# Crear un diccionario donde las claves son números del 0 al 4 y los valores son sus cuadrados
cuadrados_dict = {x: x**2 for x in range(5)}
print(
    "Diccionario de cuadrados:", cuadrados_dict
)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Crear un diccionario con números pares y su cuadrado
pares_cuadrados_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(
    "Diccionario de números pares y sus cuadrados:", pares_cuadrados_dict
)  # Salida: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# -----------------------------------
# * Compresión de Conjuntos (Sets)
# -----------------------------------
# Crear un set con los números del 0 al 4, cada uno elevado al cuadrado
cuadrados_set = {x**2 for x in range(5)}
print("Set de cuadrados:", cuadrados_set)  # Salida: {0, 1, 4, 9, 16}

# Crear un set con números pares del 0 al 9
pares_set = {x for x in range(10) if x % 2 == 0}
print("Set de números pares:", pares_set)  # Salida: {0, 2, 4, 6, 8}

# -----------------------------------
# * Compresión de Cadenas (Strings)
# -----------------------------------
# Se utiliza la función `join` para unir los elementos de una lista en una cadena
# Crear una cadena con los números del 0 al 4, cada uno elevado al cuadrado
cuadrados_str = "".join([str(x**2) for x in range(5)])
print("Cadena de cuadrados:", cuadrados_str)  # Salida: "01234"

# Crear una cadena con los caracteres de la cadena original duplicados
cadena = "abc"
duplicados = "".join([c * 2 for c in cadena])
print("Caracteres duplicados:", duplicados)  # Salida: "aabbcc"
