"""
Ejercicio 41: Promedio de una lista
-------------------------------------
Escribe una función que reciba una lista de números y devuelva su promedio (media aritmética).

Consideraciones:
-----------------
- Si la lista está vacía, devolver 0
- El resultado puede ser un número decimal

Ejemplo:
---------
numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Promedio: 45/10 = 4.5
"""

numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def calcular_promedio(numeros: list[int]) -> float:
    longitud_lista = len(numeros)

    if longitud_lista == 0:
        return 0

    suma_lista = sum(numeros)
    return suma_lista / longitud_lista


print(calcular_promedio(numeros))
