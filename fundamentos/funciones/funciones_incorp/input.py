# =====================================
# * Función incorporada input()
# =====================================
# Permite al usuario escribir datos en la consola.
# Siempre devuelve el resultado como cadena de texto (str).
#
# Forma general:
# input(mensaje_opcional)
#
# Parámetro:
# - prompt: texto que se muestra al usuario antes de que escriba.

# Ejemplo 1: Solicitar un nombre
nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")
# Si el usuario escribe: Andrés
# Salida: Hola, Andrés!

# Ejemplo 2: Conversión a número entero
edad = int(input("Introduce tu edad: "))
print(f"Tendrás {edad + 1} años el próximo año.")
# Si el usuario escribe: 25
# Salida: Tendrás 26 años el próximo año.

# Ejemplo 3: Conversión a número flotante
altura = float(input("Introduce tu altura en metros: "))
print(f"Tu altura es {altura} m.")
# Si el usuario escribe: 1.75
# Salida: Tu altura es 1.75 m

# Ejemplo 4: Leer valores separados por comas
valores = input("Introduce varios valores separados por comas: ").split(",")
print(f"Los valores son: {valores}")
# Si el usuario escribe: 1, 2, 3
# Salida: Los valores son: ['1', ' 2', ' 3']

# Ejemplo 5: Leer valores separados por espacios
valores = input("Introduce varios valores separados por espacios: ").split()
print(f"Los valores son: {valores}")
# Si el usuario escribe: 1 2 3
# Salida: Los valores son: ['1', '2', '3']

# Ejemplo 6: Leer y desempaquetar varios valores en variables
a, b, c = map(int, input("Introduce tres números separados por espacios: ").split())
print(f"Los números son: {a}, {b}, {c}")
# Si el usuario escribe: 10 20 30
# Salida: Los números son: 10, 20, 30
