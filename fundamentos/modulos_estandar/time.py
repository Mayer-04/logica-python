import time

"""
Módulo time en Python
------------------------
El módulo `time` permite trabajar con fechas, horas y pausas en la ejecución del programa.

IMPORTANTE:
Muchas funciones de este módulo devuelven valores que cambian cada vez que se ejecuta el código.
"""

# time.time()
# Devuelve el número de segundos desde el 1 de enero de 1970 (formato UNIX)
segundos_desde_1970 = time.time()
print("Segundos desde 1970:", segundos_desde_1970)  # Salida: 1759088883.258669

# time.ctime()
# Devuelve una cadena legible con la fecha y hora actual
# Ejemplo: 'Sun Sep 28 14:46:00 2025'
fecha_legible = time.ctime()
print("Fecha legible:", fecha_legible)  # Salida: Sun Sep 28 14:48:03 2025

# time.localtime()
# Devuelve una estructura con la fecha y hora actual separada por partes
estructura_tiempo = time.localtime()
print("Estructura de tiempo:", estructura_tiempo)

# time.asctime()
# Convierte una estructura de tiempo en una cadena legible
# Si no se le pasa nada, usa la hora actual
cadena_tiempo = time.asctime()
print("Cadena desde estructura:", cadena_tiempo)  # Salida: Sun Sep 28 14:48:03 2025

# time.sleep(segundos)
# Pausa la ejecución del programa durante el número de segundos indicado
print("Esperando 2 segundos...")
time.sleep(2)  # No imprime nada, solo espera
print("¡Listo!")
