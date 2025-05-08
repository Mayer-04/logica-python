"""
* Estructura de control repetitiva `for`
----------------------------------------
El bucle for en Python `itera` sobre una secuencia (como una lista, tupla, diccionario, string o rango), 
en el orden que aparecen en la secuencia y ejecuta un bloque de código por cada elemento.

Python ofrece las siguientes herramientas adicionales para el control de bucles:

- `break`: Termina el bucle antes de que se complete normalmente.
- `continue`: Salta el resto del código dentro del bucle y pasa a la siguiente iteración.
- `else`: Ejecuta un bloque de código al final del bucle, pero solo si el bucle no se interrumpió con `break`.
- En un bucle `for`, la cláusula `else` se ejecuta después de que el bucle alcance su iteración final.
- `pass`: Actúa como un marcador de posición donde se necesita una declaración, pero no se necesita hacer nada.

Algunas consideraciones adicionales:
------------------------------------
- Evita modificar la lista sobre la que estás iterando: Esto puede causar resultados inesperados o errores. 
Si necesitas modificar la lista, considera crear una copia.
- Utiliza `list comprehensions` cuando sea posible: Son más rápidas y más fáciles de leer para tareas simples.
"""

# Bucle for básico
# Este bucle itera sobre una secuencia (en este caso, una lista)
# La variable 'fruta' toma el valor de cada elemento de la lista en cada iteración.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}")


# Usando range() con for
# `range()` genera una secuencia de números enteros, útil para iterar un número específico de veces
# Por defecto se empieza en 0
for i in range(5):
    print(f"Iteración {i}")  # Imprime 0, 1, 2, 3, 4

# `range()` puede tomar hasta tres argumentos: inicio, fin y salto entre elementos
# Por defecto el salto es 1
for i in range(1, 10, 2):
    print(f"Número impar: {i}")  # Imprime 1, 3, 5, 7, 9

# Usando `range()` con una cadena de texto
for letra in "Python":
    print(f"Letra: {letra}")  # Imprime `P`, `y`, `t`, `h`, `o`, `n`


# Iterar sobre los índices de una secuencia, combinando range() y len()
# Se recomienda usar `enumerate()`
names = ["John", "Corey", "Adam", "Steve"]

for i in range(len(names)):
    print("Índice:", i, ", Nombre:", names[i])

# Bucle for con enumerate()
# `enumerate()` permite acceder tanto al índice como al valor de los elementos en una secuencia
# Esto es especialmente útil cuando necesitas el índice de los elementos en la iteración.
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


# Usando break para salir de un bucle
# `break` se usa para terminar un bucle prematuramente
for fruta in frutas:
    if fruta == "banana":
        break  # El bucle termina si se encuentra con "banana"
    print(f"Me gusta comer {fruta}")


# Usando continue para saltar una iteración
# `continue` salta el resto del código en la iteración actual y pasa a la siguiente
for fruta in frutas:
    if fruta == "banana":
        continue  # Salta la iteración actual si la fruta es "banana"
    print(f"Me gusta comer {fruta}")


# Bucle else
# El bloque `else` en un bucle se ejecuta solo si el bucle no se interrumpió con `break`
for fruta in frutas:
    print(f"Me gusta comer {fruta}")
else:
    print(
        "He terminado de comer todas las frutas."
    )  # El `else` aquí se ejecuta porque no hubo un `break`.


# Uso de bucles anidados
# Puedes anidar bucles (un bucle dentro de otro)
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")


# Comprensión de listas (List Comprehensions)
# Una forma concisa y eficiente de crear listas
# Ejemplo: Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)  # Imprime [1, 4, 9, 16, 25]


# * Recorriendo una lista y un string al revés
# Ejemplo con una lista de frutas
frutas = ["manzana", "banana", "cereza", "durazno"]

# El método `reversed()` permite invertir el orden de una secuencia
for fruta in reversed(frutas):
    print("frutas:", fruta)

# Ejemplo con una cadena
lenguaje = "JavaScript"

# Utilizando el slicing `::-1`
for letra in lenguaje[::-1]:
    print("Letras:", letra)

# Iterando una cadena saltándose elementos.
# Un elemento si y otro no
for letra in lenguaje[::2]:
    print("Letras 2 en 2:", letra)  # Imprime `JvSrp`
