"""
Ejercicio 43: Contar vocales y consonantes

Escribe una función que reciba una cadena de texto y devuelva un diccionario con la cantidad de vocales
y consonantes que contiene.

Ejemplo:
---------
texto = "Programación"
# Resultado: {'vocales': 5, 'consonantes': 7}
"""


def contar_vocales_consonantes(texto: str) -> dict[str, int]:
    vocales = "aeiouáéíóú"
    resultado = {"vocales": 0, "consonantes": 0}

    for char in texto.lower():
        if char in vocales:
            resultado["vocales"] += 1
        else:
            resultado["consonantes"] += 1

    return resultado


texto = "Programación"
print(contar_vocales_consonantes(texto))
