# =====================================
# * Función incorporada slice()
# =====================================
# La función slice() crea un objeto especial que representa
# un rango de índices, que luego puedes usar para cortar listas,
# cadenas u otras secuencias.
#
# Forma general:
# slice(inicio, fin, paso)
#
# Equivale a usar la notación de corchetes [inicio:fin:paso],
# pero permite guardarlo en una variable y reutilizarlo.

# Ejemplo básico: crear un objeto slice
mi_slice = slice(1, 5, 2)  # Desde índice 1, hasta antes del 5, avanzando de 2 en 2
print(mi_slice)  # Salida: slice(1, 5, 2)

# Ejemplo 1: Usar slice() para extraer una parte de una lista
numeros = [1, 2, 3, 4, 5]
# Esto obtiene los elementos en índices 1 y 3 (recordemos que el índice inicia en 0)
resultado = numeros[slice(1, 5, 2)]
print(resultado)  # Salida: [2, 4]

# Es equivalente a usar la notación con dos puntos:
# numeros[1:5:2]  # también daría [2, 4]

# Ejemplo 2: Guardar un slice y reutilizarlo
corte = slice(1, 4)  # Desde índice 1 hasta antes del 4
print(numeros[corte])  # Salida: [2, 3, 4]

# Ejemplo 3: Usar slice() para invertir una lista
invertir = slice(None, None, -1)
print(numeros[invertir])  # Salida: [5, 4, 3, 2, 1]

# También se puede hacer directamente con notación de corte:
# numeros[::-1]  # [5, 4, 3, 2, 1]
