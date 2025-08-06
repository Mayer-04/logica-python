"""
* Scope - (Ámbito o Alcance)
-----------------------------
El scope en Python define `dónde` una variable o función puede ser accedida dentro del código.

- El scope define en qué partes de tu código una variable está disponible para ser usada.
Si intentas usar una variable fuera de su scope, Python te dará un error, porque no la reconoce.

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

⚠️ Importante:
--------------
- Las estructuras de control como `if`, `for`, y `while` `no crean` un nuevo scope en Python.
- Las variables definidas dentro de ellas `pertenecen al mismo scope` en el que están contenidas.
"""

# 1. Scope Global
# ---------------
x = 10  # Esta variable está en el ámbito global


def funcion_global():
    # Puede acceder a 'x' porque está en el scope global
    print(x)


funcion_global()  # Imprime: 10


# 2. Scope Local
# --------------
def funcion_local():
    y = 20  # 'y' solo existe dentro de esta función (scope local)
    print(y)


funcion_local()  # Imprime: 20

# print(y)  # ❌ Esto genera un error porque 'y' no existe fuera de la función


# 3. Scope Enclosing
# ------------------
# Una función dentro de otra puede acceder a variables del scope "enclosing" (función externa)
def funcion_externa():
    numero = 30  # Variable en el scope "enclosing"

    def funcion_interna():
        # Busca 'numero' en su scope local, no la encuentra, y la encuentra en el enclosing scope
        print(numero)

    funcion_interna()


funcion_externa()  # Imprime: 30


# 4. Scope Built-in
# -----------------
# Python busca nombres en este orden: Local -> Enclosing -> Global -> Built-in
print(len([1, 2, 3]))  # 'len' es una función built-in. Imprime: 3


# Redefinir 'len' en el scope global sobrescribe la función built-in
len = "Esto ya no es la función len"  # Ahora 'len' es una variable global

print(len)  # Imprime: Esto ya no es la función len

# print(len([1, 2, 3]))  # ❌ Esto ahora generaría un error: 'str' object is not callable


# 5. Scope y estructuras de control
# ---------------------------------
# Las estructuras como 'for', 'if', 'while' NO crean un nuevo scope.
# Las variables definidas dentro de ellas siguen estando en el mismo scope.

for i in range(5):
    j = i * 2  # 'j' se define dentro del for, pero sigue siendo parte del scope global

# Como 'for' no crea un scope, 'j' está disponible aquí
print(j)  # Imprime: 8 (último valor asignado a j)