"""
## Ejercicio 49: Diccionario de índices
------------------------------------------
Dada una lista, crea un diccionario donde las claves sean los elementos y los valores sean listas
con los índices donde aparece cada elemento.

Ejemplo:
-------------
lista = ['a', 'b', 'a', 'c', 'b', 'a']
# Resultado: {'a': [0, 2, 5], 'b': [1, 4], 'c': [3]}
"""


def obtener_indices_dict(lista: list) -> dict:
    dict_indices = {}

    for i, elemento in enumerate(lista):
        if elemento not in dict_indices:
            dict_indices[elemento] = []
        dict_indices[elemento].append(i)

    return dict_indices


lista = ["a", "b", "a", "c", "b", "a"]
print(obtener_indices_dict(lista))
