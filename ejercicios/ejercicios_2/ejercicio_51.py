"""
Ejercicio 51: Promedio por categoría
--------------------------------------
Tienes un diccionario donde las claves son categorías y los valores son listas de números.
Devuelve un nuevo diccionario con el promedio de cada categoría.

Ejemplo:
---------
datos = {
    "math": [4, 5, 3],
    "science": [5, 5, 4],
    "english": [3, 4, 4]
}
Resultado: {'math': 4.0, 'science': 4.67, 'english': 3.67}
"""

datos = {"math": [4, 5, 3], "science": [5, 5, 4], "english": [3, 4, 4]}


def promediar_categoria(materias: dict[str, list[int]]) -> dict[str, float]:
    resultado = {}

    for clave, valor in materias.items():
        longitud = len(valor)
        suma = 0

        for numero in valor:
            suma += numero

        promedio = suma / longitud

        resultado[clave] = round(promedio, 2)

    return resultado


print(promediar_categoria(datos))
