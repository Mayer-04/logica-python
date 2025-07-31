"""
* Range - Rango
----------------
- La función `range` es un objeto que genera una secuencia inmutable de números enteros.
- Se suele utilizar para ser ejecutado en un bucle `for`.
- Los parámetros usados en range deben ser números enteros.
- `range` no genera todos los números en la memoria desde el inicio. En su lugar, los números
se generan cuando son necesarios, lo que lo hace eficiente en cuanto a memoria, incluso con grandes rangos.
- Los valores de un objeto `range` son inmutables, por lo que no se pueden modificar.
- Aunque es inmutable, `range` puede ser indexado y rebanado (slicing).

range toma tres argumentos:
-----------------------------
start (inicio), stop (fin) y step (salto) entre elementos.
- Si `step` se omite, se establece en 1.
- Si se omite el parámetro `start`, se establece en 0.
- Los rangos soportan índices negativos, lo que permite generar secuencias decrecientes.

IMPORTANTE: La ventaja de usar un objeto de tipo `range` en vez de uno de tipo `list` o `tuple`
es que `range` usa una cantidad fija de memoria sin importar cuán grande sea el rango.
"""

# Ejemplo 1: Un rango de 0 a 9 (el 'stop' no se incluye)
rango = range(10)
print(rango)  # Salida: range(0, 10)
print(list(rango))  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplo 2: Verifica si un número está en el rango
print(5 in rango)  # Salida: True
print(11 in rango)  # Salida: False

# Ejemplo 3: Usar start y stop, sin step
rango2 = range(3, 10)
print(list(rango2))  # Salida: [3, 4, 5, 6, 7, 8, 9]

# Ejemplo 4: Usar start, stop y un step negativo
# Cuando el step es negativo, los números en la secuencia disminuyen en lugar de aumentar.
# El valor de start debe ser mayor que el valor de stop.
rango_negativo = range(10, 0, -2)
print(list(rango_negativo))  # Salida: [10, 8, 6, 4, 2]

# Ejemplo 5: Ver uso en un bucle for
for i in range(3):
    print(i)  # Salida: 0, 1, 2

# Ejemplo 6: Indexación
print(rango[0])  # Salida: 0
print(rango[-1])  # Salida: 9 (último elemento)

# Ejemplo 7: Rebanada (slicing)
rango_slice = rango[2:5]
print(list(rango_slice))  # Salida: [2, 3, 4]

# Ejemplo 8: Longitud de un rango
print(len(rango))  # Salida: 10
print(len(rango_negativo))  # Salida: 5
