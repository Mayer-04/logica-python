"""
* Funciones en Python
----------------------
Una función es un bloque de código reutilizable que realiza una tarea específica.
Permite dividir el programa en partes más manejables, promoviendo la reutilización y mejorando la legibilidad.

Características clave:
-----------------------
- La sentencia `return` permite devolver un valor desde una función.
- Si `return` se usa sin valor o no se incluye en absoluto, la función devuelve `None` por defecto.
- La sentencia `pass` indica que el bloque no hace nada; puede usarse como marcador de posición.
- Las variables definidas dentro de una función tienen un `scope local`, es decir, solo existen dentro de ella.
- A mayor número de dependencias externas, más difícil será mantener y testear la función en el futuro.

Recomendaciones:
----------------
- Utiliza `anotaciones de tipo` (type hints) aunque sean opcionales.
  Principalmente para indicar tipos de parámetros y valores de retorno.
- Documenta tus funciones usando docstrings si esperas que otras personas (o tú en el futuro) usen ese código.

En este archivo se exploran los siguientes conceptos fundamentales:
-------------------------------------------------------------------
- Declaración de funciones
- Parámetros y argumentos
- Retorno de múltiples valores
- Valores por defecto en parámetros
- Funciones anónimas (lambdas)
- Funciones como objetos de primera clase (closures)
- Desempaquetado de argumentos (`*args`, `**kwargs`)
- Anotaciones de tipo (type hints)
- Recursividad
- Argumentos por nombre y argumentos arbitrarios
- Uso de la sentencia `pass`
- Callbacks (pasar funciones como parámetros)
- Decoradores
"""

from typing import Callable

# --------------------------------------
# * Declaración básica de funciones
# --------------------------------------


# Una función se define usando la palabra clave `def`, seguida del nombre de la función y paréntesis.
def saludar():
    print("¡Hola, mundo!")


# Llamada a la función `saludar` sin argumentos.
saludar()


# --------------------------------------
# * Parámetros y argumentos
# --------------------------------------


# Las funciones pueden recibir datos a través de parámetros,
# que se pasan como argumentos cuando se llama a la función.
def saludar_a(nombre):
    """Imprime un saludo personalizado utilizando el nombre proporcionado como argumento."""
    print(f"¡Hola, {nombre}!")


# Llamada a la función `saludar_a` pasando un argumento.
saludar_a("Mayer")


# --------------------------------------
# * Valores por defecto
# --------------------------------------


# Puedes definir valores por defecto para los parámetros.
# Si no se proporciona un argumento, se usará el valor por defecto.
def saludar_con_titulo(nombre: str, titulo: str = "Sr./Sra."):
    """Imprime un saludo personalizado utilizando un título y nombre.

    Parámetros:
    nombre (str): El nombre de la persona a saludar.
    titulo (str, opcional): El título a utilizar. Por defecto es 'Sr./Sra.'.
    """
    print(f"¡Hola, {titulo} {nombre}!")


# Usando el valor por defecto para `titulo`.
saludar_con_titulo("Mayer")  # Salida: ¡Hola, Sr./Sra. Mayer!

# Sobrescribiendo el valor por defecto para `titulo`.
saludar_con_titulo("Mayer", "Dr.")  # Salida: ¡Hola, Dr. Mayer!


# --------------------------------------
# * Múltiples parámetros
# --------------------------------------


# Las funciones pueden tener múltiples parámetros para manejar más datos.
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura


# Llamada a la función `calcular_area_rectangulo` con múltiples argumentos.
# El orden de los argumentos SI importa.
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")


# --------------------------------------
# * Retorno de múltiples valores
# --------------------------------------

from typing import Tuple


# Python permite retornar múltiples valores desde una función, separados por comas.
# Los valores retornados se `empaquetan` automáticamente en una `tupla`.
def operaciones(num1: int, num2: int) -> Tuple[int, int, int, float]:
    """Realiza operaciones básicas entre dos números.

    Retorno:
        tuple: suma, resta, multiplicación, división
    """
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division


# Llamando a la función `operaciones` y desempaquetando los valores retornados.
suma, resta, multiplicacion, division = operaciones(10, 5)
print(
    f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}"
)


# Retorno de múltiples valores 2
def prueba():
    """Retorna una cadena, un entero y una lista.

    Retorno:
        tuple: (str, int, list)
    """
    return "Andres CMS", 20, [1, 2, 3]


# Llamando a la función `prueba`
resultado = prueba()
print(resultado)  # Imprime: ('Andres CMS', 20, [1, 2, 3])

"""
* Funciones lambda
    - Una función lambda es una función anónima, es decir, que no tiene nombre.
    - Se crean con la palabra reservada `lambda`.
    - Son útiles cuando se necesita una función simple y rápida.
    - Es una característica tomada de la `programación funcional`.
    - Se pueden almacenar en variables o pasar como argumentos a otras funciones.
    - Se suelen usar en combinaciones con funciones como `map()`, `filter()` y `reduce()`.
    - Tiene un retorno implícito.
    
    Sintaxis:
    lambda parámetros: expresión
"""

# Definiendo una función `lambda` para sumar dos números.
# Los parámetros de la función lambda son `num1` y `num2`.
# El valor de retorno de la función lambda es la suma de `num1` y `num2`.
sumar_lambda = lambda num1, num2: num1 + num2

# Usando la función lambda.
result_lambda = sumar_lambda(1, 2)
print("Resultado Lambda:", result_lambda)

# Usando una función lambda en una función `map()`.
numeros = [1, 2, 3, 4, 5]
result_map = list(map(lambda num: num * 2, numeros))
print("Resultado Map:", result_map)  # [2, 4, 6, 8, 10]

