"""
* Operadores de comparación
----------------------------
Estos operadores se usan para comparar dos valores.
El resultado de una comparación siempre es un valor booleano: `True` o `False`.

También puedes encadenar varias comparaciones en una sola expresión.
Python evaluará cada comparación en orden y solo devolverá `True` si todas son verdaderas.

Ejemplos:
---------
1. Comparación simple:
   5 > 3  # Devuelve True

2. Comparación encadenada:
   3 < 5 < 10  # Devuelve True, porque 3 < 5 y 5 < 10

3. Si alguna comparación no se cumple:
   3 < 5 > 10  # Devuelve False, porque 5 no es mayor que 10
"""

# Igualdad (==)
# Compara si dos valores son iguales.
print(1 == 1)  # True, porque 1 es igual a 1

print(1 == 2)  # False, porque 1 no es igual a 2

# Desigualdad o diferente (!=)
# Compara si dos valores son diferentes.
print(1 != 1)  # False, porque 1 es igual a 1

# Mayor que (>)
# Verifica si el valor de la izquierda es mayor que el de la derecha.
print(1 > 1)  # False, porque 1 no es mayor que 1

# Menor que (<)
# Verifica si el valor de la izquierda es menor que el de la derecha.
print(1 < 1)  # False, porque 1 no es menor que 1

# Mayor o igual que (>=)
# Verifica si el valor de la izquierda es mayor o igual al de la derecha.
print(1 >= 1)  # True, porque 1 es igual a 1

# Menor o igual que (<=)
# Verifica si el valor de la izquierda es menor o igual al de la derecha.
print(1 <= 1)  # True, porque 1 es igual a 1

# Encadenar comparaciones
# Puedes escribir múltiples comparaciones seguidas.
# Python evaluará si todas las comparaciones son verdaderas.
print("Encadenar comparaciones:", 1 < 2 < 3)  # True, porque 1 < 2 y 2 < 3
