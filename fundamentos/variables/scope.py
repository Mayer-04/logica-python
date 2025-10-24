"""
* Scope: (Ámbito o Alcance)
-----------------------------
El scope en Python define `dónde` una variable o función puede ser accedida dentro del código.

- El scope define en qué partes de tu código una variable está disponible para ser usada.
- Si intentas usar una variable fuera de su scope, Python te dará un error, porque no la reconoce.

Tipos de scope y cómo Python los busca (Regla LEGB):
-----------------------------------------------------

1. Local (L):
- Es el scope más interno.
- Se refiere a las variables definidas dentro de una función.
- Estas variables solo existen y se pueden usar dentro de esa función.

2. Enclosing (E):
- Se refiere al scope de una función externa que contiene otra función interna.
- Si la función interna no encuentra una variable en su propio scope, Python buscará en la función externa.

3. Global (G):
- Es el scope más externo.
- Las variables definidas fuera de cualquier función, es decir,
en el nivel más alto de un script, son accesibles desde cualquier parte del código.

4. Built-in (B):
- Se refiere a los nombres que Python tiene incorporados por defecto, como `print()`, `len()`, etc.
- Python buscará aquí solo si no encuentra la variable en ninguno de los scopes anteriores.

Importante:
------------
- Las estructuras de control como `if`, `for`, y `while` NO crean un nuevo scope en Python.
- Las variables definidas dentro de ellas `pertenecen al mismo scope` en el que están contenidas.
"""

# Scope Global
# --------------
numero = 10  # Esta variable está en el ámbito global (variable global)


def funcion_global():
    # Puedes acceder a 'numero' porque está en el scope global
    print(numero)


funcion_global()  # Salida: 10


# Scope Local
# --------------
def funcion_local():
    y = 20  # 'y' solo existe dentro de esta función (scope local)
    print(y)


funcion_local()  # Salida: 20

# print(y)  # Esto genera un error porque 'y' no existe fuera de la función


# Scope Enclosing
# ------------------
# Una función dentro de otra puede acceder a variables del scope "enclosing" (función externa)
def funcion_externa():
    numero = 30  # Variable en el scope "enclosing"

    def funcion_interna():
        # Busca 'numero' en su scope local, no la encuentra, y la encuentra en el enclosing scope
        print(numero)

    funcion_interna()


funcion_externa()  # Salida: 30


# Ámbito Built-in y orden de resolución de nombres (LEGB)
# -----------------------------------------------------------
# 1. Local: Dentro de la función actual
# 2. Enclosing: En funciones anidadas (no aplica aquí)
# 3. Global: En el módulo actual
# 4. Built-in: En el conjunto de nombres predefinidos de Python

# Ejemplo: 'len' es una función built-in
print(len([1, 2, 3]))  # Salida: 3

# Redefinir 'len' en el ámbito global sobrescribe la función built-in
len = "Esto ya no es la función len"  # Ahora 'len' es una variable global tipo str

# Ahora 'len' ya no es la función, sino una cadena
print(len)  # Salida: Esto ya no es la función len

# Intentar usar 'len' como función ahora genera un error
# print(len([1, 2, 3]))  # TypeError: 'str' object is not callable


# Ámbito (Scope) y estructuras de control
# ------------------------------------------
# En Python, las estructuras de control como `for`, `if` y `while` NO crean un nuevo scope.
# Esto significa que las variables definidas dentro de estas estructuras siguen perteneciendo al mismo ámbito externo.
# Si esta a nivel de archivo, su scope es global. Pero si esta dentro de una función, clase, etc., si scope es local.

# Ejemplo:
for numero in range(5):
    # Aunque 'resultado' se define dentro del bucle, sigue estando en el ámbito externo
    resultado = numero * 2

# Como el bucle 'for' no crea un nuevo scope, 'resultado' sigue siendo accesible aquí
print(f"Último valor de 'resultado': {resultado}")  # Salida: 8 (cuando numero fue 4)
