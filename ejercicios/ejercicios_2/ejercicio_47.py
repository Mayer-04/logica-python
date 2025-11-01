"""
Ejercicio 47: Promedio de columnas en una matriz
--------------------------------------------------
Crea una función que reciba una matriz de números y devuelva una lista con el promedio de cada columna.

Ejemplo:
----------

matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11]
]
Promedios por columna: [3.33, 5.33, 7.33]
"""

matriz_numeros = [[2, 4, 6], [1, 3, 5], [7, 9, 11]]


def promediar_columnas_matriz(matriz: list[list[int]]) -> list[int]:
    lista_promedios = []

    for columna in range(len(matriz[0])):
        suma_columna = 0

        for fila in range(len(matriz)):
            suma_columna += matriz[fila][columna]

        promedio = suma_columna / len(matriz)
        lista_promedios.append(promedio)

    return lista_promedios


def promediar_columnas_matriz_v2(matriz: list[list[int]]) -> list[int]:
    lista_promedios = []
    suma_promedios = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            suma_promedios += matriz[columna][fila]

        promedio = suma_promedios / len(matriz)

        lista_promedios.append(promedio)

        suma_promedios = 0

    return lista_promedios


print(promediar_columnas_matriz(matriz_numeros))
print(promediar_columnas_matriz_v2(matriz_numeros))
