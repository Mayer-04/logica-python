"""
* Cadenas de caracteres: Strings (str)
--------------------------------------
Una cadena (o string) es una secuencia de caracteres, utilizada generalmente para representar texto.
Otra definición: Las cadenas de caracteres son secuencias inmutables de puntos de código Unicode.

En Python, las cadenas son inmutables, lo que significa que una vez creadas, no se puede modificar.
- Las cadenas son accesibles por `índices` y pueden ser `iteradas`.
- Puedes acceder a un carácter específico utilizando corchetes `[]` y un índice.
- Si intentas acceder a un índice fuera del rango de la cadena, Python nos dara un error `IndexError`.
- El slicing en strings está diseñado para ser seguro y no provocar errores al intentar acceder a índices
fuera del rango de la cadena.

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
nombre = str("Mayer")
print(f"Hola, mi nombre es {nombre}")

# Creación de cadenas
# Se pueden crear usando comillas dobles o simples
print("Python")
print('Python')

# Dos o más cadenas literales una al lado de la otra se concatenan automáticamente
# Solo funciona con cadenas literales, no con variables o expresiones
print("An" "dres")  # Salida: "Andres"

# Crear una cadena con salto de línea
# Las cadenas de varias líneas se pueden crean usando comillas triples.
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
# Las cadenas se pueden concatenar (unir) usando el operador `+`
print("Python " + "es un lenguaje de programación")

# Multiplicación de cadenas
# Una cadena se puede multiplicar (repetir) usando el operador `*`
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

# Formatear con `%`
print(
    "Mi nombre es %s, tengo %d años y estoy %s y mi salario es %f"
    % (name, age, active, salary)
)

# Formatear con `.format()`
print("Mi nombre es {}, tengo {} años y estoy {}".format(name, age, active))

# Formatear con f-strings (interpolación de variables)
print(f"Mi nombre es {name}, tengo {age} años y estoy {active}")

# Inmutabilidad y acceso a caracteres
# Las cadenas son secuencias inmutables: no se pueden cambiar los caracteres individuales.
name = "Mayer"
# name[0] = "L" ❌ TypeError: 'str' object does not support item assignment

# Desempaquetar caracteres de una cadena
m, a, y, e, r = name
print(m, a, y, e, r)  # Salida: M a y e r

# Usando un guión bajo _ para ignorar caracteres
m, a, y, e, _ = name  # El guión bajo se puede usar para ignorar el caracter no deseado
print(m, a, y, e)  # Salida: M a y e

# Acceso a un carácter por índice
print(name[2])  # Salida: Tercer carácter de la cadena (`y`)

# Slicing de cadenas
# Se puede obtener una 'subcadena' de una cadena utilizando las rebanadas o slicing
print(name[1:])  # Desde el segundo carácter hasta el final (`ayer`)
print(name[-1])  # Último carácter de la cadena (`r`)

# Reversión de cadenas
# Usando slicing, es posible revertir el orden de los caracteres.
print(name[::-1])  # Salida: `ryeaM`

# Recorrer cadenas
# Es posible iterar sobre cada carácter de una cadena utilizando un bucle `for`
for character in name:
    print(character)

"""
Métodos comunes de cadenas en Python
-------------------------------------
Python ofrece muchos métodos incorporados para manipular strings. 
Aquí tienes algunos de los más útiles:
"""

nombre = "Andres"

# Comprobaciones de contenido
print("a" in nombre)  # False – ¿Contiene la letra 'a'?
print(nombre.startswith("A"))  # True – ¿Empieza con 'A'?
print(nombre.endswith("s"))  # True – ¿Termina con 's'?
print(nombre.count("e"))  # 1 – ¿Cuántas veces aparece 'e'?
print(nombre.find("d"))  # 1 – Índice de 'd' o -1 si no existe
# print(nombre.index("z"))        # ❌ ValueError si no se encuentra

# Transformaciones de formato
print(nombre.upper())  # 'ANDRES' – Todo en mayúsculas
print(nombre.lower())  # 'andres' – Todo en minúsculas
print(nombre.title())  # 'Andres' – Primera letra de cada palabra en mayúscula
print(nombre.capitalize())  # 'Andres' – Solo la primera letra en mayúscula

# Validaciones de formato
print(nombre.isupper())  # False – ¿Está todo en mayúsculas?
print(nombre.islower())  # False – ¿Está todo en minúsculas?
print("123".isnumeric())  # True – ¿Es numérica?

# Limpieza y división
print(
    "   Python  ".strip()
)  # 'Python' – Elimina espacios al inicio y final y devuelve una copia limpia de la cadena

# El método `split()` divide una cadena en una lista de substrings, usando un delimitador.
print("Python es genial".split())  # ['Python', 'es', 'genial'] – Divide por espacios

# Reemplazo
print(nombre.replace("e", "a"))  # 'Andras' – Reemplaza 'e' por 'a'

# Unión de cadenas
# El método `join()` une los elementos de una lista (u otro iterable) en una sola cadena, usando un delimitador.
palabras = ["Python", "es", "genial"]
print(" ".join(palabras))  # 'Python es genial' – Une con espacios
print("-".join(palabras))  # 'Python-es-genial' – Une con guiones
