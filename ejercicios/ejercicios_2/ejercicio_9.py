"""
Escribe un programa que seleccione y muestre un elemento al azar de una lista dada.

Restricción:
-------------
- No uses la función `random.choice()`.
- Implementa tu propia lógica usando `random.randint()` o `random.random()`.

Ejemplo:
---------
lista = ["limon", "coco", "naranja", "uva"]
# El programa debe seleccionar uno al azar
"""

from random import randint, choice

frutas = ["limon", "coco", "naranja", "uva"]


def mostrar_aleatorio(frutas: list[str]) -> str:
    longitud_lista = len(frutas)
    numero_aleatorio = randint(0, longitud_lista - 1)
    return frutas[numero_aleatorio]


def show_random_element(fruit: list[str]) -> str:
    return choice(fruit)


print(mostrar_aleatorio(frutas))
print(show_random_element(frutas))
