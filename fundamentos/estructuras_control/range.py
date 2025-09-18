"""
* range() - Generador de secuencias numéricas
-------------------------------------------
`range()` es un objeto especial que representa una secuencia inmutable de números enteros.

- Se usa comúnmente en bucles `for` para repetir acciones un número determinado de veces.
- Todos sus parámetros deben ser números enteros (int).

Eficiencia de memoria:
----------------------
- `range` no almacena todos los números en memoria desde el inicio.
- Genera cada número cuando se necesita, lo que lo hace muy eficiente, incluso para secuencias enormes.

Características principales:
-----------------------------
- Es inmutable: no se pueden cambiar sus valores una vez creado.
- Se puede acceder a sus elementos por índice (como una lista): `rango[0]`, `rango[-1]`
- Admite slicing (subsecuencias): `rango[2:5]`
- Soporta índices negativos para recorrer desde el final.

Sintaxis y parámetros:
-----------------------
range(start, stop, step)

- start (inicio) → número desde donde empieza la secuencia (por defecto 0).
- stop (fin) → número donde termina la secuencia (¡no incluido!).
- step (salto) → cuánto aumenta o disminuye cada vez (por defecto 1).
  - Si es negativo, la secuencia va hacia atrás.

Ventaja frente a list o tuple:
-------------------------------
- `range` usa siempre la misma cantidad de memoria, sin importar cuántos números genere.
"""

# Ejemplo 1: Rango básico de 0 a 9
# Si pasamos un solo argumento a range(stop),
# la secuencia empieza en 0 y termina en stop - 1
rango = range(10)
print(rango)  # Salida: range(0, 10)  → representación del objeto range
print(list(rango))  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  → convertido a lista


# Ejemplo 2: Comprobar si un número está en el rango
print(5 in rango)  # True  → el número 5 está en la secuencia
print(11 in rango)  # False → el número 11 no está en la secuencia


# Ejemplo 3: Usando start y stop (sin step)
# range(start, stop) crea una secuencia que inicia en "start"
# y finaliza en stop - 1, con un incremento de 1 por defecto
rango2 = range(3, 10)
print(list(rango2))  # Salida: [3, 4, 5, 6, 7, 8, 9]


# Ejemplo 4: Secuencia decreciente con step negativo
# Si el "step" es negativo, los números disminuyen
# En este caso, "start" debe ser mayor que "stop"
rango_negativo = range(10, 0, -2)
print(list(rango_negativo))  # Salida: [10, 8, 6, 4, 2]


# Ejemplo 5: Uso en un bucle for
# range es muy usado para ejecutar un bloque de código varias veces
for i in range(3):
    print(i)  # Salida: 0, 1, 2


# Ejemplo 6: Acceso por índice
# Igual que una lista, range permite acceder a elementos por posición
print(rango[0])  # Salida: 0   → primer elemento
print(rango[-1])  # Salida: 9   → último elemento


# Ejemplo 7: Rebanado (slicing)
# Podemos extraer una parte de la secuencia usando índices
rango_slice = rango[2:5]
print(list(rango_slice))  # Salida: [2, 3, 4]


# Ejemplo 8: Longitud de un rango
# La función len() devuelve el número de elementos en el rango
print(len(rango))  # Salida: 10
print(len(rango_negativo))  # Salida: 5

# Ejemplo 9: Usando start, stop y step
# range(start, stop, step)
rango_3 = range(1, 10, 3)
print(list(rango_3))  # Salida: [1, 4, 7]

# Ejemplo 10: Ignorar el valor del índice en un bucle for
# -------------------------------------------------------
# A veces necesitamos repetir una acción varias veces,
# pero no nos importa el valor del índice del bucle.
# Por convención, en Python usamos la variable "_" para indicar
# que esa variable no se utilizará.
for _ in range(5):
    print("Mayer")

# Ejemplo 11: Recorrer una lista y un string en reversa
# -----------------------------------------------------
# range(inicio, fin_exclusivo, paso)
# En este caso:
# - inicio = len(lista) - 1 → último índice
# - fin_exclusivo = -1 → porque queremos incluir el índice 0
# - paso = -1 → vamos de atrás hacia adelante

lista = [1, 2, 3, 4, 5]
print("Recorriendo lista en reversa con range(): ")
for i in range(len(lista) - 1, -1, -1):
    print(f"Elemento: {lista[i]}")

# Recorriendo un string en reversa
cadena = "Python"
print("Recorriendo cadena en reversa con range(): ")
for i in range(len(cadena) - 1, -1, -1):
    print(f"Letra: {cadena[i]}")