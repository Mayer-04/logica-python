"""
* None
------
`None` es un valor especial en Python que representa la ausencia de un valor o un valor nulo.
Aunque se comporta como un valor "vacío", no es lo mismo que `0`, `False`, o una cadena vacía.

Características:
----------------
- Se usa para indicar que una variable aún no tiene un valor asignado.
- Una función sin una sentencia `return` devuelve `None` por defecto.
- `None` se evalúa como `False` en contextos booleanos.
- Existe una sola instancia de `None` en todo el programa, por lo que se compara con `is`, no con `==`.
- `None` ocupa espacio en memoria, y la variable que apunta a `None` también ocupa espacio en memoria.
"""

# Definir una variable sin valor asignado (valor nulo)
my_var = None

# Imprimir el contenido de la variable
print(my_var)  # Salida: None

# Ver el tipo de dato de la variable
print(type(my_var))  # Salida: <class 'NoneType'>

# Otro ejemplo: uso en condiciones
equipo = None

# Verificar si la variable no tiene un valor asignado
if equipo is None:
    print("No hay equipo")  # Se imprime esto, porque equipo es None
else:
    print("Tienes un equipo")
