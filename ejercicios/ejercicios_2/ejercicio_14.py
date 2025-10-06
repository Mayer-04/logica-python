"""
Crea dos conjuntos (sets) con algunos elementos numéricos.
Escribe una función que reciba ambos sets como parámetros y devuelva un `nuevo set` que contenga
los elementos que están en el primer set pero no en el segundo (diferencia A - B).

Restricción: No uses el operador `-` de sets.
Implementa la lógica manualmente.

Ejemplo:
---------
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
# Resultado: {1, 2}
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}


def diferencia_conjuntos(set_1: set[int], set_2: set[int]) -> set[int]:
    nuevo_conjunto = set()

    for num in set_1:
        if not num in set_2:
            nuevo_conjunto.add(num)

    return nuevo_conjunto


def difference_of_sets(set_1: set[int], set_2: set[int]) -> set[int]:
    # difference_set = set_1.difference(set_2)
    return set_1 - set_2


print(diferencia_conjuntos(set_1, set_2))
print(difference_of_sets(set_1, set_2))
