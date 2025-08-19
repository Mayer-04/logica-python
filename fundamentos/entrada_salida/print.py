"""
Función Print: Mostrar información en pantalla
-----------------------------------------------
La función `print()` en Python se utiliza para mostrar uno o más valores en la pantalla (o consola).

- `print()` acepta cualquier tipo de dato (texto, números, listas, etc.)
  porque internamente convierte todo a texto usando `str()`.
- No devuelve ningún valor útil: siempre regresa `None`.
  Por eso no se puede guardar su resultado en una variable.

Sintaxis:
---------
print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)

Parámetros principales:
------------------------
- `*objetos`: Los valores que se mostrarán. Pueden ser de cualquier tipo y se pueden pasar varios, 
  separados por comas.
- `sep`: Texto que se coloca entre cada objeto. Por defecto es un espacio `' '`.
- `end`: Texto que se añade al final. Por defecto es un salto de línea `\n`.
- `file`: Destino de la salida. Por defecto es la consola (`sys.stdout`).
- `flush`: Si es `True`, vacía el buffer inmediatamente, mostrando el texto al instante. Por defecto es `False`.

Curiosidad:
-----------
- En Python 2, `print` no era una función, sino una declaración. Se usaba sin paréntesis.
"""

# Ejemplo 1: Imprimir varios valores en la consola
print("Hola", "mundo")  # Salida: Hola mundo

# Ejemplo 2: Imprimir varios valores con un separador personalizado
# Aquí usamos un guion (-) como separador en lugar del espacio por defecto
print("Hola", "Python", sep="-")  # Salida: Hola-Python

# Ejemplo 3: Controlar lo que se imprime al final de la línea
# En lugar de terminar con un salto de línea, se añade una coma y luego se continúa imprimiendo en la misma línea
print("Hola", end=", ")
print("mundo")  # Salida: Hola, mundo (todo en una sola línea)

# Ejemplo 4: Uso de flush para forzar la impresión inmediata
# Esto asegura que el texto se muestre inmediatamente, sin esperar a que se llene un buffer intermedio
print("Ejemplo con flush", flush=True)
