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
1. Declaración de funciones
2. Docstrings
3. Parámetros y argumentos
4. Retorno de múltiples valores
5. Valores por defecto en parámetros
6. Funciones anónimas (lambdas)
7. Funciones como objetos de primera clase (closures)
8. Desempaquetado de argumentos (`*args`, `**kwargs`)
9. Anotaciones de tipo (type hints)
10. Recursividad
11. Argumentos por nombre y argumentos arbitrarios
12. Uso de la sentencia `pass`
13. Callbacks (pasar funciones como parámetros)
14. Decoradores
15. Genéricos en funciones
"""

from typing import Any, Callable, Tuple

# --------------------------------------
# * Declaración básica de funciones
# --------------------------------------


# Una función se define usando la palabra clave `def`, seguida del nombre de la función y paréntesis.
def saludar():
    print("¡Hola, mundo!")


# Llamada a la función `saludar` sin argumentos.
saludar()

# --------------------------------------
# * Docstrings en Python
# --------------------------------------
# Un docstring es una cadena de texto que documenta el propósito y uso
# de una función, clase o módulo. Se utiliza para que otros desarrolladores
# (o tú mismo en el futuro) puedan entender rápidamente el código.

def sumar(a: int, b: int) -> int:
    """
    Calcula la suma de dos números enteros.

    Parámetros:
        a (int): Primer número a sumar.
        b (int): Segundo número a sumar.

    Retorna:
        int: Resultado de sumar a y b.
    
    Ejemplo:
        >>> sumar(3, 5)
        8
    """
    return a + b

# Mostrar la documentación de la función en consola
print(sumar.__doc__)


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


# ----------------------------------------------
# * Valores por defecto y anotaciones de tipo
# ----------------------------------------------


# Puedes definir valores por defecto para los parámetros.
# Si no se proporciona un argumento, se usará el valor por defecto.
def saludar_con_titulo(nombre: str, titulo: str = "Sr./Sra.") -> None:
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
def calcular_area_rectangulo(base: int, altura: int):
    """Calcula el área de un rectángulo."""
    return base * altura


# Llamada a la función `calcular_area_rectangulo` con múltiples argumentos.
# El orden de los argumentos SI importa.
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")


# --------------------------------------
# * Retorno de múltiples valores
# --------------------------------------


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
    # float("inf") se usa para representar infinito cuando la división es entre cero
    division = num1 / num2 if num2 != 0 else float("inf")

    return suma, resta, multiplicacion, division


# Llamando a la función `operaciones` y desempaquetando los valores retornados.
suma, resta, multiplicacion, division = operaciones(10, 0)
print(
    f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}"
)


# Ejemplos 2: Retorno de múltiples valores
def prueba() -> tuple[str, int, list[int]]:
    """Retorna una cadena, un entero y una lista.

    Retorno:
        tuple: (str, int, list)
    """
    return "Andres CMS", 20, [1, 2, 3]


# Llamando a la función `prueba`
resultado = prueba()
print(resultado)  # Salida: ('Andres CMS', 20, [1, 2, 3])


# --------------------------------------
# * Funciones lambda
# --------------------------------------

# Definiendo una función `lambda` para sumar dos números
# Los parámetros de la función lambda son `num1` y `num2`
# El valor de retorno de la función lambda es la suma de `num1` y `num2`
sumar_lambda = lambda num1, num2: num1 + num2

# Usando la función lambda
result_lambda = sumar_lambda(1, 2)
print("Resultado Lambda:", result_lambda)

# Usando una función lambda en una función `map()`
numeros = [1, 2, 3, 4, 5]
result_map = list(map(lambda num: num * 2, numeros))
print("Resultado Map:", result_map)  # Salida: [2, 4, 6, 8, 10]

# Usando una función lambda en una función `filter()`
result_filter = list(filter(lambda num: num % 2 == 0, numeros))
print("Resultado Filter:", result_filter)  # Salida: [2, 4]


# Retornando una función `lambda` desde una función tradicional
def crear_suma(value: int) -> Callable[[int, int], int]:
    """Devuelve una función lambda que suma 'value' a la suma de otros dos números."""
    return lambda num1, num2: num1 + num2 + value


# Imprimiendo el resultado de la función tradicional con la función lambda.
print("Funcion tradicional con lambda:", crear_suma(5)(1, 2))  # Salida: 8


# --------------------------------------
# * Funciones anidadas: Closures
# --------------------------------------


# Una función anidada es una función definida dentro de otra función.
def funcion_externa(x: int):
    """Contiene una función interna que utiliza la variable `x` de la función externa.

    Parámetros:
    x (int): Un número utilizado en la función interna.

    Retorno:
    function: Una función interna que suma `x` a su argumento `y`.
    """

    def funcion_interna(y: int):
        """Suma `x` y `y`, donde `x` proviene de la función externa."""
        return x + y

    # Devuelve la referencia a la función interna, formando un closure.
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
def calcular_factorial(numero: int) -> int:
    """
    Calcula el factorial de un número entero positivo.

    Parámetros:
        numero (int): El número para calcular el factorial.

    Retorno:
        int: El factorial del número dado.
    """
    if numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)


# Calculando el factorial de 5.
print(calcular_factorial(5))  # Salida: 120

# --------------------------------------
# * Argumentos por nombre (keywords)
# --------------------------------------


# En Python, podemos llamar a las funciones especificando el nombre
# de cada argumento. Esto nos permite cambiar el orden en que los
# escribimos al llamar a la función, siempre que los nombremos
def describir_persona(nombre: str, edad: int):
    """Imprime la descripción de una persona con su nombre y edad.

    Parámetros:
    nombre (str): El nombre de la persona.
    edad (int): La edad de la persona.
    """
    print(f"Nombre: {nombre}, Edad: {edad}")


# Ejemplo: llamando a la función con los argumentos fuera de orden
describir_persona(edad=30, nombre="Maria")

# --------------------------------------------------------
# * Argumentos arbitrarios (arbitrary arguments): *args
# --------------------------------------------------------


# Si no sabemos cuántos argumentos recibirá nuestra función, podemos usar *args
# Python guardará todos esos valores en una `tupla`
def saludar_varios(*args: str):
    """
    Saluda a todas las personas cuyos nombres se pasan como argumentos.

    Parámetros:
    *args (tuple): Nombres de las personas a saludar.
    """
    for name in args:
        print(f"Hola {name}")


# Llamando a la función `saludar_varios` con múltiples nombres
saludar_varios("Mayer", "Andrés", "Luis")

# -------------------------------------------------------
# * Argumentos con nombre arbitrarios: **kwargs
# -------------------------------------------------------


# Si no sabemos cuántos argumentos con nombre recibirá la función, usamos **kwargs
# Python los guardará como un diccionario donde:
# - La clave es el nombre del argumento
# - El valor es el dato que se le pasó
def indeterminados_nombre(**kwargs: Any):
    """
    Imprime todos los argumentos recibidos como pares clave-valor.

    Parámetros:
    **kwargs (dict): Argumentos con nombre y su respectivo valor.
    """
    print(kwargs)


# Llamando a la función `indeterminados_nombre` con varios argumentos por nombre
# Pasamos un número, un texto y una lista
indeterminados_nombre(n=5, c="Hola Andres", l=[1, 2, 3, 4, 5])

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


# Callbacks: Funciones que se pasan como argumentos a otras funciones
def ejecutar_callback(callback: Callable[[int], int], value: int) -> int:
    """Ejecuta una función de callback pasada como argumento.

    Parámetros:
    callback (Callable[[int], int]): La función a ejecutar. Debe tomar un solo argumento de tipo int.
    value (int): El valor a pasar como argumento a la función `callback`.

    Retorno:
    int: El resultado de ejecutar la función callback con el valor proporcionado.
    """
    return callback(value)


# Definimos una función sencilla para utilizar callback
def doblar_valor(x: int) -> int:
    """Duplica el valor del parámetro."""
    return x * 2


# Usamos la función `ejecutar_callback` pasando el callback `doblar`
resultado_callback = ejecutar_callback(doblar_valor, 10)
print(f"Resultado del callback: {resultado_callback}")


# --------------------------------------
# * Decoradores
# --------------------------------------
# Un decorador es una función que toma otra función como argumento y extiende o modifica su comportamiento


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

# ----------------------------------------
# * Genéricos en funciones (Python 3.12+)
# ----------------------------------------
# Desde Python 3.12, es posible definir tipos genéricos directamente en funciones y clases
# sin necesidad de importar TypeVar o Generic desde el módulo typing (from typing import TypeVar, Generic)
# Esto mejora la legibilidad y reduce la complejidad al tipar datos

def obtener_ultimo[T](coleccion: list[T]) -> T:
    """
    Devuelve el último elemento de una lista de cualquier tipo.

    Parámetros:
        coleccion (list[T]): Lista de elementos del mismo tipo T.

    Retorna:
        T: Último elemento de la lista.

    Ejemplo:
        >>> obtener_ultimo([1, 2, 3])
        3
        >>> obtener_ultimo(["rojo", "verde", "azul"])
        'azul'
    """
    return coleccion[-1]


def crear_diccionario[K, V](clave: K, valor: V) -> dict[K, V]:
    """
    Crea un diccionario de un solo par clave-valor con tipos genéricos.

    Parámetros:
        clave (K): Cualquier tipo válido para clave.
        valor (V): Cualquier tipo válido para valor.

    Retorna:
        dict[K, V]: Diccionario con la clave y valor dados.

    Ejemplo:
        >>> crear_diccionario("edad", 30)
        {'edad': 30}
        >>> crear_diccionario(101, ["A", "B", "C"])
        {101: ['A', 'B', 'C']}
    """
    return {clave: valor}


# Ejemplos de uso
print(obtener_ultimo([5, 10, 15]))           # Salida: 15
print(obtener_ultimo(["perro", "gato"]))     # Salida: 'gato'
print(crear_diccionario("activo", True))     # Salida: {'activo': True}
print(crear_diccionario(1, {"x": 100}))      # Salida: {1: {'x': 100}}
