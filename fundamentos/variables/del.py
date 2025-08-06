"""
* Palabra reservada `del`
--------------------------
La palabra clave `del` se utiliza para eliminar variables u objetos en Python.

Puede aplicarse a:
- Variables
- Elementos de una lista
- Claves de un diccionario
- Atributos de un objeto

Cuando se elimina una referencia y no existen otras que apunten al mismo objeto,
Python puede liberar esa memoria automáticamente (esto se conoce como recolección de basura).
"""

# Eliminar una variable
numero = 10
del numero  # Ahora 'numero' ya no existe y si intentas usarla, obtendrás un error.

# Eliminar un elemento de una lista
lista = [1, 2, 3, 4]
del lista[2]
print(lista)  # Imprime: [1, 2, 4]

# Eliminar un par clave-valor de un diccionario
diccionario = {"clave1": "valor1", "clave2": "valor2"}
del diccionario["clave1"]
print(diccionario)  # Imprime: {'clave2': 'valor2'}


# Eliminar un elemento de un conjunto
# No podemos usar 'del' para eliminar un elemento de un conjunto
conjunto = {1, 2, 3, 4}
conjunto.remove(3)  # Elimina el elemento 3 del conjunto
print(conjunto)  # Imprime: {1, 2, 4}
del conjunto  # Elimina el conjunto completo


# Eliminar una tupla
tupla = (1, 2, 3, 4)
del tupla  # Elimina la tupla completa


# Eliminar el atributo 'edad' de un objeto
class Persona:
    def __init__(self):
        self.edad = 24


mayer = Persona()
# Ahora mayer.edad ya no existe
del mayer.edad
print(mayer.edad)  # Imprime: AttributeError: 'Persona' object has no attribute 'edad'
