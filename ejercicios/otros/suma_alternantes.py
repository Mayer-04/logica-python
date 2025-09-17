"""
Sumas Alternantes: Escribe un programa que reciba una lista de números y calcule la suma de los números
en posiciones pares y la resta de los números en posiciones impares.

Pasos a seguir:
- Recibir una lista de números.
- Calcular la suma de los números pares en la lista.
- Calcular la resta de los número impares en la lista.
"""


def calcular_suma_pares(lista_numeros: list[int]) -> int:
    return sum(numero for numero in lista_numeros if numero % 2 == 0)


def calcular_resta_impares(lista_numeros: list[int]) -> int:
    total_resta = 0
    for impares in lista_numeros:
        if impares % 2 == 1:
            total_resta -= impares
    return total_resta


def sumas_alternantes(lista_numeros: list[int]) -> tuple[int, int]:
    total_suma = calcular_suma_pares(lista_numeros)
    total_resta = calcular_resta_impares(lista_numeros)
    return total_suma, total_resta


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_suma, total_resta = sumas_alternantes(lista_numeros)
print(f"La suma de los números pares es: {total_suma}")
print(f"La resta de los número impares es: {total_resta}")
