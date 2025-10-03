"""
Escribe un programa que reciba un número entero como entrada y determine si es par o impar.
El programa debe mostrar un mensaje indicando el resultado.

- Un número es par si es divisible entre 2 (resto = 0).
"""


def determinar_par_impar(numero: int) -> None:
    if numero <= 0:
        print("El número es cero o negativo")
        return

    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


determinar_par_impar(3)
determinar_par_impar(-5)
determinar_par_impar(6)
determinar_par_impar(0)