# Usando una función lambda en una función `filter()`.
result_filter = list(filter(lambda num: num % 2 == 0, numeros))
print("Resultado Filter:", result_filter)  # [2, 4]


# Retornando una función `lambda` desde una función tradicional
def suma(value: int) -> Callable[[int, int], int]:
    """Devuelve una función lambda que suma 'value' a la suma de otros dos números."""
    return lambda num1, num2: num1 + num2 + value


# Imprimiendo el resultado de la función tradicional con la función lambda.
print("Funcion tradicional con lambda:", suma(5)(1, 2))  # 8


# --------------------------------------
# * Funciones anidadas: Closures
# --------------------------------------


# Una función anidada es una función definida dentro de otra función.
def funcion_externa(x):
    """Contiene una función interna que utiliza la variable `x` de la función externa.

    Parámetros:
    x (int): Un número utilizado en la función interna.

    Retorno:
    function: Una función interna que suma `x` a su argumento `y`.
    """

    def funcion_interna(y):
        """Suma `x` y `y`, donde `x` proviene de la función externa."""
        return x + y

    # Retorna la función interna, formando un closure.
    return funcion_interna


# Usando la función anidada.
suma_10 = funcion_externa(10)
resultado = suma_10(5)  # Llama a `funcion_interna(5)`, donde `x` es 10.
print(f"El resultado de la función anidada es: {resultado}")  # Salida: 15


# --------------------------------------
# * Función Recursiva
# --------------------------------------


# Una función recursiva es aquella que se llama a sí misma.
# Necesita una condición de parada o salida porque se volvera a llamar a si misma de manera infinita.
def calcular_factorial(number: int) -> int:
    """
    Calcula el factorial de un número entero positivo.

    Parámetros:
        number (int): El número para calcular el factorial.

    Retorno:
        int: El factorial del número dado.
    """
    if number == 1:
        return 1
    else:
        return number * calcular_factorial(number - 1)


# Calculando el factorial de 5.
print(calcular_factorial(5))  # Salida: 120

# --------------------------------------
# * Argumentos por nombre (keywords)
# --------------------------------------


# Python permite llamar a las funciones especificando los argumentos por nombre,
# lo cual permite ignorar el orden de los parámetros.
def describir_persona(nombre, edad):
    """Imprime la descripción de una persona con su nombre y edad.

    Parámetros:
    nombre (str): El nombre de la persona.
    edad (int): La edad de la persona.
    """
    print(f"Nombre: {nombre}, Edad: {edad}")


# Llamando a la función `describir_persona` con argumentos por nombre.
describir_persona(edad=30, nombre="Maria")


# --------------------------------------
# * Argumentos arbitrarios: **kwargs
# --------------------------------------


# Python permite recibir un número indeterminado de parámetros usando `**kwargs`.
# Crea un `diccionario` con los argumentos pasados por nombre.
def indeterminados_nombre(**kwargs):
    """Imprime los argumentos recibidos como pares clave-valor.

    Parámetros:
    **kwargs: Argumentos clave-valor arbitrarios.
    """
    print(kwargs)


# Llamando a la función `indeterminados_nombre` con varios argumentos por nombre.
indeterminados_nombre(n=5, c="Hola Andres", l=[1, 2, 3, 4, 5])

# --------------------------------------
# * Argumentos arbitrarios: *args
# --------------------------------------


# De forma similar, se puede recibir un número indeterminado de argumentos posicionales con `*args`.
# Los datos recibidos se pasan como una `tupla`.
def saludar_varios(*args):
    """Saluda a todas las personas cuyos nombres se pasan como argumentos.

    Parámetros:
    *args: Nombres de las personas a saludar.
    """
    for name in args:
        print(f"Hola {name}")


# Llamando a la función `saludar_varios` con múltiples nombres.
saludar_varios("Mayer", "Andrés", "Luis")


# --------------------------------------
# * Sentencia pass
# --------------------------------------


# La sentencia `pass` en Python no hace nada. Se usa como un marcador de posición en el código.
def pass_func():
    pass  # No hace nada


# Llamando a la función `pass_func` que no realiza ninguna acción.
pass_func()


# --------------------------------------
# * Callbacks
# --------------------------------------


# Callbacks: Funciones que se pasan como argumentos a otras funciones.
def ejecutar_callback(func: Callable[[int], int], valor: int) -> int:
    """Ejecuta una función (callback) pasada como argumento.

    Parámetros:
    func (callable): La función a ejecutar. Debe ser una función que tome un solo argumento de tipo int.
    valor (int): El valor a pasar como argumento a la función `func`.

    Retorno:
    int:
    """
    return func(valor)


# Definimos una función sencilla para utilizar callback
def doblar(x):
    return x * 2


# Usamos la función `ejecutar_callback` pasando el callback `doblar`.
resultado_callback = ejecutar_callback(doblar, 10)
print(f"Resultado del callback: {resultado_callback}")


# --------------------------------------
# * Decoradores
# --------------------------------------

# Un decorador es una función que toma otra función como argumento y extiende o modifica su comportamiento.


def decorador_saludo(func: Callable[..., None]) -> Callable[..., None]:
    """Un decorador que agrega un mensaje antes y después de la ejecución de una función.

    Parámetros:
    func (callable): La función a decorar. Debe ser una función que tome argumentos arbitrarios.

    Retorno:
    callable: Un decorador que envuelve la función original y agrega el comportamiento adicional.
    """

    def envoltura(*args, **kwargs):
        """Función envoltura que añade comportamiento antes y después de la función original."""
        print("Antes del saludo...")
        resultado = func(*args, **kwargs)
        print("Después del saludo.")
        return resultado

    return envoltura


@decorador_saludo
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")


saludar_usuario("Andrés")
