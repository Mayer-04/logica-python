"""
* Variables y constantes en Python
-----------------------------------
En Python, no es necesario usar palabras clave especiales para declarar una variable.
Simplemente se asigna un valor a un nombre utilizando el operador `=`.

Características de las variables:
---------------------------------
- Las variables en Python son `etiquetas` que hacen referencia a objetos en memoria.
- Cuando asignas un valor a una variable, estás creando una `referencia` al objeto,
no copiando el valor literalmente.
- La convención para nombrar variables es usar `snake_case`: minúsculas y guiones bajos para separar palabras.
  Ejemplo: `mi_variable`, `total_suma`, `contador_items`
- Los nombres de las variables deben ser `descriptivos` y cortos para mejorar la legibilidad del código.
- Python tiene `palabras reservadas` (como `for`, `if`, `class`, etc.)
que no pueden usarse como nombres de variables, ya que forman parte de la sintaxis del lenguaje.

Palabras reservadas: Son palabras (términos) que utiliza Python para su funcionamiento interno,
así que no se pueden usar como nombres de variables.
"""

# Declaración de variables
numero = 2  # Variable de tipo entero (int)
mi_nombre = "Mayer"  # Variable de tipo cadena de texto (str)

# Declarando múltiples variables en una sola línea
# Es una buena práctica declarar variables en líneas separadas para mayor claridad
a, b, c = 1, 2, 3  # Variables de tipo entero (int)

# Intercambiar valores entre variables
x, y = 10, 20  # Asignación múltiple
x, y = y, x  # Intercambio de valores entre 'x' y 'y'
print(
    f"Después del intercambio, x = {x}, y = {y}"
)  # Después del intercambio, x = 20, y = 10

# Uso de variables globales
# En general, el uso de variables globales se debe evitar a menos que sea necesario, ya que puede
# dificultar la comprensión y el mantenimiento del código.
new_variable = "Andres"  # Variable global

# Uso de f-strings para formatear cadenas de texto con variables
numero2 = 5
resultado = f"El resultado de sumar {numero} y {numero2} es: {numero + numero2}"
print(resultado)  # Imprime el resultado de la suma de 'numero' y 'numero2'


# Esta función modifica la variable global 'new_variable' y la imprime.
# Es importante declarar la variable como 'global' para modificar su valor dentro de la función.
def my_function():
    # Declarar la variable como 'global'.
    global new_variable

    # Modificar el valor de la variable global.
    new_variable = "Mayer"

    # Imprimir el valor de la variable global.
    print(
        f"Valor de 'new_variable' dentro de la función: {new_variable}"
    )  # Valor de 'new_variable' dentro de la función: Mayer


# Llamando a la función que modifica e imprime la variable 'new_variable'
my_function()

# Imprime el valor final de la variable global
print(
    f"Valor de 'new_variable' fuera de la función: {new_variable}"
)  # Valor de 'new_variable' fuera de la función: Mayer

"""
* Constantes
-------------
- En Python no existen las constantes. Sin embargo, se pueden definir utilizando convenciones.
- Por convención, las constantes se escriben en `mayúsculas` y deben ser solo para lectura, no para escritura.
- Las constantes ayudan a indicar que ciertos valores no deben ser modificados durante la ejecución del programa.
"""
# Constante (por convención, se usa en mayúsculas)
MY_NAME = "Mayer"
print(f"Mi nombre es: {MY_NAME}")  # Mi nombre es: Mayer

# Intento de modificar una constante
# Aunque no es recomendable, técnicamente se puede modificar el valor de una "constante" en Python.
# Esto es solo para fines ilustrativos y no es una práctica recomendada.
MY_NAME = "Andres"  # No recomendado: Modificar una "constante"
print(
    f"Mi nuevo nombre es: {MY_NAME}"
)  # Imprime el nuevo valor, lo cual muestra la flexibilidad de Python
