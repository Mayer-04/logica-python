# =====================================
# * Función incorporada round()
# =====================================
# La función round() redondea un número al número de decimales indicado.
#
# Forma general:
# round(numero, ndigits=0)
#
# Parámetros:
# - numero: el valor que quieres redondear (int o float).
# - ndigits (opcional): cuántos decimales conservar.
#   Si no se indica, redondea al entero más cercano.
#
# Nota:
# - Si el valor está exactamente a la mitad (por ejemplo, 2.5),
#   Python redondea al número par más cercano ("round half to even").

# Ejemplo 1: Redondear con 2 decimales
print(round(3.141592653589793, 2))  # Salida: 3.14

# Ejemplo 2: Redondear con 0 decimales
print(round(7.8, 0))  # Salida: 8.0 → devuelve float si ndigits está presente

# Ejemplo 3: Redondear a enteros (ndigits omitido)
print(round(7.8))  # Salida: 8
print(round(7.2))  # Salida: 7

# Ejemplo 4: Caso especial de .5
print(round(2.5))  # Salida: 2 → redondea al par más cercano
print(round(3.5))  # Salida: 4 → redondea al par más cercano
