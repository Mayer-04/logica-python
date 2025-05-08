"""
Función Print: Mostrar en pantalla
-----------------------------------
La función `print()` en Python se utiliza para mostrar uno o más valores en la pantalla (o consola).
- `print()` puede mostrar cualquier tipo de objeto, ya que internamente convierte todo lo que recibe a texto mediante `str()`.
- `print()` no devuelve ningún valor; su propósito es únicamente mostrar información. 
Siempre regresa `None`, por lo que no se puede almacenar su resultado.

Sintaxis:
print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)

Parámetros:
- `objetos`: Los valores que se mostrarán en la pantalla. Pueden ser de cualquier tipo.
- `sep`: Especifica el separador que se colocará entre los objetos. El valor por defecto es un espacio (' ').
- `end`: Especifica qué se añadirá al final de la línea. Por defecto, es un salto de línea (`\n`).
- `file`: Define el destino de la salida. Por defecto, `print()` muestra la salida en la consola (pantalla), 
que está representada por `sys.stdout`.
- `flush`: Indica si se debe "vaciar" el contenido inmediatamente, sin almacenarlo en un buffer. 
Su valor por defecto es `False`.

Curiosidad:
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
