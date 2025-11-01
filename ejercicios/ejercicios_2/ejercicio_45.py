"""
Ejercicio 45: Suma diagonal de una matriz
-------------------------------------------
Dada una matriz cuadrada (lista de listas), calcula la suma de los elementos de su `diagonal principal`.

Ejemplo:
----------
matriz = [
    [2, 5, 7],
    [4, 3, 9],
    [6, 1, 8]
]
Diagonal: 2 + 3 + 8 = 13
Resultado: 13
"""

matriz_numeros = [
    [2, 5, 7],
    [4, 3, 9],
    [6, 1, 8]
]


def sumar_diagonal_principal(matriz: list[list[int]]) -> int:
    suma_diagonal = 0

    for fila in range(len(matriz)):
        suma_diagonal += matriz[fila][fila]

    return suma_diagonal


def sumar_diagonal_principal_v2(matriz: list[list[int]]) -> int:
    suma_diagonal = 0
    longitud_matriz = len(matriz)

    for i in range(longitud_matriz):
        for j in range(longitud_matriz):
            if i == j:
                suma_diagonal += matriz[i][j]

    return suma_diagonal


def sumar_diagonal_principal_v3(matriz: list[list[int]]) -> int:
    suma_diagonal = 0

    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if i == j:
                suma_diagonal += elemento

    return suma_diagonal


print(sumar_diagonal_principal(matriz_numeros))
print(sumar_diagonal_principal_v2(matriz_numeros))
print(sumar_diagonal_principal_v3(matriz_numeros))
