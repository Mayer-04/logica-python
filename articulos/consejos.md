# Consejos y Buenas Prácticas en Python

## Iniciar Python en el Modo Interactivo

**En Windows:**

```bash
python
```

**En MacOS o Linux:**

```bash
python3
```

Para salir del modo interactivo de Python, utiliza el siguiente comando:

```shell
exit()
```

> [!NOTE]
> Para salir del modo interactivo, simplemente usa `exit()` o `Ctrl+D`.

## Lenguaje Interpretado o de Script

El código Python que escribimos no se convierte directamente en instrucciones que la computadora pueda entender **(lenguaje máquina)**. En lugar de eso, un programa especial llamado `intérprete de Python` traduce primero el código fuente a un formato intermedio llamado `bytecode`, que es una representación más eficiente que el código fuente original.

- El intérprete de Python **(La máquina virtual de Python _PVM_)** ejecuta este `bytecode`. Es decir, el intérprete lee el `bytecode` y lo traduce a instrucciones que la computadora puede entender y ejecutar.
- Los archivos `.pyc` se generan automáticamente y se guardan en un directorio especial llamado `_pycache_`, en la misma carpeta donde está tu archivo `.py` original. Esto acelera la ejecución del código, ya que evita recompilar el bytecode cada vez que se ejecuta el programa.

## Mutabilidad e Inmutabilidad

Los objetos en Python se pueden clasificar en dos categorías basadas en su capacidad para cambiar:

1. **Mutables:** Estos objetos pueden cambiar su valor después de haber sido creados. Cuando un objeto mutable se pasa como argumento a una función, se pasa por referencia, lo que significa que las modificaciones realizadas en la función afectarán al objeto original.

**Algunos objetos mutables son:**

- list (listas)
- dict (diccionarios)
- set (conjuntos)
- bytearray

2. **Inmutables:** Estos objetos no pueden cambiar su valor una vez creados. Si se intenta modificar un objeto inmutable, se creará un nuevo objeto en su lugar. Cuando un objeto inmutable se pasa como argumento a una función, se pasa por valor, es decir, la función trabaja con una copia del valor original y no puede modificar el objeto original.

**Algunos objetos inmutables son:**

- int (enteros)
- float (flotantes)
- bool (booleanos)
- str (cadenas)
- tuple
- frozenset

## Consejos para Escribir Código en Python

1. En Python, no es necesario terminar cada sentencia con un punto y coma (;).
2. **Indentación Obligatoria:** En lugar de usar llaves `{}` para agrupar bloques de código (como en otros lenguajes), Python utiliza la `indentación`. Por convención, se emplean `4 espacios` por nivel de indentación. Una indentación incorrecta resultará en un error de sintaxis.
3. **Nombres de Variables Descriptivos:** Es recomendable utilizar nombres de variables en minúsculas, separando las palabras con guiones bajos `(snake_case).`
4. Puedes multiplicar una cadena por un número para repetirla varias veces con el operador aritmetico `*`:

```py
print("Mayer" * 4) # MayerMayerMayerMayer
```

5. **Evita Comparar Tipos Diferentes:** Comparar valores de diferentes tipos puede generar errores o comportamientos inesperados. Asegúrate de que los valores sean del mismo tipo antes de compararlos.
6. **Uso de Truthy y Falsy:** Al igual que en JavaScript, Python evalúa valores como `True` o `False` en condiciones. Ejemplos de valores `Falsy` incluyen `None`, `0`, `""`, `[]`, `{}`, mientras que cualquier otro valor se considera `Truthy`.
7. **Conversión Implícita en Condicionales:** El intérprete de Python convierte `implícitamente` una variable a un booleano cuando se evalúa en una condición if. Esto sucede también en lenguajes como JavaScript.
8. **Modificación de Listas Durante la Iteración:** Modificar una lista mientras la recorres puede causar comportamientos inesperados. Para evitarlo, trabaja con una copia de la lista:

```py
for item in my_list[:]:
    if some_condition(item):
        my_list.remove(item)
```

9. **Evita Efectos Colaterales en Funciones:** Las funciones deben evitar modificar variables globales u otras partes del programa para mantener la claridad y facilitar las pruebas.
10. **Secuencias:** Es un tipo de dato que puede almacenar una colección de elementos o contener varios elementos. Algunas secuencias en Python son las listas, tuplas, cadenas de caracteres y rangos (la función `range()`).
11. **Evitar el Uso de Importaciones Generales:** No uses `from módulo import *`, ya que puede causar conflictos de nombres. Importa solo lo que necesitas o usa **alias** si es necesario.

