"""
Entre un dígito de 1 a 7. Diseñar un algoritmo que diga a que día de la semana corresponde.
Cualquier otro dígito debe mostrar un mensaje de error.
"""

# Utilizando la estructura condicional `if` y `elif`
dia = int(input("Ingrese un dígito entre 1 y 7: "))
digito_invalido = dia < 1 or dia > 7
if digito_invalido:
    print("Dígito inválido")
elif dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")


# Utilizando la estructura condicional `match`
dia = int(input("Ingrese un dígito entre 1 y 7: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dígito inválido")


"""
* Utilizando un diccionario:
- Se puede hacer con la función `get()`
- Se puede utilizar el operador `ternario`
- Se puede hacer con la palabra clave `in`
- Se puede negar la condición con la palabra clave `not`
- Se puede accediendo a los índices del diccionario
"""
dia = int(input("Ingrese un dígito entre 1 y 7: "))

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo",
}

# 1
if dias.get(dia):
    print(dias.get(dia))
else:
    print("Días inválidos")

# 1.1
print(dias.get(dia, "Días inválidos"))

# 2
mensaje = dias[dia] if dia in dias else "Días inválidos"
print("Mensaje: ", mensaje)


# 3
if dia in dias:
    print(dias[dia])
else:
    print("Días inválidos")

# 4
if dia not in dias:
    print("Días inválidos")
else:
    print(dias[dia])

# 5
if dias[dia]:
    print("Día: ", dias[dia])
else:
    print("Días inválidos")


# Utilizando una función
def obtener_dia(dia: int) -> str:
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo",
    }

    # Utilizar get() para obtener el día o un mensaje de error
    return dias.get(dia, "Día inválido")


# Ejemplo de uso
try:
    dia = int(input("Ingrese un dígito entre 1 y 7: "))
    mensaje = obtener_dia(dia)
except ValueError:
    mensaje = "Entrada inválida. Debe ser un número entero."

print(f"Día de la semana: {mensaje}")
