"""
* Asincronía en Python
----------------------
Introducida en Python 3.5.
La asincronía permite ejecutar código de forma más eficiente cuando se trabaja con operaciones que podrían bloquear
el flujo del programa, como la entrada/salida (I/O). Esto se logra utilizando las palabras clave `async` y `await`.

- La palabra clave `async` se utiliza para definir una función asíncrona, también llamada `coroutine`.
- La palabra clave `await` se utiliza para pausar la ejecución de la coroutine hasta que otra coroutine o tarea
  asíncrona se complete.
- Solo se puede usar `await` dentro de funciones declaradas con `async def`, de lo contrario, producirá un error.
- Antes de la introducción de la asincronía nativa con `async`/`await`, se solían usar `threads` o librerías
  como `Gevent`, pero estas soluciones pueden ser más complicadas de implementar y depurar.

Conceptos clave:
----------------
- `async` → define una `corrutina` (función asíncrona).
- `await` → pausa la corrutina hasta que otra corrutina/tarea finalice.
- `async for` → iteración sobre objetos asíncronos.
- `async with` → manejo de recursos asíncronos.
- `asyncio.gather` → ejecutar varias tareas en paralelo (concurrencia).

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
- El paralelismo implica ejecutar múltiples tareas al mismo tiempo en diferentes núcleos de CPU,
  se realiza con threads o procesos.

Novedades Python 3.11+:
-----------------------
- `asyncio.TaskGroup` más eficiente y recomendado para agrupación estructurada de tareas.
- Mejoras en depuración: trazas más claras al cancelar o cerrar tareas.
"""

import asyncio
from contextlib import asynccontextmanager


# Ejemplo 1: Saludo asíncrono básico
async def print_hello() -> None:
    """Imprime un saludo con una breve pausa."""
    print("Hola...", end="", flush=True)
    await asyncio.sleep(0.1)
    print("¡Bienvenido!")


# Ejemplo 2: Iteración asíncrona
async def print_numbers():
    """Imprime números con pausas entre ellos."""
    for number in range(3):
        print(number)
        await asyncio.sleep(1)


# Ejemplo 3: Uso de 'async with' para manejar recursos asíncronos
@asynccontextmanager
async def async_resource(name: str):
    """
    La función devuelve un objeto que se puede usar con la sentencia `async with`.
    El objeto se comporta como un contexto manager que, al entrar en el bloque `async with`,
    conecta el recurso y, al salir de él, lo cierra.
    """
    print(f"Conectando recurso {name}...")
    await asyncio.sleep(0.5)
    try:
        yield f"Recurso {name} listo"
    finally:
        print(f"Cerrando recurso {name}...")
        await asyncio.sleep(0.5)


async def use_resource():
    async with async_resource("Base de Datos") as resource:
        print(f"Consultando datos... (simulando {resource})")
        await asyncio.sleep(1)


# Ejemplo 4: Ejecutar varias tareas al mismo tiempo
async def task(name: str, delay: float):
    print(f"Tarea {name} iniciada...")
    await asyncio.sleep(delay)
    print(f"Tarea {name} finalizada.")


async def run_concurrent_tasks():
    """Ejecuta varias tareas simultáneamente utilizando asyncio.gather."""
    # await asyncio.gather(task("A", 1), task("B", 2), task("C", 1.5))
    tasks = [task("Task A", 1), task("Task B", 2), task("Task C", 1.5)]
    # *task es equivalente a task("Task A", 1), task("Task B", 2), task("Task C", 1.5)
    await asyncio.gather(*tasks)


# Ejemplo 5: Uso de TaskGroup (Python 3.11+)
async def run_with_taskgroup():
    """Ejecuta varias tareas al mismo tiempo utilizando TaskGroup."""
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task("X", 1))
        tg.create_task(task("Y", 0.5))


async def main():
    await print_hello()
    await print_numbers()
    await use_resource()
    await run_concurrent_tasks()
    await run_with_taskgroup()


# Ejecuta la 'courotine main' y devuelve los resultados
asyncio.run(main())
