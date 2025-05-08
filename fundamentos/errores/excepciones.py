"""
Manejo Avanzado de Errores y Excepciones en Python
---------------------------------------------------
Una excepción es un error que ocurre durante la ejecución de un programa.
- la palabra `excepción` se refiere a que este problema ocurre con poca frecuencia.
- El manejo de excepciones permite al usuario crear aplicaciones tolerantes a fallas .

Errores y excepciones en Python utilizando las palabras reservadas:
`try`, `except`, `else`, `finally`, `raise`, y otras técnicas avanzadas.

IMPORTANTE:
El error "padre" o que los maneja a todos se llama `Exception`. Todos los errores derivan de esta clase.

Instrucciones clave:
---------------------
- `try`: Intenta ejecutar el código dentro del bloque `try`.
- `except`: Captura y maneja excepciones que ocurren dentro del bloque `try`.
- `else`: Se ejecuta si no ocurre ninguna excepción en el bloque `try`.
- `finally`: Se ejecuta sin importar si se produjo o no una excepción en el bloque `try`.
- `raise`: Lanza una excepción personalizada. Crea un error definido por el usuario.

- `raise from`: Lanza una nueva excepción mientras mantiene la original para facilitar el rastreo.
* Te permite decir: "Hubo este error, y debido a ese error, estoy lanzando este nuevo error".

- `with`: Utiliza el manejo contextual para asegurar que los recursos se liberen correctamente.
* Te aseguras de que el recurso se cierre correctamente, incluso si ocurre un error.

- `assert`: Verifica condiciones que deben ser verdaderas durante la ejecución del programa.
* Verifica que la condición que pones después de assert sea verdadera.
* Si es verdadera, no pasa nada y el programa sigue como de costumbre.
* Si es falsa, el programa se detiene y muestra un mensaje de error.

Tipos comunes de errores y excepciones en Python:
-------------------------------------------------
- `Exception`: Clase base para todas las excepciones.
- `SyntaxError`: Error de sintaxis.
- `NameError`: Uso de un nombre de variable no definido.
- `TypeError`: Uso inapropiado de un tipo de dato.
- `ValueError`: Valor incorrecto para un tipo de dato.
- `IndexError`: Índice fuera del rango permitido para una lista o tupla.
- `IndentationError`: Error en la indentación del código.
- `RuntimeError`: Error que no encaja en ninguna otra categoría.
- `KeyError`: Uso de una clave no existente en un diccionario.
- `FloatingPointError`: Error en la operación de números de punto flotante.
- `ZeroDivisionError`: Intento de dividir por cero.
- `AttributeError`: Intento de acceder a un atributo no definido.
- `ImportError`: Fallo en la importación de un módulo.
- `OSError`: Errores del sistema operativo.
"""

import time

# Ejemplo de error genérico (No recomendado)
try:
    print(10 / 0)
except:
    print("Error: No se puede dividir entre 0")

# Ejemplo básico de manejo de errores generales
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")

# Ejemplo de manejo de errores con `else`
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")
else:
    print(f"Operación exitosa, el resultado es {result}")

# Ejemplo de manejo de errores con `finally`
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")
finally:
    print("Este bloque de código siempre se ejecuta, sin importar si ocurrió un error.")

# Ejemplo de captura de excepción y acceso a la información de error con `as`
# Estos errores pueden ser mejor capturarlos en un `logger` en vez de mostrarlos al usuario
# * NOTE: Para saber el nombre del error que estamos teniendo, podemos usar el `type(e).__name__`
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Error capturado: {e}")
finally:
    print("Finalizando el programa.")

# Ejemplo de cómo manejar múltiples excepciones
try:
    value = int("a")  # Esto causará un ValueError
except (ValueError, TypeError) as e:
    print(f"Error capturado: {e}")

# Ejemplo de manejo de excepciones encadenadas con `raise from`
try:
    result = 10 / 2
except ZeroDivisionError as e:
    raise ValueError("Nuevo error basado en un ZeroDivisionError") from e


# Ejemplo de uso de `assert` para validar condiciones
def suma(a, b):
    assert isinstance(a, int), "a debe ser un entero"
    assert isinstance(b, int), "b debe ser un entero"
    return a + b


try:
    suma(10, "20")
except AssertionError as e:
    print(f"Error de validación: {e}")

# Ejemplo de uso de `with` para manejo de recursos
try:
    with open("archivo.txt", "r") as file:
        contenido = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")


# Definir una excepción personalizada
class EdadFueraDeRangoError(Exception):
    """Excepción lanzada cuando la edad no está en el rango permitido."""

    def __init__(self, edad, mensaje="La edad debe estar entre 18 y 100 años."):
        super().__init__(f"{mensaje} Edad ingresada: {edad}")
        self.edad = edad
        self.mensaje = mensaje


# Función que utiliza la excepción personalizada
def verificar_edad(edad):
    # return "Edad válida" if 18 < edad <= 100 else EdadFueraDeRangoError(edad)
    if edad < 18 or edad > 100:
        raise EdadFueraDeRangoError(edad)
    return "Edad válida"


# Probar la función
try:
    resultado = verificar_edad(120)
    print(resultado)
except EdadFueraDeRangoError as e:
    print(e)


# Ejemplo de reintentos automáticos en caso de error
def retry_function(function, max_retries=3):
    """
    Ejecuta una función dada un número determinado de veces (max_retries)
    en caso de que esta lance una excepción. Si la función falla todas
    las veces, se lanza una excepción RuntimeError con un mensaje descriptivo.

    Raises
    ------
    RuntimeError
        Si la función falla todas las veces.
    """

    for _ in range(max_retries):
        try:
            return function()
        except Exception:
            time.sleep(1)
    raise RuntimeError(
        f"No se pudo ejecutar {function.__name__} después de {max_retries} reintentos"
    )


def funcion_fallida():
    """
    Función que falla al intentar dividir entre cero.
    """
    return 10 / 0


try:
    retry_function(funcion_fallida)
except Exception as e:
    print(e)
