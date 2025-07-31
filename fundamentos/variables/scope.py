"""
* Scope - (Ámbito o Alcance)
-----------------------------
El scope en Python se refiere a `dónde` puedes usar una variable o una función en tu código.

- El scope define en qué partes de tu código una variable está disponible para ser usada.
Si intentas usar una variable fuera de su scope, Python te dará un error, porque no la reconoce.

Tipos de scope y cómo Python los busca (Regla LEGB):
-----------------------------------------------------

1. Local (L): Es el scope más interno. Se refiere a las variables definidas dentro de una función.
Estas variables solo existen y se pueden usar dentro de esa función.

2. Enclosing (E): Se refiere al scope de una función externa que contiene otra función interna.
Si la función interna no encuentra una variable en su propio scope, Python buscará en la función externa.

3. Global (G): Es el scope más externo. Las variables definidas fuera de cualquier función, es decir,
en el nivel más alto de un script, tienen un scope global y se pueden usar desde cualquier parte del código.

4. Built-in (B): Se refiere a los nombres que Python tiene incorporados por defecto, como `print()`, `len()`, etc.
Python buscará aquí solo si no encuentra la variable en ninguno de los scopes anteriores.

IMPORTANTE:
- Las estructuras de control como `if`, `for`, o `while` **no crean** un nuevo scope en Python.
Las variables que defines dentro de ellas simplemente heredan el scope del bloque de código donde están.
"""

# 1. Scope Global
x = 10  # Variable global


def funcion_global():
    print(x)  # Puede acceder a 'x' porque es global


funcion_global()  # Imprime: 10


# 2. Scope Local
def funcion_local():
    y = 20  # Variable local
    print(y)


funcion_local()  # Imprime: 20
# print(y)  # Esto daría un error, porque 'y' es local y no existe fuera de la función


# 3. Scope Enclosing
def funcion_externa():
    numero = 30  # Variable en scope "Enclosing"

    def funcion_interna():
        print(
            numero
        )  # Accede a la variable 'numero' desde el scope externo (enclosing)

    funcion_interna()


funcion_externa()  # Imprime: 30

# 4. Built-in Scope
# Python buscará primero en el scope local, luego enclosing, luego global, y finalmente en el built-in.
print(len([1, 2, 3]))  # 'len' es una función built-in de Python. Imprime: 3

# Si redefinimos 'len' en el scope global:
len = "Esto ya no es la función len"  # Ahora 'len' es una variable global
print(len)  # Imprime: Esto ya no es la función len

# Las estructuras de control no crean un nuevo scope.
# Hereda el scope global porque 'for' no crea un nuevo scope y esta a nivel de script.
for i in range(5):
    j = i * 2  # 'j' se define dentro del for, pero hereda el scope global

print(
    j
)  # Imprime: 8 (el último valor de j dentro del for), porque está en el scope global
