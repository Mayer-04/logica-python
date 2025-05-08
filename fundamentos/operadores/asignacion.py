"""
* Operadores de asignación
--------------------------
- Asignar: Establecer un valor a una variable.
- Los operadores de asignación se utilizan para asignar valores a una variable.
- Cuando estamos utilizando un `operador de asignación` como `+=`, estás diciendo que quieres tomar el valor actual
de la variable, realizar una operación con otro valor, y luego almacenar el resultado de nuevo en la misma variable.

Ejemplo:
--------
1. El valor actual de `a` es `7`
a = 7

2. Le sumamos 3 al valor actual de `a` y asignamos este nuevo valor `10` de vuelta a la variable `a`.
a += 3

3. Ahora `a` tiene el valor `10`.
"""

# Asignar un valor a una variable
a = 1
print("a:", a)

# Asignación múltiple
a, b = 1, 2

# Suma y asignación a una variable +=
# Esto es equivalente a `a = a + 1`
a += 1
print("a +=", a)

# Resta y asignación a una variable -=
a -= 1
print("a -=", a)

# Multiplicación y asignación a una variable *=
a *= 1
print("a *=", a)

# División y asignación a una variable /=

a /= 1
print("a /=", a)

# División entera y asignación a una variable //=
a //= 1
print("a //=", a)

# Potencia y asignación a una variable **=
a **= 1
print("a **=", a)

# Módulo y asignación a una variable %=
a %= 1
print("a %=", a)
