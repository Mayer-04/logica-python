"""
* Estructuras de control condicionales
--------------------------------------
Las estructuras condicionales permiten que un programa ejecute diferentes bloques de código en función de ciertas
condiciones.

- `if`: Evalúa una condición y, si es verdadera, ejecuta un bloque de código.
- `elif`: Se usa después de un `if` inicial para verificar una nueva condición si la primera es falsa.
Es una abreviación de “else if” (si no - de lo contrario si).
- `else`: Se ejecuta si todas las condiciones anteriores (`if` y `elif`) son falsas.
- `match`: Introducido en Python 3.10, similar a `switch` en otros lenguajes, 
permite seleccionar un bloque de código para ejecutar basado en el valor de una expresión.

Las condiciones que se evalúan en estas estructuras deben resolverse en valores booleanos 
(`True` o `False`) para determinar el flujo de ejecución.

- Es mala practica poner `pass` dentro de un `else` ya que es redundante.
"""

numero = 5

# Condicional if básico
# Verificamos si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")  # Se ejecuta si la condición es verdadera

# Introducción a las condiciones con 'if' y 'else'
# Este ejemplo verifica si un número es positivo o negativo

numero = -3

# Condición para verificar si el número es mayor que cero
if numero > 0:
    print("El número es positivo.")
else:
    print(
        "El número es negativo o cero."
    )  # Se ejecuta si la condición del 'if' es falsa

# Introducción a las condiciones con 'if', 'elif' y 'else'
# Este ejemplo verifica si un número es positivo, negativo o cero
numero = 0

# Se evalúan múltiples condiciones secuencialmente
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print(
        "El número es cero."
    )  # Se ejecuta si todas las condiciones anteriores son falsas

# Uso de múltiples condiciones con 'if', 'elif' y 'else'
# Este ejemplo clasifica a una persona según su edad
edad = 25

if edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# Curiosidad: Condiciones en una sola línea con el Operador Ternario
# Sintaxis: <valor_si_true> if <condición> else <valor_si_false>
# [código si se cumple] if [condición] else [código si no se cumple]
# Este operador es útil para expresiones cortas y claras
numero = 5
mensaje = (
    "Positivo" if numero > 0 else "No positivo"
)  # Asigna 'Positivo' si la condición es verdadera, de lo contrario 'No positivo'
print(mensaje)  # Imprime 'Positivo'

"""
* Profundizando en el operador ternario:
Si la calificación es 6 o más, se asignará 'Aprobado', de lo contrario 'Reprobado'.
"""
calificacion = 8
condicion = calificacion >= 6
mensaje = "Aprobado" if condicion else "Reprobado"
print(
    mensaje
)  # Imprime 'Aprobado' porque la condición es verdadera (calificación >= 6)

# * Uso del operador walrus (:=) - A partir de Python 3.8+
# Este operador permite asignar y evaluar en una misma expresión.
# Útil cuando queremos utilizar una variable tanto en la condición como en el bloque de código
if (n := 10) > 5:
    print(
        f"El número {n} es mayor que 5."
    )  # Asigna 10 a 'n' y verifica si es mayor que 5 en una sola línea
