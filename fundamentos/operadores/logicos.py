"""
* Operadores lógicos
---------------------
Los operadores lógicos se utilizan para evaluar múltiples condiciones y tomar decisiones
en función de si son verdaderas o falsas.

En Python, los principales operadores lógicos son:
- `and`: devuelve `True` solo si `todas` las condiciones son verdaderas.
- `or`: devuelve `True` si `al menos una` condición es verdadera.
- `not`: invierte el valor lógico; convierte `True` en `False` y viceversa.

Aunque están diseñados para trabajar con valores booleanos (`True` o `False`),
en Python también pueden usarse con otros tipos de objetos.
En ese caso, devuelven el primer valor que determina el resultado lógico.
"""

# Con booleanos
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# Con otros valores (evaluación de "truthiness")
print(0 or 5)  # 5 (porque 0 es falso y 5 es verdadero)
print("" and "Hola")  # "" (cadena vacía es falso, por eso se devuelve)
print("Hola" and 123)  # 123 (ambos son verdaderos, devuelve el último)

number = 5

# and: y
# Devuelve True solo si ambas condiciones son verdaderas.
# Si todas las condiciones son verdaderas, devuelve el último valor.
# Si alguna es falsa, devuelve el primer valor falso que encuentra.
print(number > 0 and number < 10)

# or: o
# Devuelve True si al menos una de las condiciones es verdadera.
# Devuelve el primer valor verdadero que encuentra.
# Si todas son falsas, devuelve el último valor que encontró.
print(number > 0 or number < 10)

# not: no
# Devuelve el valor opuesto, si es verdadero devuelve falso y viceversa.
print(not number > 0)
