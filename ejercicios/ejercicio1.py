"""
Tienes una función que recibe un objeto como parámetro.
La función debe retornar un array con el nombre de las propiedades que su tipo sea boolean.
Por ejemplo, para el objeto { a: true, b: 42, c: false } la función debe retornar ['a', 'c'],
ya que son las dos propiedades que tienen valores booleanos.
"""


def get_boolean_properties(obj: dict[str, bool | int]) -> list[str]:
    return [key for key, value in obj.items() if isinstance(value, bool)]


dictionary = {"a": True, "b": 42, "c": False}
result = get_boolean_properties(dictionary)
print(result)


# Segunda solución
def get_boolean_properties2(obj: dict[str, bool | int]) -> list[str]:
    boolean_properties = []
    for key, value in obj.items():
        if isinstance(value, bool):
            boolean_properties.append(key)
    return boolean_properties


dictionary = {"a": True, "b": 42, "c": False}
result = get_boolean_properties2(dictionary)
print(result)
