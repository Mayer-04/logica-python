"""
* Cadenas de caracteres: Strings (str)
--------------------------------------

Una cadena (o string) es una secuencia de caracteres, utilizada generalmente para representar texto. 
En Python, las cadenas son inmutables, lo que significa que una vez creada una cadena, no se puede modificar.
- Otra definición: Las cadenas de caracteres son secuencias inmutables de puntos de código Unicode.
- Las cadenas son accesibles por `índices` y pueden ser `iteradas`.
- Puedes acceder a un carácter específico utilizando corchetes `[]` y un índice.
- Si intentas acceder a un índice fuera del rango de la cadena, Python nos dara un error `IndexError`.
- El slicing en strings está diseñado para ser seguro y no provocar errores al intentar acceder a índices fuera del rango
de la cadena.

Algunas características de las cadenas:
---------------------------------------
- Creación de cadenas
- Concatenación y multiplicación de cadenas
- Secuencias de escape (salto de línea, tabulación)
- Longitud de cadenas
- Formateo de cadenas
- Inmutabilidad y acceso a caracteres
- Slicing de cadenas
- Reversión de cadenas
- Iteración sobre cadenas
- Métodos comunes de cadenas
"""

# Creando una cadena de caracteres usando el contructor `str()`
mi_nombre = str("Mayer")
print(f"Hola soy {mi_nombre}")

# Creación de cadenas
# Se pueden crear usando comillas dobles o simples.
print("Python")
print('Python')

# Dos o más cadenas literales una al lado de la otra se concatenan automáticamente.
# Solo funciona con cadenas literales, no con variables o expresiones.
print("An" "dres")  # Imprime: "Andres"

# Creación de una cadena con salto de línea.
# Las cadenas de varias líneas se crean usando comillas triples.
apellido = """chaves"""
print(apellido)
print(
    """
    Python
    es un lenguaje 
    de programación
    """
)

# Concatenación de cadenas
# Las cadenas se pueden concatenar (unir) usando el operador `+`.
print("Python " + "es un lenguaje de programación")

# Multiplicación de cadenas
# Una cadena se puede multiplicar usando el operador `*`, repitiendo su contenido.
print("Python " * 3)

# Secuencias de escape
# `\n` se usa para un salto de línea, y `\t` para tabulación.
print("Python\nes un lenguaje de programación")
print("Python\tes un lenguaje de programación")

# Longitud de una cadena
# La función `len()` devuelve el número de caracteres en una cadena.
print(len("Python"))

"""
Formateo de cadenas:
--------------------
En Python, hay varias maneras de formatear cadenas para incluir variables y valores:
1. Formateo con el operador `%`:
   - %s para cadenas (strings)
   - %d para enteros (integers)
   - %f para números flotantes (floats)
2. Método `.format()`
3. f-strings (disponible a partir de Python 3.6)
"""

name = "Mayer"
age = 24
active = True
salary = 24.5

# Formateo con `%`
print(
    "Mi nombre es %s, tengo %d años y estoy %s y mi salario es %f"
    % (name, age, active, salary)
)

# Formateo con `.format()`
print("Mi nombre es {}, tengo {} años y estoy {}".format(name, age, active))

# Formateo con f-strings (interpolación de variables)
print(f"Mi nombre es {name}, tengo {age} años y estoy {active}")

# Inmutabilidad y acceso a caracteres
# Las cadenas son secuencias inmutables: no se pueden cambiar los caracteres individuales.
name = "Mayer"

# Desempaquetamiento de caracteres de una cadena
m, a, y, e, r = name
print(m, a, y, e, r)

# Usando un guion bajo _ para ignorar caracteres
m, a, y, e, _ = name  # El guion bajo se usa para ignorar la "r"
print(m, a, y, e)

# Acceso a un carácter por índice
print(name[2])  # Imprime el tercer carácter de la cadena (`y`)

# Slicing de cadenas
# Se puede obtener una subcadena de una cadena utilizando las rebanadas o slicing.
print(name[1:])  # Desde el segundo carácter hasta el final (`ayer`)
print(name[-1])  # Último carácter de la cadena (`r`)

# Reversión de cadenas
# Usando slicing, es posible revertir el orden de los caracteres.
print(name[::-1])  # Imprime la cadena al revés (`reyaM`)

# Recorrer cadenas
# Es posible iterar sobre cada carácter de una cadena utilizando un bucle `for`.
for character in name:
    print(character)

"""
* Métodos comunes de cadenas:
-----------------------------
Python proporciona muchos métodos incorporados para manipular cadenas. 
Algunos de los más útiles se describen a continuación:
"""

# Convertir a mayúsculas
print(name.upper())  # `MAYER`

# Devuelve True si la cadena esta en mayusculas en caso contrario False
print(name.isupper())

# Convertir a minúsculas
print(name.lower())  # `mayer`

# Devuelve True si la cadena esta en minúsculas en caso contrario False
print(name.islower())

# Convertir a título (primera letra de cada palabra en mayúscula)
print(name.title())  # `Mayer`

# Capitalizar (solo la primera letra en mayúscula)
print(name.capitalize())  # `Mayer`

# Contar ocurrencias de un carácter
print(name.count("a"))  # Cuenta cuántas veces aparece `a` (`1`)

# Comprobar si una cadena empieza con un carácter o secuencia
print(name.startswith("M"))  # `True`

# Comprobar si una cadena termina con un carácter o secuencia
print(name.endswith("r"))  # `True`

# Buscar dentro de una cadena la subcadena que se pasa como argumento. Devuelve el índice de la subcadena.
# Si la subcadena no se encuentra, devuelve -1.
print(name.find("y"))  # Devuelve el índice de `y` (`2`)

# Buscar dentro de una cadena la subcadena que se pasa como argumento. Devuelve el índice de la subcadena.
# Si la subcadena no se encuentra, lanza una excepción `ValueError`.
print(name.index("y"))  # Devuelve el índice de `y` (`2`)

# Dividir una cadena en una lista de palabras
print(
    name.split()
)  # Devuelve una lista con una única palabra en este caso (`['Mayer']`)

# Reemplazar caracteres o subcadenas
print(name.replace("y", "a"))  # Reemplaza `y` con `a` (`Maaer`)

# Comprobar si la cadena es numérica
print("Python".isnumeric())  # `False`, porque "Python" no es numérico

# Devuelve una copia de la cadena y remueve los espacios en blanco iniciales y finales.
print("   Python  ".strip())

# Unir una lista de cadenas en una sola cadena.
# El método `join()` une los elementos de una lista (u otro iterable) en una sola cadena, usando un delimitador.
words = ["Python", "es", "genial"]
sentence = " ".join(words)  # Une las palabras con un espacio entre ellas
print(sentence)  # Imprime: "Python es genial"

# Usar un separador "-" en el método `join()`
separator = "-".join(["Python", "es", "genial"])
print(separator)  # Imprime: Python-es-genial
