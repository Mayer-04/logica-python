"""
* Enum: Enumeración
--------------------
Un enum permite definir un conjuntos de valores simbólicos asociados a un nombre, cada uno de ellos único y constante.

Valor simbólico: Es el nombre de un miembro de una enumeración. Representen conceptos claros y significativos dentro de tu código.

- Son útiles para representar un conjunto limitado de opciones o constantes que no cambiarán a lo largo del tiempo.
- Cada miembro de una enumeración tiene un valor único. Intentar asignar el mismo valor a dos nombres diferentes
en la misma enumeración generará un error.
- Los miembros de la enumeración son inmutables. Una vez definidos, ni los nombres ni los valores de los miembros pueden cambiarse.
- Los miembros de una enumeración se pueden comparar usando los operadores `==` y `is`.
- Usa el operador `is` en lugar de `==` para comparar miembros de la enumeración, ya que `is` compara la identidad
de los objetos, no solo sus valores.
- Las enumeraciones ayudan a evitar el uso de valores "mágicos" como `0`, `1`, `True`, `False`, `None`, etc.
- Siempre que tengas un conjunto fijo de valores que no cambiarán utiliza los enums.
"""

from enum import Enum


class Color(Enum):
    AMARILLO: int = 1
    AZUL: int = 2
    ROJO: int = 3


print(Color(1))  # Color.AMARILLO
print(Color.ROJO)  # Color.ROJO
print(repr(Color.ROJO))  # <Color.ROJO: 3>
print(Color.ROJO.name)  # ROJO
print(Color.ROJO.value)  # 3


class EstadoOrden(Enum):
    PENDIENTE = "Pendiente"
    EN_PROCESO = "En proceso"
    COMPLETADA = "Completada"
    CANCELADA = "Cancelada"


# Uso
estado_actual = EstadoOrden.PENDIENTE
print(estado_actual)  # EstadoOrden.PENDIENTE
print(estado_actual.value)  # 'Pendiente'

# Comparando con el operador 'is'
print(estado_actual is EstadoOrden.PENDIENTE)  # True

# Comparando con el operador '=='
print(estado_actual == EstadoOrden.PENDIENTE)  # True
