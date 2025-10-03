"""
Escribe un programa que convierta grados Celsius a Fahrenheit.
Fórmula: F = (C * 9/5) + 32

El programa debe:
------------------
1. Solicitar al usuario la temperatura en grados Celsius
2. Validar que sea un número válido
3. Realizar la conversión y mostrar el resultado con 2 decimales

Extensión: Permite también la conversión inversa (Fahrenheit a Celsius).
"""


def convertir_temperatura(temp_celsius: float) -> float:
    return round((temp_celsius * 9 / 5) + 32, 2)


try:
    temperatura = float(input("Ingresa la temperatura en grados Celsius: "))
    resultado = convertir_temperatura(temperatura)
except ValueError as e:
    print("Entrada inválida: Ingresa un número")
    print(f"Error: {e}")
else:
    print(f"La temperatura en Fahrenheit es: {resultado}")
