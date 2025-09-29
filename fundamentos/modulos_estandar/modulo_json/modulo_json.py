import json

"""
Módulo json en Python
------------------------
JSON (JavaScript Object Notation) es un formato de texto para guardar y compartir datos.
Es muy usado en aplicaciones web, APIs, y archivos de configuración.

Python incluye el módulo `json` para convertir datos entre:
- Objetos de Python (como diccionarios o listas)
- Cadenas JSON (texto con estructura)

Funciones principales:
-----------------------
- json.dumps(objeto): convierte un objeto de Python en una cadena JSON.
- json.loads(cadena): convierte una cadena JSON en un objeto de Python.
"""

# Convertir un diccionario de Python a una cadena JSON
persona = {"nombre": "Andrés", "edad": 25}
json_persona = json.dumps(persona)
print("Diccionario a JSON:", json_persona)
# Salida: {"nombre": "Andrés", "edad": 25}

# Convertir una `cadena JSON` a un diccionario de Python
json_texto = '{"nombre": "Mayer", "edad": 50}'
persona_recuperada = json.loads(json_texto)
print("JSON a diccionario:", persona_recuperada)
# Salida: {'nombre': 'Mayer', 'edad': 50}

# Convertir una lista de diccionarios a JSON
lista_personas = [{"nombre": "Linus", "edad": 55}, {"nombre": "Ken", "edad": 82}]
json_lista = json.dumps(lista_personas)
print("Lista a JSON:", json_lista)
# Salida: [{"nombre": "Linus", "edad": 55}, {"nombre": "Ken", "edad": 82}]

# * Leer los datos desde el archivo "datos.json"
# Ruta relativa del archivo
ruta = "fundamentos/modulos_estandar/modulo_json/datos.json"

with open(ruta, "r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)

print("Datos desde archivo:", datos_recuperados)


# Convierte un objeto de Python a JSON y lo guarda directamente en un archivo.
nombre_archivo = "persona.json"
ruta = f"fundamentos/modulos_estandar/modulo_json/{nombre_archivo}"

persona = {"nombre": "Mayer", "edad": 25, "profesion": "Desarrollador de software"}
with open(ruta, "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo)

print("JSON guardado en el archivo")
