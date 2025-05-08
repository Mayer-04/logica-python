"""
* Dates

- El módulo `datetime` que proporciona clases para manipular fechas y horas.
"""

from datetime import datetime

fecha_hora = datetime(
    2024,
    8,
    18,
)
print("Fecha y hora:", fecha_hora)

# Imprime la fecha actual en el formato `%Y-%m-%d %H:%M:%S.%f`
fecha = datetime.now()
print("Fecha:", fecha)  # 2024-08-18 18:31:04.237221


# Imprimir el año actual
año = fecha.year
print("Año:", año)

# Imprimir el mes actual
mes = fecha.month
print("Mes:", mes)

# Imprimir el día de la semana actual
# 0: Lunes, 7: Domingo
semana_actual = fecha.weekday()
print("Dia de la semana:", semana_actual)

# Imprimir el día actual
dia = fecha.day
print("Dia:", dia)

# Imprime la hora actual en el formato `%H:%M:%S.%f`
# Podemos hacer también `datetime.now().time()`
hora = fecha.time()
print("Hora:", hora)

nueva_hora = fecha.hour
print("Nueva hora:", nueva_hora)

# Imprimir el minuto
minuto = fecha.minute
print("Minuto:", minuto)

# Imprimir el segundo
segundo = fecha.second
print("Segundo:", segundo)

# Timestamps
# Imprime el número de segundos desde el 1 de enero de 1970
timestamp = fecha.timestamp()
print("Timestamp:", timestamp)
