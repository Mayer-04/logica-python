import random

"""
Módulo random en Python
-------------------------
El módulo `random` permite generar valores al azar. Es útil para juegos, simulaciones, sorteos, y más.

Funciones principales:
-----------------------
- random.randint(a, b) -> int: Devuelve un número entero aleatorio entre `a` y `b`, incluyendo ambos.

- random.random() -> float: Devuelve un número decimal (float) entre 0 (incluido) y 1 (excluido).

- random.choice(secuencia): Elige un solo elemento aleatorio de una lista, tupla o cadena.

- random.choices(secuencia, k=n): Devuelve una lista con `n` elementos aleatorios. Puede haber repetidos.

- random.shuffle(lista) -> None: Mezcla los elementos de una lista. Cambia el orden original.

- random.sample(secuencia, k): Devuelve `k` elementos únicos al azar. No hay repeticiones.
"""

# Número entero aleatorio entre 1 y 10
numero_entero = random.randint(1, 10)
print("Número entero entre 1 y 10:", numero_entero)

# Número decimal aleatorio entre 0 y 1
numero_decimal = random.random()
print("Número decimal entre 0 y 1:", numero_decimal)  # Salida: 0.5844065190781639

# Elegir un elemento al azar de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
color_elegido = random.choice(colores)
print("Color elegido al azar:", color_elegido)

# Seleccionar varios elementos aleatorios (pueden repetirse)
frutas = ["manzana", "limon", "banano", "naranja"]
frutas_aleatorias = random.choices(frutas, k=3)
print("Frutas seleccionadas (pueden repetirse):", frutas_aleatorias)

# Mezclar una lista (desordenarla)
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)  # Cambia el orden original
print("Lista desordenada:", numeros)

# Seleccionar varios elementos únicos (sin repetir)
# Ideal para sorteos o selección sin duplicados
participantes = ["Mayer", "Luis", "Andres", "Lucas", "Kelly"]
ganadores = random.sample(participantes, k=3)
print("Ganadores del sorteo:", ganadores)

# Generar una lista de 5 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(5)]
print("Lista de 5 números aleatorios:", numeros_aleatorios)
