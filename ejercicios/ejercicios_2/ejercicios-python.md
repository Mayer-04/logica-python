# Ejercicios de lógica de programación en Python

## Ejercicio 1: Área de un triángulo rectángulo

Crea una función en Python que calcule el área de un triángulo rectángulo.
El usuario debe ingresar la longitud de los dos catetos (lado A y lado B).
El programa debe mostrar el resultado del área utilizando la fórmula:
`area = (cateto1 * cateto2) / 2`

**Considera:** Validar que los valores ingresados sean números positivos.

## Ejercicio 2: Número par o impar

Escribe un programa que reciba un número entero como entrada y determine si es par o impar.
El programa debe mostrar un mensaje indicando el resultado.

**Recuerda:** Un número es par si es divisible entre 2 (resto = 0).

## Ejercicio 3: Verificar palíndromo

Escribe una función que determine si una palabra o frase es un palíndromo.
Un palíndromo se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios, signos de puntuación y mayúsculas/minúsculas.

**Ejemplo:** "Anita lava la tina" → es un palíndromo.

**Pasos sugeridos:**

1. Convertir todo a minúsculas
2. Eliminar espacios y signos de puntuación
3. Comparar la cadena con su reverso

## Ejercicio 4: Número mayor y menor en una lista

Crea una función que reciba una lista de números como parámetro y devuelva el número mayor y el número menor dentro de esa lista.

**Restricción:** No utilices las funciones built-in `max()` y `min()`. Implementa tu propia lógica de comparación.

**Ejemplo:**

```python
numeros = [45, 23, 78, 12, 90, 5]
# La función debe devolver: (90, 5)
```

## Ejercicio 5: Suma de múltiplos de 3 o 5

Dado un número **n**, encuentra la suma de todos los números positivos menores que n que sean múltiplos de 3 o de 5.

**Ejemplo:** para n = 10 → 3 + 5 + 6 + 9 = 23

**Nota:** Un número puede ser múltiplo de ambos (como el 15), pero solo debe sumarse una vez.

## Ejercicio 6: FizzBuzz

Escribe un programa que muestre los números del 1 al 100, pero aplicando las siguientes reglas:

- Si el número es múltiplo de 3, mostrar "Fizz".
- Si el número es múltiplo de 5, mostrar "Buzz".
- Si el número es múltiplo de 3 y 5 a la vez, mostrar "FizzBuzz".
- En los demás casos, mostrar el número.

**Salida esperada:** 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...

## Ejercicio 7: Factorial de un número

Escribe un programa que calcule el factorial de un número entero positivo.
Puedes hacerlo utilizando un bucle o de manera recursiva.

**Ejemplo:** `5! = 5 * 4 * 3 * 2 * 1 = 120`

**Desafío adicional:** Implementa ambas versiones (iterativa y recursiva) y compara su eficiencia.

## Ejercicio 8: Eliminar duplicados de una lista

Crea una función que reciba una lista como parámetro y devuelva una nueva lista sin elementos duplicados, manteniendo el orden de primera aparición.

**Restricción:** No puedes usar la conversión con `set()` ni métodos como `list(dict.fromkeys())`.

**Ejemplo:**

```python
original = [1, 2, 2, 3, 4, 4, 5, 1]
# Resultado: [1, 2, 3, 4, 5]
```

## Ejercicio 9: Seleccionar un elemento aleatorio

Escribe un programa que seleccione y muestre un elemento al azar de una lista dada.

**Restricción:** No uses la función `random.choice()`. Implementa tu propia lógica usando `random.randint()` o `random.random()`.

**Ejemplo:**

```python
lista = ["manzana", "banana", "naranja", "uva"]
# El programa debe seleccionar uno al azar
```

## Ejercicio 10: Conversión de temperaturas

Escribe un programa que convierta grados Celsius a Fahrenheit.
**Fórmula:** `F = (C * 9/5) + 32`

El programa debe:

