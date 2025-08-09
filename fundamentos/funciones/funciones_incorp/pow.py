# =====================================
# * Función incorporada pow()
# =====================================
# Calcula la potencia de un número: base elevado a exponente.
#
# Forma general:
# pow(base, exponente[, modulo])
#
# Parámetros:
# - base: número que se eleva.
# - exponente: número al que se eleva la base.
# - modulo (opcional): si se especifica, devuelve (base**exponente) % modulo.

# Ejemplo 1: Potencia básica
print(pow(2, 3))  # Salida: 8  → 2^3 = 8

# Ejemplo 2: Potencia con número decimal
print(pow(4.0, 0.5))  # Salida: 2.0  → raíz cuadrada de 4

# Ejemplo 3: Potencia negativa (inverso)
print(pow(2, -2))  # Salida: 0.25  → 1 / (2^2)

# Ejemplo 4: Uso del parámetro modulo
print(pow(2, 5, 3))  # Salida: 2  → (2^5 = 32) y 32 % 3 = 2
