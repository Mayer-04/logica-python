"""
Construir escalera de asteriscos
---------------------------------
Crea una función que reciba como parámetro un número entero positivo llamado `niveles` y retorne
una cadena de texto que forme una escalera ascendente usando asteriscos `(*)`.
Cada nivel debe tener un número creciente de asteriscos, separados por saltos de línea.
Usa `range()` para controlar cuántos asteriscos imprimir en cada nivel.

Parámetros:
- niveles (int): Número de niveles que tendrá la escalera.
Retorna:
- (str): Cadena con la escalera formada por asteriscos.
Caso 1:

- Input: niveles = 3
- Output:
            *
            **
            ***

Caso 2:
- Input: niveles = 5
Output:
            *
            **
            ***
            ****
            *****
"""


def generate_asc_ladder(levels: int) -> str:
    ladder = ""

    for i in range(1, levels + 1):
        ladder += "*" * i + "\n"

    return ladder


def generate_asc_ladder_2(levels: int) -> str:
    ladder = ""

    for i in range(1, levels + 1):
        line = ""
        for _ in range(i):
            line += "*"
        ladder += line + "\n"

    return ladder


def construir_escalera(niveles: int) -> str:
    lineas = ["*" * i for i in range(1, niveles + 1)]
    return "\n".join(lineas)


print(generate_asc_ladder(3))
print(generate_asc_ladder_2(5))
print(construir_escalera(4))
