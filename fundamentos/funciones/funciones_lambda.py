"""
* Funciones lambda
    - Una función lambda es una función anónima, es decir, una función que no necesita un nombre explícito.
    - Se define usando la palabra reservada `lambda`.
    - Se usan para crear funciones pequeñas y rápidas sin necesidad de escribir una definición completa con `def`.
    - Provienen de la programación funcional.
    - Se pueden guardar en variables o pasar directamente como argumento a otras funciones.
    - Son muy comunes junto con funciones como `map()`, `filter()` y `reduce()`.
    - Devuelve automáticamente el valor de esa expresión (retorno implícito).

    Sintaxis:
        lambda argumentos: expresión

Buenas prácticas:
-----------------
- Una función lambda debe ser corta y clara. Si supera los 2-3 elementos lógicos, mejor usar `def`.
- Usarlas para funciones de paso rápido.
- Usar anotaciones de tipo cuando sea útil.
"""

from typing import Callable  # Importa Callable para definir tipos de funciones
from functools import reduce  # Trabajar con funciones y para la programación funcional

# Ejemplo básico de función lambda que suma dos números
sumar = lambda num1, num2: num1 + num2
print(sumar(2, 3))  # Salida: 5

# Ejemplo con anotaciones de tipo: esta lambda recibe dos enteros y devuelve un entero
restar: Callable[[int, int], int] = lambda a, b: a - b
print(restar(4, 2))  # Salida: 2

# Lambda con un valor por defecto en el parámetro
saludar = lambda nombre="Mundo": f"Hola, {nombre}!"
print(saludar())  # Salida: Hola, Mundo!
print(saludar("Mayer"))  # Salida: Hola, Mayer!

# Ordenar una lista con sort() usando lambda como clave
lista = [5, 3, 8, 1]
lista.sort(key=lambda x: x)  # Ordena por el valor mismo
print(lista)  # Salida: [1, 3, 5, 8]

# Ordenar lista de tuplas por el segundo elemento usando lambda
datos = [("Mayer", 25), ("Andres", 30), ("Luis", 20)]
datos.sort(key=lambda x: x[1])  # Ordena por la edad (índice 1 de cada tupla)
print(datos)  # Salida: [('Luis', 20), ('Mayer', 25), ('Andres', 30)]

# Ordenar por varias claves (edad y luego nombre)
personas = [("Juan", 25), ("Ana", 30), ("Pedro", 20), ("Ana", 20)]
ordenadas = sorted(personas, key=lambda x: (x[1], x[0]))
print(ordenadas)
# Salida: [('Ana', 20), ('Pedro', 20), ('Juan', 25), ('Ana', 30)]

# Usar lambda con map(): aplica una operación a cada elemento de la lista
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))  # Eleva cada número al cuadrado
print(cuadrados)  # Salida: [1, 4, 9]

# Usar lambda con filter(): filtra elementos que cumplan una condición
pares = list(filter(lambda x: x % 2 == 0, range(10)))  # Solo números pares
print(pares)  # Salida: [0, 2, 4, 6, 8]

# Uso avanzado: lambda con el operador walrus (:=) en comprensiones de listas
# Calcula la raíz cuadrada de cada número y guarda solo las que sean mayores que 3
datos_complejos = [1, 4, 9, 16, 25, 36, 49]
resultados = [y for x in datos_complejos if (y := (lambda n: n**0.5)(x)) > 3]
print(f"Raíces mayores a 3: {resultados}")  # Raíces mayores a 3: [4.0, 5.0, 6.0, 7.0]

# Clasificar números como 'Par' o 'Impar' usando if-else en una lambda
clasificar = lambda x: "Par" if x % 2 == 0 else "Impar"
print(clasificar(3))  # Salida: Impar
print(clasificar(8))  # Salida: Par

# Multiplicar todos los elementos de la lista
numeros = [1, 2, 3, 4]
producto = reduce(lambda a, b: a * b, numeros)
print(producto)  # Salida: 24

# Diccionario de operaciones con funciones lambda
operaciones = {
    "sumar": lambda a, b: a + b,
    "restar": lambda a, b: a - b,
    "multiplicar": lambda a, b: a * b,
}
print(operaciones["sumar"](5, 3))  # Salida: 8
print(operaciones["multiplicar"](5, 3))  # Salida: 15
