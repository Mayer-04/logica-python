"""
* Operadores de Identidad
--------------------------
El nombre de este operador se da a partir de querer comprobar la identidad (si son el mismo objeto).

- Se utiliza la palabra clave `is` y `is not` para chequear la `identidad` de un objeto.
- Se utilizan para comparar si dos objetos son idénticos o no (si apuntan al mismo objeto en memoria).
- Si son iguales devuelve `True`, de lo contrario `False`.
- Si dos variables distintas tienen el mismo `id()`, el resultado de `is` es `True`.
"""

number = 2
number2 = 3

# Si ambos objetos apuntan al mismo objeto en memoria
print("Operador is:", number is number2)  # False
# Si ambos operandos no son el mismo objeto en memoria
print("Operador is not:", number is not number2)  # True


# Python reutiliza el mismo objeto que almacena el valor "Hello" para ambas variables.
# Las listas tienen un `id` diferente aún si en dos variables diferentes son iguales
var = "Hello"
var2 = "Hello"

print("id de var:", id(var))  # 2759573135520
print("id de var2:", id(var2))  # 2759573135520

print("var es igual a var2:", var is var2)  # True

# Comprobando el `id` de las listas
new_list = [1, 2, 3]
new_list2 = [1, 2, 3]

# Las listas presentan un `id` diferente aún siendo iguales en su valor
print("nueva tupla:", id(new_list))  # 3107485702400
print("otra tupla:", id(new_list2))  # 3107485700480

print("nueva tupla es igual a otra tupla:", new_list is new_list2)  # False
