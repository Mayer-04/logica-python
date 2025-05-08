"""
* None

Es un valor especial que representa la ausencia de un valor o un valor nulo, 
pero no es considerado un tipo de dato básico como cadenas, booleanos o enteros.

- Es usado para indicar la `ausencia de un valor` o un `valor nulo`.
- Las variables pueden ser inicializadas con `None` para indicar que no se le ha asignado un valor aún.
- Si una función en Python no tiene una sentencia `return` por defecto devuelve None.
- El objeto `None` ocupa espacio en memoria, y la variable que apunta a None también ocupa espacio.
- None se considera como `False` en el contexto booleano.
- Solo hay una `instancia` de None en toda la ejecución del programa, por lo que se puede comparar usando `is`.
"""

# Definiendo una variable que no contiene un valor - None
my_var = None

# Imprimiendo la variable
print(my_var)  # Imprime None

# Tipo de dato de la variable
print(type(my_var))  # Imprime <class 'NoneType'>

equipo = None

# Comparando la variable 'equipo' con 'None'
if equipo is None:
    print("No hay equipo")  # Imprime: 'No hay equipo'
else:
    print("Tienes un equipo")
