import time

"""
* Time
- El módulo time proporciona métodos para trabajar con la fecha y hora.
"""


# time.time(): Devuelve la hora actual en segundos desde la época.
current_time = time.time()
print("Current time:", current_time)


# time.ctime: Devuelve una cadena con la fecha y hora actual
# Es equivalente a `time.asctime()`
print(time.ctime())

# time.localtime: Devuelve una tupla con la fecha y hora actual
print("Local time:", time.localtime())

# time.asctime: Devuelve una cadena con la fecha y hora actual
# Devuelve una tupla de tiempo en una cadena.
# Cuando la tupla de tiempo no está presente, la hora actual es la devuelta por `localtime()`
print(time.asctime())

# time.sleep: Pausa la ejecución del programa durante el número de segundos especificado.
print(time.sleep(2))