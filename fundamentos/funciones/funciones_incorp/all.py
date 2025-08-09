# =====================================
# * Función incorporada all()
# =====================================
# La función all() devuelve True si `todos`` los elementos de un iterable
# (lista, tupla, conjunto, etc.) son evaluados como verdaderos (True).
# Si encuentra al menos un elemento falso, devuelve False.
#
# Forma general:
# all(iterable)
#
# Regla de oro:
# - Un valor se considera "falso" si es False, 0, None, "", [], etc.
# - Todo lo demás se considera "verdadero"

# Ejemplo 1: Todos son True
print(all([True, True, True]))  # Salida: True → porque todos los elementos son True

# Ejemplo 2: Hay al menos un False
print(all([True, False, True]))  # Salida: False → porque hay un elemento que es False

# Ejemplo 3: Usando números
print(all([1, 2, 3]))  # Salida: True → todos son distintos de 0 (son "verdaderos")
print(all([1, 0, 3]))  # Salida: False → porque 0 se considera "falso"

# Ejemplo 4: Lista vacía
print(all([]))
# Salida: True → se considera "verdadero" porque no hay ningún elemento falso
# (es lo que se llama "verdadero por vacuidad")

# Ejemplo 5: Combinado con condiciones
edades = [18, 21, 35, 40]
print(
    all(edad >= 18 for edad in edades)
)  # Salida: True → porque todas las edades son 18 o más
