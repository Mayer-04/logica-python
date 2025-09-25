"""
* Cadenas de caracteres: Strings (str)
--------------------------------------
Una cadena (o string) es una secuencia de caracteres, normalmente usada para representar texto.

Otra definición: 
-----------------
Las cadenas de caracteres son secuencias inmutables de puntos de código Unicode.
(permiten emojis, acentos, símbolos, etc).

En Python, las cadenas son inmutables, lo que significa que una vez creadas, no se pueden modificar.
- Puedes acceder a caracteres individuales usando `índices`.
- Se pueden recorrer (iterar) con un bucle `for`.
- Puedes acceder a un carácter específico utilizando corchetes `[]` y un índice.
- Si intentas acceder a un índice fuera del rango de la cadena (no existe), Python nos dara un error `IndexError`.
- El slicing (rebanada) en strings está diseñado para ser seguro y no provocar errores al intentar acceder a índices
fuera del rango de la cadena.

Algunas características de las cadenas:
---------------------------------------
1. Creación de cadenas
2. Concatenación y multiplicación de cadenas
3. Secuencias de escape (salto de línea, tabulación)
4. Longitud de cadenas
5. Formateo de cadenas
6. Inmutabilidad y acceso a caracteres
7. Slicing de cadenas
8. Reversión de cadenas
9. Iteración sobre cadenas
10. Métodos comunes de cadenas

Notas:
-------
- Índices comienzan en 0.
- El segundo valor en slicing (`inicio:fin`) es excluyente (no se incluye).
- El tercer valor en slicing (`inicio:fin:paso`) indica el paso.
- El `paso` puede ser negativo para recorrer la cadena en orden inverso.
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
# Las cadenas de varias líneas se pueden crean usando comillas triples
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
# `\n` se usa para un salto de línea, y `\t` para tabulación
print("Python\nes un lenguaje de programación")
print("Python\tes un lenguaje de programación")

# Longitud de una cadena
# La función `len()` devuelve el número de caracteres en una cadena
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

"""
Formateo numérico con f-strings:
--------------------------------
El formato `.f` dentro de una f-string se usa para mostrar números flotantes con una cantidad específica
de decimales.

Sintaxis:
---------
f"{valor:.2f}"
"""

precio = 3.14159

# Mostrar con 2 decimales
print(f"Precio con 2 decimales: {precio:.2f}")  # Salida: 3.14

# Mostrar con 4 decimales
print(f"Precio con 4 decimales: {precio:.4f}")  # Salida: 3.1416

# Alinear a la derecha con 10 espacios
print(f"Precio alineado: {precio:10.2f}")  # Salida:        3.14

# Mostrar porcentaje con 1 decimal
porcentaje = 0.875
print(f"Porcentaje: {porcentaje:.1%}")  # Salida: Porcentaje: 87.5%


# ------------------------------------
# * Expresiones dentro de un f-string
# ------------------------------------

greet = f"Hola {(
    nombre.upper() # Convertir el nombre a mayúsculas
)}!"
print(greet)  # Salida: Hola MAYER

nums = [1, 2, 3]
print(f"Suma: {sum(x**2 for x in nums)}") # Suma: 14

print(f"Reemplazo: {'abc'.replace('a', 'Z').upper()}") # Reemplazo: ZBC

# Inmutabilidad de cadenas
# Las cadenas (str) en Python son INMUTABLES: no se puede cambiar un carácter específico.
name = "Mayer"
# name[0] = "L"  # ❌ Esto produce: TypeError: 'str' object does not support item assignment

# Desempaquetar caracteres
# Puedes asignar cada carácter de la cadena a variables separadas
m, a, y, e, r = name
print(m, a, y, e, r)  # M a y e r

# Ignorar caracteres con guión bajo (_)
# El guión bajo se usa para “descartar” valores que no nos interesan
m, a, y, e, _ = name
print(m, a, y, e)  # M a y e

# Acceder a un carácter por índice
# Los índices empiezan en 0, name[2] es el tercer carácter
print(name[2])  # y

# Slicing (rebanado) de cadenas
# Permite obtener subcadenas: name[inicio:fin] → fin es excluyente
print(name[1:])   # ayer (desde el índice 1 hasta el final)
print(name[-1])   # r (último carácter)

# Revertir una cadena con slicing
# Ignora el parámetro de inicio y el parámetro de fin
print(name[::-1])  # ryeaM

# Recorrer cada carácter con un bucle 'for'
for character in name:
    print(character)

# Recorrer cada carácter y su índice con 'enumerate()'
for index, character in enumerate(name):
    print(index, character)
    
# Recorrer cada carácter con zip()
for index, character in zip(range(len(name)), name):
    print(index, character)
    
# Recorrer cada carácter con un bucle 'while'
index = 0
while index < len(name):
    print(name[index])
    index += 1

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
# print(nombre.index("z"))        # ValueError si no se encuentra

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

# El método `split()` divide una cadena en una lista de substrings, usando un delimitador
print("Python es genial".split())  # ['Python', 'es', 'genial'] – Divide por espacios

# Reemplazo
print(nombre.replace("e", "a"))  # 'Andras' – Reemplaza 'e' por 'a'

# Unión de cadenas
# El método `join()` une los elementos de una lista (u otro iterable) en una sola cadena, usando un delimitador
palabras = ["Python", "es", "genial"]
print(" ".join(palabras))  # 'Python es genial' – Une con espacios
print("-".join(palabras))  # 'Python-es-genial' – Une con guiones
