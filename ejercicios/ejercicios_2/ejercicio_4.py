"""
Crea una función que reciba una lista de números como parámetro y devuelva el número mayor
y el número menor dentro de esa lista.

Restricción: No utilices las funciones built-in `max()` y `min()`.
Implementa tu propia lógica de comparación.

Ejemplo:
---------
numeros = [45, 23, 78, 12, 90, 5]
# La función debe devolver: (90, 5)
"""


def obtener_numero_mayor(numeros: list[int]) -> int:
    numero_mayor = numeros[0]

    for numero in numeros:
        if numero_mayor < numero:
            numero_mayor = numero

    return numero_mayor


print(obtener_numero_mayor([45, 23, 78, 12, 90, 5]))
