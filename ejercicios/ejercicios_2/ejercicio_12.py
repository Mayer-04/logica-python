"""
Escribe una función que reciba dos listas y un valor booleano como parámetros.

Parámetros:
------------
- lista1: primera lista de elementos
- lista2: segunda lista de elementos
- comunes: valor booleano que determina el tipo de resultado

Reglas:
--------
- Si comunes es `True` → devolver una lista con los elementos que aparecen en ambas listas
- Si comunes es `False` → devolver una lista con los elementos que aparecen en una sola de las listas

Ejemplos:
----------
comparar_listas([1, 2, 3], [2, 3, 4], True)  # → [2, 3]
comparar_listas([1, 2, 3], [2, 3, 4], False) # → [1, 4]
"""


def comparar_listas(lista1: list[int], lista2: list[int], comunes: bool) -> list[int]:
    list_true = []
    list_false = []
    if comunes:
        for p in lista1:
            if p in lista2:
                list_true.append(p)
        return list_true
    else:
        for p in lista1:
            if p not in lista2:
                list_false.append(p)
        for s in lista2:
            if s not in lista1:
                list_false.append(s)
        return list_false


def comparar_listas_2(lista1: list[int], lista2: list[int], comunes: bool) -> list[int]:
    set1 = set(lista1)
    set2 = set(lista2)
    if comunes:
        return list(set1 & set2)
    else:
        return list(set1 ^ set2)


def compare_lists(list_1: list[int], list_2: list[int], common: bool) -> list[int]:
    if common:
        return [p for p in list_1 if p in list_2]
    else:
        return [p for p in list_1 if p not in list_2] + [s for s in list_2 if s not in list_1]


print(comparar_listas([1, 2, 3], [2, 3, 4], True))
print(comparar_listas_2([1, 2, 3], [2, 3, 4], False))
print(compare_lists([1, 2, 3], [2, 3, 4], True))
