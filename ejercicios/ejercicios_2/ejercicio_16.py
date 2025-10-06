"""
Crea un diccionario donde las claves sean nombres de ciudades y los valores sean sus temperaturas actuales
en grados Celsius.

Escribe una función que reciba el diccionario y devuelva el nombre de la ciudad con la temperatura más alta.

Ejemplo:
---------
temperaturas = {
    "Madrid": 28,
    "Barcelona": 25,
    "Sevilla": 35,
    "Valencia": 30
}
# La función debe devolver: "Sevilla"

Considera: ¿Qué hacer si hay un empate? Puedes devolver la primera ciudad encontrada.
"""

temperaturas = {"Madrid": 28, "Barcelona": 25, "Sevilla": 35, "Valencia": 30}


def cuidad_temp_alta(temperaturas: dict[str, int]) -> str:
    ciudad = ""
    lista_temp = []

    for temp in temperaturas.values():
        lista_temp.append(temp)

    temp_mas_alta = max(lista_temp)

    for city, temp in temperaturas.items():
        if temp == temp_mas_alta:
            ciudad = city

    return ciudad


def ciudad_temp_alta_2(temperaturas: dict[str, int]) -> str:
    temp_mas_alta = max(temperaturas.values())
    for ciudad, temp in temperaturas.items():
        if temp == temp_mas_alta:
            return ciudad
    return ""


def city_high_temperature(temperaturas: dict[str, int]) -> str:
    return max(temperaturas, key=lambda ciudad: temperaturas[ciudad])


print(cuidad_temp_alta(temperaturas))
print(ciudad_temp_alta_2(temperaturas))
print(city_high_temperature(temperaturas))
