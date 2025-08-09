# =====================================
# * Función incorporada any()
# =====================================
# La función any() devuelve True si `al menos un` elemento de un iterable
# (lista, tupla, conjunto, etc.) es evaluado como verdadero.
# Si todos los elementos son falsos, devuelve False.
#
# Forma general:
# any(iterable)
#
# Regla de evaluación:
# - Falso: False, 0, "", None, [], {}, set(), etc.
# - Verdadero: cualquier otro valor.

# Ejemplo 1: Todos falsos
print(any([False, False, False]))  # Salida: False → ningún elemento es verdadero

# Ejemplo 2: Al menos uno verdadero
print(any([False, True, False]))  # Salida: True → porque hay un True en la lista

# Ejemplo 3: Usando números
print(
    any([0, 0, 5])
)  # Salida: True → 5 es distinto de 0, por eso se considera "verdadero"

# Ejemplo 4: Lista vacía
print(any([]))  # Salida: False → no hay elementos verdaderos

# Ejemplo 5: Combinado con condiciones
edades = [15, 21, 17, 19]
print(any(edad >= 18 for edad in edades))
# Salida: True → porque hay al menos una edad mayor o igual a 18
