"""
None
-------
`None` es un valor especial en Python que representa la ausencia de un valor o un valor nulo.
Aunque se comporta como un valor "vacío", no es lo mismo que `0`, `False` o una cadena vacía.

Características:
-----------------
- Se usa para indicar que una variable aún no tiene un valor asignado.
- Una función sin una sentencia `return` devuelve `None` por defecto.
- `None` se evalúa como `False` en contextos booleanos.
- Existe una sola instancia de `None` en todo el programa, por lo que se compara con `is`, no con `==`.
- `None` ocupa espacio en memoria, y la variable que apunta a `None` también ocupa espacio en memoria.
- Cualquier operación con `None` lanza TypeError.
"""

# Inicializar una variable sin valor definido
my_var = None
print(my_var)  # Salida: None

# Verificar el tipo de dato
print(type(my_var))  # Salida: <class 'NoneType'>

# Comparación segura con 'is'
if my_var is None:
    print("La variable no tiene valor asignado")

# Incorrecto: comparación con '=='
if my_var == None:  # Funciona, pero no es recomendable
    print("Evita usar '==' con None, usa 'is'")

# Evaluación booleana
if not my_var:
    print("Se evalúa como False en contextos booleanos")


# Una función que no retorna nada explícitamente nos devolvera 'None'
def saludo():
    print("Hola")


resultado = saludo()
print(resultado)  # Salida: None


# Uso como valor por defecto en funciones
def conectar(host=None):
    if host is None:
        host = "localhost"
    print(f"Conectando a {host}")


conectar()  # Salida: Conectando a localhost
conectar("192.167.1.2")  # Salida: Conectando a 192.167.1.2


# Evitar errores en cálculos
def calcular_total(precio, descuento=None):
    if descuento is None:
        descuento = 0
    return precio - descuento


print(calcular_total(100))  # Salida: 100
print(calcular_total(100, 20))  # Salida: 80
