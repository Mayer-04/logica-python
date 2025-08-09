# =====================================
# * Función incorporada ascii()
# =====================================
# Devuelve la representación en cadena de un objeto,
# pero reemplaza los caracteres no ASCII con secuencias de escape.
#
# Útil para mostrar texto que contenga caracteres especiales
# de forma "segura" para ASCII.
#
# Forma general:
# ascii(objeto)

# Ejemplo 1: Texto con caracteres especiales
texto = "Hola, mundo 🌎"
print(ascii(texto))  # Salida: 'Hola, mundo \U0001f30e'
# (El emoji se muestra como su código Unicode)

# Ejemplo 2: Caracteres acentuados
palabra = "canción"
print(ascii(palabra))  # Salida: 'canci\u00f3n'
# (La ó se reemplaza por su código Unicode)

# Ejemplo 3: Lista con símbolos
datos = ["mañana", "☀️", "árbol"]
print(ascii(datos))  # Salida: ['ma\u00f1ana', '\u2600\ufe0f', '\u00e1rbol']
