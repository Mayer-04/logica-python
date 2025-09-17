"""
Crea una función en Python que calcule el área de un triángulo rectángulo.
El usuario debe ingresar la longitud de los dos catetos (lado A y lado B).
El programa debe mostrar el resultado del área utilizando la fórmula:
area = (cateto1 * cateto2) / 2
"""


def calcular_area_triangulo(primer_cateto: float, segundo_cateto: float) -> float:
    """
    Calcula el área de un triángulo rectángulo dado sus catetos.

    La fórmula es: area = (cateto1 * cateto2) / 2

    Argumentos:
    primer_cateto (float): Longitud del primer cateto.
    segundo_cateto (float): Longitud del segundo cateto.

    Retorna:
    float: El área del triángulo rectángulo.
    """
    if primer_cateto <= 0 or segundo_cateto <= 0:
        raise ValueError("Ambos catetos deben ser valores positivos")

    return (primer_cateto * segundo_cateto) / 2


area = calcular_area_triangulo(5, 6)
print(area)
