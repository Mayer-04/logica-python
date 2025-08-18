"""
Anotaciones de tipo en Python (Type Hints / Type Annotations)
-------------------------------------------------------------
Introducidas en la versión de Python 3.5, las anotaciones de tipo permiten indicar qué `tipo de dato`
se espera que tengan las variables, los parámetros de funciones y los valores de retorno.

Declaración de tipos (desde Python 3.12):
-----------------------------------------
Desde la versión 3.12, se puede utilizar la función `type` para crear `alias de tipos`, es decir, 
nombres personalizados que representan tipos complejos.

Ejemplo:
--------
type UsuarioID = int

def obtener_usuario(id: UsuarioID) -> str:
    return f"Usuario con ID {id}"

Beneficios:
-----------
- Mejoran la `legibilidad` del código y funcionan como documentación integrada.
- Ayudan a detectar errores mediante herramientas de análisis estático 
  (como Pyright, MyPy, o el sistema de inspección de PyCharm).
- Aunque no son obligatorias, permiten a los editores de código proporcionar `autocompletado, advertencias
  y sugerencias` más precisas.
- No afectan el comportamiento en tiempo de ejecución, ya que `Python no aplica comprobación estricta de tipos` 
  en ese momento.

Notas:
------
- Python `no valida` los tipos en tiempo de ejecución.
- Las anotaciones sirven como guía, pero puedes seguir asignando valores de otro tipo sin que Python
  arroje un error directamente.
- En el editor de código `Visual Studio Code` puedes hacer que el editor te indique errores o advertencias
  buscando `Type Checking Mode`.
"""

# Variable sin anotación de tipo
# Python permite que esta variable cambie de tipo en cualquier momento
no_tipado = "Texto sin tipo específico"

# Variable con anotación de tipo
tipado: str = "Texto tipado"  # Se indica que 'tipado' debería ser una cadena (str)

# A pesar de la anotación, Python permite cambiar el tipo de dato en tiempo de ejecución
tipado = 1  # No lanza error, pero rompe la intención del tipo declarado
print(f"tipado: {tipado}")  # Salida: tipado: 1

# -------------------------------------------
# * Diferentes tipos de anotaciones de tipo
# -------------------------------------------

# Lista de strings
my_list: list[str] = ["uno", "dos", "tres"]
print(f"my_list: {my_list}")  # Salida: ['uno', 'dos', 'tres']

# Tupla de tres enteros
my_tuple: tuple[int, int, int] = (1, 2, 3)
print(f"my_tuple: {my_tuple}")  # Salida: (1, 2, 3)

# Diccionario con claves tipo 'str' y valores tipo 'int'
my_dict: dict[str, int] = {"uno": 1, "dos": 2, "tres": 3}
print(f"my_dict: {my_dict}")  # Salida: {'uno': 1, 'dos': 2, 'tres': 3}

# Diccionario con valores que pueden ser 'str' o 'int'
my_dict2: dict[str, str | int] = {"uno": 1, "dos": "2", "tres": 3}
print(f"my_dict2: {my_dict2}")  # Salida: {'uno': 1, 'dos': '2', 'tres': 3}

# Función con anotaciones de tipo
# Se especifica el tipo de dato de los parámetros como el tipo de dato de retorno de la función
def sumar_numeros(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b

resultado = sumar_numeros(1, 2)
print(f"Resultado de la suma: {resultado}")  # Salida: 3

# Función que no devuelve ningún valor (retorno: None)
def imprimir_mensaje(mensaje: str) -> None:
    """Imprime un mensaje en la consola."""
    print(mensaje)

imprimir_mensaje("Hola, anotaciones de tipo!")  # Salida: Hola, anotaciones de tipo!

# Anotaciones de tipo en clases
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def saludar(self) -> str:
        """Devuelve un saludo personalizado."""
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona = Persona("Mayer", 25)
print(persona.saludar())  # Salida: Hola, mi nombre es Mayer y tengo 25 años.

# Alias de tipo para simplificar anotaciones
Color = tuple[str, str, str]  # Un color representado por 3 cadenas (por ejemplo: RGB con nombres)
colores: Color = ("Rojo", "Verde", "Azul")
print(f"colores: {colores}")  # Salida: ('Rojo', 'Verde', 'Azul')

# Declaración de tipos usando 'type' (Python 3.12+)
type Number = tuple[int, int]  # Alias de tipo para una tupla de dos enteros
numeros: Number = (4, 11)
print(f"numeros: {numeros}")  # Salida: (4, 11)