1. Solicitar al usuario la temperatura en grados Celsius
2. Validar que sea un número válido
3. Realizar la conversión y mostrar el resultado con 2 decimales

**Extensión:** Permite también la conversión inversa (Fahrenheit a Celsius).

## Ejercicio 11: Generador de contraseñas

Escribe una función que genere contraseñas aleatorias según criterios especificados.

**Parámetros de entrada:**

- `longitud`: longitud de la contraseña (mínimo 4)
- `incluir_mayusculas`: booleano para incluir letras mayúsculas (A-Z)
- `incluir_minusculas`: booleano para incluir letras minúsculas (a-z)
- `incluir_numeros`: booleano para incluir dígitos (0-9)
- `incluir_simbolos`: booleano para incluir símbolos (!@#$%^&\*)

**Requisitos:**

- Al menos una opción debe estar en True
- La contraseña debe contener al menos un carácter de cada tipo seleccionado

## Ejercicio 12: Comparación de listas

Escribe una función que reciba dos listas y un valor booleano como parámetros.

**Parámetros:**

- `lista1`: primera lista de elementos
- `lista2`: segunda lista de elementos
- `comunes`: valor booleano que determina el tipo de resultado

**Reglas:**

- Si `comunes` es `True` → devolver una lista con los elementos que aparecen en ambas listas
- Si `comunes` es `False` → devolver una lista con los elementos que aparecen en una sola de las listas

**Ejemplos:**

```python
comparar_listas([1, 2, 3], [2, 3, 4], True)  # → [2, 3]
comparar_listas([1, 2, 3], [2, 3, 4], False) # → [1, 4]
```

## Ejercicio 13: Conversión a milisegundos

Escribe una función que reciba cuatro parámetros: días, horas, minutos y segundos.
La función debe calcular y devolver el tiempo total equivalente en milisegundos.

**Conversiones:**

- 1 segundo = 1,000 milisegundos
- 1 minuto = 60 segundos
- 1 hora = 60 minutos
- 1 día = 24 horas

**Ejemplo:**

```python
tiempo_a_ms(1, 2, 30, 45)  # 1 día, 2 horas, 30 minutos, 45 segundos
# Resultado: 95,445,000 milisegundos
```

## Ejercicio 14: Diferencia entre dos sets

Crea dos conjuntos (sets) con algunos elementos numéricos.
Escribe una función que reciba ambos sets como parámetros y devuelva un nuevo set que contenga los elementos que están en el primer set pero no en el segundo (diferencia A - B).

**Restricción:** No uses el operador `-` de sets. Implementa la lógica manualmente.

**Ejemplo:**

```python
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
# Resultado: {1, 2}
```

## Ejercicio 15: Elementos únicos de una lista

Crea una función `unique(lista)` que reciba una lista como parámetro y devuelva una nueva lista que contenga solo los elementos únicos (sin duplicados), preservando el orden de primera aparición.

**Diferencia con ejercicio 8:** Aquí puedes usar cualquier método que prefieras, incluyendo `set()` si lo deseas.

## Ejercicio 16: Ciudad más calurosa

Crea un diccionario donde las claves sean nombres de ciudades y los valores sean sus temperaturas actuales en grados Celsius.
Escribe una función que reciba el diccionario y devuelva el nombre de la ciudad con la temperatura más alta.

**Ejemplo:**

```python
temperaturas = {
    "Madrid": 28,
    "Barcelona": 25,
    "Sevilla": 35,
    "Valencia": 30
}
# La función debe devolver: "Sevilla"
```

**Considera:** ¿Qué hacer si hay un empate? Puedes devolver la primera ciudad encontrada.

## Ejercicio 17: Intersección de sets

Define dos conjuntos con algunos elementos en común.
Crea una función que reciba estos dos sets como parámetros y devuelva un nuevo set que contenga únicamente los elementos presentes en ambos conjuntos.

**Restricción:** No uses el operador `&` de sets. Implementa la intersección manualmente usando bucles.

## Ejercicio 18: Unión de sets

Crea dos conjuntos con valores únicos y escribe una función que reciba ambos y devuelva un nuevo set que contenga la unión de los dos (todos los elementos distintos presentes en al menos uno de ellos).

**Restricción:** No uses el operador `|` de sets. Implementa la unión manualmente.

## Ejercicio 19: Información de un canal

Crea una función que reciba dos parámetros: `name` (nombre del canal) y `subs` (número de suscriptores).
La función debe devolver un diccionario con la siguiente información:

- `'name'`: valor del parámetro name
- `'subscribers'`: valor del parámetro subs
- `'hash'`: longitud del string name multiplicada por subs
- `'getStatus'`: una función anidada que devuelva el texto:
  `"El canal de <name> tiene <subs> suscriptores."`

**Ejemplo:**

```python
canal = crear_canal("MiCanal", 1500)
print(canal['getStatus']())  # "El canal de MiCanal tiene 1500 suscriptores."
```

## Ejercicio 20: Propiedades booleanas

Escribe una función que reciba un diccionario como parámetro y devuelva una lista con los nombres de las claves que tienen valores booleanos (True o False).

**Ejemplo:**

```python
datos = {'activo': True, 'edad': 25, 'premium': False, 'nombre': 'Juan'}
# Resultado: ['activo', 'premium']
```

## Ejercicio 21: Multiplicar propiedades numéricas

Crea una función `multiplicar_numericos(diccionario)` que multiplique por 2 todas las propiedades numéricas de un diccionario (int y float).

**Importante:** La función debe modificar el diccionario directamente, no crear uno nuevo.

**Ejemplo:**

```python
datos = {'precio': 100, 'nombre': 'Producto', 'descuento': 0.15, 'activo': True}
multiplicar_numericos(datos)
# Resultado: {'precio': 200, 'nombre': 'Producto', 'descuento': 0.30, 'activo': True}
```

## Ejercicio 22: Suma de salarios

Dado un diccionario con los salarios de un equipo, escribe un programa que calcule la suma total de todos los salarios.

**Ejemplo:**

```python
salarios = {
    "Ana": 1200,
    "Carlos": 1500,
    "María": 1800,
    "Pedro": 1100
}
```

**Requisitos:**

1. Calcular la suma total
2. Si el diccionario está vacío, la suma debe ser 0
3. Guardar el resultado en una variable llamada `suma_total`
4. Mostrar el resultado con formato: "La suma total de salarios es: $X"

## Ejercicio 23: Buscar parejas que sumen un número dado

Escribe una función que encuentre todas las parejas de números en una lista cuya suma sea igual a un número objetivo.

**Parámetros:**

- `lista`: lista de números enteros
- `objetivo`: número objetivo para la suma

**Requisitos:**

- No repetir parejas invertidas (si incluyes (2,7), no incluyas (7,2))
- Devolver una lista de tuplas con las parejas encontradas

**Ejemplo:**

```python
buscar_parejas([2, 4, 3, 7, 5], 9)
# Resultado: [(2, 7), (4, 5)] -> 2 + 7 = 9 y 4 + 5 = 9
```

## Ejercicio 24: Copia de la primera mitad de una lista

Dada una lista de números, crea una copia de la primera mitad utilizando slicing en Python.

**Consideraciones:**

- Si la lista tiene un número impar de elementos, incluye el elemento central en la primera mitad
- Muestra tanto la lista original como la copia
- La copia debe ser independiente (modificar una no debe afectar la otra)

**Ejemplo:**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# Primera mitad: [1, 2, 3, 4]

numeros_impares = [1, 2, 3, 4, 5, 6, 7]
# Primera mitad: [1, 2, 3, 4]
```

## Ejercicio 25: Procesar pedido de restaurante

En un restaurante, los pedidos se representan como listas donde el primer elemento es el nombre del cliente y el resto son los platillos ordenados.

Escribe una función `procesar_pedido(pedido)` que:

1. Extraiga el nombre del cliente (primer elemento)
2. Añada "bebida" al inicio de la lista (promoción gratis)
3. Añada el nombre del cliente al final (para entrega)
4. Devuelva la lista modificada

**Ejemplo:**

```python
pedido_original = ["Ana", "pizza", "ensalada", "pasta"]
resultado = procesar_pedido(pedido_original)
# Resultado: ["bebida", "pizza", "ensalada", "pasta", "Ana"]
```

## Ejercicio 26: Suma de números pares

Escribe una función que reciba una lista de números y devuelva la suma de todos los números pares en la lista.

**Considera:** Si no hay números pares, devolver 0.

**Ejemplo:**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Pares: 2 + 4 + 6 + 8 + 10 = 30
```

## Ejercicio 27: Palabras terminadas en "a"

Crea una función que reciba una lista de palabras y devuelva `True` si **todas** las palabras terminan con la letra "a" (mayúscula o minúscula). Si al menos una no cumple la condición, devolver `False`.

**Considera:** ¿Qué pasa con una lista vacía? Por convención, devuelve `True`.

**Ejemplo:**

```python
palabras1 = ["casa", "mesa", "silla"]  # → True
palabras2 = ["casa", "mesa", "sofá"]   # → False (sofá termina en á)
```

## Ejercicio 28: Ordenar por valor absoluto

Dada una lista de números enteros (positivos y negativos), escribe una función que ordene los números de menor a mayor según su valor absoluto, manteniendo el signo original.

**Ejemplo:**

```python
numeros = [5, -10, -2, 25, -7, 3]
# Ordenados por valor absoluto: [-2, 3, 5, -7, -10, 25]
```

**Pista:** Usa la función `sorted()` con el parámetro `key`.

## Ejercicio 29: Palabras más largas que el índice

Escribe una función que reciba una lista de palabras y una palabra específica. La función debe:

1. Encontrar el índice de la palabra específica dentro de la lista.
2. Crear y devolver una nueva lista que contenga las palabras cuya longitud sea mayor que ese índice.

**Consideraciones:**

- Si la palabra no existe en la lista, la función debe devolver una lista vacía.
- Los índices comienzan desde 0.

**Ejemplo:**

```python
palabras = ["sol", "luna", "estrella", "planeta"]
palabra_buscar = "luna"  # índice = 1
# Palabras con longitud > 1 → ["luna", "estrella", "planeta"]
```

## Ejercicio 30: Orden ascendente y descendente

Escribe una función que reciba una lista de números y devuelva un diccionario con dos listas:

- `'asc'`: números ordenados de menor a mayor
- `'desc'`: números ordenados de mayor a menor

**Nota:** Preservar elementos duplicados en ambas listas.

**Ejemplo:**

```python
numeros = [7, 5, 7, 8, 6]
# Resultado: {'asc': [5, 6, 7, 7, 8], 'desc': [8, 7, 7, 6, 5]}
```

## Ejercicio 31: Filtrar nombres por terminación

Crea una función que reciba una lista de nombres y una cadena de terminación, y devuelva una nueva lista con los nombres que terminan con esa cadena.

**Consideraciones:**

- La comparación debe ser insensible a mayúsculas/minúsculas
- Si la cadena de terminación está vacía, devolver lista vacía

**Ejemplo:**

```python
nombres = ["Ana", "María", "Sofía", "Lola", "Carla"]
filtrar_nombres(nombres, "ía")  # → ["María", "Sofía"]
filtrar_nombres(nombres, "la")  # → ["Lola", "Carla"]
```

## Ejercicio 32: Verificar mayoría de edad

Tienes una lista de diccionarios, donde cada uno representa una persona con las propiedades `'nombre'` y `'edad'`.
Escribe una función que devuelva `True` si **todas** las personas tienen 18 años o más, y `False` si al menos una es menor.

**Ejemplo:**

```python
personas = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Carlos', 'edad': 17},
    {'nombre': 'María', 'edad': 22}
]
# Resultado: False (Carlos es menor de edad)
```

## Ejercicio 33: Filtrar números pares

Escribe una función que reciba una lista de números y devuelva una nueva lista que contenga solo los números pares.

**Extensión:** Crea también una versión que filtre números impares.

## Ejercicio 34: Encontrar el primer número mayor que 10

Escribe una función que reciba una lista de números y devuelva el primer número que sea mayor que 10.
Si no existe ninguno, debe devolver `None`.

**Ejemplo:**

```python
numeros1 = [3, 7, 15, 8, 12]  # → 15 (primer número > 10)
numeros2 = [1, 2, 3, 4, 5]    # → None (ninguno > 10)
```

## Ejercicio 35: Longitud de palabras

Escribe una función que reciba una lista de palabras y devuelva una nueva lista con la longitud de cada palabra.

**Ejemplo:**

```python
palabras = ["hola", "python", "programación", "sol"]
# Resultado: [4, 6, 12, 3]
```

## Ejercicio 36: Suma de elementos

Escribe una función que reciba una lista de números y devuelva la suma de todos sus elementos.

**Restricción:** No uses la función built-in `sum()`. Implementa tu propia lógica con un bucle.

## Ejercicio 37: Palabra con más de 5 caracteres

Escribe una función que reciba una lista de strings y devuelva `True` si al menos uno de los elementos tiene más de 5 caracteres. En caso contrario, devolver `False`.

**Ejemplo:**

```python
palabras1 = ["sol", "luna", "estrella"]  # → True ("estrella" tiene 8)
palabras2 = ["sol", "luna", "mar"]       # → False (todas ≤ 5)
```

## Ejercicio 38: Filtrar cadenas por longitud mínima

Escribe una función que reciba una lista de strings y un número mínimo de caracteres, y devuelva una nueva lista con las cadenas cuya longitud sea igual o superior al mínimo indicado.

**Ejemplo:**

```python
palabras = ["sol", "luna", "estrella", "mar", "montaña"]
filtrar_longitud(palabras, 5)  # → ["estrella", "montaña"]
```

## Ejercicio 39: Buscar "JavaScript" en una matriz

Dada una matriz (lista de listas) de cadenas de texto, escribe una función que busque la palabra "JavaScript" y devuelva su posición como una lista `[fila, columna]`.
Si no se encuentra, devolver `[-1, -1]`.

**Ejemplo:**

```python
matriz = [
    ["HTML", "CSS", "JavaScript"],
    ["Java", "C++", "Python"],
    ["Ruby", "Go", "Swift"]
]
# La función debe devolver: [0, 2]
```

**Considera:** ¿La búsqueda debe ser sensible a mayúsculas/minúsculas?

## Ejercicio 40: Promedio de números pares

Escribe una función que reciba una lista de números y calcule el promedio (media aritmética) solo de los números pares.
Si no hay números pares en la lista, devolver 0.

**Ejemplo:**

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# Pares: [2, 4, 6, 8] → Promedio: (2+4+6+8)/4 = 5.0
```

## Ejercicio 41: Promedio de una lista

Escribe una función que reciba una lista de números y devuelva su promedio (media aritmética).

**Consideraciones:**

- Si la lista está vacía, devolver 0
- El resultado puede ser un número decimal

**Ejemplo:**

```python
numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Promedio: 45/10 = 4.5
```

## Ejercicio 42: Unión de listas sin duplicados

Escribe una función que reciba dos listas y devuelva una nueva lista con la unión de ambas, eliminando los elementos duplicados y preservando el orden de aparición.

**Criterio de orden:** Primero los elementos de la primera lista (sin duplicados), luego los elementos de la segunda lista que no aparecían en la primera.

**Ejemplo:**

```python
lista1 = [1, 2, 3, 2]
lista2 = [3, 4, 5, 1]
# Resultado: [1, 2, 3, 4, 5]
```

---

## Ejercicio 43: Contar vocales y consonantes

Escribe una función que reciba una cadena de texto y devuelva un diccionario con la cantidad de vocales y consonantes que contiene.

**Ejemplo:**

```python
texto = "Programación"
# Resultado: {'vocales': 5, 'consonantes': 7}
```

## Ejercicio 44: Eliminar palabras cortas

Escribe una función que reciba una lista de palabras y un número entero `n`, y devuelva una nueva lista con las palabras cuya longitud sea `mayor que n`.

**Ejemplo:**

```python
palabras = ["sol", "computadora", "luna", "python"]
n = 4
# Resultado: ["computadora", "python"]
```

## Ejercicio 45: Suma diagonal de una matriz

Dada una matriz cuadrada (lista de listas), calcula la suma de los elementos de su `diagonal principal`.

**Ejemplo:**

```python
matriz = [
    [2, 5, 7],
    [4, 3, 9],
    [6, 1, 8]
]
# Diagonal: 2 + 3 + 8 = 13
# Resultado: 13
```

## Ejercicio 46: Reemplazar vocales

Escribe un programa que reciba una cadena y reemplace todas las vocales por el símbolo `*`.

**Ejemplo:**

```python
texto = "Hola mundo"
# Resultado: "H*l* m*nd*"
```

## Ejercicio 47: Promedio de columnas en una matriz

Crea una función que reciba una matriz de números y devuelva una lista con el promedio de cada columna.

**Ejemplo:**

```python
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11]
]
# Promedios por columna: [3.33, 5.33, 7.33]
```

## Ejercicio 48: Reorganizar palabras por longitud

Crea una función que reciba una frase y devuelva una lista con las palabras ordenadas por su longitud, de menor a mayor.
Si dos palabras tienen la misma longitud, mantener el orden original.

**Ejemplo:**

```python
frase = "Python es un lenguaje poderoso y elegante"
# Resultado: ['un', 'es', 'y', 'Python', 'poderoso', 'lenguaje', 'elegante']
```

## Ejercicio 49: Diccionario de índices

Dada una lista, crea un diccionario donde las claves sean los elementos y los valores sean listas con los índices donde aparece cada elemento.

**Ejemplo:**

```python
lista = ['a', 'b', 'a', 'c', 'b', 'a']
# Resultado: {'a': [0, 2, 5], 'b': [1, 4], 'c': [3]}
```

## Ejercicio 50: Reemplazar duplicados con contador

Dada una lista, reemplaza los elementos duplicados agregando un número incremental al final para diferenciarlos.

**Ejemplo:**

```python
lista = ["python", "java", "python", "c", "java"]
# Resultado: ["python", "java", "python_2", "c", "java_2"]
```

## Ejercicio 51: Promedio por categoría

Tienes un diccionario donde las claves son categorías y los valores son listas de números.
Devuelve un nuevo diccionario con el promedio de cada categoría.

**Ejemplo:**

```python
datos = {
    "math": [4, 5, 3],
    "science": [5, 5, 4],
    "english": [3, 4, 4]
}
# Resultado: {'math': 4.0, 'science': 4.67, 'english': 3.67}
```

## Ejercicio 52: Combinar nombres y edades

Tienes dos listas, una de nombres y otra de edades.
Crea un diccionario que relacione cada nombre con su edad, ignorando los sobrantes si las listas tienen longitudes diferentes.

**Ejemplo:**

```python
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25]
# Resultado: {'Ana': 20, 'Luis': 25}
```

## Ejercicio 53: Eliminar valores None de un diccionario

Dado un diccionario con posibles valores `None`, devuelve uno nuevo sin esos pares clave-valor.

**Ejemplo:**

```python
datos = {'nombre': 'Ana', 'edad': None, 'pais': 'Colombia'}
# Resultado: {'nombre': 'Ana', 'pais': 'Colombia'}
```

## Ejercicio 54: Suma en forma de zigzag

Dada una matriz numérica rectangular, suma los elementos en zigzag:
Primera fila izquierda→derecha, segunda fila derecha→izquierda, tercera izquierda→derecha, etc.

**Ejemplo:**

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Zigzag: 1+2+3+6+5+4+7+8+9 = 45
```
