import random

"""
Librería Random
----------------
La librería estándar `random` de Python se usa para generar números aleatorios o elementos al azar.

- `random.randint(a, b)`: Retorna un número entero aleatorio entre `a` y `b` (ambos incluidos).
- `random.random()`: Genera un número aleatorio de tipo decimal (float) entre 0 y 1 (0 incluido, 1 excluido).
- `random.choice(seq)`: Selecciona y retorna un elemento aleatorio de una secuencia (como una lista o tupla).
- `random.choices(seq, k=n)`: Retorna una lista con `n` elementos aleatorios de una secuencia. 
Los elementos pueden repetirse.
- `random.shuffle(seq)`: Mezcla o desordena los elementos de una lista. Modifica la lista original.
"""

# Generar un número entero aleatorio entre dos valores
print(random.randint(1, 10))  # Output: 6

# Generar un número decimal aleatorio entre 0 y 1
# El número generado será de tipo float.
print(random.random())  # Output: 0.5078513921608502

# Elegir un elemento al azar de una lista
print(random.choice([1, 2, 3, 4, 5]))  # Output: 4

# Seleccionar varios elementos aleatorios de una lista
# Se seleccionan 3 elementos de manera aleatoria y los valores pueden repetirse.
print(random.choices([1, 2, 3, 4, 5], k=3))  # Output: [4, 3, 2]

# Seleccionar varios elementos aleatorios de una tupla
# Funciona igual que con las listas. Se seleccionan 3 elementos aleatorios.
print(random.choices((1, 2, 3, 4, 5), k=3))  # Output: [5, 3, 5]

# Barajar una lista de elementos
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)  # Desordena la lista original.
print("Lista desordenada:", shuffle_list)  # Lista desordenada: [2, 5, 1, 3, 4]
