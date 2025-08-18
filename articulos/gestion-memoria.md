# Gestión de la memoria en Python

La gestión de memoria en Python está diseñada para ser automática y eficiente. El `intérprete de Python` se encarga de la asignación y liberación de memoria a través de su propio `administrador de memoria`, lo que significa que los desarrolladores no tienen que preocuparse directamente por la administración de recursos de memoria.

Todos los objetos y estructuras de datos en Python se almacenan en un área especial de memoria llamada `montón privado`.

## Montón (Heap)

El **montón** es una zona de la `memoria` de la computadora donde se guardan datos que no tienen un tamaño fijo o que se crean **dinámicamente** durante la ejecución de un programa.

- Es más flexible porque permite que se asigne y libere memoria según sea necesario mientras el programa está en funcionamiento.
- Cuando creas un objeto o una estructura de datos como una **lista** o un **diccionario** en Python, estos no tienen un tamaño fijo (pueden crecer o reducirse), por lo que se almacenan en el montón.
- El montón es más lento que la `pila`.

### Montón privado

El **montón privado** de Python es una porción específica (reservada) de la memoria que solo el `intérprete de Python` puede gestionar.

Cuando trabajas con objetos en Python **(como listas, diccionarios, cadenas, etc.)**, estos se almacenan en ese **montón privado**. Este montón es "privado" en el sentido de que, como desarrollador, no puedes controlarlo directamente (acceder ni modificar esta área).

Esto significa que, aunque estés creando y usando objetos en tu código Python, el sistema interno del lenguaje es el que decide cómo y dónde se almacenan esos datos en el **montón privado**.

## Gestión dinámica de memoria en Python

1. **Reutilización de memoria:** Python intenta reutilizar espacios ya asignados para reducir el consumo.
2. **Asignación anticipada:** Se reserva memoria por adelantado en lugar de hacerlo solo cuando es necesario.
3. **Almacenamiento en caché:** Guarda temporalmente datos para acceder más rápido en futuras operaciones.
4. **Solicitud de memoria:** Python solicita memoria al sistema operativo según sea necesario.
5. **Asignadores de objetos:** Python utiliza asignadores específicos para diferentes tipos de objetos (enteros, cadenas, tuplas, etc.), optimizando el rendimiento y el uso de memoria según el tipo de datos.

**Ejemplos:**

- Los `enteros` suelen requerir menos espacio de memoria que las `cadenas` o los `diccionarios`.

```python
import sys

# Crear un entero
numero = 11
print("Memoria usada por entero:", sys.getsizeof(numero), "bytes")  # 28 bytes

# Crear una cadena
cadena = "Hola mundo"
print("Memoria usada por cadena:", sys.getsizeof(cadena), "bytes")  # 51 bytes

# Crear un diccionario
diccionario = {"numero": 15}
print("Memoria usada por diccionario:", sys.getsizeof(diccionario), "bytes") # 184 bytes
```

> [!NOTE]
> La función `sys.getsizeof()` muestra cuántos **bytes** ocupa cada objeto en memoria.

- La gestión de memoria para **cadenas** se enfoca en reducir el desperdicio, mientras que para **enteros** se prioriza la velocidad.

```python
a = "Python"
b = "Python"

print("¿a y b comparten la misma dirección de memoria?", a is b) # True
```

- Aunque Python maneja la memoria de forma interna, los desarrolladores no tienen control directo sobre su gestión, a diferencia de lenguajes como **C o C++**.
