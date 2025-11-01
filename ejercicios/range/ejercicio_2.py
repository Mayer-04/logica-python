"""
Contar múltiplos en un rango
------------------------------
Crea una función que reciba dos números enteros `inicio`, `fin` y un número `multiplo`.
La función debe retornar cuántos múltiplos del número `multiplo` existen en el rango desde `inicio` hasta
`fin` (sin incluir `fin`).
Usa `range()` para generar la secuencia y contar solo los múltiplos.

Parámetros:
------------
- inicio (int): Número donde comienza el rango
- fin (int): Número donde termina el rango (no incluido)
- multiplo (int): Número del cual buscar múltiplos

Retorna:
---------
- (int): Cantidad de múltiplos encontrados

Casos de prueba:
-----------------
Caso 1:

Input: inicio = 1, fin = 20, multiplo = 3
Output: 6
Explicación: Los múltiplos de 3 son: 3, 6, 9, 12, 15, 18 (total: 6)

Caso 2:

Input: inicio = 10, fin = 50, multiplo = 7
Output: 6
Explicación: Los múltiplos de 7 son: 14, 21, 28, 35, 42, 49 (total: 6)
"""


def encontrar_multiplos(inicio: int, fin: int, multiplo: int) -> int:
    multiplos_encontrados = 0
    for num in range(inicio, fin):
        if num % multiplo == 0:
            multiplos_encontrados += 1
    return multiplos_encontrados


def encontrar_multiplos_v2(inicio: int, fin: int, multiplo: int) -> int:
    return len([num for num in range(inicio, fin) if num % multiplo == 0])


def encontrar_multiplos_v3(inicio: int, fin: int, multiplo: int) -> int:
    if multiplo <= 0:
        return 0

    # Cantidad de múltiplos desde 0 hasta fin-1
    count_hasta_fin = (fin - 1) // multiplo

    # Cantidad de múltiplos desde 0 hasta inicio-1
    count_hasta_inicio = (inicio - 1) // multiplo

    return count_hasta_fin - count_hasta_inicio


print(encontrar_multiplos(1, 20, 3))
print(encontrar_multiplos_v2(10, 50, 7))
print(encontrar_multiplos_v3(20, 40, 5))
