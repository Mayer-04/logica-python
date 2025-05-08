# Iterables e Iteradores

## Conceptos Claves

- **Colección:** Es cualquier `agrupación` de elementos. No necesita cumplir reglas estrictas; los elementos pueden estar o no ordenados, y es posible tener varios elementos idénticos dentro de la colección.
- **Conjunto:** Al igual que una colección, un conjunto agrupa varios elementos, pero de manera más estricta. Los elementos de un conjunto son únicos (no hay duplicados), y no necesitan estar ordenados.

> [!IMPORTANT]
> SIMILITUDES: Agrupar varios elementos.

- **Recorrer o iterar:** Significa acceder _(pasar)_ a sus elementos uno por uno, de manera ordenada, para realizar alguna acción con cada elemento. Esto es útil cuando necesitamos procesar o manipular cada elemento de una colección o conjunto.

## Iterables

Un iterable es cualquier colección de elementos que se puede `recorrer` uno por uno.

- Podemos utilizar ciclos como `for` y `while` o convertirlos en un `iterador`.
- Los elementos pueden ser `indexados` (acceder a ellos mediante un índice). Sin embargo, no todos los iterables son indexados; esta característica es exclusiva de ciertos tipos de datos.
- **No todos los iterables son indexados:** Estructuras de datos como los `sets` o los `diccionarios` no permiten el acceso a sus elementos usando índices, pero igual son `iterables`.
- **Diccionarios:** En Python, los diccionarios permiten acceder a sus elementos usando **claves** en lugar de índices. Estas claves deben ser de un **tipo de dato inmutable (como números, cadenas, o tuplas)**, y están asociadas a valores. Puedes iterar sobre las claves, valores o ambos.
- **Sets:** Los sets son colecciones no ordenadas de elementos únicos. No tienen índices porque **no garantizan un orden**, pero puedes verificar si un elemento está presente en el set con el **operador de pertenencia** `elemento in set`, y también puedes recorrerlos usando un ciclo `for`.

## Index o Indexado: Acceso a Elementos por Posición

Un índice es un **número** que indica la posición de un elemento dentro de una estructura de datos (colección o conjunto de datos).

La mayoría de los lenguajes de programación comienzan a contar los índices desde 0, lo que significa que el primer elemento tiene índice 0, el segundo índice 1, y así sucesivamente.

- Cuando hablamos de acceder a un elemento por su índice, nos referimos a seleccionar un elemento específico dentro de una colección utilizando su posición.

- Normalmente, se utilizan `corchetes []` para acceder a un elemento. El número dentro de los corchetes indica la posición del elemento que queremos (índice).

```py
animales = ["🦁", "🐺", "🦍", "🐒"]
print(animales[0])  # Imprime '🦁'
```

## Iterador

Un iterador es un `objeto` que permite `recorrer` los elementos de un **iterable** de uno en uno, pero de manera más controlada.

Mientras que un ciclo `for` oculta los detalles de cómo se accede a cada elemento, un iterador permite hacerlo manualmente con más control, utilizando los métodos `iter()` y `next()`.

**Aplicando un `iter()` a un iterable, obteniendo un `iterador`:**

```py
numeros = [2, 4, 6, 8, 10]
iterador = iter(numeros)
```

**Obtener el siguiente elemento del iterador usando `next()`:**

```py
print(next(iterador))  # Imprime 2
print(next(iterador))  # Imprime 4
```

El iterador _"recuerda"_ su posición, por lo que cada vez que llamas a `next()`, te da el siguiente elemento. Si intentas obtener más elementos cuando ya no hay, se lanza una excepción `StopIteration`.

### Otro concepto

Un iterador es una herramienta o mecanismo que nos permite `movernos` por los elementos de un **iterable**. El iterador actúa como un "guía" que nos lleva de un elemento al siguiente.

- El iterador nos permite avanzar por los elementos del iterable, uno por uno.
- El iterador mantiene el estado de dónde te encuentras en el recorrido. Así, sabe qué elemento devolver a continuación.
- Cuando llegas al final del iterable, el iterador te indica que ya no hay más elementos para recorrer.

### Los Iteradores en la Vida Real

Imagina una fila de personas esperando para ingresar a un evento. La _fila_ es un `iterable`, ya que puedes ir pasando por cada persona una por una. El `iterador` sería como un _guía_ que lleva a las personas una por una hacia la entrada del evento. Este guía "recuerda" quién es la siguiente persona en la fila, y sigue avanzando hasta que ya no quedan más personas por pasar.
