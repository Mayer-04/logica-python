"""
* Operadores de asignación
---------------------------
Asignar: Significa darle un valor a una variable.

Los operadores de asignación se usan para guardar un valor en una variable.

Por ejemplo:
- El operador `=` asigna directamente un valor.
- Mientras que operadores como `+=` combinan una operación con la asignación.

Cuando usamos `+=`, estamos diciendo:
“Toma el valor actual de la variable, súmale otro valor, y guarda el resultado en la misma variable”.

Ejemplo:
--------
1. Asignamos el valor 7 a la variable `numero`:
   numero = 7

2. Usamos `+=` para sumarle 3 al valor actual de `numero`:
   numero += 3  # Ahora numero vale 10

3. El nuevo valor de `numero` es 10.
"""

# Asignar un valor a una variable
numero = 1
print("numero:", numero)

# Asignación múltiple
numero1, numero2 = 1, 2

# Suma y asignación a una variable +=
# Esto es equivalente a `numero = numero + 1`
numero += 2
print("numero +=", numero)

# Resta y asignación a una variable -=
numero -= 1
print("numero -=", numero)

# Multiplicación y asignación a una variable *=
numero *= 4
print("numero *=", numero)

# División y asignación a una variable /=
numero /= 2
print("numero /=", numero)

# División entera y asignación a una variable //=
numero1 //= 2
print("numero1 //=", numero1)

# Potencia y asignación a una variable **=
numero2 **= 4
print("numero2 **=", numero2)

# Módulo y asignación a una variable %=
numero1 %= 1
print("numero1 %=", numero1)