```py
# Correcto
from math import sqrt

# Incorrecto
from math import *
```

## Buenas Prácticas de Programación en Python

1. **Uso de Funciones Incorporadas (Built-ins):** Python ofrece muchas funciones incorporadas que pueden simplificar tu código, como **len()**, **sum()**, **max()**, **min()**, entre otras. Siempre que sea posible, utiliza estas funciones en lugar de reinventar la rueda.
2. **Comprensión de Listas y Comprensión de Generadores:** Utiliza comprensión de listas y generadores para crear listas, diccionarios, o conjuntos de manera concisa y eficiente:

### List Comprehension

La `comprensión de listas` es una forma concisa y elegante de crear listas. En lugar de usar un bucle for largo para añadir elementos a una lista, puedes escribir todo en una línea de código.

- Crea y almacena todos los elementos en una lista en memoria de una vez.

```py
cuadrados = [x**2 for x in range(10)]
```

### Generator Comprehension

Los `generadores` son como las listas, pero en lugar de calcular y almacenar todos los elementos en memoria de una vez, los generan sobre la marcha. Esto hace que sean mucho más eficientes en términos de memoria cuando trabajas con secuencias grandes.

- Genera cada elemento sobre la marcha cuando es necesario, lo que puede ser más eficiente si tienes una secuencia muy grande.

```py
cuadrados_tup = (x**2 for x in range(10))
```

### Entornos Virtuales

Para evitar conflictos de dependencias entre proyectos, utiliza entornos virtuales. Esto te permite gestionar paquetes y versiones de manera aislada para cada proyecto.

- Los entornos virtuales permiten tener diferentes versiones de las bibliotecas instaladas en diferentes proyectos, todo de manera aislada.
- Python crea una carpeta dedicada a ese proyecto donde se almacenan todas las dependencias **(paquetes, bibliotecas, etc.)**. Luego, cuando trabajas dentro de ese entorno, Python utilizará solo las dependencias instaladas allí, y no las globales de tu sistema.
- Para crear un entorno virtual, navega hasta el directorio de tu proyecto y ejecuta:

**En Linux y Mac OS:**

```bash
python3 -m venv <nombre_entorno>
```

**Windows:**

```bash
python -m venv <nombre_entorno>
```

## Diccionarios en Python

1. Las claves de un diccionario deben ser `inmutables`, como enteros, cadenas o tuplas. No uses listas o diccionarios como claves.
2. **Acceso Seguro a Valores con get():** Utiliza el método `get()` para acceder a los valores de un diccionario sin riesgo de lanzar un error si la clave no existe:

```py
diccionario = {"cuidad": "medellin"}
print(diccionario.get("clave2", "Valor por defecto"))  # Salida: Valor por defecto
```

3. **Comprensión de Diccionarios:** Usa la comprensión de diccionarios para crear diccionarios de manera concisa y eficiente:

```py
cuadrados_dict = {x: x**2 for x in range(10)}
```

4. **Evita Modificar un Diccionario Durante la Iteración:** Similar a las listas, modificar un diccionario mientras lo iteras puede causar errores. Usa métodos como `copy()` si necesitas modificarlo dentro de un bucle.

## Características Avanzadas

1. **Desempaquetado:** Utiliza `*` y `**` para desempaquetar listas y diccionarios al pasar argumentos a funciones o al realizar asignaciones:

```py
my_list = [1, 2, 3]
print(*my_list)  # Salida: 1 2 3
```

**Desempaquetado de diccionarios:**

```py
my_dict = {"a": 1, "b": 2, "c": 3}
new_dict = {**my_dict}
print(new_dict) # salida: {'a': 1, 'b': 2, 'c': 3}
```

```py
def generar_diccionario(a, b, c):
    print(a, b, c)

diccionario = {'a': 1, 'b': 2, 'c': 3}
generar_diccionario(**diccionario)  # Salida: 1 2 3
```

## Objetos: Identidad, Tipo y Valor

Recordemos que en **objeto** en Python es una _instancia_ de una clase. Cada objeto en Python tiene tres características fundamentales: `identidad`, `tipo` y `valor`.

