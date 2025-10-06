"""
Crea una función `unique()` que reciba una lista como parámetro y devuelva una `nueva lista` que
contenga solo los elementos únicos (sin duplicados), preservando el orden de primera aparición.

Diferencia con el ejercicio 8:
-------------------------------
Aquí puedes usar cualquier método que prefieras, incluyendo `set()` si lo deseas.
"""


def unico(lista: list) -> list:
    # return list(set(lista))
    return [*set(lista)]


def unique(list_elements: list) -> list:
    dictionary = {}
    for element in list_elements:
        dictionary[element] = None
    return [key for key in dictionary.keys()]


def unique_2(list_elements: list) -> list:
    return list(dict.fromkeys(list_elements))


print(unico([1, 1, 2, 3, 4, 4, 5]))
print(unique(["Mayer", "Mayer", "Andres", "Chaves", "Andres"]))
print(unique_2(["lobo", "ballena", "lobo", "elefante", "ballena"]))
