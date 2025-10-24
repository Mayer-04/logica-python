"""
* Palabra reservada `del`
--------------------------
La palabra clave `del` se utiliza para eliminar variables u objetos en Python.

Se puede aplicar a:
-------------------
- Variables
- Elementos de una lista
- Claves de un diccionario
- Atributos de un objeto

Cuando se elimina una referencia y no existen otras que `apunten` al mismo objeto,
Python puede liberar esa memoria automáticamente (esto se conoce como recolección de basura).
"""

numero = 10
# Eliminar la variable 'numero'
del numero  # Ahora 'numero' ya no existe, si intentas usarla, obtendrás un error

# Eliminar un elemento de una lista
lista = [1, 2, 3, 4]
del lista[2]
print(lista)  # Salida: [1, 2, 4]

# Eliminar un par clave-valor de un diccionario
diccionario = {"edad": 25, "edad2": 50}
del diccionario["edad2"]
print(diccionario)  # Salida: {'edad': 25}


# Eliminar un elemento de un conjunto
# No podemos usar 'del' para eliminar un elemento de un conjunto, necesitamos usar su método 'remove'
conjunto = {1, 2, 3, 4}
conjunto.remove(3)  # Elimina el tercer elemento del conjunto
print(conjunto)  # Salida: {1, 2, 4}

# Eliminar el conjunto completo
del conjunto

# Eliminar una tupla
tupla = (1, 2, 3, 4)
del tupla  # Eliminar la tupla completa

# Eliminar un rango de elementos de una lista
mi_lista = [1, 2, 3, 4, 5]
del mi_lista[2:]  # Eliminar desde el tercer elemento hasta el final
print(mi_lista)  # Salida: [1, 2]


# Eliminar el atributo 'edad' de un objeto
class Persona:
    def __init__(self):
        self.edad = 25


mayer = Persona()
# Ahora 'mayer.edad' ya no existe
del mayer.edad
print(mayer.edad)  # Salida: AttributeError: 'Persona' object has no attribute 'edad'