- **Identidad:** La identidad de un objeto es un identificador único (número entero) que lo distingue de otros objetos. Esta identidad es inmutable durante la vida del objeto y se puede verificar usando el operador `is`, que determina si dos referencias apuntan al mismo objeto en memoria.
- **Tipo:** El tipo de un objeto define la naturaleza de los datos que contiene y las operaciones que se pueden realizar sobre él. Una vez que se crea un objeto, su tipo no cambia. El tipo de un objeto se puede consultar con la función `type()`.
- **Valor:** El valor de un objeto es el contenido que almacena. Dependiendo de si el objeto es `mutable` o `inmutable`, su valor puede o no cambiar durante la ejecución del programa.

Ejemplo de como se veria esto:

```py
# Creando un objeto (en este caso una lista)
mi_lista = [1, 2, 3]

# Identidad: el identificador único del objeto
# Se representa como un número entero
identidad = id(mi_lista)
print(f"Identidad: {identidad}") # Identidad: 2706717792512

# Tipo: el tipo del objeto
tipo = type(mi_lista)
print(f"Tipo: {tipo}") # Tipo: <class 'list'>

# Valor: el contenido del objeto
valor = mi_lista
print(f"Valor: {valor}") # Valor: [1, 2, 3]

# Comparación de identidad con otro objeto similar
# Las listas son mutables por lo que crea un nuevo objeto en memoria,
# incluso si el contenido de la lista es idéntico al de otra lista.
otra_lista = [1, 2, 3]
print(f"¿mi_lista es la misma que otra_lista? {mi_lista is otra_lista}") # False

# Modificación del objeto mutable
mi_lista.append(4)
print(f"Valor modificado: {mi_lista}") # Valor modificado: [1, 2, 3, 4]
```

## Entorno de código de nivel superior `__main__`

### ¿Qué es `__name__`?

En Python, cada archivo de código se trata como un **módulo**. Cuando Python ejecuta o importa un archivo, le asigna una variable especial llamada `__name__` que identifica el **módulo**. Dependiendo de cómo se utilice el archivo (si es ejecutado directamente o importado), el valor de `__name__` será diferente.

- Si importas un módulo en otro archivo usando `import`, el valor de `__name__` será el nombre del archivo (sin la extensión .py).

```py
import math
print(math.__name__)  # Imprime 'math'
```

- Si ejecutas un archivo directamente (por ejemplo, desde la línea de comandos), el valor de `__name__` será `'__main__'`, lo que indica que ese archivo es el que se está ejecutando.

Esto permite que Python sepa si un archivo está siendo ejecutado como el programa principal o si solo está siendo utilizado como un módulo en otro archivo.

### ¿Por qué es útil if `__name__ == '__main__'`?

Cuando escribes código que debería ejecutarse solo cuando el archivo se ejecuta directamente y no cuando se importa en otro archivo, puedes usar este bloque:

```py
if __name__ == '__main__':
    # Este código se ejecutará solo si el archivo se ejecuta directamente
```

Este bloque es útil cuando quieres que algunas partes del código solo se ejecuten si el archivo está siendo ejecutado como el `programa principal` y no cuando se importa como un módulo en otro programa.

- `if __name__ == '__main__'` es una estructura que permite ejecutar código solo cuando el archivo es ejecutado directamente, no cuando es importado.

```py
def saludar():
    print("¡Hola Mayer!")

if __name__ == '__main__':
    saludar()  # Solo se ejecutará esta función si corres este archivo directamente
```

### ¿Qué es el "entorno de código de máximo nivel"?

El "entorno de código de máximo nivel" se refiere al archivo que inicia todo el programa, importando otros módulos si es necesario; Este archivo es el que se ejecuta directamente y cuyo `__name__` es `'__main__'`.

Es importante porque este archivo puede importar otros módulos y coordinar la ejecución del programa, pero solo debería ejecutar ciertas acciones **(como correr pruebas o iniciar la aplicación)** si es el archivo que se está ejecutando directamente, no si es importado por otro módulo.

- Definir un punto de entrada en aplicaciones más grandes, donde el archivo principal coordina la ejecución de diferentes partes del programa.

- Permite escribir módulos reutilizables que no ejecutan código innecesario cuando son importados por otros scripts.

```py
def main():
    # Lógica principal de la aplicación
    print("La aplicación principal")

if __name__ == '__main__':
    main()  # Este código solo se ejecuta si el archivo es ejecutado directamente
```
