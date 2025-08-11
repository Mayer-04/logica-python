"""
* Estructura de control repetitiva `for`
----------------------------------------
En Python, el bucle for recorre (itera) una secuencia de elementos, por ejemplo, una lista, tupla, diccionario,
cadena de texto (string) o un rango numérico (range) en el orden en que aparecen.
En cada iteración, toma un elemento de la secuencia y ejecuta un bloque de código con él.

Python incluye herramientas para controlar el flujo dentro de un bucle:

- `break`: Detiene el bucle de inmediato, sin terminar las iteraciones restantes.
- `continue`: Salta al inicio de la siguiente iteración, ignorando el código que queda en la actual.
- `else`: Se ejecuta una sola vez al final del bucle, pero solo si este no terminó con break.
- `pass`: No hace nada; se usa como marcador de posición cuando la sintaxis requiere una instrucción
   pero aún no quieres escribir código allí.

Notas importantes:
------------------
- No modifiques directamente la lista o secuencia que estás recorriendo; esto puede producir errores o
  comportamientos inesperados. Si necesitas cambiarla, trabaja con una copia (lista[:] o list(lista)).
- Para operaciones simples y expresiones cortas, considera usar `list comprehensions` cuando sea posible:
  Son más rápidas y más fáciles de leer para tareas simples.
"""

# Bucle for básico
# Recorre cada elemento de la lista en orden
# La variable 'fruta' va tomando el valor de cada elemento en cada vuelta
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}")

# Usando range() con for
# range(n) crea números del 0 hasta n-1
for i in range(5):
    print(f"Iteración {i}")  # Imprime 0, 1, 2, 3, 4

# range(inicio, fin, salto)
# 'salto' indica cada cuántos números avanzar en la secuencia
# Por defecto, el salto es 1
for i in range(1, 10, 2):
    print(f"Número impar: {i}")  # Imprime 1, 3, 5, 7, 9

# Recorrer un string
# El bucle `for` también funciona sobre cada letra (carácter) de un texto
for letra in "Python":
    print(f"Letra: {letra}")  # Imprime P, y, t, h, o, n


# Iterar usando índices (no recomendado)
# Se usa len() para saber cuántos elementos hay
names = ["John", "Corey", "Adam", "Steve"]
for i in range(len(names)):
    print("Índice:", i, ", Nombre:", names[i])

# Bucle for con enumerate()
# `enumerate()` permite acceder tanto al índice como al valor de los elementos en una secuencia
# Devuelve el índice y el valor al mismo tiempo
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


# break: salir del bucle antes de tiempo
for fruta in frutas:
    if fruta == "banana":
        break  # Termina el bucle si encuentra "banana"
    print(f"Me gusta comer {fruta}")


# Usando continue para saltar una iteración
# `continue` salta el resto del código en la iteración actual y pasa a la siguiente
for fruta in frutas:
    if fruta == "banana":
        continue  # Salta la iteración actual si la fruta es "banana"
    print(f"Me gusta comer {fruta}")


# else en un bucle
# El bloque `else` en un bucle se ejecuta solo si el bucle no se interrumpió con `break`
for fruta in frutas:
    print(f"Me gusta comer {fruta}")
else:
    print(
        "He terminado de comer todas las frutas."
    )  # El `else` aquí se ejecuta porque no hubo un `break`.


# Bucles anidados
# Un bucle dentro de otro para combinaciones de valores.
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Comprensión de listas (List Comprehensions)
# Una forma concisa y eficiente de crear listas
# Ejemplo: Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)  # Imprime [1, 4, 9, 16, 25]


# Recorriendo una lista y un string al revés
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

# Iterando una cadena saltándose elementos
# Recorrer saltando elementos (de 2 en 2)
for letra in lenguaje[::2]:
    print("Letras 2 en 2:", letra)  # Imprime `JvSrp`
