"""
* Estructura de Control Match
-----------------------------
Match permite comparar una expresión con varios `patrones` y ejecutar el código correspondiente a cada coincidencia.

La sentencia `match` es una estructura de control introducida en Python 3.10, 
similar a `switch` en otros lenguajes de programación.

- Patrones: Son las condiciones o criterios que Python utiliza para comparar
y hacer coincidir un valor o estructura de datos con uno o varios casos específicos.

- La sentencia `match` recibe una expresión y compara su valor con uno o más bloques `case`.
- Cada bloque `case` se evalúa secuencialmente hasta encontrar una coincidencia.
- Es posible agrupar opciones en un mismo `case` usando el operador `|`.
- El patrón `_` actúa como un comodín y se ejecuta si ninguna de las condiciones anteriores se cumple.

IMPORTANTE: `match` es más que un simple `switch` ya que soporta patrones complejos y deconstrucción de datos, 
lo que lo convierte en una herramienta poderosa para el control de flujo.
"""

# Ejemplo 1: Uso básico de 'match' para verificar el estado de un semáforo.
color = "verde"

match color:
    case "verde":
        print("Puedes avanzar.")
    case "amarillo":
        print("Precaución.")
    case "rojo":
        print("Detente.")
    case (
        _
    ):  # El caso '_' se usa como un caso por defecto si ninguno de los anteriores coincide
        print("Color desconocido.")


# Ejemplo 2: Uso de `match` para manejar errores HTTP con agrupación de opciones
def http_error(status):
    match status:
        case 400:
            return "Petición incorrecta"
        case 401 | 403 | 405:  # Agrupando varias opciones en el mismo `case`
            return "No autorizado"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"  # Este es un código de error de broma en HTTP
        case _:  # Caso por defecto para manejar cualquier otro código de estado
            return "Algo anda mal con internet"


print(http_error(404))  # Imprime: No encontrado


# Ejemplo 3: Uso de `match` con tuplas para identificar puntos en un plano cartesiano
x = 0
y = 10
point = (x, y)

match point:
    case (0, 0):
        print("En el origen")
    case (0, y):  # Coincide cualquier punto en el eje Y
        print(f"En el eje Y: {y}")
    case (x, 0):  # Coincide cualquier punto en el eje X
        print(f"En el eje X: {x}")
    case (x, y):  # Coincide cualquier otro punto en el plano
        print(f"En algún lugar: X={x}, Y={y}")
    case _:  # Caso por defecto si el punto no corresponde a ningún caso anterior
        print("No es un punto válido")


# Ejemplo 4: Uso avanzado de `match` con patrones complejos
# Este ejemplo demuestra cómo `match`:
# puede trabajar con estructuras de datos más complejas como listas y diccionarios
data = {"name": "Andres", "age": 24, "location": "Colombia"}

match data:
    case {"name": name, "age": age, "location": "Colombia"}:
        print(f"{name}, de {age} años, vive en Colombia.")
    case {"name": name, "age": age}:
        print(f"{name}, de {age} años, tiene una ubicación desconocida.")
    case _:
        print("Datos no reconocidos")


# Ejemplo 5: Combinación de tipos de patrones en un mismo `match`
status_code = 403
error_info = {"method": "GET"}
# Compara el valor de status_code y error_info con diferentes patrones.
match status_code, error_info:
    case 403, {"method": method}:
        print(f"Acceso denegado al intentar {method}")
        # si status_code es 404 y error_info puede ser cualquier valor (`_` es un comodín)
    case 404, _:
        print("Recurso no encontrado")
    case _:
        print("Error desconocido")
