"""
Escribe una función que reciba cuatro parámetros: días, horas, minutos y segundos.
La función debe calcular y devolver el tiempo total equivalente en milisegundos.

Conversiones:
--------------
- 1 segundo = 1,000 milisegundos
- 1 minuto = 60 segundos
- 1 hora = 60 minutos
- 1 día = 24 horas

Ejemplo:
---------
tiempo_a_ms(1, 2, 30, 45)  # 1 día, 2 horas, 30 minutos, 45 segundos
# Resultado: 95,445,000 milisegundos
"""


def convert_milliseconds(days: int, hours: int, minutes: int, seconds: int) -> int:
    return (
        days * 24 * 60 * 60 * 1000
        + hours * 60 * 60 * 1000
        + minutes * 60 * 1000
        + seconds * 1000
    )


def tiempo_a_ms(dias: int, horas: int, minutos: int, segundos: int) -> int:
    factores = {
        "dias": 24 * 60 * 60 * 1000,
        "horas": 60 * 60 * 1000,
        "minutos": 60 * 1000,
        "segundos": 1000,
    }

    valores = [dias, horas, minutos, segundos]
    return sum(v * f for v, f in zip(valores, factores.values()))


print(convert_milliseconds(1, 2, 30, 45))
print(tiempo_a_ms(2, 3, 15, 25))
