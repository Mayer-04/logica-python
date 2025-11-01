"""
Ejercicio 46: Reemplazar vocales
----------------------------------
Escribe un programa que reciba una cadena y reemplace todas las vocales por el símbolo `*`.

Ejemplo:
---------
texto = "Hola mundo"
# Resultado: "H*l* m*nd*"
"""


def reemplazar_vocales(texto: str) -> str:
    vocales = "aeiou"
    palabra = texto

    for vocal in vocales:
        palabra = palabra.replace(vocal, "*")

    return palabra


texto = "Hola mundo"
print(reemplazar_vocales(texto))
