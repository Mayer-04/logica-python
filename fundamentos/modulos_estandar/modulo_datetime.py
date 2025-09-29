from datetime import datetime

"""
Módulo datetime en Python
----------------------------
El módulo `datetime` permite trabajar con fechas y horas.

Algunas funciones:
-------------------
- datetime(año, mes, día): crea una fecha específica.

- datetime.now(): obtiene la fecha y hora actual.

- .year, .month, .day, .hour, .minute, .second: extraen partes de la fecha.

- .weekday(): devuelve el día de la semana (0 = lunes, 6 = domingo).

- .timestamp(): devuelve los segundos desde el 1 de enero de 1970 (formato UNIX).

IMPORTANTE:
------------
Algunos de los valores que veas en la consola pueden ser diferentes cada vez que corras el programa.
"""

# Crear una fecha específica (sin hora)
fecha_personalizada = datetime(2025, 9, 28)
print("Fecha personalizada:", fecha_personalizada)  # Salida: 2025-09-28 00:00:00

# Obtener la fecha y hora actual
fecha_actual = datetime.now()
print("Fecha y hora actual:", fecha_actual)  # Salida: 2025-09-28 14:08:24.304864

# Extraer partes de la fecha actual
print("Año actual:", fecha_actual.year)  # Salida: 2025
print("Mes actual:", fecha_actual.month)  # Salida: 9
print("Día del mes:", fecha_actual.day)  # Salida: 28

# Día de la semana (0 = lunes, 6 = domingo)
dia_semana = fecha_actual.weekday()
print("Día de la semana:", dia_semana)  # Salida: 6
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Día de la semana:", dias[dia_semana])  # Salida: Domingo

# Extraer la hora actual
hora_actual = fecha_actual.time()
print("Hora completa:", hora_actual)  # Salida: 14:10:26.556238
print("Solo la hora:", fecha_actual.hour)  # Salida: 14
print("Minuto:", fecha_actual.minute)  # Salida: 10
print("Segundo:", fecha_actual.second)  # Salida: 26

# Obtener el timestamp (segundos desde 1970)
segundos_desde_1970 = fecha_actual.timestamp()
print(
    "Timestamp (segundos desde 1970):", segundos_desde_1970
)  # Salida: 1759086626.556238
