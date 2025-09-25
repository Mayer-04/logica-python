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
también pueden usarse con otros tipos de datos. En ese caso, Python evalúa si los valores
son "verdaderos" o "falsos" según su contenido (esto se llama truthiness).
"""

# Solo devuelve True si ambas condiciones son verdaderas
print(True and True)  # True
print(True and False)  # False

# Devuelve True si al menos una condición es verdadera
print(False or True)  # True
print(False or False)  # False

# Invierte el valor lógico
print(not True)  # False
print(not False)  # True

# Evaluación de "truthiness"
# En Python, algunos valores se consideran "falsos":
# - 0, "", None, [], {}, etc.

# Ejemplo con números
print(0 or 5)  # Salida: 5 → 0 es falso, 5 es verdadero → devuelve el primero verdadero
print(10 and 20)  # Salida: 20 → ambos son verdaderos → devuelve el último

# Ejemplo con cadenas de texto
print("" or "Hola")  # Salida: "Hola" → cadena vacía es falso, "Hola" es verdadero
print("Python" and "")  # Salida: "" → la segunda es falsa → devuelve la primera falsa
print("Hola" and "Mundo")  # Salida: "Mundo" → ambas son verdaderas → devuelve la última


number = 5

# and: y
# Devuelve True solo si ambas condiciones son verdaderas.
# Si todas las condiciones son verdaderas, devuelve el último valor.
# Si alguna es falsa, devuelve el primer valor falso que encuentra.
print(number > 0 and number < 10)  # True

# or: o
# Devuelve True si al menos una de las condiciones es verdadera.
# Devuelve el primer valor verdadero que encuentra.
# Si todas son falsas, devuelve el último valor que encontró.
print(number > 0 or number < 10)  # True

# not: no
# Devuelve el valor opuesto, si es verdadero devuelve falso y viceversa.
# Negamos una condición
print(not number > 0)  # False
