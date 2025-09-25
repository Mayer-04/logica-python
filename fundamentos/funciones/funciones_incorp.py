"""
* Funciones Incorporadas en Python
----------------------------------
Las funciones incorporadas en Python son aquellas que ya vienen definidas dentro del propio lenguaje.
Estas funciones permiten realizar diversas operaciones como manipular datos, efectuar cálculos matemáticos,
interactuar con el usuario, etc.

Estas funciones están disponibles de forma nativa en Python,
por lo que no requieren importar módulos adicionales.
"""

# Función incorporada `print()`
# Imprime una cadena de texto o cualquier otro tipo de dato en la consola.
print("Hola, mundo")  # Salida: Hola, mundo

# Función incorporada `type()`
# Retorna el tipo de dato de un objeto dado.
print(type("Hola, mundo"))  # Salida: <class 'str'>

# Función incorporada `len`
# Retorna la longitud (número de caracteres) de una cadena de texto o elementos de una secuencia.
print(len("Hola, mundo"))  # Salida: 10

# Función incorporada `max()`
# Retorna el valor máximo de una lista o cualquier otro iterable.
print(max([1, 2, 3, 4, 5]))  # Salida: 5

# Función incorporada `min()`
# Retorna el valor mínimo de una lista o cualquier otro iterable.
print(min([1, 2, 3, 4, 5]))  # Salida: 1

# Función incorporada `sum()`
# Suma todos los elementos de una lista o cualquier otro iterable que contenga números.
print(sum([1, 2, 3, 4, 5]))  # Salida: 15

# Función incorporada `range()`
# Genera una secuencia de números dentro de un rango especificado.
# El resultado debe convertirse en lista para poder visualizarse.
print(list(range(1, 6)))  # Salida: [1, 2, 3, 4, 5]

# Función incorporada `abs()`
# Retorna el valor absoluto de un número (sin signo).
print(abs(-5))  # Salida: 5

# Función incorporada `pow()`
# Calcula la potencia de un número dado. `pow(base, exponente)`
print(pow(2, 3))  # Salida: 8 (2^3)

# Función incorporada `round()`
# Redondea un número al número de decimales especificado.
print(round(3.141592653589793, 2))  # Salida: 3.14

# Función incorporada `reversed()`
# Invierte el orden de los elementos de una lista o cualquier otro iterable.
# El resultado debe convertirse en lista para poder visualizarse.
print(list(reversed([1, 2, 3, 4, 5])))  # Salida: [5, 4, 3, 2, 1]

# Función incorporada `filter()`
# Filtra los elementos de una lista o iterable usando una función condicional.
# En este caso, filtra los números pares de la lista.
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))  # Salida: [2, 4, 6]

# Función incorporada `map()`
# Aplica una función a cada elemento de una lista o iterable. Devuelve un objeto de tipo `map` que es un iterable
# El objeto `map` no contiene los resultados directamente, sino que está diseñado para generarlos cuando se itera sobre el.
# En este ejemplo, multiplica cada número por 2.
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5, 6])))  # Salida: [2, 4, 6, 8, 10, 12]

# Función `isinstance()`
# Verifica si un objeto es de un tipo especificado.
print(isinstance(5, int))  # Salida: True
print(isinstance("Hola", str))  # Salida: True
print(isinstance(True, bool))  # Salida: True
print(isinstance("Andres", float))  # Salida: False

# Función incorporada `id()`
# Devuelve la `identidad` de un objeto.
# Se trata de un `número entero` que se garantiza que será `único` para este objeto durante su vida.
print(id("Hola"))  # Salida: 2313322522224
print(id(3))  # Salida: 140734135859704

# Función incorporada `any()`
# Verifica si al menos uno de los elementos de una secuencia (iterables) es `verdadero`.
print(any([False, False, False]))  # Salida: False
print(any([False, True, False]))  # Salida: True

# Función incorporada `all()`
# Verifica si todos los elementos de una secuencia (iterables) son `verdadero`.
print(all([True, True, True]))  # Salida: True
print(all([True, False, True]))  # Salida: False

# Función incorporada `input()`
# Permite al usuario introducir datos a través de la consola.
# El valor ingresado por el usuario es de tipo cadena.
nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")  # Salida: Hola, [nombre del usuario]

# Función incorporada `help()`
# Muestra la documentación de una función o módulo, proporcionando detalles sobre su uso.
help(print)
