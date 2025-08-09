# =====================================
# * Función incorporada zip()
# =====================================
# Combina elementos de dos o más iterables (listas, tuplas, etc.)
# creando pares (o tuplas) con el elemento correspondiente de cada uno.
# Devuelve un objeto zip, que es un iterable.
#
# Forma general:
# zip(iterable1, iterable2, ...)
#
# Si los iterables no tienen la misma longitud,
# zip() se detiene en el más corto.

# Ejemplo 1: Unir dos listas
nombres = ["Mayer", "Luis", "Andres"]
edades = [25, 30, 22]
combinados = zip(nombres, edades)
print(list(combinados))  # Salida: [('Mayer', 25), ('Luis', 30), ('Andres', 22)]

# Ejemplo 2: Unir tres listas
ciudades = ["Seul", "Barcelona", "Bogotá"]
datos = zip(nombres, edades, ciudades)
print(list(datos))
# Salida: [('Mayer', 25, 'Seul'), ('Luis', 30, 'Barcelona'), ('Andres', 22, 'Bogotá')]

# Ejemplo 3: Usar zip() para crear un diccionario
claves = ["nombre", "edad", "ciudad"]
valores = ["Mayer", 25, "Seul"]
diccionario = dict(zip(claves, valores))
print(diccionario)  # Salida: {'nombre': 'Mayer', 'edad': 25, 'ciudad': 'Seul'}
