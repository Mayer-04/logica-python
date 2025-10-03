"""
Escribe un programa que calcule el factorial de un número entero positivo.
Puedes hacerlo utilizando un bucle o de manera recursiva.

Ejemplo: `5! = 5 * 4 * 3 * 2 * 1 = 120`

Desafío adicional: Implementa ambas versiones (iterativa y recursiva) y compara su eficiencia.
"""


def calcular_factorial(numero: int) -> int:
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


def calculate_factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1

    return num * calculate_factorial(num - 1)



print(calcular_factorial(5))
print(calculate_factorial(5))
