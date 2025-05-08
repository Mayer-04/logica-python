"""
* Operadores de Pertenencia
---------------------------
El nombre de este operador se da a partir de querer comprobar si un elemento está presente en una secuencia.

- Se utiliza la palabra clave `in` y `not in`.
- not in: Verifica si el elemento `no` está presente en la secuencia.
- Se utilizan para verificar si un elemento está presente (o no) en una secuencia (lista, tupla, conjunto, etc.).
- Si el elemento está presente devuelve `True`, de lo contrario `False`.
- Sintaxis: `element in sequence` o `element not in sequence`.
"""

# Es como decir: ¿El número 2 está presente en la lista?
print(2 in [1, 2, 3])  # Imprime True
print(4 in [1, 2, 3])  # Imprime False


# Operador `not in`
# Es como decir: ¿El número 3 no está presente en la lista?
print(3 not in [1, 2, 4, 5])  # Imprime True
print(5 not in [1, 2, 4, 5])  # Imprime False

# Se crea una lista con elementos enteros
numbers = [1, 2, 3, 4, 5, 6]

# Verificar si un elemento está presente en la lista
print(1 in numbers)  # Imprime True
print(5 in numbers)  # Imprime False


print(3 in 3)  # Imprime un error: El argumento de tipo `int` no es iterable.
