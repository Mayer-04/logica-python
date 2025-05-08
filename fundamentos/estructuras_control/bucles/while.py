"""
* Estructura de control repetitiva `while`
------------------------------------------
El bucle while en Python permite ejecutar un bloque de código de manera repetitiva,
mientras se cumpla una condición específica.

- El código dentro del bloque del bucle se ejecutará siempre que la condición especificada sea verdadera.
- Cada vez que el bloque de código se ejecuta, se denomina una "iteración".
- Cualquier expresión o variable puede usarse como `condición` del bucle while.
- En Python, el bucle while evaluará y transformará la condición en un valor booleano (True o False).
- Partes de un bucle while:
    - Inicialización: Se declara y se da valor a una variable antes de comenzar el bucle.
    - Condición: Es una expresión que se evalúa antes de cada iteración del bucle. (True o False)
    - Cuerpo del bucle: El bloque de código que se ejecuta en cada iteración del bucle.
    - Actualización: La variable de "inicio" se "incrementa" o "decrementa" en cada iteración del bucle.
- En un bucle `while`, la cláusula `else` se ejecuta después de que la condición del bucle se vuelve falsa,
solo si el bucle no se interrumpio con `break`.
"""

# Bucle while básico
# Este bucle sigue ejecutándose mientras la condición sea verdadera
# Importante: Asegúrate de que la condición eventualmente se vuelva falsa para evitar bucles infinitos.
contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1  # Incrementa el contador en cada iteración


# Bucle while con else
# El bucle `else` en un bucle `while` se ejecuta solo si el bucle no se interrumpió con `break`
contador = 0
while contador < 3:
    print(f"El contador es: {contador}")
    contador += 1
else:
    print("El bucle while ha terminado.")


# Bucle while con la palabra reservada `break`
# Podemos forzar una salida del bucle en cualquier momento antes de que la condición se vuelva falsa.
i = 0
while i < 10:
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print("Bucle while con break:", i)
    i += 1

# Bucle while con la palabra reservada `continue`
# No detiene el bucle completo.
# En su lugar, detiene la iteración actual y fuerza al bucle a comenzar una nueva (si la condición lo permite).
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Salta al siguiente ciclo si i es par
    print(f"Bucle while con continue: {i}")  # Solo imprime números impares


# Bucle while con la palabra reservada `pass`
i = 0
while i < 10:
    i += 1
    if i == 5:
        pass
    print("Bucle while con pass:", i)


# Bucle while anidado
# Un bucle dentro de otro bucle
i = 0
while i < 3:  # Bucle exterior
    j = 0
    while j < 2:  # Bucle interior
        print(f"i={i}, j={j}")
        j += 1
    i += 1


# * Simulando un bucle `do while` en Python
# El bloque de código se ejecute al menos una vez, y la condición dentro del bucle decide cuándo salir de él.
# Este ejemplo pide al usuario que ingrese un número positivo y no termina hasta que se ingrese un valor válido.
while True:
    # Código que se ejecuta al menos una vez
    numero = int(input("Introduce un número positivo: "))
    # Condición para romper el bucle
    if numero > 0:
        break
    print("El número no es positivo. Inténtalo de nuevo.")

print(f"Número válido introducido: {numero}")
