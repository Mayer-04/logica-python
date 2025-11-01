"""
Ejercicio 48: Reorganizar palabras por longitud
--------------------------------------------------
Crea una función que reciba una frase y devuelva una lista con las palabras ordenadas por su longitud,
de menor a mayor. Si dos palabras tienen la misma longitud, mantener el orden original.

Ejemplo:
----------
frase = "Python es un lenguaje poderoso y elegante"
# Resultado: ['un', 'es', 'y', 'Python', 'poderoso', 'lenguaje', 'elegante']
"""


def ordenar_palabras_longitud(frase: str) -> list[str]:
    palabras_ordenadas = []
    palabras = {}

    for word in frase.split():
        palabras[word] = len(word)

    ordenar_valores = sorted(palabras.values())

    for longitud in ordenar_valores:
        for palabra, long in palabras.items():
            if long == longitud and palabra not in palabras_ordenadas:
                palabras_ordenadas.append(palabra)

    return palabras_ordenadas


def ordenar_palabras(frase: str) -> list[str]:
    lista_palabras = frase.split()
    return sorted(lista_palabras, key=len)


frase = "Python es un lenguaje poderoso y elegante"
print(ordenar_palabras_longitud(frase))
print(ordenar_palabras(frase))
