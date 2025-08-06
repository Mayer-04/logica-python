"""
* Operadores de identidad
--------------------------
Los operadores de identidad se utilizan para comprobar si dos variables hacen `referencia` al mismo objeto
en memoria.

En Python, esto se hace con las palabras clave:
- `is`: devuelve `True` si dos variables son el mismo objeto (tienen el mismo `id()`).
- `is not`: devuelve `True` si dos variables `no` son el mismo objeto.

- Si dos variables distintas tienen el mismo `id()`, el resultado de `is` es `True`.

NOTA: Es importante notar que `ser el mismo objeto` no es lo mismo que `tener el mismo valor`.
"""

number = 2
number2 = 3

# Si ambos objetos apuntan al mismo objeto en memoria
print("Operador is:", number is number2)  # False
# Si ambos operandos no son el mismo objeto en memoria
print("Operador is not:", number is not number2)  # True


# Python reutiliza el mismo objeto que almacena el valor "Hello" para ambas variables.
# Las listas tienen un `id` diferente aún si en dos variables diferentes son iguales
saludo = "Hello"
saludo2 = "Hello"

print("id de saludo:", id(saludo))  # 129013293168080
print("id de saludo2:", id(saludo2))  # 129013293168080

print("saludo es igual a saludo2:", saludo is saludo2)  # True

# Comprobando el `id` de las listas
new_list = [1, 2, 3]
new_list2 = [1, 2, 3]

# Las listas presentan un `id` diferente aún siendo iguales en su valor
print("nueva lista:", id(new_list))  # 129013292737344
print("otra lista:", id(new_list2))  # 129013294913280

print("nueva lista es igual a otra lista:", new_list is new_list2)  # False

# Otros ejemplos de identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, porque b apunta al mismo objeto que a
print(a is c)  # False, aunque tengan el mismo valor, son objetos diferentes en memoria
print(a == c)  # True, porque sus valores son iguales

print(a is not c)  # True, porque a y c no son el mismo objeto
