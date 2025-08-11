"""
* Estructuras de control condicionales
--------------------------------------
Las estructuras condicionales permiten que un programa tome decisiones:
dependiendo de si una condición es verdadera (True) o falsa (False), se ejecuta un bloque de código u otro.

- if: Evalúa una condición; si es verdadera, ejecuta su bloque de código.
- elif: ("else if") Se usa después de un if para evaluar una nueva condición si la anterior fue falsa.
- else: Se ejecuta cuando todas las condiciones anteriores (if y elif) resultaron falsas.

A partir de Python 3.10, también existe:
----------------------------------------
- match: Similar a `switch` en otros lenguajes, permite comparar un valor contra varios patrones y ejecutar
  el bloque que coincida. Muy útil para evitar largas cadenas de `if/elif`.

Notas importantes:
------------------
- Las condiciones se evalúan como valores booleanos (True o False).
- Aunque es válido usar `pass` en un `else`, normalmente es innecesario y se considera mala práctica.
"""

# if básico
# Ejecuta el bloque solo si la condición es verdadera
numero = 5
if numero > 0:
    print("El número es positivo.")  # Se cumple porque 5 > 0

# if con else
# Si la condición es falsa, se ejecuta el bloque de 'else'
numero = -3
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")

# if, elif y else
# Permite evaluar varias condiciones en orden
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print(
        "El número es cero."
    )  # Se ejecuta si todas las condiciones anteriores son falsas

# Uso con múltiples rangos de valores
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

# * Condiciones en una sola línea con el `Operador Ternario`
#
# Sintaxis: <valor_si_true> if <condición> else <valor_si_false>
#
# [código si se cumple] if [condición] else [código si no se cumple]
#
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
