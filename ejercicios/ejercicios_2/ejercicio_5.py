"""
Dado un número `n`, encuentra la suma de todos los números positivos menores que `n` que sean múltiplos
de 3 o de 5.

Ejemplo: para n = 10 → 3 + 5 + 6 + 9 = 23

Nota: Un número puede ser múltiplo de ambos (como el 15), pero solo debe sumarse una vez.
"""


def sumar_num_positivos(n: int) -> int:
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)


def add_positive_numbers(n: int) -> int:
    numeros = []

    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            numeros.append(i)

    return sum(numeros)


print(sumar_num_positivos(10))
print(add_positive_numbers(10))
