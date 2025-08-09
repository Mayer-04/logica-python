# =====================================
# * Función incorporada map()
# =====================================
# La función map() aplica una función a cada elemento de un iterable
# (lista, tupla, conjunto, etc.) y devuelve un `objeto de tipo map`,
# que es un iterable que genera los resultados al recorrerlo.
#
# Forma general:
# map(funcion, iterable)
#
# Nota importante:
# - El objeto map no muestra los resultados directamente.
# - Para verlos, normalmente lo convertimos a lista o tupla.

# Ejemplo 1: Multiplicar cada número por 2
numeros = [1, 2, 3, 4, 5, 6]
resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  # Salida: [2, 4, 6, 8, 10, 12]

# Ejemplo 2: Convertir cadenas a mayúsculas
palabras = ["hola", "mundo", "python"]
resultado = map(str.upper, palabras)  # Usamos una función ya existente
print(list(resultado))  # Salida: ['HOLA', 'MUNDO', 'PYTHON']

# Ejemplo 3: Calcular la longitud de cada palabra
longitudes = map(len, palabras)
print(list(longitudes))  # Salida: [4, 5, 6]

# Ejemplo 4: Usar map() con varias listas a la vez
a = [1, 2, 3]
b = [4, 5, 6]
resultado = map(lambda x, y: x + y, a, b)
print(list(resultado))  # Salida: [5, 7, 9]

# Ejemplo 5: Evitar map() cuando una lista por comprensión es más legible
dobles = [x * 2 for x in numeros]
print(dobles)  # Salida: [2, 4, 6, 8, 10, 12]
# A veces las listas por comprensión son más fáciles de leer que map() con lambda.
