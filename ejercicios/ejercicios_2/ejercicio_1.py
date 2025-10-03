"""
Crea una función en Python que calcule el área de un triángulo rectángulo.
El usuario debe ingresar la longitud de los dos catetos (lado A y lado B).
El programa debe mostrar el resultado del área utilizando la fórmula:
area = (cateto1 * cateto2) / 2
"""


def calcular_area_triangulo(primer_cateto: float, segundo_cateto: float) -> float:
    if primer_cateto <= 0 or segundo_cateto <= 0:
        raise ValueError("Ambos catetos deben ser positivos")

    return (primer_cateto * segundo_cateto) / 2


try:
    area = calcular_area_triangulo(5, 6)
except ValueError as e:
    print(f"Error al calcular el área: {e}")
else:
    print(f"El área del triángulo es: {area}")
