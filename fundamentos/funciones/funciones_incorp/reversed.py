# =====================================
# * Función incorporada reversed()
# =====================================
# La función reversed() devuelve un iterador que recorre un iterable
# (lista, tupla, cadena, etc.) en orden inverso.
#
# Forma general:
# reversed(iterable)
#
# Nota:
# - No devuelve una lista directamente, sino un iterador.
# - Para verlo como lista o tupla, debemos convertirlo con list() o tuple().

# Ejemplo 1: Invertir una lista
numeros = [1, 2, 3, 4, 5]
print(list(reversed(numeros)))  # Salida: [5, 4, 3, 2, 1]
print(numeros)  # Salida: [1, 2, 3, 4, 5] → la lista original no cambia

# Ejemplo 2: Invertir una cadena
texto = "Python"
print("".join(reversed(texto)))  # Salida: nohtyP

# Ejemplo 3: Invertir una tupla
tupla = (10, 20, 30)
print(tuple(reversed(tupla)))  # Salida: (30, 20, 10)

# Ejemplo 4: Diferencia con slicing
# También se puede invertir usando slicing con paso -1
print(numeros[::-1])  # [5, 4, 3, 2, 1]
# Sin embargo, reversed() es más claro y no crea una copia en memoria inmediatamente.
