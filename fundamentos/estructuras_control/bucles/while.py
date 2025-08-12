"""
* Estructura de control repetitiva: while
-----------------------------------------
El bucle `while` en Python ejecuta un bloque de código repetidamente
mientras se cumpla una condición.

Conceptos clave:
----------------
- Una "iteración" es cada vez que el bloque de código se ejecuta.
- La condición puede ser cualquier expresión o variable que Python
  pueda evaluar como True o False.
- Partes típicas de un bucle `while`:
    1. Inicialización → Se prepara una o varias variables antes del bucle.
    2. Condición → Se evalúa antes de cada iteración.
    3. Cuerpo del bucle → Código que se ejecuta en cada iteración.
    4. Actualización → Cambio en las variables para evitar bucles infinitos.
- El bloque `else` después de un `while` se ejecuta solo si la condición
  se vuelve falsa y el bucle no fue interrumpido con `break`.

Nota importante:
----------------
- Asegúrate de que la condición pueda volverse falsa, o tendrás
  un bucle infinito.
"""

# ------------------------------------------------
# * Bucle while básico
# ------------------------------------------------
contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1  # Actualización para evitar bucle infinito


# ------------------------------------------------
# * while con else
# ------------------------------------------------
# El bloque `else` se ejecuta solo si el bucle termina de forma natural,
# es decir, sin que un `break` lo interrumpa
contador = 0
while contador < 3:
    print(f"El contador es: {contador}")
    contador += 1
else:
    print("El bucle while ha terminado.")


# ------------------------------------------------
# * while con break
# ------------------------------------------------
# `break` interrumpe el bucle inmediatamente, sin importar la condición
i = 0
while i < 10:
    if i == 5:
        break  # Salimos cuando i es igual a 5
    print("Bucle while con break:", i)
    i += 1


# ------------------------------------------------
# * while con continue
# ------------------------------------------------
# `continue` salta a la siguiente iteración, sin ejecutar
# el resto del código de la iteración actual
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Saltar si i es par
    print(f"Bucle while con continue: {i}")  # Solo imprime impares


# ------------------------------------------------
# * while con pass
# ------------------------------------------------
# `pass` no hace nada: es un "marcador de posición" para cuando la sintaxis exige
# una instrucción pero no queremos ejecutar ninguna acción
i = 0
while i < 10:
    i += 1
    if i == 5:
        pass  # No hace nada especial cuando i es 5
    print("Bucle while con pass:", i)


# ------------------------------------------------
# * while anidado
# ------------------------------------------------
# Un bucle dentro de otro bucle
i = 0
while i < 3:  # Bucle exterior
    j = 0
    while j < 2:  # Bucle interior
        print(f"i={i}, j={j}")
        j += 1
    i += 1


# ------------------------------------------------
# * Simulación de do-while en Python
# ------------------------------------------------
# En otros lenguajes, "do-while" ejecuta el bloque al menos una vez
# En Python se simula con while True y un break manual
while True:
    numero = int(input("Introduce un número positivo: "))
    if numero > 0:
        break  # Salimos si el número es válido
    print("El número no es positivo. Inténtalo de nuevo.")

print(f"Número válido introducido: {numero}")
