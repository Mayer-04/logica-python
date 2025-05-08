"""
* Operadores Lógicos
--------------------
- Se utilizan para tomar una decisión basada en múltiples condiciones.
- Actúan sobre valores booleanos (`True` o `False`), pero también pueden aplicarse a cualquier objeto en Python, 
devolviendo el primer valor que satisfaga la condición lógica.
"""

number = 5

# and - y
# Devuelve True solo si ambas condiciones son verdaderas.
# Si todas las condiciones son verdaderas, devuelve el último valor.
# Si alguna es falsa, devuelve el primer valor falso que encuentra.
print(number > 0 and number < 10)

# or - o
# Devuelve True si al menos una de las condiciones es verdadera.
# Devuelve el primer valor verdadero que encuentra.
# Si todas son falsas, devuelve el último valor que encontró.
print(number > 0 or number < 10)

# not - no
# Devuelve el valor opuesto, si es verdadero devuelve falso y viceversa.
print(not number > 0)
