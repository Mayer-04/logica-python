# Gestión de la Memoria en Python

La gestión de memoria en Python está diseñada para ser automática y eficiente. El `intérprete` se encarga de la asignación y liberación de memoria a través de su propio `administrador de memoria`, lo que significa que los desarrolladores no tienen que preocuparse directamente por la administración de recursos de memoria

Todos los objetos y estructuras de datos de Python se almacenan en un `montón privado`.

## Montón

El montón es una parte de la `memoria` de una computadora donde se almacenan datos que no tienen un tamaño fijo o que se crean **dinámicamente** durante la ejecución de un programa.

- Es más flexible porque permite que se asigne y libere memoria según sea necesario mientras el programa está en funcionamiento.
- Cuando creas un objeto o una estructura de datos como una lista o un diccionario en Python, estos no tienen un tamaño fijo (pueden crecer o reducirse), por lo que se almacenan en el montón.
- El montón es más lento que la `pila`.

### Montón Privado

El `montón privado` de Python es una porción específica (reservada) de la memoria que solo el `intérprete de Python` puede gestionar.
Cuando trabajas con objetos en Python **(como listas, diccionarios, cadenas, etc.)**, estos se almacenan en ese montón privado. Este montón es "privado" en el sentido de que, como desarrollador, no puedes controlarlo directamente

Esto significa que, aunque estés creando y usando objetos en tu código Python, el sistema interno del lenguaje es el que decide cómo y dónde se almacenan esos datos en el montón privado.

## Gestión Dinámica de Memoria en Python

1. **Reutilización de Memoria:** Python optimiza el uso de recursos reutilizando espacios de memoria cuando es posible.
2. **Asignación Anticipada:** Se reserva memoria por adelantado en lugar de hacerlo solo cuando es necesario.
3. **Almacenamiento en Caché:** Se mantienen datos en memoria temporalmente para acelerar el acceso futuro.
4. **Solicitud de Memoria:** Python solicita memoria al sistema operativo según sea necesario.
5. **Asignadores de Objetos:** Python utiliza asignadores específicos para diferentes tipos de objetos (enteros, cadenas, tuplas, etc.), optimizando el rendimiento y el uso de memoria según el tipo de datos.

**Ejemplos:**

- Los `enteros` suelen requerir menos espacio de memoria que las `cadenas` o los `diccionarios`.
- La gestión de memoria para `cadenas` se enfoca en reducir el desperdicio, mientras que para enteros se prioriza la velocidad.
- Aunque Python maneja la memoria de forma interna, los desarrolladores no tienen control directo sobre su gestión, a diferencia de lenguajes como **C o C++**.
