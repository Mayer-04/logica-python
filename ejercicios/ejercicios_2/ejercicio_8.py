"""
Crea una función que reciba una lista como parámetro y devuelva una nueva lista sin elementos duplicados,
manteniendo el orden de primera aparición.

Restricción:No puedes usar la conversión con `set()` ni métodos como `list(dict.fromkeys())`.

Ejemplo:
original = [1, 2, 2, 3, 4, 4, 5, 1]
Resultado: [1, 2, 3, 4, 5]
"""

original = [1, 2, 2, 3, 4, 4, 5, 1]


def eliminar_duplicados(numeros: list[int]) -> list[int]:
    lista_sin_dupl = []
    for num in numeros:
        if num not in lista_sin_dupl:
            lista_sin_dupl.append(num)
    return lista_sin_dupl


def remove_duplicates(numeros: list[int]) -> list[int]:
    elementos_sin_dupl = set(numeros)
    return [e for e in elementos_sin_dupl]


print(eliminar_duplicados(original))
print(remove_duplicates(original))
