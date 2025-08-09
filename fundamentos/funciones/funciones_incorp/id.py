# =====================================
# * Función incorporada id()
# =====================================
# La función id() devuelve un número entero que identifica
# de forma única a un objeto en memoria `mientras existe`.
#
# Forma general:
# id(objeto)
#
# Nota:
# - Este número es interno de Python y no es necesario saberlo para la mayoría de programas.
# - Dos objetos distintos pueden tener el mismo `id` en momentos diferentes, pero nunca al mismo tiempo.

# Ejemplo 1: Identidad de objetos
print(id("Hola"))  # Ejemplo de salida: 2313322522224
print(id(3))  # Ejemplo de salida: 140734135859704

# Ejemplo 2: Mismo id para la misma variable
x = [1, 2, 3]
print(id(x))  # Ej: 124391937417792
print(id(x))  # Mismo número porque es el mismo objeto en memoria

# Ejemplo 3: Objetos diferentes, distinto id
y = [1, 2, 3]
print(id(x))  # Ej: 124391937417792
print(id(y))  # Ej: 124391939462656 → distinta lista aunque tengan el mismo contenido

# Ejemplo 4: Variables apuntando al mismo objeto
z = x
print(id(x) == id(z))  # True → ambas variables apuntan al mismo objeto
