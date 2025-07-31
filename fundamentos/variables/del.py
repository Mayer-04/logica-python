"""
* Palabra reservada `del`
--------------------------
Se utiliza para eliminar una variable o un objeto.
- Puede aplicarse a variables, elementos de listas, elementos de un diccionario, atributos de objetos, etc.
- Si no hay otras referencias a esos objetos, se eliminan de la memoria, ayudando a la recolección de basura en Python.
"""

# Eliminar una variable
numero = 10
del numero  # Ahora 'number' ya no existe y si intentas usarla, obtendrás un error.

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
