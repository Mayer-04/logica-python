# =====================================
# * Función incorporada isinstance()
# =====================================
# La función isinstance() verifica si un objeto es de un tipo o clase específicos.
#
# Forma general:
# isinstance(objeto, tipo_o_tupla_de_tipos)
#
# Parámetros:
# - objeto: el valor que quieres comprobar
# - tipo_o_tupla_de_tipos: puede ser un solo tipo (int, str, list, etc.)
#   o una tupla con varios tipos
#
# Devuelve:
# - True si el objeto es de ese tipo o de un subtipo (herencia en clases)
# - False si no lo es

# Ejemplo 1: Comprobando tipos simples
print(isinstance(5, int))  # True → 5 es un número entero
print(isinstance("Hola", str))  # True → "Hola" es una cadena
print(isinstance(True, bool))  # True → True es un valor booleano
print(isinstance("Andres", float))  # False → una cadena no es un número flotante

# Ejemplo 2: Comprobando contra varios tipos
PI = 3.14
print(
    isinstance(PI, (int, float))
)  # True → 3.14 es un float, que está en la tupla de tipos

# Ejemplo 3: Uso con listas y diccionarios
datos = [1, 2, 3]
print(isinstance(datos, list))  # True → es una lista
print(isinstance(datos, dict))  # False → no es un diccionario

# Ejemplo 4: Evitar errores al trabajar con tipos
# En vez de asumir el tipo y arriesgar un error:
# longitud = len(123)  # ❌ Esto daría error, porque un int no tiene len()
# Podemos validar antes:
numero = 123
if isinstance(numero, str):
    print(len(numero))
else:
    print("No es una cadena, no se puede calcular la longitud.")
