"""
* Asincronía en Python
----------------------
Introducida en Python 3.5.
La asincronía permite ejecutar código de forma más eficiente cuando se trabaja con operaciones que podrían bloquear
el flujo del programa, como la entrada/salida (I/O). Esto se logra utilizando las palabras clave `async` y `await`.

- La palabra clave `async` se utiliza para definir una función asíncrona, también llamada `coroutine`.
- La palabra clave `await` se utiliza para pausar la ejecución de la coroutine hasta que otra coroutine o tarea asíncrona se complete.
- Solo se puede usar `await` dentro de funciones declaradas con `async def`, de lo contrario, producirá un error.
- Antes de la introducción de la asincronía nativa con `async`/`await`, se solían usar `threads` o librerías como `Gevent`, 
pero estas soluciones pueden ser más complicadas de implementar y depurar.

¿Qué es una coroutine?
----------------------
Una coroutine es una función especial en Python que puede ser pausada en un punto determinado 
(por ejemplo, mientras espera una operación de I/O) y luego reanudada más tarde. 
Esto permite que otras tareas continúen ejecutándose sin bloquear el programa.

- Usar coroutines es una forma de concurrencia: Múltiples tareas pueden ejecutarse de manera intercalada, 
pero no simultáneamente en múltiples núcleos de CPU (que sería paralelismo).
- Una coroutine puede contener las palabras clave `await`, `async for` y `async with` 
para manejar asincronía y otros patrones de control.

Diferencia entre concurrencia y paralelismo:
--------------------------------------------
- La concurrencia permite cambiar entre tareas mientras algunas están esperando (como en una coroutine).
- El paralelismo implica ejecutar múltiples tareas al mismo tiempo en diferentes núcleos de CPU, se realiza con threads o procesos.
"""

import asyncio


async def print_hello():
    """Imprime un mensaje de bienvenida."""
    print(
        "Hola...", end=""
    )  #  No añade ningún carácter al final del texto. Por defecto print() agrega un "\n".
    await asyncio.sleep(0.1)  # Simula una operación de espera asíncrona
    print("¡Bienvenido!")


# `run()` Ejecute la corrutina y devuelva el resultado.
asyncio.run(print_hello())


# async for se utiliza para iterar sobre un objeto asincrónico
async def print_numbers():
    """
    Imprime los números del 0 al 2 con un intervalo de 1 segundo entre cada número.
    """
    for number in range(3):
        # Imprime el número actual
        print(number)

        # Pausa la ejecución de la corrutina por 1 segundo para simular una operación asíncrona
        await asyncio.sleep(1)


asyncio.run(print_numbers())
