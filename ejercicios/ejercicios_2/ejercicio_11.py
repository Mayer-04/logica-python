"""
Escribe una función que genere contraseñas aleatorias según criterios especificados.

Parámetros de entrada:
-----------------------
- longitud: longitud de la contraseña (mínimo 8)
- incluir_mayusculas: booleano para incluir letras mayúsculas (A-Z)
- incluir_minusculas: booleano para incluir letras minúsculas (a-z)
- incluir_numeros: booleano para incluir dígitos (0-9)
- incluir_simbolos: booleano para incluir símbolos (!@#$%^&\*)

Requisitos:
------------
- Al menos una opción debe estar en True
- La contraseña debe contener al menos un carácter de cada tipo seleccionado
"""

# from dataclasses import dataclass

# @dataclass
# class ConfiguracionContrasena:
#     longitud: int = 8
#     incluir_mayusculas: bool = True
#     incluir_minusculas: bool = True
#     incluir_numeros: bool = True
#     incluir_simbolos: bool = False

# config = {
#     "longitud": 12,
#     "incluir_mayusculas": True,
#     "incluir_minusculas": True,
#     "incluir_numeros": True,
#     "incluir_simbolos": True,
# }

# def generador_contraseñas(longitud: int = 4, mayuscula: bool, minuscula: bool, numeros: int, simbolos: int):
