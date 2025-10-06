"""
Crea una función que reciba una lista de números como parámetro y devuelva el número mayor
y el número menor dentro de esa lista.

Restricción: No utilices las funciones built-in `max()` y `min()`.
Implementa tu propia lógica de comparación.

Ejemplo:
---------
numeros = [45, 23, 78, 12, 90, 5]
# La función debe devolver: (90, 5)
"""

numero_mayor = lambda nums: max(nums)
numero_menor = lambda nums: min(nums)


def obtener_num_mayor_menor(numeros: list[int]) -> tuple[int, int]:
    return (numero_mayor(numeros), numero_menor(numeros))


def obtener_num_mayor_menor_2(numeros: list[int]) -> tuple[int, int]:
    return max(numeros), min(numeros)


def obtener_num_mayor_menor_3(numeros: list[int]) -> tuple[int, int]:
    mayor = numeros[0]
    menor = numeros[0]

    actualizar_mayor = lambda actual, nuevo: nuevo if nuevo > actual else actual
    actualizar_menor = lambda actual, nuevo: nuevo if nuevo < actual else actual

    for num in numeros[1:]:
        mayor = actualizar_mayor(mayor, num)
        menor = actualizar_menor(menor, num)

    return (mayor, menor)


print(obtener_num_mayor_menor([45, 23, 78, 12, 90, 5]))
print(obtener_num_mayor_menor_2([45, 23, 78, 12, 90, 5]))
print(obtener_num_mayor_menor_3([45, 23, 78, 12, 90, 5]))
