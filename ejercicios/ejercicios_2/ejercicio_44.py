"""
Ejercicio 44: Eliminar palabras cortas

Escribe una función que reciba una lista de palabras y un número entero `n`, y devuelva una nueva lista
con las palabras cuya longitud sea `mayor que n`.

Ejemplo:
---------
palabras = ["sol", "computadora", "luna", "python"]
n = 4
# Resultado: ["computadora", "python"]
"""

palabras = ["sol", "computadora", "luna", "python"]


def eliminar_palabras_cortas(palabras: list[str], numero: int) -> list[str]:
    return [palabra for palabra in palabras if len(palabra) > numero]


print(eliminar_palabras_cortas(palabras, 4))
