"""
* Diccionarios en Python:
-------------------------
Un diccionario es una estructura de datos que almacena información en pares `clave-valor`.
Es ideal para representar relaciones entre elementos.

📝 NOTAS:
- Las claves en un diccionario deben ser únicas e inmutables (por ejemplo: strings, números, tuplas).
- Los valores pueden ser de cualquier tipo de dato (incluso otros diccionarios).

- Se definen con llaves: `{}`.
- En un diccionario, se accede o se modifica un valor utilizando su clave entre `corchetes`,
  por ejemplo: mi_dict["nombre"] = "Mayer".
- Los diccionarios son mutables, lo que significa que puedes agregar,
eliminar o modificar pares clave-valor después de su creación.
- Se pueden anidar, es decir, un diccionario puede contener otros diccionarios como valores.
- Los diccionarios son iterables, permitiendo recorrer sus claves, valores o ambos utilizando bucles como `for`.
- Desde `Python 3.7`, los diccionarios preservan el orden de inserción,
  lo que significa que los elementos aparecerán en el orden en que fueron agregados.

Operaciones comunes con diccionarios:
-------------------------------------
- Crear diccionarios.
- Acceder, modificar, agregar o eliminar elementos.
- Recorrer (iterar) claves y valores.

Métodos útiles con diccionarios:
--------------------------------
- `get()`:
- `setdefault()`:
- `pop()`
- `update()`
- `keys()`,
- `values()`
- `items()`
- `copy()`
- `fromkeys()`
"""

# -------------------------------------
# * CREAR DICCIONARIOS
# -------------------------------------

# Crear un diccionario vacío usando el constructor dict()
my_dict = dict()
print(my_dict)  # Salida {}

# Crear un diccionario vacío usando llaves {}
empty_dict = {}
print(empty_dict)  # Salida {}

# Crear un diccionario con elementos iniciales
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)  # Salida {'a': 1, 'b': 2, 'c': 3}

# -------------------------------------
# * TAMAÑO DEL DICCIONARIO
# -------------------------------------
print(len(my_dict))  # Salida 3 (cantidad de pares clave-valor)

# -------------------------------------
# * ACCESO Y MODIFICACIÓN
# -------------------------------------

# Usamos corchetes [] para acceder a los valores de las claves

# Acceder al valor de una clave
print(my_dict["a"])  # Salida 1 (valor asociado a la clave 'a')
print(my_dict["b"])  # Salida 2 (valor asociado a la clave 'b')

# Añadir un nuevo par clave-valor al diccionario
my_dict["d"] = 4
print(my_dict)  # Salida {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Modificar el valor de una clave existente
my_dict["a"] = 10
print(my_dict)  # Salida {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Eliminar un elemento usando su clave
del my_dict["d"]
print(my_dict)  # Salida {'a': 10, 'b': 2, 'c': 3}

# -------------------------------------
# * VERIFICAR SI UNA CLAVE EXISTE
# -------------------------------------

# Utilizamos el operador `in`

print("a" in my_dict)  # Salida True (la clave 'a' está presente)
print("z" in my_dict)  # Salida False (la clave 'z' no está presente)

# -------------------------------------
# * RECORRER UN DICCIONARIO
# -------------------------------------

# Iterar sobre un diccionario
# Obtenemos las claves del diccionario usando el bucle `for`
# Posteriormente, accedemos al valor asociado a cada clave
for key in my_dict:
    print(
        f"Clave: {key}, Valor: {my_dict[key]}"
    )  # Salida cada clave y su valor asociado

# Iterar sobre las claves del diccionario
# Utilizamos el método `keys()`
for key in my_dict.keys():
    print(f"Clave: {key}")  # a, b, c

# Iterar sobre los valores del diccionario
# Utilizamos el método `values()`
for value in my_dict.values():
    print(f"Valor: {value}")  # 10, 2, 3

# Iterar sobre los pares clave-valor del diccionario
# Utilizamos el método `items()`
for key, value in my_dict.items():
    print(
        f"Clave: {key}, Valor: {value}"
    )  # Salida cada clave junto a su valor asociado

# -------------------------------------
# * DICCIONARIOS ANIDADOS
# -------------------------------------

# Crear un diccionario con otro diccionario como valor (un diccionario dentro de otro diccionario)
nested_dict = {"a": 1, "b": 2, "c": {"d": 4, "e": 5}}
print(nested_dict)
# Salida {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}

# Acceder a un valor dentro de un diccionario anidado
print(nested_dict["c"]["d"])  # Salida 4 (valor asociado a la clave 'd' dentro de 'c')

# Eliminar una clave dentro de un diccionario anidado
del nested_dict["c"]["e"]
print(nested_dict)
# Salida {'a': 1, 'b': 2, 'c': {'d': 4}}

# -------------------------------------
# * MÉTODOS ÚTILES DE DICCIONARIOS
# -------------------------------------

# get()
# Devuelve el valor de una clave si existe
# Si la clave no existe, devuelve None (o un valor por defecto si se especifica)
print(nested_dict.get("a"))  # Salida 1
print(nested_dict.get("z"))  # Salida None

# keys(), values(), items()
# keys()   → Devuelve todas las claves
# values() → Devuelve todos los valores
# items()  → Devuelve pares (clave, valor)
print(nested_dict.keys())  # Salida dict_keys(['a', 'b', 'c'])
print(nested_dict.values())  # Salida dict_values([1, 2, {'d': 4}])
print(nested_dict.items())  # Salida dict_items([('a', 1), ('b', 2), ('c', {'d': 4})])

# setdefault()
# Devuelve el valor de la clave si existe
# Si no existe, la crea con un valor por defecto y lo devuelve
print(nested_dict.setdefault("f", 6))  # 6
print(nested_dict)  # Salida {'a': 1, 'b': 2, 'c': {'d': 4}, 'f': 6}

# copy()
# Crea una copia superficial (shallow copy) del diccionario
original = {"a": 1, "b": 2}
copia = original.copy()
print("copy:", copia)  # Salida {'a': 1, 'b': 2}

# fromkeys()
# Crea un nuevo diccionario con claves dadas y un mismo valor para todas
keys = ["a", "b", "c"]
nuevo_dic = dict.fromkeys(keys, 0)
print("fromkeys:", nuevo_dic)  # Salida {'a': 0, 'b': 0, 'c': 0}

# pop()
# Elimina una clave y devuelve su valor
dic = {"a": 1, "b": 2}
valor = dic.pop("b")
print("pop:", dic)  # Salida {'a': 1}

# update()
# Añade o actualiza pares clave-valor desde otro diccionario
d1 = {"a": 1}
d2 = {"b": 2, "c": 3}
d1.update(d2)
print("update:", d1)  # Salida {'a': 1, 'b': 2, 'c': 3}

# Desempaquetado con **
# Desempaquetar: Significa extraer los elementos de una colección (lista, tupla, diccionario, etc.)
# y “abrirlos” para usarlos de forma individual

# Combina diccionarios en uno nuevo
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5}
d3 = {**d1, **d2}
print("unpacked:", d3)  # Salida {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
