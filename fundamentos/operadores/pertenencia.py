"""
* Operadores de pertenencia
----------------------------
Los operadores de pertenencia se utilizan para verificar si un elemento está presente (o no)
dentro de una `secuencia`, como una lista, tupla, conjunto, cadena, etc.

Palabras clave:
- `in`: devuelve `True` si el elemento `está` en la secuencia.
- `not in`: devuelve `True` si el elemento `no está` en la secuencia.

Estos operadores ayudan a hacer verificaciones rápidas y legibles sobre la existencia de elementos.

Sintaxis:
---------
elemento in secuencia
elemento not in secuencia
"""

# Es como decir: ¿El número 2 está presente en la lista?
print(2 in [1, 2, 3])  # Salida: True
print(4 in [1, 2, 3])  # Salida: False

lenguaje = "Python"
print("y" in lenguaje)  # True, la letra 'y' está en lenguaje
print("z" in lenguaje)  # False, la letra 'z' no está en lenguaje

# Operador `not in`
# Es como decir: ¿El número 3 no está presente en la lista?
print(3 not in [1, 2, 4, 5])  # Salida: True
print(5 not in [1, 2, 4, 5])  # Salida: False

# Operador `in` con un argumento de tipo `int`
print(3 in 3)  # Salida: un error: El argumento de tipo `int` no es iterable.
