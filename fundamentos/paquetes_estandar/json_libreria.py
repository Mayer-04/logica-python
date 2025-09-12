import json

"""
* JSON (JavaScript Object Notation)

JSON es un formato de datos que se utiliza para representar datos en forma de texto.

- json.dumps(): Convierte un objeto Python (como un diccionario o una lista) en una cadena JSON.
- json.loads(): Convierte una cadena JSON en un objeto Python.
"""

# Convertir un diccionario a JSON
data = {"nombre": "Andres", "edad": 24}
json_string = json.dumps(data)
print("Diccionario a JSON:", json_string)  # {"nombre": "Juan", "edad": 30}

# Convertir una cadena JSON a un diccionario
json_string = '{"nombre": "Diego", "edad": 40}'
data = json.loads(json_string)
print("JSON a diccionario:", data)  # {'nombre': 'Juan', 'edad': 30}

# Convertir una lista a JSON
data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
json_str = json.dumps(data)
print(
    "Lista a JSON:", json_str
)  # Imprime: '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
