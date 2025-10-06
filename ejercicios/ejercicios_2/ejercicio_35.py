"""
## Ejercicio 35: Longitud de palabras

Escribe una función que reciba una lista de palabras y devuelva una nueva lista con la longitud
de cada palabra.

Ejemplo:

palabras = ["hola", "python", "programación", "sol"]
# Resultado: [4, 6, 12, 3]
"""

palabras = ["hola", "python", "programación", "sol"]


def encontrar_longitud(palabras: list[str]) -> list[int]:
    lista_longitud = []

    for palabra in palabras:
        # Reinicia el contador cada vez que empieza una nueva palabra
        contador = 0
        for _ in palabra:
            contador += 1
        lista_longitud.append(contador)

    return lista_longitud


def encontrar_longitud_2(palabras: list[str]) -> list[int]:
    return [len(palabra) for palabra in palabras]


def find_length(words: list[str]) -> list[int]:
    lengths = {}

    for word in words:
        counter = 0
        for _ in word:
            counter += 1
        lengths[word] = counter

    return [value for value in lengths.values()]


print(encontrar_longitud(palabras))
print(encontrar_longitud_2(palabras))
print(find_length(palabras))
